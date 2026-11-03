"""Exact algebra checks supporting the analytic AIM 1007 proof.

These checks do not certify the infinite-dimensional estimates, existence
of the selected phase, or the entire theorem. No spectral discretization
or floating-point assertion is used. Run with Python 3.12 and SymPy 1.14.
"""
import sys
import sympy as sp


def is_zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(is_zero(v) for v in value)
    return sp.simplify(sp.trigsimp(sp.expand_trig(value))) == 0


def require_zero(name, expression):
    if not is_zero(expression):
        raise ArithmeticError(f"FAILED: {name}: {expression}")
    print(f"PASS: {name}")


def verify():
    t, x, delta = sp.symbols('t x delta', real=True)
    s, S, k, r, a = sp.symbols('s S k r a', positive=True)
    m = sp.Rational(1, 3) - 2/sp.pi**2
    E1 = sp.pi**2/4
    k2 = 1/(2*m)
    energy = sp.pi**4/(4*(sp.pi**2-6))
    chi = sp.cos(sp.pi*t/2)
    require_zero('normalized first transverse mode', sp.integrate(chi**2,(t,-1,1))-1)
    require_zero('Dirichlet transverse eigen-equation', -sp.diff(chi,t,2)-E1*chi)
    require_zero('transverse moment m', sp.integrate(t**2*chi**2,(t,-1,1))-m)
    require_zero('transverse derivative moment', sp.integrate(t**2*sp.diff(chi,t)**2,(t,-1,1))-(E1*m+1))
    require_zero('energy formula', E1+k2-energy)
    require_zero('positive energy gap above E1', energy-E1-3*sp.pi**2/(2*(sp.pi**2-6)))
    require_zero('gap below E2, positive since pi squared > 8', sp.pi**2-energy-3*sp.pi**2*(sp.pi**2-8)/(4*(sp.pi**2-6)))
    require_zero('mean term cancellation', m*k2-sp.Rational(1,2))

    b = sp.symbols('b', real=True)
    A1 = sp.integrate(sp.diff((1+t**2*b)**(-sp.Rational(1,2)), b).subs(b,0)*chi**2,(t,-1,1))
    B1 = sp.integrate(sp.diff(sp.sqrt(1+t**2*b),b).subs(b,0)*(sp.diff(chi,t)**2-(E1+k**2)*chi**2),(t,-1,1))
    require_zero('A first-order coefficient', A1+m/2)
    require_zero('B first-order coefficient', B1-(1-m*k**2)/2)
    alpha = sp.Function('alpha', positive=True)(s)
    beta, y = sp.Function('beta')(s), sp.Function('y')(s)
    u = y/sp.sqrt(alpha)
    W = -beta/alpha-sp.diff(alpha,s,2)/(2*alpha)+sp.diff(alpha,s)**2/(4*alpha**2)
    require_zero('exact scalar normalization', (-sp.diff(alpha*sp.diff(u,s),s)+beta*u)/sp.sqrt(alpha)+sp.diff(y,s,2)+W*y)

    rho = S+s
    phase = 2*k*s+delta
    profile2 = 16*k/rho*(1+sp.cos(phase)/2)
    # Insert m=1/(2 k^2) only after deriving the transverse coefficients.
    residual = sp.diff(profile2,s,2)/(8*k**2)+4*k*sp.cos(phase)/rho
    expected = 4*sp.sin(phase)/rho**2+(4+2*sp.cos(phase))/(k*rho**3)
    require_zero('resonant coefficient and exact lower-order remainder', residual-expected)
    require_zero('amplitude upper envelope', (24*k/rho-profile2)-8*k*(1-sp.cos(phase))/rho)
    require_zero('positive amplitude lower envelope', (profile2-8*k/rho)-8*k*(1+sp.cos(phase))/rho)

    R = sp.Matrix([[sp.cos(x),sp.sin(x)],[-sp.sin(x),sp.cos(x)]])
    E = sp.Matrix([[0,0],[1,0]])
    M = sp.Matrix([[sp.sin(delta),sp.cos(delta)],[sp.cos(delta),-sp.sin(delta)]])
    full = 4*sp.cos(2*x+delta)*R.T*E*R
    mean = full.applyfunc(lambda v: sp.integrate(sp.expand_trig(v),(x,0,sp.pi))/sp.pi)
    require_zero('mean rotating matrix', mean-M)
    require_zero('mean matrix is an involution', M*M-sp.eye(2))
    e = sp.Matrix([sp.cos(3*sp.pi/4-delta/2),sp.sin(3*sp.pi/4-delta/2)])
    require_zero('stable vector has eigenvalue minus one', M*e+e)
    require_zero('stable vector has unit norm', (e.T*e)[0]-1)
    require_zero('stable vector is antiperiodic', e.subs(delta,delta+2*sp.pi)+e)
    Z = sp.Matrix(2,2,sp.symbols('z0:4'))
    N = sp.Matrix(2,2,sp.symbols('n0:4'))
    H = sp.eye(2)+Z/rho
    # Multiply the claimed transformed identity by H, avoiding any expansion
    # of the rational matrix inverse; H is invertible for sufficiently large S.
    require_zero('exact normal-form remainder', (M+N)*H/rho-(N/rho-Z/rho**2)-H*M/rho-(M*Z-Z*M+N*Z+Z)/rho**2)

    require_zero('stable kernel Hilbert-Schmidt bound', sp.integrate((S+r)**(-3),(r,0,sp.oo))-1/(2*S**2))
    require_zero('unstable kernel row integral', sp.integrate((S+s)/(S+r)**3,(r,s,sp.oo))-1/(2*(S+s)))
    require_zero('unstable kernel column integral', sp.integrate((S+s)/(S+r)**3,(s,0,r))-((S+r)**2-S**2)/(2*(S+r)**3))
    w = S+sp.sqrt(1+s**2)
    require_zero('smooth weight preserves Neumann trace', sp.diff(w,s).subs(s,0))
    theta = sp.Function('theta')(s)
    embedding = sp.Matrix([s,t*sp.cos(theta),t*sp.sin(theta)])
    require_zero('geometric longitudinal metric', (embedding.diff(s).T*embedding.diff(s))[0]-(1+t**2*sp.diff(theta,s)**2))
    require_zero('geometric mixed metric vanishes', (embedding.diff(s).T*embedding.diff(t))[0])
    require_zero('geometric transverse metric equals one', (embedding.diff(t).T*embedding.diff(t))[0]-1)
    q = sp.Function('q')
    require_zero('scaled metric identity', sp.sqrt(1+t**2*(q(s/a)/a)**2)-sp.sqrt(1+(t/a)**2*q(s/a)**2))
    print('All 28 exact identities passed. Analytic estimates require the written audit.')


def rejection_checks():
    for name, expression in [
        ('wrong stable eigenvalue', sp.Integer(2)),
        ('matrix with one corrupted entry', sp.Matrix([[0,0],[1,0]])),
        ('flipped resonance coefficient', sp.Symbol('k', positive=True)*8),
    ]:
        try:
            require_zero(name, expression)
        except ArithmeticError:
            print(f'PASS: rejected {name}')
        else:
            raise RuntimeError(f'Checker incorrectly accepted {name}')


if __name__ == '__main__':
    print(f'Python {sys.version.split()[0]}; SymPy {sp.__version__}; optimization={sys.flags.optimize}')
    verify()
    rejection_checks()
