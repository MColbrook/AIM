"""Independent exact audit via a closed coefficient list and rational LDL factorization."""
from pathlib import Path
from fractions import Fraction as Q
import json
J=json.loads((Path(__file__).resolve().parent / '935_exact_certificate.json').read_text(encoding='utf-8'))
A=J['A']; result={}
for label,sign in [('plus',1),('minus',-1)]:
    M=J['M_'+label]
    # Ordered monomials: x^4,y^4,z^4,x^3y,x^3z,y^3x,y^3z,z^3x,z^3y,
    #                    x^2y^2,x^2z^2,y^2z^2,x^2yz,xy^2z,xyz^2.
    actual=[M[0][0],M[1][1],M[2][2],2*M[0][3],2*M[0][4],2*M[1][3],2*M[1][5],2*M[2][4],2*M[2][5],
            2*M[0][1]+M[3][3],2*M[0][2]+M[4][4],2*M[1][2]+M[5][5],
            2*(M[0][5]+M[3][4]),2*(M[1][4]+M[3][5]),2*(M[2][3]+M[4][5])]
    expected=[10002-sign*10*A[i][i] for i in range(3)] + [-sign*10*A[i][j] for i,j in [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]]+[0]*6
    assert actual==expected, (actual,expected)
    # Rational LDL^t computed without determinants or Bareiss elimination.
    L=[[Q(i==j) for j in range(6)] for i in range(6)]; D=[]
    for j in range(6):
        pivot=Q(M[j][j])-sum(L[j][k]**2*D[k] for k in range(j))
        assert pivot>0
        D.append(pivot)
        for i in range(j+1,6):
            L[i][j]=(Q(M[i][j])-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/pivot
    for i in range(6):
        for j in range(6):
            assert sum(L[i][k]*D[k]*L[j][k] for k in range(6))==M[i][j]
    dets=[]; det=Q(1)
    for d in D:
        det*=d; assert det.denominator==1; dets.append(det.numerator)
    assert dets==J[label+'_leading_principal_minors']
    result[label]={'quartic_coefficients':actual, 'ldl_diagonal':[str(d) for d in D], 'determinants':dets}
w=J['v']; Aw=[sum(A[i][j]*w[j] for j in range(3)) for i in range(3)]
assert Aw==J['Av']
quotient_fourth=Q(sum(u**4 for u in Aw),1000**4*sum(u**4 for u in w))
lower=Q(3537,1250)
assert quotient_fourth>lower**4
radius=Q(5001,5000); ratio=radius/lower
assert ratio==Q(1667,4716)
assert ratio**2<Q(1,8)
# M_4=1/(2 sqrt2) follows from (1+t^4)^2-8(t-t^3)^2=(t^4-4t^2+1)^2,
# with equality for t=sqrt(2-sqrt3) in(0,1).
result.update({'norm_quotient_fourth':str(quotient_fourth),'norm_quotient_numeric':float(quotient_fourth)**0.25,'upper_index':str(ratio),'upper_index_numeric':float(ratio),'M4_numeric':1/(2*2**0.5), 'strict_squared_gap':str(Q(1,8)-ratio**2)})
(Path(__file__).resolve().parent / '935_independent_audit.json').write_text(json.dumps(result,indent=2)+'\n', encoding='utf-8', newline='\n')
print(json.dumps(result,indent=2))
