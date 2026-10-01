#!/usr/bin/env python3
"""Optional symbolic and high-precision cross-checks for AIM 558.

Dependencies: sympy and mpmath. Audited with SymPy 1.14.0 and mpmath 1.3.0.
Run: python symbolic_audit_558.py
This does not replace the proof or constitute formal verification.
"""
import sympy as sp
import mpmath as mp


def require(condition, message):
    if not condition:
        raise AssertionError(message)
    print("PASS:", message)


def main():
    a = sp.symbols("a", real=True)
    r = sp.Matrix([[1, sp.Rational(4, 5), sp.Rational(4, 5)],
                   [sp.Rational(4, 5), 1, sp.Rational(3, 10)],
                   [sp.Rational(4, 5), sp.Rational(3, 10), 1]])
    k = (r.inv() + 9*sp.eye(3))/10
    c = (213*a+370)/(5*(49*a+10))
    h = a*k-(a-1)*sp.diag(c, 1, 1)
    s = h.inv()
    factor = -a*(a-10)*(7311*a-64010)/((3*a+70)*(49*a+10)*(213*a+370))
    require(sp.factor(s[0, 0]-1/c) == 0,
            "S_11(tbar)=1/c(a) identically")
    require(sp.factor(s[1, 1]-1-factor) == 0 and s[1, 1] == s[2, 2],
            "The general-alpha leaf residual has the stated exact factorization")
    print("S_22-1 =", factor)
    hplus = (49*a+10)/10
    schur = 37*a/5-(a-1)*c-32*a*a/hplus
    require(sp.factor(schur-c) == 0,
            "The comparison-point Schur complement equals c(a)")

    y = sp.symbols("y", real=True)
    x = 5*(649*y-100)/(6413*y-3700)
    hs = 11*k-10*sp.diag(1/x, 1/y, 1/y)
    ss = hs.inv()
    require(sp.factor(ss[0, 0]-x) == 0,
            "The displayed x(y) satisfies first-coordinate stationarity at alpha=11")
    poly = 303828701*y**3-573214290*y**2+295302000*y-25900000
    ratio = sp.factor((ss[1, 1]-y)/poly)
    expected_ratio = -11*y/((649*y-100)*(803*y-700)*(6413*y-3700))
    require(sp.factor(ratio-expected_ratio) == 0,
            "The supplemental stationarity cubic has exactly the stated prefactor")
    print("(S_22-y)/P(y) =", ratio)

    # Independent numerical solution of the original two precision equations,
    # rather than solving the already-reduced cubic.
    mp.mp.dps = 90
    km = mp.matrix([[mp.mpf(int(k[i, j].p))/int(k[i, j].q)
                     for j in range(3)] for i in range(3)])

    def residual(t, u):
        sm = (11*km-10*mp.diag([t, u, u]))**-1
        return sm[0, 0]-1/t, sm[1, 1]-1/u

    t, u = mp.findroot(residual, (mp.mpf("0.988"), mp.mpf("1.00027")),
                       tol=mp.mpf("1e-80"))
    error = max(abs(z) for z in residual(t, u))
    least_eigenvalue = min(mp.eigsy(11*km-10*mp.diag([t, u, u]),
                                   eigvals_only=True))
    require(t > 0 and u > 0 and error < mp.mpf("1e-75")
            and least_eigenvalue > 0,
            "90-digit precision solution is feasible and stationary to <1e-75 residual")
    require(1/t > 1 and 0 < 1/u < 1,
            "The numerical variances reproduce the exact counterexample ordering")
    print("v_1(11) =", mp.nstr(1/t, 70))
    print("v_2(11) = v_3(11) =", mp.nstr(1/u, 70))
    print("maximum stationarity residual =", mp.nstr(error, 8))
    print("smallest eigenvalue of H =", mp.nstr(least_eigenvalue, 30))


if __name__ == "__main__":
    main()
