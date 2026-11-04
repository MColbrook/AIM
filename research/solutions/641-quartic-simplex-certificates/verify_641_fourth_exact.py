#!/usr/bin/env python3
"""Standard-library verification of the all-dimensional quartic fourth-power bound.

Imports exact polynomial/number-field arithmetic from verify_641_exact.py.
Independently builds the stable power-sum deficit from the cardinal formulas,
checks exact evaluations in different dimensions, and checks an exact witness
for the dimension-independent directional derivative inequality.
"""
from verify_641_exact import E, P, cardinal, check, r, q, Fr
from itertools import combinations
from functools import lru_cache
from collections import Counter
from math import factorial
from pathlib import Path
import json

ZERO=E(0)


def add_term(dic, powers, c):
    alpha=[0]*16
    for index,power in powers:
        check(1<=index<=16,'invalid power-sum index')
        alpha[index-1]+=power
    alpha=tuple(alpha)
    dic[alpha]=dic.get(alpha,ZERO)+c
    if not dic[alpha]:del dic[alpha]


def stable_deficit():
    """Build H(p1,...,p16)=p1^16-sum(cardinal^4) by distinct-index sums."""
    H={}
    add_term(H,[(1,16)],E(1))
    z,s1,s2,s3=[P.var(4,i) for i in range(4)]
    V=2*z*((101+17*r)/11*z**3-(13+2*r)*z**2*s1
        +(130+27*r)/22*z*s1**2-(259+51*r)/264*s1**3
        +s2*((9+r)/8*s1-(24+17*r)/22*z)
        +s3*((45+3*r)/44-Fr(5,3)))
    for (a,b,c,d),co in (V**4).d.items():
        add_term(H,[(a,1),(1,b),(2,c),(3,d)],-co)
    z,w,s1,s2=[P.var(4,i) for i in range(4)]
    U=(61+7*r)/22*(z**2+w**2)+(3+9*r)/11*z*w \
        -(41+13*r)/22*(z+w)*s1+(8+2*r)/11*s1**2-(7-r)/11*s2
    W=(7+r)/2*(w**2-z**2)+(5+r)/2*(z-w)*s1
    plus=Fr(49,6)*z*w*(U+q*W);minus=Fr(49,6)*z*w*(U-q*W)
    mid=Fr(4,33)*z*w*((100-8*r)*(z**2+w**2)+(672-96*r)*z*w
        +(62*r-302)*(z+w)*s1+(82-40*r)*s2+(76-14*r)*s1**2)
    for (a,b,c,d),co in (plus**4+minus**4+mid**4).d.items():
        # 1/2 sum_{i != j} x_i^a x_j^b = (p_a p_b-p_{a+b})/2.
        add_term(H,[(a,1),(b,1),(1,c),(2,d)],-co/2)
        add_term(H,[(a+b,1),(1,c),(2,d)],co/2)
    z,w,v,s1=[P.var(4,i) for i in range(4)]
    T=(73+r)/2*z*w*v*((1+r)*z+(3-r)/2*(w+v)-s1)
    for (a,b,c,d),co in (T**4).d.items():
        # Each distinguished triple is counted twice by ordered distinct triples.
        add_term(H,[(a,1),(b,1),(c,1),(1,d)],-co/2)
        add_term(H,[(a+b,1),(c,1),(1,d)],co/2)
        add_term(H,[(a+c,1),(b,1),(1,d)],co/2)
        add_term(H,[(b+c,1),(a,1),(1,d)],co/2)
        add_term(H,[(a+b+c,1),(1,d)],-co)
    # e4(x_i^4)=(p4^4-6 p4^2 p8+3 p8^2+8 p4 p12-6 p16)/24.
    for powers,coeff in [([(4,4)],1), ([(4,2),(8,1)],-6),
                         ([(8,2)],3), ([(4,1),(12,1)],8), ([(16,1)],-6)]:
        add_term(H,powers,E(-Fr(256**4*coeff,24)))
    check(len(H)==163,'unexpected stable deficit term count')
    for a,c in H.items():
        check(sum((i+1)*v for i,v in enumerate(a))==16,'wrong weighted degree')
        check(c.c[2]==c.c[3]==0,'uncancelled edge radical')
    return H


def evaluate(F,values):
    ans=E(0)
    powers=[[v**j for j in range(17)] for v in values]
    for alpha,c in F.items():
        term=c
        for i,a in enumerate(alpha):
            if a:term=term*powers[i][a]
        ans=ans+term
    return ans


def derivatives(H):
    D1={};D0={}
    for a,c in H.items():
        for j,k in enumerate(a):
            if k:
                b=list(a);b[j]-=1
                if j==0:
                    b=tuple(b);D1[b]=D1.get(b,ZERO)+k*c
                else:
                    b[j-1]+=1;b=tuple(b);D0[b]=D0.get(b,ZERO)+(j+1)*k*c
    return ({a:c for a,c in D0.items() if c}, {a:c for a,c in D1.items() if c})


@lru_cache(None)
def partitions(total, maximum=None):
    if total==0:return ((),)
    if maximum is None or maximum>total:maximum=total
    ans=[]
    for first in range(maximum,0,-1):
        ans.extend((first,)+rest for rest in partitions(total-first,first))
    return tuple(ans)


