"""Finite exact transcription checks for the AIM 1032 counterexample.

Only Python's standard library is used. No floating-point eigensolver,
filesystem writes, network calls, or unbounded experiments are performed.
The all-degree statements are proved analytically in the manuscript.

Checks cover all n mod 3: rectangular factors, column stochasticity,
all compound minors, positive principal minors and adjacent-move minors
for n=3,...,17; characteristic polynomials and zero multiplicity for
n=3,...,11. Characteristic coefficients use Faddeev--LeVerrier in exact
rational arithmetic.
"""

from fractions import Fraction as F
from itertools import combinations
import json


def mat(rows, cols):
    return [[F(0) for _ in range(cols)] for _ in range(rows)]


def mul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def det(A):
    B = [row[:] for row in A]
    value = F(1)
    for k in range(len(B)):
        pivot = next((i for i in range(k, len(B)) if B[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            B[k], B[pivot] = B[pivot], B[k]
            value = -value
        x = B[k][k]
        value *= x
        for i in range(k+1, len(B)):
            if B[i][k]:
                ratio = B[i][k]/x
                for j in range(k+1, len(B)):
                    B[i][j] -= ratio*B[k][j]
                B[i][k] = F(0)
    return value


def minor(A, I, J):
    return det([[A[i][j] for j in J] for i in I])


def char(A):
    n = len(A)
    B = mat(n, n)
    for i in range(n):
        B[i][i] = F(1)
    coeff = [F(1)]
    for k in range(1, n+1):
        B = mul(A, B)
        ck = -sum(B[i][i] for i in range(n))/k
        coeff.append(ck)
        for i in range(n):
            B[i][i] += ck
    return list(reversed(coeff))


summary = []
for n in range(3, 18):
    q, r = divmod(n, 3)
    c = [F(j*(j-1)*(j-2), n*(n-1)*(n-2)) if j >= 3 else F(0)
         for j in range(n+1)]
    A = mat(n+1, n+1)
    for j in range(n+1):
        if j < n:
            A[j+1][j] = 1-c[j]
        if j >= 3:
            A[j-2][j] = c[j]
    assert all(sum(A[i][j] for i in range(n+1)) == 1
               for j in range(n+1))
    I1 = list(range(1, n+1, 3))
    I2 = list(range(2, n+1, 3))
    I3 = list(range(3, n+1, 3))
    d1 = q+(r >= 1)
    d2 = q+(r == 2)
    assert (len(I1), len(I2), len(I3)) == (d1, d2, q)
    U1 = mat(d2, d1)
    U2 = mat(q, d2)
    L = mat(d1, q)
    for a in range(d2):
        U1[a][a] = 1-c[1+3*a]
        if a+1 < d1:
            U1[a][a+1] = c[4+3*a]
    for a in range(q):
        U2[a][a] = 1-c[2+3*a]
        if a+1 < d2:
            U2[a][a+1] = c[5+3*a]
        L[a][a] = c[3+3*a]
        if a+1 < d1:
            L[a+1][a] = 1-c[3+3*a]
    for factor, I, J in ((U1, I2, I1), (U2, I3, I2), (L, I1, I3)):
        assert factor == [[A[i][j] for j in J] for i in I]
        assert all(x >= 0 for row in factor for x in row)
    C = mul(U2, mul(U1, L))
    count = 0
    for p in range(1, q+1):
        sets = list(combinations(range(q), p))
        for I in sets:
            assert minor(C, I, I) > 0
            for J in sets:
                m = minor(C, I, J)
                assert m >= 0
                count += 1
                left = set(I)-set(J)
                right = set(J)-set(I)
                if (len(left) == len(right) == 1 and
                        abs(next(iter(left))-next(iter(right))) == 1):
                    assert m > 0
    if n <= 11:
        ac = char(A)
        cc = char(C)
        expected = [F(0) for _ in range(n+2)]
        for degree, value in enumerate(cc):
            expected[r+1+3*degree] = value
        assert ac == expected
        assert next(i for i, x in enumerate(ac) if x) == r+1
    summary.append({'n': n, 'r': r, 'shape': [d1, d2, q],
                    'compound_minors_checked': count,
                    'charpoly_checked': n <= 11})

print('PASS: exact factors, stochasticity, all compound minors, principal '
      'minors and adjacent-move positivity for n=3,...,17')
print('PASS: exact characteristic identity and zero multiplicity for n=3,...,11')
print(json.dumps(summary))

def rising(x, n):
    out = F(1)
    for j in range(n):
        out *= x+j
    return out

from math import comb
for ell in range(13):
    integral_moment = comb(3*ell,ell)*sum(
        (F((-1)**j*comb(2*ell,j),3*ell+3*j+1) for j in range(2*ell+1)),F(0))
    product_moment = rising(F(1,3),ell)/rising(F(1),ell)
    product_moment *= rising(F(1),3*ell)/rising(F(4,3),3*ell)
    if integral_moment != product_moment:
        raise ArithmeticError('Beta-product moment mismatch '+str(ell))
print('PASS: exact beta-product moment identity for ell=0,...,12')
