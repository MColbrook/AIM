#!/usr/bin/env python3
"""Exact rational checks for the AIM 558 counterexample.

Run with Python 3.10+; no third-party packages or network are required.
These checks audit the finite-dimensional algebra in the accompanying proof.
They are not a formal proof of the convexity and existence arguments.
"""
from __future__ import annotations

from fractions import Fraction as Q
from typing import Sequence

Matrix = list[list[Q]]


def mat(rows: Sequence[Sequence[int | Q]]) -> Matrix:
    return [[Q(x) for x in row] for row in rows]


def eye(n: int) -> Matrix:
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def diag(values: Sequence[Q | int]) -> Matrix:
    return [[Q(values[i]) if i == j else Q(0) for j in range(len(values))]
            for i in range(len(values))]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c: Q | int, a: Matrix) -> Matrix:
    return [[Q(c) * x for x in row] for row in a]


def mul(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("The matrix must be square.")
    ident = eye(n)
    aug = [row[:] + ident[i] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        if pivot is None:
            raise ValueError("The matrix is singular.")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        den = aug[j][j]
        aug[j] = [x / den for x in aug[j]]
        for i in range(n):
            if i != j:
                coefficient = aug[i][j]
                aug[i] = [x - coefficient * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def determinant(a: Matrix) -> Q:
    n = len(a)
    b = [row[:] for row in a]
    result = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if b[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            result = -result
        value = b[j][j]
        result *= value
        for i in range(j + 1, n):
            ratio = b[i][j] / value
            for k in range(j + 1, n):
                b[i][k] -= ratio * b[j][k]
    return result


def check(condition: bool, message: str) -> None:
    # Deliberately not an assert: checks remain enabled with python -O.
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def leading_minors(a: Matrix) -> list[Q]:
    return [determinant([row[:k] for row in a[:k]])
            for k in range(1, len(a) + 1)]


def main() -> None:
    r = mat([[1, Q(4, 5), Q(4, 5)],
             [Q(4, 5), 1, Q(3, 10)],
             [Q(4, 5), Q(3, 10), 1]])
    k = mat([[Q(37, 5), -4, -4],
             [-4, Q(243, 70), Q(17, 7)],
             [-4, Q(17, 7), Q(243, 70)]])
    sigma = mat([[Q(295, 583), Q(200, 583), Q(200, 583)],
                 [Q(200, 583), Q(33910, 42559), Q(-6900, 42559)],
                 [Q(200, 583), Q(-6900, 42559), Q(33910, 42559)]])
    ident = eye(3)
    check(leading_minors(r) == [Q(1), Q(9, 25), Q(7, 500)],
          "R is positive definite by its exact leading principal minors")
    check(k == scale(Q(1, 10), add(inverse(r), scale(9, ident))),
          "K = (R^{-1} + 9 I)/10")
    check(all(x > 0 for x in leading_minors(k)),
          "K has positive leading principal minors")
    check(mul(k, sigma) == ident, "The displayed covariance is exactly K^{-1}")

    h10 = add(scale(10, k), scale(-9, ident))
    s10 = inverse(h10)
    check(s10 == r and all(s10[i][i] == 1 for i in range(3)),
          "The feasible point t=(1,1,1) is stationary at alpha=10")

    a = Q(11)
    tbar = [Q(2713, 2745), Q(1), Q(1)]
    h11 = add(scale(a, k), scale(-(a - 1), diag(tbar)))
    check(all(t > 0 for t in tbar) and all(x > 0 for x in leading_minors(h11)),
          "The rational comparison point is feasible at alpha=11")
    s11 = inverse(h11)
    expected = mat([[Q(2745, 2713), Q(2200, 2713), Q(2200, 2713)],
                    [Q(2200, 2713), Q(153231490, 153412011),
                     Q(48970900, 153412011)],
                    [Q(2200, 2713), Q(48970900, 153412011),
                     Q(153231490, 153412011)]])
    check(s11 == expected, "The alpha=11 inverse is the displayed rational matrix")
    grad = [(a - 1) * (s11[i][i] - 1 / tbar[i]) for i in range(3)]
    check(grad == [Q(0), Q(-1805210, 153412011), Q(-1805210, 153412011)],
          "The gradient is exactly (0,g,g), where g<0")
    check(determinant(h11) == Q(279439, 3500),
          "det H_11(tbar) = 279439/3500")

    cmat = [[x * x for x in row] for row in r]
    one = mat([[1], [1], [1]])
    rhs = scale(Q(1, 10), add(mul(cmat, one), scale(-1, one)))
    deriv = mul(inverse(add(ident, scale(9, cmat))), rhs)
    check(deriv == mat([[Q(3392, 260905)], [Q(-91, 521810)],
                       [Q(-91, 521810)]]),
          "The exact variance derivative at alpha=10 has two negative entries")

    def polynomial(y: Q) -> Q:
        return 303828701*y**3 - 573214290*y**2 + 295302000*y - 25900000

    check(polynomial(Q(9997, 10000)) < 0 < polynomial(Q(4999, 5000)),
          "The supplemental stationarity cubic changes sign between 0.9997 and 0.9998")
    check(polynomial(Q(1)) == 16411, "The cubic does not vanish at y=1")
    print("\nAll exact arithmetic checks passed.")
    print("The accompanying proof supplies global optimality and the convex comparison.")


if __name__ == "__main__":
    main()
