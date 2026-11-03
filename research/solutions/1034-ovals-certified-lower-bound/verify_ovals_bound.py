"""Directed-rounding certificate for a partial bound in AIM problem 1034.

Only Python's standard library is used. Every transcendental quantity is
enclosed by an explicit convergent series with a proved tail bound. Decimal
arithmetic is directed outwards. This verifies the numerical evaluation of
the explicit dual certificate in aim1034.tex; it does not replace the
analytic argument, and it does not prove the conjectured constant 1.
"""

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import json

PREC = 65


def rnd(op, mode):
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = mode
        return +op()


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def coerce(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        other = I.coerce(other)
        return I(rnd(lambda: self.lo + other.lo, ROUND_FLOOR),
                 rnd(lambda: self.hi + other.hi, ROUND_CEILING))

    __radd__ = __add__

    def __neg__(self):
        # Decimal unary negation is context sensitive; use copy_negate.
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-I.coerce(other))

    def __rsub__(self, other):
        return I.coerce(other) - self

    def __mul__(self, other):
        other = I.coerce(other)
        pairs = [(a, b) for a in [self.lo, self.hi]
                 for b in [other.lo, other.hi]]
        lows = [rnd(lambda a=a, b=b: a*b, ROUND_FLOOR) for a, b in pairs]
        highs = [rnd(lambda a=a, b=b: a*b, ROUND_CEILING) for a, b in pairs]
        return I(min(lows), max(highs))

    __rmul__ = __mul__

    def inv(self):
        assert self.lo > 0 or self.hi < 0
        return I(rnd(lambda: Decimal(1)/self.hi, ROUND_FLOOR),
                 rnd(lambda: Decimal(1)/self.lo, ROUND_CEILING))

    def __truediv__(self, other):
        return self * I.coerce(other).inv()

    def __rtruediv__(self, other):
        return I.coerce(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out, base = I(1), self
        while n:
            if n & 1:
                out = out * base
            n //= 2
            if n:
                base = base * base
        return out

    def sqrt(self):
        assert self.lo >= 0
        # Decimal.sqrt is correctly rounded in round-to-nearest mode.
        # A deliberately generous absolute enclosure is safe here, since
        # all square-root arguments in this certificate lie in [0.01, 1].
        assert self.lo >= Decimal('0.01') and self.hi <= 1
        with localcontext() as ctx:
            ctx.prec = PREC
            left, right = self.lo.sqrt(), self.hi.sqrt()
        error = I('1e-62')
        return I(left, right) + I(-error.hi, error.hi)

    def positive_part(self):
        return I(max(self.lo, Decimal(0)), max(self.hi, Decimal(0)))

    def strings(self):
        return [str(self.lo), str(self.hi)]


def atan_small(x, n=100):
    """Alternating arctan series, with the next-term remainder."""
    assert 0 < x.lo <= x.hi < 1
    total = I(0)
    for j in range(n):
        term = x**(2*j + 1) / (2*j + 1)
        total = total + term if j % 2 == 0 else total - term
    next_term = x**(2*n + 1)/(2*n + 1)
    if n % 2 == 0:
        return total + I(0, next_term.hi)
    return total + I(-next_term.hi, 0)


def arcsin_cube(r, n=2000):
    """asin(r^3); all coefficients are positive and <= 1.

    asin(r^3) = sum c_j r^(6j+3)/(2j+1),
    c_j = binom(2j,j)/4^j.
    The omitted tail is bounded by
       r^(6n+3)/((2n+1)*(1-r^6)).
    """
    assert 0 < r.lo <= r.hi < 1
    c, power, ratio, total = I(1), r**3, r**6, I(0)
    for j in range(n):
        total = total + c*power/(2*j + 1)
        power = power*ratio
        c = c*(2*j + 1)/(2*j + 2)
    tail = power/((2*n + 1)*(1-ratio))
    return total + I(0, tail.hi)


def sine_four_thirds_integral(ra, rb, n=2000):
    """Integral of sin(t)^(4/3) from asin(ra^3) to asin(rb^3).

    Substitute u=sin(t), expand (1-u^2)^(-1/2), and integrate.
    Every term is positive:
       sum 3*c_j*(rb^(6j+7)-ra^(6j+7))/(6j+7).
    A valid tail upper bound discards the negative ra contribution and
    replaces c_j by 1.
    """
    assert 0 < ra.lo <= ra.hi < rb.lo <= rb.hi < 1
    c, pa, pb, total = I(1), ra**7, rb**7, I(0)
    qa, qb = ra**6, rb**6
    for j in range(n):
        total = total + 3*c*(pb-pa)/(6*j + 7)
        pa, pb = pa*qa, pb*qb
        c = c*(2*j + 1)/(2*j + 2)
    tail = 3*pb/((6*n + 7)*(1-qb))
    return total + I(0, tail.hi)


def main():
    pi = 16*atan_small(I(1)/5)-4*atan_small(I(1)/239)
    L = pi/2
    a, c = I('0.5467'), I('1.09786')
    b, lagrange = 2*a, 2/c**3
    ra, rb = a/c, b/c
    ta, tb = arcsin_cube(ra), arcsin_cube(rb)
    ca, cb = (1-ra**6).sqrt(), (1-rb**6).sqrt()
    Ia = (ta-ra**3*ca)/2
    Ib = (L-tb+rb**3*cb)/2
    middle = sine_four_thirds_integral(ra, rb)
    lower_rise = lagrange*(1-ca)-2*Ia/a**3
    upper_fall = 2*Ib/b**3-lagrange*cb
    Fstar = Ia/a**2+middle/c**2+Ib/b**2
    D = 3*Fstar-lagrange-(2*upper_fall-lower_rise).positive_part()
    C = 4*D/pi
    assert lower_rise.lo > 0 and upper_fall.lo > 0
    assert C.lo > Decimal('0.96221')
    assert C.hi < Decimal('0.96222')
    result = {
        'precision_decimal_digits': PREC,
        'series_terms': 2000,
        'a': a.strings(), 'b': b.strings(), 'c': c.strings(),
        'pi': pi.strings(),
        'ta': ta.strings(), 'tb': tb.strings(),
        'lower_rise': lower_rise.strings(),
        'upper_fall': upper_fall.strings(),
        'D': D.strings(), 'universal_bound_C': C.strings(),
        'proved_numeric_comparison': '0.96221 < C < 0.96222',
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
