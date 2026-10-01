"""Exact rational certificate for the counterexample to AIM problem 558."""
from fractions import Fraction as F


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def det3(a):
    return sum(a[0][j] *
               (a[1][(j + 1) % 3] * a[2][(j + 2) % 3] -
                a[1][(j + 2) % 3] * a[2][(j + 1) % 3])
               for j in range(3))


def positive_definite(a):
    assert a == [list(x) for x in zip(*a)]
    assert a[0][0] > 0
    assert a[0][0] * a[1][1] - a[0][1] * a[1][0] > 0
    assert det3(a) > 0


q = [[F(1), F(4, 5), F(4, 5)],
     [F(4, 5), F(1), F(3, 10)],
     [F(4, 5), F(3, 10), F(1)]]
sigma = [[F(295, 583), F(200, 583), F(200, 583)],
         [F(200, 583), F(33910, 42559), F(-6900, 42559)],
         [F(200, 583), F(-6900, 42559), F(33910, 42559)]]
positive_definite(q)
positive_definite(sigma)
assert det3(q) == F(7, 500)
assert mul([[F(i == j) + 9 * q[i][j] for j in range(3)]
            for i in range(3)], sigma) == [[10 * x for x in row] for row in q]
assert [q[i][i] for i in range(3)] == [1, 1, 1]
r = [[x * x for x in row] for row in q]
h = [[F(i == j) + 9 * r[i][j] for j in range(3)] for i in range(3)]
positive_definite(h)
dt = [[F(-3392, 260905)], [F(91, 521810)], [F(91, 521810)]]
assert mul(h, dt) == [[(1 - sum(row)) / 10] for row in r]
dpsi = [-x[0] for x in dt]
assert dpsi[1] < 0 and dpsi[2] < 0
print("PASS: exact feasibility, stationarity, and negative variance derivatives")
print("Psi'(10) =", ", ".join(str(x) for x in dpsi))
