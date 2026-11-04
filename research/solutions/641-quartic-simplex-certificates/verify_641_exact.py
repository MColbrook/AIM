#!/usr/bin/env python3
"""Exact certificate for Bos's quartic Fejer inequality on a tetrahedron.

Standard library only. Every algebraic operation is over Q(sqrt(5),sqrt(3/7)).
The certificate does not use numerical optimization or floating point tests.
The last step uses the known planar quartic Fejer inequality (Bos, 1983/2023).
"""
from fractions import Fraction as Fr
from itertools import combinations, permutations
from math import comb, lcm
import json
from pathlib import Path


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


class E:
    """A+B*r+C*q+D*r*q, r^2=5 and q^2=3/7."""
    __slots__ = ('c',)
    def __init__(self,a=0,b=0,c=0,d=0):
        self.c = tuple(map(Fr,(a,b,c,d)))
    @staticmethod
    def cast(z):
        if isinstance(z,E): return z
        if isinstance(z,(int,Fr)): return E(z)
        return NotImplemented
    def __add__(self,z):
        z=E.cast(z)
        if z is NotImplemented: return z
        return E(*(a+b for a,b in zip(self.c,z.c)))
    __radd__=__add__
    def __neg__(self):return E(*(-a for a in self.c))
    def __sub__(self,z):
        z=E.cast(z)
        if z is NotImplemented:return z
        return self+-z
    def __rsub__(self,z):
        z=E.cast(z)
        if z is NotImplemented:return z
        return z+-self
    def __mul__(self,z):
        z=E.cast(z)
        if z is NotImplemented:return z
        ans=[Fr(0)]*4
        for i,a in enumerate(self.c):
            if a:
                for j,b in enumerate(z.c):
                    if b:
                        fac=(5 if i&j&1 else 1)*(Fr(3,7) if i&j&2 else 1)
                        ans[i^j]+=a*b*fac
        return E(*ans)
    __rmul__=__mul__
    def __truediv__(self,z):
        if isinstance(z,(int,Fr)):return E(*(a/z for a in self.c))
        return NotImplemented
    def __pow__(self,n):
        check(isinstance(n,int) and n>=0,'invalid algebraic exponent')
        ans=E(1);base=self
        while n:
            if n&1:ans=ans*base
            n//=2
            if n:base=base*base
        return ans
    def __bool__(self):return any(self.c)
    def __eq__(self,z):
        z=E.cast(z)
        return z is not NotImplemented and self.c==z.c
    def __repr__(self):return repr(self.c)


class P:
    """Polynomial in n indeterminates with exact E coefficients."""
    __slots__=('n','d')
    def __init__(self,n,d):
        self.n=n;self.d={a:E.cast(c) for a,c in d.items() if E.cast(c)}
    @staticmethod
    def const(n,z):return P(n,{(0,)*n:E.cast(z)})
    @staticmethod
    def var(n,i):
        a=[0]*n;a[i]=1;return P(n,{tuple(a):E(1)})
    def cast(self,z):
        if isinstance(z,P):
            check(z.n==self.n,'polynomial dimension mismatch');return z
        z=E.cast(z)
        if z is NotImplemented:return z
        return P.const(self.n,z)
    def __add__(self,z):
        z=self.cast(z)
        if z is NotImplemented:return z
        d=self.d.copy()
        for a,c in z.d.items():
            d[a]=d.get(a,E(0))+c
            if not d[a]:del d[a]
        return P(self.n,d)
    __radd__=__add__
    def __neg__(self):return P(self.n,{a:-c for a,c in self.d.items()})
    def __sub__(self,z):
        z=self.cast(z)
        if z is NotImplemented:return z
        return self+-z
    def __rsub__(self,z):
        z=self.cast(z)
        if z is NotImplemented:return z
        return z+-self
    def __mul__(self,z):
        z=self.cast(z)
        if z is NotImplemented:return z
        d={}
        for a,c in self.d.items():
            for b,h in z.d.items():
                ab=tuple(i+j for i,j in zip(a,b))
                d[ab]=d.get(ab,E(0))+c*h
        return P(self.n,d)
    __rmul__=__mul__
    def __truediv__(self,z):return P(self.n,{a:c/z for a,c in self.d.items()})
    def __pow__(self,n):
        check(isinstance(n,int) and n>=0,'invalid polynomial exponent')
        ans=P.const(self.n,1);base=self
        while n:
            if n&1:ans=ans*base
            n//=2
            if n:base=base*base
        return ans
    def __eq__(self,z):
        z=self.cast(z)
        return z is not NotImplemented and self.d==z.d


r=E(0,1);q=E(0,0,1)

def cardinal(x):
    """Homogeneous degree-four cardinal formulas, valid in every dimension.

    Relative to the displayed 2022 preprint formulas, the midpoint bracket
    includes the term (76-14*r)*s1^2; the second linear edge term uses x_j.
    These corrections are verified here from cardinal interpolation itself.
    """
    n=len(x);s1=sum(x);s2=sum(u**2 for u in x);s3=sum(u**3 for u in x)
    out=[]
    for u in x:
        out.append(2*u*((101+17*r)/11*u**3-(13+2*r)*u**2*s1
            +(130+27*r)/22*u*s1**2-(259+51*r)/264*s1**3
            +s2*((9+r)/8*s1-(24+17*r)/22*u)
            +s3*((45+3*r)/44-Fr(5,3))))
    for i,j in combinations(range(n),2):
        u,v=x[i],x[j]
        U=(61+7*r)/22*(u**2+v**2)+(3+9*r)/11*u*v \
            -(41+13*r)/22*(u+v)*s1+(8+2*r)/11*s1**2-(7-r)/11*s2
        V=(7+r)/2*(v**2-u**2)+(5+r)/2*(u-v)*s1
        out.extend([Fr(49,6)*u*v*(U+q*V),Fr(49,6)*u*v*(U-q*V)])
        out.append(Fr(4,33)*u*v*((100-8*r)*(u**2+v**2)
            +(672-96*r)*u*v+(62*r-302)*(u+v)*s1
            +(82-40*r)*s2+(76-14*r)*s1**2))
    for i,j,k in combinations(range(n),3):
        for a,b,c in [(i,j,k),(j,i,k),(k,i,j)]:
            out.append((73+r)/2*x[a]*x[b]*x[c]
                *((1+r)*x[a]+(3-r)/2*(x[b]+x[c])-s1))
    for i,j,k,l in combinations(range(n),4):
        out.append(256*x[i]*x[j]*x[k]*x[l])
    return out


