"""Exact rational checks used in the elementary parallelogram Steklov proof.
No floating-point calculation is used to establish any assertion.
"""
from fractions import Fraction as F
from math import factorial


def exp_bounds(x, n=20):
    lo = sum((x**j / factorial(j) for j in range(n + 1)), F(0))
    first = x**(n + 1) / factorial(n + 1)
    hi = lo + first / (1 - x / (n + 2))
    return lo, hi


def tanh_bounds(x):
    lo, hi = exp_bounds(2 * x)
    return (lo - 1) / (lo + 1), (hi - 1) / (hi + 1)


def sin_bounds(x):
    hi = sum(((-1)**j * x**(2*j + 1) / factorial(2*j + 1) for j in range(9)), F(0))
    return hi - x**19 / factorial(19), hi


def cos_bounds(x):
    hi = sum(((-1)**j * x**(2*j) / factorial(2*j) for j in range(9)), F(0))
    return hi - x**18 / factorial(18), hi


def root_function_bounds(x):
    sl, su = sin_bounds(x)
    cl, cu = cos_bounds(x)
    hl, hu = tanh_bounds(x)
    return sl * hl - cu, su * hu - cl


kl, ku, hl, hu = F(93,100), F(94,100), F(73,100), F(74,100)
assert root_function_bounds(kl)[1] < 0
assert root_function_bounds(ku)[0] > 0
assert tanh_bounds(kl)[0] > hl
assert tanh_bounds(ku)[1] < hu

delta_lower = (kl**2 * (1-hu**4) + hl**2) / (2*ku*hu)
beta_lower = hl/ku - hu**2
beta_upper = hu/kl - hl**2
kappa_lower = (1+hl**4)/(2*ku*hu)
square_lower = 8*kl*hl
assert delta_lower > F(4,5)
assert beta_lower > 0
assert beta_upper < F(1,3)
assert kappa_lower > F(2,3)
assert square_lower > F(224,45)
assert square_lower**2 > 12
# Positivity used for the small-shear diagonal trial.
assert F(4,15)-F(5,24)-F(1,1536) > 0
print('All exact rational inequalities for the parallelogram proof verified.')
