# AIM 1034: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Partially resolved — checked partial progress.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1034-ovals-certified-lower-bound/aim1034.pdf), [TeX](../../solutions/1034-ovals-certified-lower-bound/aim1034.tex), and [source receipt](../../solutions/1034-ovals-certified-lower-bound/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1034](../../../problems/1034-the-sharp-curvature-schrodinger-inequality-for-closed-loops.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

A certified universal lower bound greater than 0.96221 holds for the curvature operator on the full smooth closed-curve class.

**Remaining target:** Raise the universal lower bound to one for every smooth closed spatial curve of length $`2\pi`$, or construct a counterexample. No optimality claim is made for the new bound.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# AIM 1034: independent mathematical audit

Date: 2026-11-03. Reviewer: Codex AI, geometric-constants review lane C. This is an independent AI audit, not human peer review or proof-assistant verification.

Canonical revision inspected: `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Authoritative target: `problems/1034-the-sharp-curvature-schrodinger-inequality-for-closed-loops.md` and row 1034 of `data/spectral.json`. The complete supplied argument in `submission/sections/1034.md`/`.tex`, `verification/verify_ovals_bound.py`, and `verification/ovals_certificate.json` were read. TeX SHA-256: `8e1a22664b463ae6f38a1140218a7125e8f8cb272a483fee156809c6f868e3a7`.

## Verdict and exact scope

**PARTIAL: the stated universal improvement is proved, with no substantive mathematical gap found.** For every smooth closed unit-speed curve of length 2pi in R^m, m>=2, and every periodic H1 test function, the curvature Schrodinger form is at least C0 times its squared L2 norm, where

```text
0.9622177760565015683848281814 < C0
  < 0.9622177760565015683848697651.
```

This includes the complete geometric class of canonical problem 1034: spatial curves, self-intersections permitted, with no planarity or convexity assumption on the original curve. It proves a weaker constant for that full class; it does not prove the target constant 1. Retain `Partially resolved`.

Recommended catalogue scope:

- Known cases/bounds: the circle and the previously known oval family attain 1; the present audited argument gives the universal lower bound C0>0.96221.
- Remaining target: raise the universal lower bound to 1 for every smooth closed spatial curve of length 2pi, or produce a counterexample.
- Equivalently, the currently proved global interval is C0 <= inf_gamma lambda_1(H_gamma) <= 1.

**Canonical wording correction needed:** the present Known cases note and its repeated online-recheck paragraph say "The sharp constant is one for all smooth closed spatial curves". That sentence states the unresolved target as a known result. Replace it by the bounds/remaining-target distinction above when integrating this advance.

## Reduction and proof checks

1. **Global geometric reduction.** Denzler's Theorem 1 explicitly concerns closed W2,2 (or C2) curves in R^n, with no embeddedness assumption. Its minimizer is planar, convex, analytic and has positive curvature. The arXiv Theorems 6, 8 and 9 give the relaxed alternative, with the digon the only possible exceptional minimizer. Its quotient is 1. Therefore a bound C0<1 on smooth strictly convex planar curves passes to all original smooth curves. The supplied argument is not restricted to convex original curves and does not require a stronger unproved reduction.

2. **Antipodal arclength constraints.** The angle-coordinate function g is positive and 2pi-periodic, and closure gives integral exp(i theta)g(theta) dtheta=0. Direct Fubini calculation of the inner kernel gives i(1+exp(i(beta-theta))), including the wrapped half-circle case. This proves the weighted sine identity. Differentiating ell gives g(alpha+pi)-g(alpha); its variation on any interval of length pi is at most the total mass 2pi. These constraints and all normalizations are correct.

3. **Projection averaging.** For Y=psi T, orthogonality of T and T' gives the exact form identity. Each real scalar projection has zero trace at the two antipodal tangent points and satisfies the Dirichlet interval inequality on both arcs. For a fixed point s, its occurrence in the first oriented arc is parametrized by alpha in (phi(s)-pi,phi(s)); this produces pi^2 J(phi(s)). The complementary-arc integral is identical. Dividing their sum by the angular average pi yields exactly 2pi J. Applying the real argument to real and imaginary parts covers complex psi. Thus equation (7) and its factor 2pi check independently.

4. **Symmetrization and half-interval constraints.** Reflection t -> pi-t preserves the weight sin(t), and convexity of x -> x^(-2) gives equation (10). The endpoint sum fixes the symmetrized endpoint at 1. Total variation cannot increase under averaging; symmetry halves both the weighted mass and the total variation. Hence v(0)=1, integral v sin=1, and TV(v)<=1 hold exactly. No further feasibility assertion about v_star is used or needed.

5. **Dual inequality.** The residual r is nonnegative, zero, then nonpositive on the three specified intervals. Its primitive q increases from B-A to B, stays B, and then decreases to zero, so its supremum norm is max(B,A-B). Integration by parts, v(0)=1 and TV(v)<=1 give integral r v >= -max(0,2B-A). The displayed supporting line is the exact tangent inequality for the convex function sin^2(t)/v^2. Combining it with the unit weighted mass proves F(v)>=D. Finally J>=2D/pi^2 and the preceding projection bound give C0=4D/pi. Every factor and sign is correct.

6. **Explicit constants and series.** The expressions for I_a and I_b are the exact integrals of sin^2 over their intervals. Substitution u=sin(t) gives the positive series for I_m with coefficient 3d_j/(6j+7). The arcsine series and both tail bounds have the correct powers and denominators. In particular, replacing d_j by 1 and discarding the negative lower-endpoint contribution is a valid upper tail estimate for I_m.

## Certificate inspection and fresh reproduction

The supplied script uses only Python standard-library `decimal` and `json`, performs no writes, and was inspected before execution. Directed addition, multiplication, division, nonnegative integer powers, and positive-part operations enclose the true values. Decimal negation is correctly handled with `copy_negate` where context rounding could matter. All square-root inputs are explicitly checked to lie in [0.01,1]; the added absolute 1e-62 padding safely exceeds the rounding error of a 65-digit square root in that interval. The alternating Machin calculation also has an explicit next-term enclosure.

The fresh run used Python 3.12.14 and `-B`, and reproduced the supplied JSON endpoints, including

```text
D lower = 0.75572407410315354459185997743982991229030521161745297662414349632
D upper = 0.75572407410315354459189263714459183772967242933331088322377232952
C lower = 0.96221777605650156838482818142212356313104547909082246860285849093
C upper = 0.96221777605650156838486976504974582190230907302553936813093581638
```

Both asserted comparisons, C>0.96221 and C<0.96222, passed. Script SHA-256: `0a634ae150d80916367984e2b96b4859b288ed42a42e41c746b05d515e92c7b6`.

Reproduction command from the repository root:

```sh
python -B research/solutions/1034-ovals-certified-lower-bound/verify_ovals_bound.py
```

This checks the explicit arithmetic certificate. It does not replace the analytic proof or certify the target constant 1.

## Independent arithmetic implementation

In addition to reproducing the supplied Decimal code, I implemented and executed a separate interval calculation using **only integer fixed-point arithmetic** at scale 10^100. Square roots were enclosed with `math.isqrt`, not `Decimal.sqrt`. Machin series used 160 terms and the positive arcsine/integral series used 10,000 terms. Exact integer floor/ceiling operations enclosed every arithmetic operation; the same proved analytic series tails were applied.

This implementation did not import the supplied script. Its resulting intervals, outward shortened here, imply

```text
A = 0.0038498884939164883723294021544898472390814917238323153703557777563795...
B = 0.0019254831281556816899786388855424314359580381264629891778503909956025...
D = 0.7557240741031535445918680167381693341023463317690427049879249297170094...

