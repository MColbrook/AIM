"""Exact checks supporting the analytic construction for AIM 1021.

Requires SymPy 1.14.0 and mpmath 1.3.0. These checks do not prove the
adiabatic estimates, convergence of the induction, or the spectral theorem.
Use explicit exceptions so python -O runs the same checks.
"""

import sys

import sympy as sp


def require_zero(name, expression):
    entries = list(expression) if isinstance(expression, sp.MatrixBase) else [expression]
    if any(sp.simplify(sp.trigsimp(sp.expand_trig(value))) != 0 for value in entries):
        raise ArithmeticError(f"FAILED: {name}: {expression}")
    print(f"PASS: {name}")


def require_true(name, condition):
    if condition is not True and condition is not sp.S.true:
        raise ArithmeticError(f"FAILED: {name}: {condition}")
    print(f"PASS: {name}")


def transfer(energy, value):
    return sp.Matrix([[energy - value, -1], [1, 0]])


def monodromy(energy, values):
    matrix = sp.eye(2)
    for value in values:
        matrix = transfer(energy, value) * matrix
    return matrix


def verify():
    energy, theta, h, g = sp.symbols('E theta h g', real=True)
    beta = sp.symbols('beta', positive=True)
    t, x, y = sp.symbols('t x y', real=True)
    J = sp.Matrix([[0, -1], [1, 0]])
    R = sp.Matrix([[sp.cos(theta), -sp.sin(theta)],
                   [sp.sin(theta), sp.cos(theta)]])
    B = sp.Matrix([[sp.sqrt(beta), 0], [t/sp.sqrt(beta), 1/sp.sqrt(beta)]])
    require_zero('determinant of the elliptic conjugacy', B.det() - 1)
    conjugated = B * J * B.inv()
    require_zero('elliptic conjugacy formula', conjugated - sp.Matrix([
        [t, -beta], [(1+t*t)/beta, -t]]))
    require_zero('local density conjugacy coefficient', conjugated[0, 1] + beta)

    # Check the product derivative with the exact indexing used in the paper.
    for values in [(0,), (2, -1), (100, 0, 0), (1, -2, 3, 0)]:
        prefix = sp.eye(2)
        C = sp.zeros(2)
        projector = sp.diag(1, 0)
        for value in values:
            C += prefix.T * projector * prefix
            prefix = transfer(energy, value) * prefix
        require_zero(f'energy derivative, period {len(values)}',
                     prefix.inv()*prefix.diff(energy) + J*C)

    M = monodromy(energy, (100, 0, 0))
    discriminant = energy**3 - 100*energy**2 - 3*energy + 100
    require_zero('initial discriminant', sp.trace(M) - discriminant)
    require_zero('initial diagonal-measure monodromy entry', M[0, 1] - (1-energy**2))
    require_zero('initial D+2 factorization', discriminant+2-(energy-1)*(energy**2-99*energy-102))
    require_zero('initial D-2 factorization', discriminant-2-(energy+1)*(energy**2-101*energy+98))
    require_zero('D at 0.988', discriminant.subs(energy, sp.Rational(988, 1000))-sp.Rational(386030272, 10**9))
    require_zero('D at 0.992', discriminant.subs(energy, sp.Rational(992, 1000))+sp.Rational(406208512, 10**9))
    require_zero('upper-cluster derivative at 100', sp.diff(discriminant, energy).subs(energy, 100)-9997)
    require_true('initial upper-band width bound', sp.Rational(4, 9997) < sp.Rational(401, 10**6))
    require_true('initial shifted clusters are separated', sp.Rational(4, 9997) < sp.Rational(2, 1000))

    # Enlarging an unchanged period must not divide a local spectral density.
    A = M.subs(energy, sp.Rational(99, 100))
    require_true('density check energy is strictly elliptic', abs(sp.trace(A)) < 2)
    for repetitions in (2, 3, 5):
        C = A**repetitions
        require_true(f'enlarged-period discriminant is elliptic, factor {repetitions}', abs(sp.trace(C)) < 2)
        require_zero(f'local density independent of period factor {repetitions}',
                     C[0, 1]**2/(4-sp.trace(C)**2)-A[0, 1]**2/(4-sp.trace(A)**2))
    free = transfer(energy, 0)
    require_zero('free local-density normalization squared',
                 free[0, 1]**2/(4-sp.trace(free)**2)-1/(4-energy**2))

    L = sp.Matrix([[x, y], [t, -x]])
    require_zero('conjugacy derivative contributes zero to phase trace',
                 sp.trace(J*(R.T*L*R-L)))
    S1, S2 = sp.diag(1, -1), sp.Matrix([[0, 1], [1, 0]])
    require_zero('adjoint action on first symmetric basis vector',
                 R*S1*R.T-sp.cos(2*theta)*S1-sp.sin(2*theta)*S2)
    require_zero('adjoint action on second symmetric basis vector',
                 R*S2*R.T+sp.sin(2*theta)*S1-sp.cos(2*theta)*S2)
    adjoint = sp.Matrix([[sp.cos(2*theta), -sp.sin(2*theta)],
                         [sp.sin(2*theta), sp.cos(2*theta)]])
    require_zero('homological equation is invertible in elliptic region',
                 (adjoint-sp.eye(2)).det()-4*sp.sin(theta)**2)
    X = x*S1+y*S2
    S = R*X*R.T-X
    normalized = (sp.eye(2)-h*X)*(sp.eye(2)-h*(g*J+S))*R*(sp.eye(2)+h*X)
    require_zero('adiabatic first-order nonrotational cancellation',
                 normalized.diff(h).subs(h, 0)+g*J*R)

    # The derivative of the sole boundary bond is the conserved current.
    a, b, c, d = sp.symbols('a b c d', real=True)
    z0, zlast = a+sp.I*b, c+sp.I*d
    phase = sp.cos(theta)+sp.I*sp.sin(theta)
    hf = -sp.I*sp.conjugate(phase)*sp.conjugate(z0)*zlast + sp.I*phase*sp.conjugate(zlast)*z0
    current = 2*sp.im(phase*z0*sp.conjugate(zlast))
    require_zero('boundary Hellmann-Feynman derivative equals minus current', hf+current)
    distance = sp.symbols('distance', positive=True)
    require_zero('Combes-Thomas conjugation norm budget',
                 2*sp.sinh(sp.asinh(distance/4))-distance/2)
    require_zero('Cayley-Hamilton for transfer matrices', A*A-sp.trace(A)*A+sp.eye(2))
    require_zero('three-block inverse identity', A+A.inv()-sp.trace(A)*sp.eye(2))
    require_true('geometric total amplitude', sp.Rational(4, 3)*sp.Rational(1, 1000) < sp.Rational(2, 1000))
    require_true('singular-cluster mass lower bound',
                 1-sp.Rational(2)/sp.Rational(97998, 1000)**2 > sp.Rational(99979, 100000))


def rejection_checks():
    for name, expression in [('wrong free normalization', sp.Integer(1)),
                             ('wrong matrix entry', sp.Matrix([[0, 0], [1, 0]]))]:
        try:
            require_zero(name, expression)
        except ArithmeticError:
            print(f'PASS: rejected {name}')
        else:
            raise RuntimeError(f'Checker accepted {name}')


if __name__ == '__main__':
    print(f'Python {sys.version.split()[0]}; SymPy {sp.__version__}; optimization={sys.flags.optimize}')
    verify()
    rejection_checks()
    print('All checks passed. The analytic proof requires the written mathematical review.')
