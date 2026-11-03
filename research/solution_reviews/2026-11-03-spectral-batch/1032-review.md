# AIM 1032: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Counterexample.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1032-heun-star-counterexample/aim1032.pdf), [TeX](../../solutions/1032-heun-star-counterexample/aim1032.tex), and [source receipt](../../solutions/1032-heun-star-counterexample/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1032](../../../problems/1032-the-spectral-tree-for-high-order-heun-operators.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

The operator with leading coefficient z^4-z has a limiting three-spoke spectral star, with the leading root zero a branch point rather than a leaf.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

# Independent second audit of AIM 1032

Reviewed 2026-11-03 by an independent Codex AI mathematical reviewer. This is an AI audit, not human refereeing or formal proof verification. The complete submitted `1032.tex` and the complete canonical statement were read; the coordinating reviewer's preliminary verdict was not used as proof evidence. No canonical or manuscript-package file was edited.

**Verdict: complete counterexample to the exact universal leaf clause.** No substantive mathematical gap found. The proof establishes full-sequence weak convergence and exact support for the third-order example, not merely matching exterior moments. It does not refute the later conjecture restricted to generic leading polynomials.

## Target and source identity

The authoritative current target is `problems/1032-the-spectral-tree-for-high-order-heun-operators.md`, source key `FURTHER-f2efae695b2822f4`, SHA-256 `92baa1e7415fe750927e8457e2f7c346127d902779209bb6f8a70ab70f393574`. The inspected submission is `.cache/spectral-batch/_sources/submission/sections/1032.tex`, SHA-256 `ef16fbb73eea0e2f7d9f452ff157ee00878754c8c98eeeb01eaed22646ee9272`.

For `Q_3(z)=z^4-z`, the four leading roots are simple and are not all collinear. The support proved in the submission has three arms meeting at the leading root zero. Thus zero is an internal branch vertex, so the required assertion that every leading root is a leaf fails. A single such operator disproves the universal statement, even though convergence, positivity, the finite-tree property and the exterior-moment constraints hold for this example.

## Finite spectral problem and exact multiplicity

The highest-degree coefficient fixes the leading Van Vleck coefficient at `-theta_n`. Moving terms gives the finite operator A_n exactly as in (3). For every degree below n, the raising coefficient is nonzero. Any eigenvector must therefore have degree n. Conversely every eigenvector supplies an admissible degree-n Stieltjes polynomial and the associated Van Vleck root. The matrix is nonnegative with unit column sums, and no transition enters the constant monomial. Hence its characteristic polynomial is t times that of B_n and its eigenvalues lie in the unit disk. Algebraic multiplicities are the appropriate spectral-polynomial multiplicities; equivalently, the nonzero raising entries make the coefficient elimination a single characteristic-polynomial equation in the Van Vleck parameter.

For the three residue classes, I derived the following factor shapes directly from monomial transitions:

| n mod 3 | U_1 shape | U_2 shape | L shape | position of terminal coefficient c_n=1 |
|---|---|---|---|---|
| 0 | q by q | q by q | q by q | last diagonal of L |
| 1 | q by q+1 | q by q | q+1 by q | last superdiagonal of U_1 |
| 2 | q+1 by q+1 | q by q+1 | q+1 by q | last superdiagonal of U_2 |

The listed diagonal and off-diagonal formulas agree with all transitions. The vanishing raising coefficient `1-c_n` never appears at an existing listed entry. Every listed factor entry is strictly positive, including the possible terminal coefficient one. The leading q by q diagonal and needed off-diagonal minors exist in all cases; q=1 causes no exception.

For nonzero t, eliminating the first two residue blocks gives

`det(tI-B_n) = t^(d_1+d_2) det(tI_q-t^(-2)U_2U_1L) = t^r det(t^3I_q-C_q)`.

The exponent follows from `d_1+d_2=2q+r`. Both sides are polynomials, so the identity extends to t=0. Because C_q has positive determinant, B_n has precisely r zero eigenvalues counted algebraically; A_n has precisely r+1. There is no inference of exact multiplicity from merely knowing a lower bound on the kernel dimension. The nonzero spectral roots occur in complete cube-root triples, giving exact rotation invariance of the empirical measures.

## Total nonnegativity, compounds and positive simple return spectrum

Every minor of a rectangular bidiagonal factor has at most one nonzero permutation term. If it exists, it is order preserving, so the determinant is a product of nonnegative entries. Cauchy--Binet therefore gives total nonnegativity of C_q without assuming square factors.

For any p-subset I of the first q indices, retain I in every intermediate Cauchy--Binet index set. The three principal factor minors are positive. Thus every diagonal entry of the pth compound is positive. In particular `det C_q>0` when p=q.

If J is obtained from I by moving one occupied site one step to an adjacent vacancy, then:

- For an increase in that site, select the positive minor `L[J,I]` and diagonal minors of U_1 and U_2 at J.
- For a decrease, select `U_1[J,I]`, the diagonal minor of L at I and that of U_2 at J.

The other indices keep their natural order and the moved entry uses a strictly positive first off-diagonal. All intermediate subsets stay inside the first q indices; rectangular extra rows and columns cannot invalidate these terms. The graph of p-subsets with these moves is connected (move occupied sites one at a time to the ordered leftmost configuration, and reverse such moves). Positive diagonals remove any period obstruction. Every compound is thus primitive, including the single-entry compound at p=q.

To make the last spectral step explicit, order the eigenvalues of C_q by decreasing modulus. Primitivity at p=1 makes the first positive and uniquely dominant. If the next two moduli were tied, the pth compound would have two eigenvalues of maximal modulus counting algebraic multiplicity. This contradicts Perron--Frobenius. Its positive Perron root is the product of the first p eigenvalues. Induction makes each next eigenvalue positive and separates its modulus from the following one. Positive determinant supplies the last positive eigenvalue. Hence all q are positive and simple, as asserted. No numerical eigenvalue approximation is used.

