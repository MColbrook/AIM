#!/usr/bin/env python3
"""Additional exact pre-submission audit of the cubic Fejer certificate.

Run with Python 3.10+ and SymPy 1.14.0. This checker independently expands
the induction polynomial with symbolic M in a rational polynomial ring;
it does not import or call verify_cubic.py or its coefficient recursion.
It also compares all printed table entries with the JSON certificate and
checks the cardinal values over Q(sqrt(5)). All tests remain active with -O.
"""
from collections import defaultdict
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import json
import re
import sys

import sympy as sp
from sympy.parsing.sympy_parser import (
    implicit_multiplication_application, parse_expr, standard_transformations,
)
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

HERE = Path(__file__).resolve().parent
M, u = sp.symbols('M u')


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def certificate():
    records = json.loads((HERE / 'cubic_certificate.json').read_text())
    require(len(records) == 45, 'Certificate must have 45 records')
    result = {}
    for record in records:
        key = record['z_power'], tuple(record['partition'])
        require(key not in result, 'Duplicate certificate key')
        c = sp.sympify(record['coefficient'], locals={'M': M})
        p = sp.Poly(c.subs(M, u + 8), u, domain=QQ)
        require(p.degree() <= 5, 'Unexpected coefficient degree')
        require(all(v > 0 for v in p.all_coeffs()), 'Nonpositive shifted coefficient')
        require([int(p.nth(j)) for j in range(6)] ==
                record['shifted_coefficients_ascending'], 'Stored shift mismatch')
        result[key] = sp.Poly(c, M, domain=QQ)
    return result


def printed_table(table):
    tex = (HERE / 'aim641_cubic_fejer.tex').read_text(encoding='utf-8')
    rows = re.findall(r'^([1-8]) & \$(.*?)\$ & \$(.*?)\$ & \$\((.*?)\)\$\\\\\s*$',
                      tex, flags=re.MULTILINE)
    require(len(rows) == 45, 'Cannot identify all 45 printed rows')
    seen = set()
    for k, partition, factor, coefficients in rows:
        alpha = []
        if partition != r'\varnothing':
            for part in partition.strip('()').split(','):
                match = re.fullmatch(r'(\d+)(?:\^\{(\d+)\})?', part)
                require(match is not None, 'Invalid printed partition')
                alpha.extend([int(match[1])] * int(match[2] or 1))
        key = int(k), tuple(alpha)
        require(key not in seen and key in table, 'Unexpected printed key')
        seen.add(key)
        factor = factor.replace(r'\left', '').replace(r'\right', '')
        factor = re.sub(r'\^\{(\d+)\}', r'**\1', factor)
        F = parse_expr(factor, local_dict={'M': M}, transformations=
                       standard_transformations + (implicit_multiplication_application,))
        coeffs = [int(a.strip()) for a in coefficients.split(',')]
        require(all(a > 0 for a in coeffs), 'Nonpositive printed array')
        require(all(a > 0 for a in sp.Poly(F.subs(M, u + 8), u).all_coeffs()),
                'Printed prefactor does not have positive shifted coefficients')
        displayed = F.subs(M, u + 8) * sum(a * u**j for j, a in enumerate(coeffs))
        require(sp.expand(table[key].as_expr().subs(M, u + 8) - displayed) == 0,
                f'Printed table mismatch: {key}')
    require(seen == set(table), 'Printed table does not cover certificate')
    print('PASS: all 45 printed table rows and all stored shifted arrays agree exactly.')


def kernel(p):
    S, p2, p3, p4, p5, p6 = p
    return (54*p6 + 78*S*p5 + 29*S**2*p4 - QQ(391, 2)*p2*p4
            - 18*S**3*p3 - 144*S*p2*p3 + 50*p3**2
            + QQ(9, 4)*S**4*p2 + QQ(47, 2)*S**2*p2**2 + QQ(487, 4)*p2**3)


def symbolic_ring(table):
    R, *variables = ring('mu0,mu1,mu2,mu3,mu4,mu5,mu6,z,M', QQ)
    mu, z, dim = variables[:7], variables[7], variables[8]
    S = sum(mu) + z
    # Seven nonzero mu coordinates, M-7 other coordinates equal to z/M.
    # W_j = M**j p_j. Homogeneity clears all denominators with M**6.
    W = [sum((dim*x + z)**j for x in mu) + (dim-7)*z**j for j in range(1, 7)]
    P = [sum(x**j for x in mu) for j in range(1, 7)]
    D_numerator = dim**6*S**6 - kernel(W) - dim**6*(P[0]**6-kernel(P))
    Q_times_M = 4*S**2*D_numerator
    grouped = defaultdict(dict)
    for powers, value in Q_times_M.items():
        require(powers[-1] >= 1, 'M denominator does not cancel')
        require(powers[-2] >= 1, 'z-free term does not cancel')
        base, m_power = powers[:-1], powers[-1] - 1
        grouped[base][m_power] = sp.Rational(value.numerator, value.denominator)
    require(len(grouped) == comb(14, 7) == 3432, 'Unexpected monomial count')
    seen = set()
    for powers, m_coeffs in grouped.items():
        key = powers[-1], tuple(sorted((a for a in powers[:-1] if a), reverse=True))
        require(key in table, 'Unknown symmetric monomial type')
        direct = sp.Poly.from_dict({(j,): a for j, a in m_coeffs.items()}, M, domain=QQ)
        require(direct == table[key], f'Symbolic direct expansion differs for {powers}')
        seen.add(key)
    require(seen == set(table), 'Symbolic expansion missed a type')
    print('PASS: independent symbolic-M expansion, all 3432 monomial coefficients and 45 types.')


def cardinal_values():
    F = QQ.algebraic_field(sp.sqrt(5))
    zero, one = F.zero, F.one
    sqrt5 = F.from_sympy(sp.sqrt(5))
    t = (one + one/sqrt5)/2
    A, B = (3 + sqrt5)/2, (3 - sqrt5)/2
    count = 0
    for m in range(2, 7):
        indices = [('v', (i,)) for i in range(m)]
        indices += [('e', ij) for ij in permutations(range(m), 2)]
        indices += [('f', ijk) for ijk in combinations(range(m), 3)]
        require(len(indices) == comb(m+2, 3), 'Node count mismatch')
        for at, (kind, ijk) in enumerate(indices):
            x = [zero] * m
            if kind == 'v':
                x[ijk[0]] = one
            elif kind == 'e':
                x[ijk[0]], x[ijk[1]] = t, one-t
            else:
                for i in ijk:
                    x[i] = one/3
            S, p2 = sum(x, zero), sum((a*a for a in x), zero)
            values = [a*(12*a*a - 12*S*a + 3*S*S - p2)/2 for a in x]
            values += [5*x[i]*x[j]*(A*x[i]+B*x[j]-S)
                       for i, j in permutations(range(m), 2)]
            values += [27*x[i]*x[j]*x[k] for i, j, k in combinations(range(m), 3)]
            for which, value in enumerate(values):
                require(value == (one if which == at else zero), 'Cardinal value mismatch')
                count += 1
    print(f'PASS: {count} exact cardinal values in dimensions 1 through 5 over Q(sqrt(5)).')


def main():
    print(f'Python {sys.version.split()[0]}; SymPy {sp.__version__}')
    table = certificate()
    printed_table(table)
    symbolic_ring(table)
    cardinal_values()
    print('ALL ADDITIONAL EXACT AUDIT CHECKS PASSED.')


if __name__ == '__main__':
    main()
