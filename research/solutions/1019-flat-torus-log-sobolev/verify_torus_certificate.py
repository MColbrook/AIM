"""Exact Fourier moments and rational witness for AIM 1019.
This checks arithmetic in the proof; the entropy remainder is proved there.
Run with Python 3. No third-party dependencies.
"""
from collections import defaultdict
from fractions import Fraction as F

steps=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
poly={(0,0):F(1)}
moments=[]
for power in range(1,5):
    out=defaultdict(F)
    for (a,b),c in poly.items():
        for x,y in steps: out[a+x,b+y]+=c/2
    poly=dict(out)
    moments.append(poly.get((0,0),F(0)))
assert moments==[F(0),F(3,2),F(3,2),F(45,8)]
eps=F(1,6)
m2,m3,m4=moments[1:]
energy=eps**2*m2
entropy_lower=2*eps**2*m2+F(2,3)*eps**3*m3-eps**4*(F(8,27)*m4+m2*m2/2)
assert energy==F(1,24)
assert entropy_lower==F(2669,31104)
assert energy/entropy_lower==F(1296,2669)<F(1,2)
assert F(787,1728)<F(1,2)<F(941,1805)
print("PASS: exact moments",moments)
print("PASS: entropy >=",entropy_lower,"and alpha <=",energy/entropy_lower)
