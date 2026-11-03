# AIM 1018: final review and scope

**Author and submitter:** Matthew J. Colbrook.

**Disposition:** Solved — Counterexample.

**Reviewed:** 3 November 2026, by Codex (AI). An independent reviewer read the complete argument; the coordinator checked the target mapping, applied the editorial corrections, verified the final manuscripts and repository consistency, and independently audited the torus and Heun arguments. This does not assert human peer review or Lean verification.

**Proof:** [Standalone manuscript](../../solutions/1018-limit-periodic-hull-spectral-type/aim1018.pdf), [TeX](../../solutions/1018-limit-periodic-hull-spectral-type/aim1018.tex), and [source receipt](../../solutions/1018-limit-periodic-hull-spectral-type/SOURCE_RECEIPT.json).

**Target:** [Current AIM 1018](../../../problems/1018-can-spectral-type-vary-within-a-limit-periodic-schrodinger-hull.md) at base `3fa50884d129a08fec3c09cb4765e8ecad97d6ee`. Its Problem statement is preserved.

One uniform limit-periodic hull contains both a phase with a nonzero point spectral component and a phase with no eigenvalues.

The editorial and citation refinements recommended below have been applied. They do not change the construction or the claimed theorem. This record distinguishes each proved theorem from the full catalogue question.

## Detailed mathematical audit

### Exact target mapping

The current question asks whether the *set of nonzero spectral components* is constant over every uniform limit-periodic hull, with constant off-diagonal coefficients equal to one. It does not ask for pure point spectrum at the exceptional phase. The manuscript constructs a bounded real sampling function on the dyadic odometer and two members of the same uniform hull: the zero phase has a nonzero point spectral component; the explicitly constructed other phase has no eigenvalues. That is sufficient to make the two component sets different and disproves the entire universal assertion.

### Independent proof checks

1. The triangular functions have increments bounded by `2^{-k}` even at the corners of the cyclic distance function. Consequently the increment series is uniformly convergent, while the original triangular-function series is only needed on the integer orbit. Its tail on that orbit is exactly a geometric multiple of `|n|` once `16^k >= 2|n|`.
2. With the least admissible `K`, one has `16^K <= 32|n|`, including `K=1`. The lower bound in (11) therefore gives `H(n)^4 >= |n|^3/2`. This proves square summability of `exp(-H(n))`; it is an all-integer estimate rather than an inference from a numerical sample.
3. Absolute convergence on integers justifies subtraction of `H(n+1)` and `H(n)`. It gives exactly the uniformly defined increment `b(n)`. Both ratios of the proposed positive eigenfunction therefore agree with the two exponential terms in the potential. The zero-energy eigenvalue equation is exact.
4. The potential is bounded and uniformly approximated by periodic potentials, with the advertised `2e 2^{-K}` error. The phase-to-potential map is continuous in the uniform norm because each finite approximation factors through a finite quotient and the error is uniform. Compactness and density of the integer orbit give equality with the entire uniform hull. Injectivity is not needed.
5. At the chosen phase, the center displacement is divisible by `16^{K_{j+1}}`. The corresponding finite-level potential is exactly reflection-symmetric about `n_j`; two uniform approximation errors give (17). Since `K_{j+1} >= n_j^2`, the reflection error defeats every fixed exponential transfer bound.
6. I recomputed the reflection Wronskian identity with the manuscript's sign convention. Summation from minus infinity is justified because both square-summable sequences tend to zero. Cauchy--Schwarz bounds the whole Wronskian by `d_j`, uniformly in the site. At the reflection center, either the value of the original solution is at most `sqrt(d_j)`, yielding a small symmetric pair, or the antisymmetric pair is small by division of the Wronskian estimate. The latter division is made only in the strict complementary case. In both cases the residual has pointwise magnitude at most `d_j` after the eigenfunction has norm one. Backward propagation for `n_j` sites gives a bound of the form `C C_E^{n_j}(sqrt(d_j)+n_j d_j)`. It tends to zero by the lemma's stated hypothesis. The reflected solution tends to zero at sites zero and one, which forces two successive values of the original solution to vanish. This excludes every eigenvalue, including the case of exact reflection error zero.
7. The supplementary factorization expands to the negative of the Schrödinger quadratic form: its diagonal term is `e^{-b(n)}+e^{b(n-1)}` and its off-diagonal term is minus twice the adjacent real product. This verifies the upper-edge statement. The Baire argument uses uniform-norm continuity of reflection and a dense tail of the negative integer orbit; it proves the stated dense set without an additional spectral theorem. Scaling the increment series by any fixed positive delta preserves square summability and all reflection estimates. A constant shift preserves spectral components.

### Required or advisable editorial edits

At submitted `1018.tex:125`, replace **“The series is finite”** by **“The series converges to a finite value”**. For a nonzero integer, infinitely many of its terms are nonzero. The subsequent estimate already proves the correct assertion, so this is wording, not a repair of the construction.

For standalone publication, state the full target in the introduction: define the component set or explicitly say that having a nonzero point component at one phase and no point component at another answers the all-hull classification question. Cite Damanik--Fillman Question 10.2 at that statement. Add the following bibliography entries as appropriate:

- D. Damanik and J. Fillman, *Spectral Properties of Limit-Periodic Operators*, in *Analysis and Geometry on Graphs and Manifolds*, M. Keller, D. Lenz and R. K. Wojciechowski (eds.), London Mathematical Society Lecture Note Series **461**, Cambridge University Press, 2020, pp. 382--444. DOI: <https://doi.org/10.1017/9781108615259.016>. Exact question body inspected in <https://arxiv.org/pdf/1802.05794v1>, Question 10.2, printed p.36. Do not silently transfer that locator to the published chapter, whose complete body was not accessed here.
- D. Damanik and Z. Gan, *Spectral properties of limit-periodic Schrödinger operators*, *Communications on Pure and Applied Analysis* **10** (2011), no.3, 859--871. DOI: <https://doi.org/10.3934/cpaa.2011.10.859>. Primary body: <https://arxiv.org/html/0906.3337v3>, Theorem 1.1, Remark (v), and Lemma 2.2. An optional introductory sentence citing Remark (v) accurately identifies the earlier phase-uniformity question.
- J. Kwiatkowski and A. Siemaszko, *Discrete orbits in topologically transitive cylindrical transformations*, *Discrete and Continuous Dynamical Systems* **27** (2010), no.3, 945--961. DOI and publisher record: <https://www.aimsciences.org/article/doi/10.3934/dcds.2010.27.945>. The publisher abstract confirms the odometer/discrete-orbit context. No theorem from that paper is needed or was used in validating this construction.

### Script

Inspected all of `verify_lp_cocycle.py` before executing it. It uses only `fractions`, has no filesystem/network operations, and computes the infinite geometric tail exactly. Reproduction:

```sh
python -B research/solutions/1018-limit-periodic-hull-spectral-type/verify_lp_cocycle.py
```

Exit zero; output: `PASS: exact cocycle, parity, boundedness, and growth checks on [-1024,1024]`; tail parameter `K = 3`. This is a finite transcription/consistency check, not the proof of the all-integer result or of the reflection lemma.
