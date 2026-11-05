"""Independent numerical stress checks, NOT a substitute for the proof.

Checks the explicit Blaschke product, non-even mass identity, output
reconstruction, and the energy/mass contraction using Fourier quadrature.
Only numpy and the Python standard library are required.
"""
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import json
import numpy as np

P = 2*np.pi


def inner(z, d, y, s0, J):
    c = np.pi/(4*d)
    tau = np.tan(c*y)
    bplus, bminus = np.exp(-2j*c*y), -np.exp(2j*c*y)
    B = np.ones_like(z, dtype=complex)
    logarithmic_derivative = np.zeros_like(z, dtype=complex)
    for k in range(-J,J+1):
        arg = c*(z-s0+k*P)
        side = np.where(np.real(arg)>=0,1.,-1.)
        exp_tail = np.exp(-2*side*arg)
        t = side*(1-exp_tail)/(1+exp_tail)
        factor = (t-1j*tau)/(1+1j*tau*t)
        derivative = c*(1-t*t)*(1-tau*tau)/(1+1j*tau*t)**2
        logarithmic_derivative += derivative/factor
        B *= factor/(bplus if k>0 else bminus if k<0 else 1)
    return B, logarithmic_derivative


def run_case(d, theta, chi, seed, grid):
    rng = np.random.default_rng(seed)
    y, s0 = d*(1-2*chi), .734567
    a = s0+1j*y
    theta_out = theta-chi
    # A non-even positive p, with a direct pointwise lower bound .39.
    pc = np.array([.19+.06j, -.05+.035j, .015-.02j])
    x = (np.arange(grid)+.173)*P/grid
    p = np.ones(grid)
    rho = np.ones(grid)
    for k,b in enumerate(pc,1):
        p += 2*np.real(b*np.exp(1j*k*x))
        rho += 2*np.real(b*np.exp(1j*k*x))/np.cosh(d*k)
    if not 1-2*np.sum(np.abs(pc))>0:
        raise ValueError('The middle weight must have a positive lower bound')
    m = np.arange(-3,4)
    coeff = (rng.normal(size=7)+1j*rng.normal(size=7))/(1+m*m)
    def V(z):
        return np.exp(1j*theta*z)*(np.exp(1j*(z-a))-1)*np.sum(
            coeff[:,None]*np.exp(1j*m[:,None]*z[None,:]),axis=0)
    J = max(8,int(np.ceil(30*d/P)))
    # Product convergence and phase tested away from its zeros.
    probe = np.array([.12+.21j*d,2.31-.31j*d,5.21+.67j*d])
    B0,_ = inner(probe,d,y,s0,J)
    B1,_ = inner(probe+P,d,y,s0,J)
    B2,_ = inner(probe,d,y,s0,J+4)
    phase_error = np.max(np.abs(B1-np.exp(2j*np.pi*chi)*B0))
    product_error = np.max(np.abs(B2-B0))
    edges = []
    beta = []
    edge_mod_error = 0.
    for sign in [1,-1]:
        z = x+sign*1j*d
        B,LD = inner(z,d,y,s0,J)
        edge_mod_error = max(edge_mod_error,float(np.max(np.abs(abs(B)-1))))
        edges.append((V(z),V(z)/B))
        # outward derivative log|B| = +/- Re(i B'/B).
        beta.append(sign*np.real(1j*LD))
    Bmid,_ = inner(x.astype(complex),d,y,s0,J)
    vmid = V(x.astype(complex)); wmid = vmid/Bmid
    vp,wp = edges[0]; vn,wn = edges[1]
    u = (vp+vn)/2; out = (wp+wn)/2
    mass = P*np.mean(rho*abs(u)**2)
    mass_out = P*np.mean(rho*abs(out)**2)
    mass_split = P*np.mean(rho*(abs(vp)**2+abs(vn)**2)/4+p*abs(vmid)**2/2)
    mass_out_split = P*np.mean(rho*(abs(wp)**2+abs(wn)**2)/4+p*abs(wmid)**2/2)
    freq = np.fft.fftfreq(grid)*grid
    def q(top,ph):
        f = np.fft.fft(top*np.exp(-1j*ph*x))/grid
        k = freq+ph
        return float(P*np.sum(k*np.tanh(d*k)*abs(f)**2))
    qv,qw = q(u,theta),q(out,theta_out)
    boundary_difference = P/4*np.mean(beta[0]*abs(wp)**2+beta[1]*abs(wn)**2)
    # Independently recover wmid from the divided top trace.
    f = np.fft.fft(out*np.exp(-1j*theta_out*x))/grid
    # Grid has an offset; fft coefficient phases are kept by using ifft.
    k = freq+theta_out
    sech = 2*np.exp(-abs(d*k))/(1+np.exp(-2*abs(d*k)))
    recovered = np.fft.ifft(grid*f*sech)*np.exp(1j*theta_out*x)
    return dict(d=d,theta=theta,chi=chi,grid=grid,
        phase_error=float(phase_error),product_error=float(product_error),
        edge_modulus_error=edge_mod_error,
        mass_identity_relative=float(abs(mass-mass_split)/mass),
        output_mass_identity_relative=float(abs(mass_out-mass_out_split)/mass_out),
        energy_identity_relative=float(abs(qv-qw-boundary_difference)/max(qv,1e-300)),
        bottom_reconstruction_relative=float(np.linalg.norm(recovered-wmid)/np.linalg.norm(wmid)),
        reconstruction_error_relative_to_top=float(np.linalg.norm(recovered-wmid)/np.linalg.norm(out)),
        top_to_bottom_norm_ratio=float(np.linalg.norm(out)/np.linalg.norm(wmid)),
        middle_max_modulus=float(max(abs(Bmid))),
        minimum_edge_beta=float(min(np.min(b) for b in beta)),
        mass_ratio=float(mass_out/mass),energy_ratio=float(qw/qv),
        quotient_ratio=float((qw/mass_out)/(qv/mass)))


