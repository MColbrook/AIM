#!/usr/bin/env python3
"""Exact verification of the all-dimensional cubic Fejer certificate.

Requirements: Python 3.10+, SymPy.  No floating-point assertions are used.
This program independently checks the cardinal-polynomial identity in six
variables, checks the two-dimensional base decomposition, checks the four
finite induction steps, and proves the remaining induction uniformly by
nonnegative coefficients in the symbolic dimension M-8.
"""
from __future__ import annotations
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import sympy as s

p = s.symbols('p0:7')
z, M, u = s.symbols('z M u')

def kernel(q):
    """Sum of squares of homogeneous cubic cardinal polynomials."""
    S, q2, q3, q4, q5, q6 = q[1:7]
    return (54*q6 + 78*S*q5 + 29*S*S*q4 - s.Rational(391,2)*q2*q4
            -18*S**3*q3 -144*S*q2*q3 +50*q3*q3
            +s.Rational(9,4)*S**4*q2 +s.Rational(47,2)*S*S*q2*q2
            +s.Rational(487,4)*q2**3)

def deficit(xs):
    ps = [len(xs)] + [sum(x**j for x in xs) for j in range(1,7)]
    return ps[1]**6-kernel(ps)

@lru_cache(None)
def partitions(n, largest=None):
    if n == 0:
        return ((),)
    largest = min(n, n if largest is None else largest)
    return tuple((j,)+a for j in range(largest,0,-1)
                 for a in partitions(n-j, min(j,n-j)))

@lru_cache(None)
def power_coefficient(parts, alpha):
    """Coefficient of x**alpha in product_j sum_i x_i**parts[j]."""
    if not parts:
        return int(all(a == 0 for a in alpha))
    j = parts[0]
    total = 0
    for i, a in enumerate(alpha):
        if a >= j:
            beta = list(alpha)
            beta[i] -= j
            total += power_coefficient(parts[1:], tuple(beta))
    return total

def orbit_coefficients(poly, degree, max_length=None):
    buckets = {}
    for exps, coeff in poly.terms():
        parts = tuple(j for j,e in enumerate(exps[1:],1) for _ in range(e))
        buckets.setdefault(exps[0], []).append((parts,coeff))
    for k in range(1, degree+1):
        for alpha in partitions(degree-k):
            if max_length is not None and len(alpha) > max_length:
                continue
            c = sum(coeff*power_coefficient(parts,alpha)
                    for parts,coeff in buckets.get(k,[]))
            yield k, alpha, s.factor(c)

def checks():
    # Independent, direct expansion of the three cardinal-polynomial types.
    x = s.symbols('x0:6')
    S = sum(x)
    p2 = sum(t*t for t in x)
    rt5 = s.sqrt(5)
    card = [t*(12*t*t-12*S*t+3*S*S-p2)/2 for t in x]
    card += [5*x[i]*x[j]*((3+rt5)*x[i]/2+(3-rt5)*x[j]/2-S)
             for i in range(6) for j in range(6) if i != j]
    from itertools import combinations
    card += [27*x[i]*x[j]*x[k] for i,j,k in combinations(range(6),3)]
    assert s.expand(sum(t*t for t in card)-kernel([6]+[sum(t**j for t in x) for j in range(1,7)])) == 0
    print('PASS: direct cardinal sum-of-squares identity (six variables).')

    v,w = s.symbols('v w')
    assert s.expand(deficit([u,v])-12*u*v*(u*u-3*u*v+v*v)**2) == 0
    E = (104*(u**3+v**3)*w*w+106*(u*u*v+u*v*v)*w*w
         -27*(u**4+v**4)*w+522*(u**3*v+u*v**3)*w+405*u*u*v*v*w
         +108*(u**5+v**5)-351*(u**4*v+u*v**4)
         +1062*(u**3*v*v+u*u*v**3))
    base = (s.Rational(262,81)*(u*u-u*v+v*v)*w**4
            +12*u*v*(u*u-3*u*v+v*v)**2+s.Rational(2,27)*w*E)
    assert s.expand(deficit([u+w/3,v+w/3,w/3])-base) == 0
    assert all(c >= 0 for c in s.Poly(s.expand((u+v+w)**4*E),u,v,w).coeffs())
    print('PASS: base cases, dimensions one and two.')

    shifted = [M]+[
        sum(comb(j,i)*p[i]*(z/M)**(j-i) for i in range(1,j+1))
        + z**j/M**(j-1) for j in range(1,7)]
    D = (p[1]+z)**6-kernel(shifted)-p[1]**6+kernel(p)
    for m,r in [(4,8),(5,5),(6,3),(7,3)]:
        q = s.Poly(s.expand((p[1]+z)**r*D.subs(M,m)),z,*p[1:])
        coeffs = list(orbit_coefficients(q,6+r,m-1))
        assert all(c >= 0 for _,_,c in coeffs)
        # At z=0 the difference vanishes identically.
        assert q.as_expr().subs(z,0) == 0
        print(f'PASS: dimension {m-1}, elevation {r}, {len(coeffs)} coefficient types.')

    q = s.Poly(s.expand(4*M**5*(p[1]+z)**2*D),z,*p[1:])
    assert q.as_expr().subs(z,0) == 0
    records = []
    for k,alpha,c in orbit_coefficients(q,8):
        shifted_c = s.Poly(s.expand(c.subs(M,u+8)),u)
        assert all(b >= 0 for b in shifted_c.all_coeffs())
        assert all(b.is_Integer for b in shifted_c.all_coeffs())
        records.append({'z_power':k,'partition':list(alpha),
                        'coefficient':str(c),
                        'shifted_coefficients_ascending':[int(shifted_c.nth(j)) for j in range(6)]})
    assert len(records) == 45
    print('PASS: all 45 symbolic coefficient types are nonnegative for M >= 8.')
    output = Path(__file__).with_name('cubic_certificate.json')
    output.write_text(json.dumps(records,indent=2)+'\n')
    print('ALL EXACT CHECKS PASSED. Certificate:', output.name)

if __name__ == '__main__':
    checks()
