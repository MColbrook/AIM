"""Exact arithmetic checks for the explicit interval corollary.
The analytic inequalities are proved in aim935.tex; this verifies
all rational arithmetic and the strict rational bound below 1/(2sqrt(2)).
"""
from fractions import Fraction as F
epsilon=F(1,10000)
gamma=F(5001,5000)
L=F(3537,1250)
R=F(3351,1000)
C=F(15,2)*(R/29+gamma/39)
assert C==F(399237,377000)
upper=(gamma+C*epsilon)*(1+epsilon/7)/L
assert upper==F(87994832581079,248910480000000)
lower=F(7071,20000)-F(15,58)*epsilon
assert lower==F(51261,145000)
gap=lower-upper
assert gap==F(1030282921,248910480000000)>0
assert 8*7071**2<20000**2
lo,hi=F(39999,10000),F(40001,10000)
assert (hi/(hi-1),lo/(lo-1))==(F(40001,30001),F(39999,29999))
print('PASS: every exact arithmetic check in the 935 interval corollary.')
print('Ratio upper bound:',upper)
print('M_p lower bound:',lower)
print('Strict rational separation:',gap)
