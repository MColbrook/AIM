#!/usr/bin/env python3
"""Exact certificate for the negative answer to AIM problem 935 at p=4.
Only Python standard-library integers and fractions are used.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
A=[[-10,2255,-40],[-1437,0,-1914],[34,2480,6]]
v=[185,1000,-179]
M_plus=[[10102,-6298,-14,-11275,200,214],[-6298,10002,-7757,7185,-4,9570],[-14,-7757,9942,-188,-170,-12400],[-11275,7185,-188,12596,-214,4],[200,-4,-170,-214,28,188],[214,9570,-12400,4,188,15514]]
M_minus=[[9902,-6433,-8,11275,-200,218],[-6433,10002,-7646,-7185,-4,-9570],[-8,-7646,10062,-204,170,12400],[11275,-7185,-204,12866,-218,4],[-200,-4,170,-218,16,204],[218,-9570,12400,4,204,15292]]
monomials=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
def det(M):
 # Fraction-free Bareiss elimination; determinants here have nonzero pivots.
 B=[list(row) for row in M];last=1;n=len(B)
 if n==1:return B[0][0]
 for k in range(n-1):
  pivot=B[k][k];assert pivot!=0
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=B[i][j]*pivot-B[i][k]*B[k][j]
    assert num%last==0
    B[i][j]=num//last
  for i in range(k+1,n):B[i][k]=0
  last=pivot
 return B[-1][-1]
def coefficients(M):
 out={}
 for i in range(6):
  for j in range(6):
   key=tuple(monomials[i][k]+monomials[j][k] for k in range(3))
   out[key]=out.get(key,0)+M[i][j]
 return {k:v for k,v in out.items() if v}
def expected(sign):
 out={(4,0,0):10002,(0,4,0):10002,(0,0,4):10002}
 for i in range(3):
  for j in range(3):
   key=[0,0,0];key[i]+=3;key[j]+=1;key=tuple(key)
   out[key]=out.get(key,0)-sign*10*A[i][j]
 return {k:v for k,v in out.items() if v}
result={}
for label,sg,M in [('plus',1,M_plus),('minus',-1,M_minus)]:
 assert all(M[i][j]==M[j][i] for i in range(6) for j in range(6))
 assert coefficients(M)==expected(sg),'Quartic coefficient mismatch'
 minors=[det([row[:k] for row in M[:k]]) for k in range(1,7)]
 assert all(m>0 for m in minors),'Not positive definite'
 result[label+'_leading_principal_minors']=minors
 print(label,'leading principal minors:',minors)
Av=[sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
Nv=sum(x**4 for x in v);NAv=sum(x**4 for x in Av)
# ||(A/1000)v||_4 > (3537/1250)||v||_4
margin=625*NAv-14148**4*Nv
assert margin>0
print('Av =',Av)
print('sum v_i^4 =',Nv)
print('sum (Av)_i^4 =',NAv)
print('norm witness integer margin =',margin)
# c/(3537/1250) = 1667/4716 < 1/(2sqrt2)
ratio=Fraction(5001,5000)/Fraction(3537,1250)
assert ratio==Fraction(1667,4716)
gap=4716**2-8*1667**2
assert gap>0
print('certified numerical-index upper bound =',ratio)
print('strict comparison integer margin =',gap)
result.update({'A':A,'v':v,'Av':Av,'M_plus':M_plus,'M_minus':M_minus,'quartic_denominator':10000,'numerical_radius_upper':'5001/5000','operator_norm_lower':'3537/1250','numerical_index_upper':'1667/4716','norm_integer_margin':margin,'comparison_integer_margin':gap})
(Path(__file__).resolve().parent / '935_exact_certificate.json').write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8', newline='\n')
print('ALL EXACT CHECKS PASSED')