def validate_case(row):
    """Reject failed or non-finite diagnostics even when Python uses -O."""
    for name, value in row.items():
        if not np.isfinite(value):
            raise ValueError(f"Non-finite {name}: {value}")
    upper_bounds = {
        'phase_error': 1e-10, 'product_error': 1e-10,
        'edge_modulus_error': 1e-10, 'mass_identity_relative': 1e-10,
        'output_mass_identity_relative': 1e-8, 'energy_identity_relative': 1e-8,
        # A deep-strip output can be tiny relative to its input. Check the
        # smoothing operation against its top input norm; retain the forward
        # relative error in the JSON rather than suppressing cancellation.
        'reconstruction_error_relative_to_top': 1e-12,
    }
    for name, limit in upper_bounds.items():
        if not 0 <= row[name] < limit:
            raise ValueError(f"{name}={row[name]} is outside [0, {limit})")
    conditions = {
        'mass_ratio': row['mass_ratio'] >= 1-1e-10,
        'energy_ratio': -1e-10 <= row['energy_ratio'] <= 1+1e-10,
        'quotient_ratio': -1e-10 <= row['quotient_ratio'] <= 1+1e-10,
        'middle_max_modulus': 0 <= row['middle_max_modulus'] <= 1+1e-10,
        'minimum_edge_beta': row['minimum_edge_beta'] >= -1e-10,
    }
    for name, valid in conditions.items():
        if not valid:
            raise ValueError(f"Failed {name}: {row[name]}")


def main():
    cases = []
    for j,d in enumerate([.12,.7,2.,6.]):
        for k,chi in enumerate([.013,.23,.5,.87,.987]):
            theta = [-.49,0.,.17,.499][(j+k)%4]
            cases.append(run_case(d,theta,chi,173+j*7+k,8192))
    # Refine the case most sensitive to a zero near the edge.
    cases.append(run_case(.12,-.49,.013,173,32768))
    for row in cases:
        validate_case(row)
    print(json.dumps({'scope':'Floating-point diagnostic only, not a certificate','cases':cases},indent=2))


if __name__=='__main__':
    main()
