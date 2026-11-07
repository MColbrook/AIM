import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import numpy as np

def modulus(epsilon,beta=0j,tau=1.,degree=32,grid=240):
    radius=np.cosh(tau); scale=np.cosh(2*tau)
    angle=2*np.pi*np.arange(grid)/grid
    inner=np.exp(1j*angle)+epsilon*np.exp(2j*angle)
    outer=radius*np.exp(1j*angle)+epsilon*scale*np.exp(2j*angle)
    z=np.r_[inner,outer]; z=z+beta*z.conjugate()
    powers=np.arange(1,degree+1)
    plus=(z[:,None]/radius)**powers; minus=(1/z[:,None])**powers
    matrix=np.column_stack([np.ones(2*grid),np.log(abs(z)),plus.real,plus.imag,minus.real,minus.imag])
    rhs=np.r_[np.zeros(grid),np.ones(grid)]
    solution=np.linalg.lstsq(matrix,rhs,rcond=None)[0]
    residual=float(np.max(np.abs(matrix@solution-rhs)))
    value=float(1/solution[1])
    if not np.isfinite(value) or not np.isfinite(residual) or residual>1e-6: raise ValueError('Failed collocation diagnostic')
    return value,residual

if __name__=='__main__':
    radius=np.cosh(1.); baseline=np.log(radius)
    print('Floating-point collocation diagnostic only; not a global optimization certificate.')
    for epsilon in [.04,.02,.01,.005,.002]:
        value,residual=modulus(epsilon)
        print('epsilon',epsilon,'modulus',value,'second-order coefficient',(value-baseline)/epsilon**2,'residual',residual)
    print('Harmonic predicted coefficient:',-(1-radius**-2))
    for beta in [.04,.02,.01,.005]:
        value,residual=modulus(0.,beta)
        print('beta',beta,'second-order coefficient',(value-baseline)/beta**2,'residual',residual)
    print('Affine predicted coefficient:',-2*(radius**2-1)/(radius**2+1))
    value,residual=modulus(.02,.003933496,degree=40,grid=300)
    print('Supplied candidate affine parameter: modulus',value,'baseline deficit',baseline-value,'residual',residual)
