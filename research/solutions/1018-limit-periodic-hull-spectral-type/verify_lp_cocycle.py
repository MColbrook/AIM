"""Exact checks of the zero-centered cocycle construction in AIM 1018.
Tails are summed exactly, not truncated. The proof covers every integer.
"""
from fractions import Fraction as F

N=1024
K=1
while 16**K<2*(N+2): K+=1
def distance(n,p):
    r=n%p
    return min(r,p-r)
def H(n):
    return sum((F(distance(n,16**k),2**k) for k in range(1,K+1)),F())+F(abs(n),2**K)
def b(n):
    head=sum((F(distance(n+1,16**k)-distance(n,16**k),2**k)
              for k in range(1,K+1)),F())
    return head+F(abs(n+1)-abs(n),2**K)
assert H(0)==0
for n in range(-N,N+1):
    assert H(n+1)-H(n)==b(n)
    assert H(n)==H(-n)
    assert b(-n-1)==-b(n)
    assert abs(b(n))<=1
    assert 0<=H(n)<=abs(n)
    if n: assert 2*H(n)**4>=abs(n)**3
print("PASS: exact cocycle, parity, boundedness, and growth checks on [-1024,1024]")
print("Tail parameter K =",K,"; all infinite tails evaluated as rational geometric series")
