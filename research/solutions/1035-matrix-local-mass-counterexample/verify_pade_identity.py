"""Exact coefficient checks for the elementary Padé identity in AIM 1035.
The all-degree identity is proved by integration by parts in the manuscript.
These finite checks guard against transcription and indexing errors.
"""
from fractions import Fraction as F
from math import factorial as fac

for n in range(1,17):
    q=[F((-1)**(n+k)*fac(2*n-1-k)*fac(n),
         fac(n-1)*fac(n-k)*fac(k)) for k in range(n+1)]
    p=[F((-1)**n*fac(2*n-1-k),fac(n-1-k)*fac(k)) for k in range(n)]
    assert q[-1]==1
    for degree in range(2*n+9):
        coeff=sum((q[k]/fac(degree-k) for k in range(min(n,degree)+1)),F())
        if degree<n: coeff-=p[degree]
        if degree<2*n:
            expected=F()
        else:
            j=degree-2*n
            # Integral t^(n+j)(1-t)^(n-1) / ((n-1)! j!)
            expected=F(fac(n+j),fac(2*n+j)*fac(j))
        assert coeff==expected,(n,degree,coeff,expected)
print("PASS: monicity and remainder coefficients for n=1,...,16")