The unit-disk bound for A_n then puts every `s_j` in `(0,1]`; each cube root lies on one of the three specified radial arms. This proves exact star confinement for every degree n>=3, covering all congruence classes.

## Moments, determinacy and exact support

A closed path of length m has displacement `m-3d`, where d counts downward steps. Thus only m divisible by three contributes to the trace. For m=3l, there are l downward steps and 2l upward steps, with the stated binomial number of orderings. A fixed buffer of 6l safely avoids both endpoints. Uniformly over remaining starts, `c_(j+O(1))=(j/n)^3+O(1/n)`. Products have the claimed uniform error since the path length is fixed and all factors are bounded by one. The bounded number of omitted starts has vanishing normalized contribution. This validates the Riemann-sum limit along the full sequence.

Substitution `u=t^3` in the integral independently gives

`m_l = Gamma(3l+1) Gamma(l+1/3) / [3 Gamma(l+1) Gamma(3l+4/3)]`.

These are the moments of `XY^3` for independent `X~Beta(1/3,2/3)` and `Y~Beta(1,1/3)`. After the cube map, all measures are probabilities on the compact interval [0,1]. Density of scalar polynomials in the continuous functions makes ordinary moment convergence determining there. This is the decisive extra support input; no planar holomorphic-moment uniqueness is assumed.

Exact rotation invariance then reconstructs each original measure from its pushforward by averaging the three continuous cube-root branches. The averaged test function is continuous at zero because all three branches coalesce. This proves full weak convergence to the stated law, including all residue subsequences.

Both beta densities are positive throughout (0,1). Every interior value of their product has positive mass in each neighborhood; endpoints belong to the support by closure. Thus the pushforward support is exactly [0,1], and the original support is exactly the complete three-spoke star. Zero has three incident nontrivial arcs despite its limiting atom having mass zero. If one interprets “supported on a tree” as allowing a larger finite tree, deleting zero from any such tree still separates these three arms: a connection bypassing zero would create a cycle. Consequently no enclosing tree can make zero a leaf.

The optional higher-order family along n=kq also follows from the same derivation: one lower and k-1 upper square bidiagonal factors, displacement `m-kd`, and beta moments with 1/3 replaced by 1/k. The fully detailed k=3 case already suffices for the target.

## Primary conjectures and suggested matrix reference

I independently inspected the primary passages rather than relying on the coordinator's scope assessment:

- B. Shapiro and M. Tater, *On spectral polynomials of the Heun equation. I*, arXiv:0812.2321v1, section 4, Conjecture 3, printed p.13: <https://arxiv.org/pdf/0812.2321v1>. Its leaf condition is universal over the stated generalized Heun equations.
- B. Shapiro, *Van Vleck spectra of high-order Heun operators: finite-band universality and exterior asymptotics*, arXiv:2607.02700v1, Conjecture 1, printed p.4; compare Conjecture 2, printed p.18: <https://arxiv.org/pdf/2607.02700>. The former assumes simple leading roots; the latter explicitly adds genericity. The counterexample addresses the former, not the generic refinement.

The manuscript's matrix argument is complete, but a standard reference should be added after the statements about compound eigenvalue-products and the positive simple spectrum:

F. Gantmakher and M. Krein, *Sur les matrices complètement non négatives et oscillatoires*, *Compositio Mathematica* **4** (1937), 445--476. Primary PDF: <https://www.numdam.org/item/CM_1937__4__445_0.pdf>. Section 4, printed p.461, states the compound product rule as Kronecker's theorem, the Perron theorem, and Theorem 10 on positive simple eigenvalues of oscillatory matrices. Those statements and the spectral proof were read. No appeal to this theorem is needed in place of the submitted explicit compound proof.

A modern optional reference is A. Pinkus, *Totally Positive Matrices*, Cambridge University Press, 2009, chapter 5, section 5.2, Theorem 5.3. The publisher confirms the section/theorem locator and chapter pagination 127--153 at <https://doi.org/10.1017/CBO9780511691713.006>; full chapter body access was unavailable, so the original Gantmakher--Krein reference above has the stronger body-level verification.

No mathematical repair is required. An optional explanatory sentence can spell out the eigenvalue induction just as above, since the sentence “successively applying this fact” compresses a standard step. Retain the explicit disclaimer about the generic variant.

## Exact finite checks retained for reproducibility

The supplied `verification/heun_check.py` was inspected. It uses NumPy/SciPy floating-point diagnostics only at degrees divisible by three and is not needed to verify the all-degree proof. I did not run it or perform any large nonnormal eigenvalue experiment.

I wrote and executed independent standard-library exact-rational checks, then retained the same computations as `heun_exact_check.py` in this review directory at the coordinator's explicit request. Finite output:

```text
PASS: exact factors, stochasticity, all compound minors, principal minors and adjacent-move positivity for n=3,...,17
PASS: exact characteristic identity and zero multiplicity for n=3,...,11
```

The executed code used `fractions.Fraction`, direct rational elimination for determinants, and Faddeev--LeVerrier coefficients for characteristic polynomials. It checked all three residue classes, including q=1 boundary cases. These are finite transcription checks; they do not replace the analytic proof above. The saved script retains the executed computations and only adds documentation and formatting; it was not rerun to duplicate the same checks.

Reproduction command from the repository root:

```sh
python -B research/solutions/1032-heun-star-counterexample/heun_exact_check.py
```

Bounded current searches on 2026-11-03 for the spectral-tree question, the quartic example and the July 2026 paper did not identify an exact earlier counterexample among examined results. This is not an exhaustive priority certification.
