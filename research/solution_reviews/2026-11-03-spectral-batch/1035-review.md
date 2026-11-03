# AIM 1035: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Counterexample.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1035-matrix-local-mass-counterexample/aim1035.pdf), [TeX](../../solutions/1035-matrix-local-mass-counterexample/aim1035.tex), and [source receipt](../../solutions/1035-matrix-local-mass-counterexample/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1035](../../../problems/1035-do-matrix-local-mass-bounds-imply-stahltotik-regularity.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

A normalized 2-by-2 matrix measure satisfies polynomial local-mass bounds but its determinant regularity limit is zero.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

## Detailed mathematical audit

### Exact target mapping and primary-source scope

The canonical target is the implication from local matrix mass, for every positive eta, to determinant regularity for a nontrivial matrix measure whose block Jacobi essential spectrum is a finite interval union. The example has `ell=2`, `E=[-1,1]`, uniform mass bounded below by a positive constant times `m^{-3}` at every point of E, and determinant root limit zero rather than `Cap(E)^2=1/4`. These data contradict the complete implication.

The relevant primary source was read in the published-layout journal PDF at <https://www.math.auckland.ac.nz/sat/papers/11/11.pdf>, with the matching arXiv v2 also accessible at <https://arxiv.org/pdf/0711.2703>. The newer journal URL in the catalogue could not be fetched directly. The body explicitly defines matrix measures using positive-semidefinite matrices; its nontriviality condition is strict positivity for nonzero polynomial vectors. Conjecture 5.9 adds no positive-definite-a.e. density hypothesis. The rank-one density is therefore within scope. The stronger density hypothesis of the nearby Widom theorem is not an assumption of this conjecture.

### Independent proof checks

1. Direct integration gives the displayed total-mass matrix. Its determinant is `e^2-e^{-2}-(e-e^{-1})^2 = 2(1-e^{-2}) > 0`. Thus normalization by its positive inverse square root is legitimate.
2. If the vector-polynomial norm vanishes, continuity makes `a(x)+e^x b(x)` vanish throughout the interval, then the identity theorem makes it vanish everywhere. If `b` is nonzero, its exponential term dominates the polynomial `a` along the positive real axis, a contradiction. The invertible normalization preserves this property. All finite vector-polynomial moment forms and all monic matrix norms are therefore strictly positive, so the block orthogonalization and invertible off-diagonal blocks are legitimate.
3. The isometry `f -> v^T C f` has range containing every scalar polynomial and hence dense range in scalar L2. Its extension is onto and intertwines multiplication by x. Multiplication by x on scalar Lebesgue L2 of the interval has spectrum and essential spectrum exactly the whole interval and no discrete spectrum. This verifies the correct block-Jacobi essential spectrum, despite spectral multiplicity one. No full-matrix multiplicity assumption is required.
4. Expanding the determinant gives one half of the double integral of `(e^s-e^t)^2`. On the interval, the derivative lower bound gives at least `e^{-2}L^4/12`. Dividing by the trace upper bound gives the advertised `L^3` lower bound on the smallest eigenvalue. Under conjugation by C this loses at most the factor `lambda_max(M)`. The truncated interval always has length at least `1/m`, including endpoints and m=1. Finally a fixed positive power-law lower bound exceeds `exp(-eta m)` for all large m, for each fixed eta.
5. Repeated integration by parts gives the Padé identity for every positive n. At t=1 the first nonzero endpoint derivative is of order n-1 and has value `(-1)^{n-1}(n-1)!`, making the polynomial multiplying the exponential monic of degree n. At t=0 the first nonzero derivative has order n, so the other polynomial has degree at most n-1. This independently checks the normalization and indexing. The beta integral yields exactly the bound `e n!/(2n)!` on the interval; no approximation theorem is imported.
6. The trial matrix is monic because both diagonal entries have leading coefficient one and the upper-right entry has degree at most n-1. Its normalized version `C^{-1} T_n C` is still monic, and its norm is exactly `C K_n C`. For any monic competitor, its difference from the orthogonal monic polynomial has degree below n, so both cross terms vanish and the norm dominates H_n in Loewner order. Positive-definite determinant monotonicity is applicable.
7. The Gram determinant is at most the product of its diagonal entries. The displayed bound `4e^2 (n!/(2n)!)^2` is valid (and slightly loose). Dividing by `det M` correctly accounts for normalization. From the leading coefficient recurrence one obtains `det H_n = |det(A_1 ... A_n)|^2`; source equation (2.34) confirms the same convention. The factorial ratio is bounded by `(n+1)^{-n}`, so taking nth roots proves the actual limit is zero, not only a small liminf. Capacity one half for the interval gives the required contradiction.

No mathematical repair is required. The rank-one scope explanation should remain in the standalone paper: a variant requiring a positive-definite density almost everywhere is not addressed.

### Standalone bibliography and citation placement

Use a bibliography entry with key such as `DPS08`:

D. Damanik, A. Pushnitski and B. Simon, *The Analytic Theory of Matrix Orthogonal Polynomials*, *Surveys in Approximation Theory* **4** (2008), 1--85. Published PDF: <https://www.math.auckland.ac.nz/sat/papers/11/11.pdf>. Author archive: <https://arxiv.org/abs/0711.2703> (v2, 31 January 2008).

Suggested precise placements in the submitted source:

- In the opening attribution, cite `DPS08`, Conjecture 5.9 and (5.20), printed p.72.
- After the assertion about the admissible matrix measures and their polynomial nondegeneracy, cite section 1.2, printed p.5, and Lemma 2.1, printed p.16.
- The monic variational statement may additionally cite Theorem 2.4, printed p.17, though it is proved in the manuscript.
- At the regularity definition or the comparison value, cite Theorem 5.4(i), printed p.70.
- Replace **“This is also equation (2.34) of the primary source”** with **“This is also [DPS08, Eq. (2.34)]”**, printed p.21. Do not leave an undefined “primary source” reference in the standalone manuscript.

### Script

Inspected all of `verify_pade_identity.py` before execution. It uses only exact fractions and factorials, with no filesystem/network operations. Reproduction:

```sh
python -B research/solutions/1035-matrix-local-mass-counterexample/verify_pade_identity.py
```

Exit zero; output: `PASS: monicity and remainder coefficients for n=1,...,16`. The all-degree identity is justified by the integration-by-parts argument, independently of this finite check.