0.9622177760565015683848384173746812387083 < C0
  < 0.9622177760565015683848384173746812387084.
```

The full independently computed C interval was

```text
[0.9622177760565015683848384173746812387083943477985691037661166993545508740881549551552389653950532186,
 0.9622177760565015683848384173746812387083943477985691037661166993545508740881549551552389653950751632].
```

It lies strictly inside the supplied enclosure. In particular, 2B-A>0 is independently certified, and the positive-part branch in D has been evaluated consistently.

## Verified references and dated search

- [Jochen Denzler, arXiv:1301.6322v1](https://arxiv.org/html/1301.6322v1): Theorem 1, the definition of the original R^n variational problem, and Theorems 6, 8, 9 were checked. These are the correct arXiv theorem numbers. The author's [publication list](https://web.math.utk.edu/~jdenzler/Publications/index.html) confirms *Transactions of the AMS* 367 (2015), 3829-3845. Citing the pinned arXiv theorem numbers avoids confusion with the published renumbering.
- [Durvudkhan Suragan, arXiv:2609.10775v1](https://arxiv.org/html/2609.10775v1): Lemma 2.2 is the closure convolution identity, Proposition 3.1 is the exact projection-averaging inequality, and Section 4 states the global reduction from Denzler. The hypotheses, factors and cited September constant match the manuscript. Those geometric inequalities were also checked directly above; the new total-variation constraint and the dual certificate are given in the supplied manuscript itself.

Searches on 2026-11-03 included `ovals problem 0.96221`, `ovals 0.962217`, `ovals conjecture proof 2026 curvature 1`, and `Benguria Loss ovals 2026 improvement`. I checked the current arXiv record for Suragan. No matching complete proof of the target value 1 was located. This bounded search does not establish novelty or exclude an unindexed later result.

## Integration recommendation

Accept this universal estimate as a checked partial advance. Preserve the exact certificate and its reproduction instructions with the standalone manuscript. Retain the explicit gap to 1, correct the canonical wording identified above, and avoid an optimality claim for either C0 or the numerically optimized scalar profile. No repair to the mathematical argument is required.