def nodes(n):
    out=[]
    for i in range(n):
        z=[E(0)]*n;z[i]=E(1);out.append(z)
    for i,j in combinations(range(n),2):
        for t in [(1+q)/2,(1-q)/2,E(Fr(1,2))]:
            z=[E(0)]*n;z[i]=t;z[j]=1-t;out.append(z)
    for i,j,k in combinations(range(n),3):
        for a,b,c in [(i,j,k),(j,i,k),(k,i,j)]:
            z=[E(0)]*n;z[a]=(4+r)/11;z[b]=z[c]=(7-r)/22;out.append(z)
    for inds in combinations(range(n),4):
        z=[E(0)]*n
        for i in inds:z[i]=E(Fr(1,4))
        out.append(z)
    return out


def coefficient_positive(c):
    """Exact sign of an element of Q(sqrt5)."""
    A,B,C,D=c.c
    check(C==D==0,'unexpected sqrt(3/7) coefficient')
    if B==0:return A>0
    if A>=0 and B>=0:return True
    if A<=0 and B<=0:return False
    return 5*B*B>A*A if B>0 else A*A>5*B*B


def verify(output_directory=None):
    n=4;ns=nodes(n);N=comb(n+3,4)
    check(len(ns)==N==35,'wrong number of interpolation nodes')
    selected=set()
    for z in ns:
        check(sum(z)==1,'node not in barycentric hyperplane')
        vals=cardinal(z)
        one=[i for i,c in enumerate(vals) if c==1]
        check(len(one)==1 and all(c==0 or c==1 for c in vals),'cardinal identity failed')
        selected.add(one[0])
    check(len(selected)==N,'duplicate cardinal row')
    print('PASS: all 35 x 35 cardinal values verified in the exact number field.',flush=True)
    x=[P.var(n,i) for i in range(n)]
    ls=cardinal(x)
    F=sum(x)**8-sum(p**2 for p in ls)
    check(all(sum(a)==8 for a in F.d),'deficit is not homogeneous of degree eight')
    for c in F.d.values():check(c.c[2]==c.c[3]==0,'edge radical did not cancel')
    for pi in permutations(range(n)):
        permuted={tuple(a[pi[i]] for i in range(n)):c for a,c in F.d.items()}
        check(permuted==F.d,'deficit not symmetric')
    print('PASS: exact degree-eight deficit is symmetric and belongs to Q(sqrt5).',flush=True)
    # Linear substitution x_i = y_i+...+y_3, evaluated independently by polynomial arithmetic.
    powers=[[sum(x[i:])**k for k in range(9)] for i in range(n)]
    G=P.const(n,0)
    for a,c in F.d.items():
        pp=P.const(n,c)
        for i,k in enumerate(a):pp=pp*powers[i][k]
        G=G+pp
    R=P(n,{a:c for a,c in G.d.items() if a[3]>0})
    check(len(R.d)==116,'unexpected remainder term count')
    Q=sum(x)**12*R
    check(len(Q.d)==1536,'unexpected elevated term count')
    check(all(coefficient_positive(c) for c in Q.d.values()),'nonpositive elevated coefficient')
    # Uniform, elementary rational interval check supplies an independent sign test.
    lo=2236067977499789;hi=2236067977499790;scale=10**15
    check(lo*lo<5*scale*scale<hi*hi,'invalid square-root enclosure')
    lower=[c.c[0]+c.c[1]*Fr(lo if c.c[1]>=0 else hi,scale) for c in Q.d.values()]
    check(min(lower)==60,'unexpected coefficient lower bound')
    print('PASS: all 1536 coefficients of (u+v+w+t)^12 R are positive; each is at least 60.',flush=True)
    den=lcm(*(a.denominator for c in R.d.values() for a in c.c))
    check(den==363,'unexpected coefficient denominator')
    def packed(p):
        out=[]
        for a,c in sorted(p.d.items()):
            A,B,C,D=c.c
            check(C==D==0 and (A*den).denominator==(B*den).denominator==1,'invalid field packing')
            out.append({'alpha':list(a),'A':int(A*den),'B':int(B*den)})
        return out
    result={'variables':['u','v','w','t'],'root':5,'denominator':den,'raise_degree':12,
        'remainder_coefficients':packed(R),'elevated_coefficients':packed(Q),
        'sqrt_lower_num':lo,'sqrt_upper_num':hi,'sqrt_den':scale,
        'coefficient_count':len(Q.d),'minimum_rational_lower_bound':60}
    if output_directory:
        p=Path(output_directory);p.mkdir(parents=True,exist_ok=True)
        (p/'fejer_641_certificate_independent.json').write_text(json.dumps(result,indent=2))
    return result


if __name__=='__main__':
    import sys
    verify(sys.argv[1] if len(sys.argv)>1 else None)
