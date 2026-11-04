#!/usr/bin/env python3
"""Exact identities for an elementary proof of the known planar Fejer base.

Python 3 standard library only.  The proof reduces a symmetric ternary octic
to its boundary and two-equal-coordinate restrictions by concavity in e3.
This file checks every polynomial identity and every algebraic sign used.
It imports the frozen cardinal formulas and exact arithmetic without editing
them.  No certificate file, numerical optimization or symbolic package is used.
"""
from verify_641_exact import E, P, Fr, r, cardinal, check, coefficient_positive


def deficit(x):
    return sum(x)**8-sum(L**2 for L in cardinal(x))


def verify():
    x,y,z=[P.var(3,i) for i in range(3)]
    e1=x+y+z; e2=x*y+x*z+y*z; e3=x*y*z
    formal=(20*e1**6*e2+(4623-57*r)/11*e1**5*e3
            -360*e1**4*e2**2+(-125333+7219*r)/33*e1**3*e2*e3
            +2100*e1**2*e2**3+(-136228+14134*r)/11*e1**2*e3**2
            +(29764-2772*r)/3*e1*e2**2*e3-3920*e2**4
            +(77200-3296*r)/3*e2*e3**2)
    check(deficit([x,y,z])==formal,'elementary-symmetric deficit identity failed')
    c0=(-136228+14134*r)/11
    c1=(77200-3296*r)/3
    upper=(-376852+90950*r)/99
    check(c0+c1/3==upper,'concavity upper coefficient identity failed')
    check(coefficient_positive(c1),'e2 coefficient is not positive')
    check(coefficient_positive(-upper),'concavity upper coefficient is not negative')
    print('PASS: planar deficit identity and strict e3 concavity verified exactly.',flush=True)

    a,b=[P.var(2,i) for i in range(2)]
    zero=P.const(2,0)
    edge=20*a*b*(a-b)**2*(a*a-5*a*b+b*b)**2
    check(deficit([a,b,zero])==edge,'edge factorization failed')
    p=(-4397+383*r)/880
    q2=(15854+251*r)/330
    q1=(-121549+44817*r)/660
    q0=(39744-17344*r)/165
    quartic=a**4+2*p*a**3*b+q2*a*a*b*b+q1*a*b**3+q0*b**4
    repeated=40*a*b*(a-(3+r)/2*b)**2*quartic
    check(deficit([a,b,b])==repeated,'two-equal-coordinate factorization failed')
    print('PASS: edge and two-equal-coordinate factorizations verified exactly.',flush=True)

    A=(23382299+5935673*r)/1161600
    B=(-229907+88485*r)/1320
    C=(39579-17344*r)/165
    determinant=(-529859170431+237067014259*r)/11979000
    check(A==q2-p*p-2 and B==q1-2*p and C==q0-1,
          'square-plus-quadratic coefficient identity failed')
    check(quartic==(a*a+p*a*b+b*b)**2+b*b*(A*a*a+B*a*b+C*b*b),
          'positive quartic decomposition failed')
    check(4*A*C-B*B==determinant,'positive quadratic determinant identity failed')
    check(all(coefficient_positive(c) for c in [A,C,determinant]),
          'quadratic form is not positive definite')
    print('PASS: the remaining quartic is a square plus a positive-definite quadratic form times b^2.',flush=True)
    print('PASS: all algebraic ingredients of the independent planar Fejer proof hold.',flush=True)
    return True


if __name__=='__main__':
    verify()