@lru_cache(None)
def power_product_to_monomial(lam):
    """Coefficient of a fixed monomial; use backward rather than forward multiplication."""
    if not lam:return {():1}
    k=lam[-1];old=power_product_to_monomial(lam[:-1]);ans={}
    for nu in partitions(sum(lam)):
        coefficient=0
        for j,a in enumerate(nu):
            if a>=k:
                mu=list(nu);mu[j]-=k
                mu=tuple(sorted((v for v in mu if v),reverse=True))
                coefficient+=old.get(mu,0)
        if coefficient:ans[nu]=coefficient
    return ans


def monomial_coefficients(F):
    ans={}
    for a,c in F.items():
        lam=tuple(j+1 for j,k in enumerate(a) for _ in range(k))
        for mu,mult in power_product_to_monomial(lam).items():
            ans[mu]=ans.get(mu,ZERO)+mult*c
    return {a:c for a,c in ans.items() if c}


def multiply_p1(C):
    degree=sum(next(iter(C)))
    out={}
    for nu in partitions(degree+1):
        c=E(0)
        for j in range(len(nu)):
            mu=list(nu);mu[j]-=1
            mu=tuple(sorted((v for v in mu if v),reverse=True))
            c=c+C.get(mu,ZERO)
        if c:out[nu]=c
    return out


def positive(c):
    A,B,C,D=c.c
    check(C==D==0,'unexpected coefficient field')
    if B==0:return A>0
    if A>=0 and B>=0:return True
    if A<=0 and B<=0:return False
    return 5*B*B>A*A if B>0 else A*A>5*B*B


def nonnegative(c):return c==0 or positive(c)


def orbit(mu):
    o=factorial(len(mu))
    for m in Counter(mu).values():o//=factorial(m)
    return o


def majorizes(a,b):
    return len(a)==len(b) and sum(a)==sum(b) and all(sum(a[:j])>=sum(b[:j]) for j in range(1,len(a)))


def verify(certificate_path):
    H=stable_deficit()
    D0,D1=derivatives(H)
    print('PASS: stable fourth-power deficit independently derived (163 power-sum terms).',flush=True)
    # Exact test points supplement the formal distinct-index derivation.
    for n in [2,3,4,5,6,9,17]:
        vals=[E(Fr(i+1,n*(n+1)//2)) for i in range(n)]
        pk=[sum(x**j for x in vals) for j in range(1,17)]
        target=sum(vals)**16-sum(f**4 for f in cardinal(vals))
        check(evaluate(H,pk)==target,'stable deficit evaluation mismatch')
    # Independently differentiate along the all-ones direction at a rational point.
    n=5;t=P.var(1,0)
    vals=[Fr(i+1,n*(n+1)//2) for i in range(n)]
    direct=(sum(vals)+n*t)**16-sum(f**4 for f in cardinal([v+t for v in vals]))
    pk=[sum(E(v)**j for v in vals) for j in range(1,17)]
    check(direct.d.get((1,),ZERO)==evaluate(D0,pk)+n*evaluate(D1,pk),'directional derivative mismatch')
    print('PASS: exact cardinal/power-sum evaluations in seven dimensions and derivative check.',flush=True)
    C0=monomial_coefficients(D0);C1=monomial_coefficients(D1)
    for _ in range(8):C0=multiply_p1(C0);C1=multiply_p1(C1)
    C5={a:C0.get(a,ZERO)+5*C1.get(a,ZERO) for a in set(C0)|set(C1)}
    check(len(C1)==1255 and all(nonnegative(c) for c in C1.values()),'invalid slope coefficient certificate')
    check(sum(not nonnegative(c) for c in C5.values())==11,'wrong negative coefficient count')
    cert=json.loads(Path(certificate_path).read_text())
    check(cert['denominator']==395307 and cert['elevation']==8 and cert['degree']==23,'wrong certificate metadata')
    den=cert['denominator']
    def unpack(rows):
        ans={}
        for row in rows:
            a=tuple(row['partition']);check(a not in ans,'duplicate partition')
            ans[a]=E(Fr(row['A'],den),Fr(row['B'],den))
        return ans
    check(unpack(cert['D1_coefficients'])==C1,'certificate slope coefficients mismatch')
    check(unpack(cert['D5_coefficients'])==C5,'certificate D5 coefficients mismatch')
    coverage={}
    lengths=set()
    for row in cert['payments']:
        a=tuple(row['positive']);b=tuple(row['negative'])
        c=E(Fr(row['A'],den),Fr(row['B'],den))
        check(majorizes(a,b) and positive(c),'invalid same-length Muirhead payment')
        lengths.add(len(a))
        coverage[a]=coverage.get(a,ZERO)+c
        coverage[b]=coverage.get(b,ZERO)-c
    residual=unpack(cert['residual_mean_coefficients'])
    for a,c in residual.items():
        check(nonnegative(c),'negative residual coefficient')
        coverage[a]=coverage.get(a,ZERO)+c
    coverage={a:c for a,c in coverage.items() if c}
    expected={a:orbit(a)*c for a,c in C5.items() if c}
    check(coverage==expected,'Muirhead transport identity failed')
    check(len(cert['payments'])==28 and lengths=={3,4,5},'unexpected transport structure')
    print('PASS: all 1255 slope coefficients nonnegative; 28 exact, equal-length Muirhead payments.',flush=True)
    print('PASS: the derivative certificate holds for every number of variables, hence proves the fourth-power induction.',flush=True)
    return True


if __name__=='__main__':
    import sys
    path=sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('fourth_641_muirhead_certificate.json')
    verify(path)
