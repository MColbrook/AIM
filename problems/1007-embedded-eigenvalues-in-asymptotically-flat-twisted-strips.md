# 1007. Embedded eigenvalues in asymptotically flat twisted strips

**Area:** Spectral geometry and waveguides
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Consider the all-Dirichlet Laplace–Beltrami operator $`H`$ on the abstract Riemannian strip $`\Omega_0=\mathbb R\times(-a,a)`$, with metric induced by the ruled-surface immersion

```math
\Omega=\{\Gamma(s)+tN_{\Theta}(s):s\in\mathbb R,\ -a<t<a\}\subset\mathbb R^{n+1},
```


with $`n\geq2`$, $`a>0`$, a unit-speed $`C^{1,1}`$ reference curve $`\Gamma`$, and a Lipschitz unit normal field $`N_{\Theta}`$ built from a relatively parallel normal frame as in Krejčiřík–Zahradová. Thus self-intersections of the image do not identify points of $`\Omega_0`$. Write $`k(s)`$ for the curvature vector and $`\Theta(s)`$ for the unit twisting vector. Under **all the hypotheses of their Corollary 5.3**—in particular $`k\cdot\Theta=0`$, $`\Theta'\not\equiv0`$, $`a\|\Theta'\|_{L^\infty}\leq\sqrt2`$, and $`|\Theta'(s)|\to0`$ as $`|s|\to\infty`$—does $`H`$ have **no eigenvalues strictly above** $`E_1=(\pi/2a)^2`$?

This is the unresolved point-spectrum part of their published Open Problem 5.6. The source asks about $`[E_1,\infty)`$, but its proven Hardy inequality $`H-E_1\geq c/(1+s^2)`$ already excludes an eigenfunction at $`E_1`$. The separate resonance question in Open Problem 5.6 is not part of this entry.

## Application

The model tests whether geometric twisting can prevent a waveguide from supporting a localized bound state whose energy lies inside its propagating spectrum.

## Known results and scope

Theorem 5.1 gives the positive Hardy bound. Corollary 5.3 proves $`\sigma(H)=\sigma_{\mathrm{ess}}(H)=[E_1,\infty)`$ and excludes discrete eigenvalues below the continuum; it does **not** determine whether $`\sigma_{\mathrm p}(H)\cap(E_1,\infty)`$ is empty. Results for planar mixed-boundary strips, solid tubes, quasi-conical domains or asymptotically diverging twist do not answer this all-Dirichlet, asymptotically flat ruled-strip question.

## References

1. D. Krejčiřík and K. Zahradová, [*Quantum strips in higher dimensions*](https://files.ele-math.com/articles/oam-14-41.pdf), *Operators and Matrices* **14** (2020), 635–665, [DOI:10.7153/oam-2020-14-41](https://doi.org/10.7153/oam-2020-14-41), Eq. (3.1), Theorem 5.1, Corollary 5.3 and Open Problem 5.6 (printed p. 654). [Original arXiv version](https://arxiv.org/abs/1906.02431v1).
2. D. Krejčiřík, [*Spectral geometry: old questions and new answers*](https://arxiv.org/html/2609.28602v1), arXiv:2609.28602v1 (2026), Section 2.3. This survey's embedded-eigenvalue discussion uses different domain geometries.
3. S. Sadeghi, [*An embedded eigenvalue in an asymptotically flat purely twisted strip*](../research/solutions/siavash-sadeghi-1007/twisted-strip-counterexample.pdf), 2 November 2026, revised 3 November 2026. [TeX source](../research/solutions/siavash-sadeghi-1007/twisted-strip-counterexample.tex), [solution package](../research/solutions/siavash-sadeghi-1007/README.md), and [independent maintainer audit](../research/solution_reviews/2026-11-03-pr181/1007-review.md).

## Status review

**Outcome:** Counterexample.

**Resolution, 2026-11-03:** Sadeghi constructs an admissible purely twisted strip with a nonzero square-integrable eigenfunction strictly between its first two transverse thresholds. For unit half-width, put

```math
m=\frac13-\frac2{\pi^2},\qquad k=(2m)^{-1/2},\qquad
\lambda_* = \frac{\pi^4}{4(\pi^2-6)}.
```

For every sufficiently large scale $`S`$, some phase $`\delta\in[0,2\pi]`$ makes the twist profile

```math
q(s)^2=\frac{16k}{S+|s|}\left(1+\frac12\cos(2k|s|+\delta)\right)
```

support this embedded eigenvalue. Taking $`S\ge12k`$ as well as the proof's contraction bounds gives $`\|q\|_\infty\le\sqrt2`$; the twist is nonzero and tends to zero at both ends. A straight reference curve with rotating normal realizes the required metric and satisfies every hypothesis in the Problem statement. Dilation gives a counterexample for every half-width $`a>0`$, at energy $`a^{-2}\lambda_*`$, in every allowed ambient dimension.

The [independent maintainer audit](../research/solution_reviews/2026-11-03-pr181/1007-review.md) checked the complete argument at PR revision `9491e1e3d3ac403100ce5ff6b8b663d0998fc922`, including all closed transverse modes, the weighted inverse estimates, the exact nonlocal scalar equation, phase selection, and the full operator-domain identity after reflection. Codex performed this AI review on 3 November 2026 and reproduced the 28 exact symbolic identities in normal and optimized Python. This is an analytic existence proof; no numerical scale or phase, human peer review, or Lean verification is asserted. The separate resonance question remains outside this entry.

### Earlier status checks, through 2026-10-30

The asymptotically flat nontrivially twisted strip has all Corollary 5.3 hypotheses and only eigenvalues strictly above threshold are asked. Other waveguide geometries and the known Hardy threshold exclusion do not settle embedded point spectrum here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published paper retains the exact question. Targeted later-primary, proof, counterexample and announcement searches through 23 October 2026 found no matching complete answer for the stated strip class. A semantic check found no matching AIM or admitted FURTHER problem; AIM 095 concerns a different perturbed-periodic Schrödinger setting. These checks are bounded and cannot establish absence of all results. The [source and status audit](../FURTHER_problems/_tracking/arxiv2139-two-candidate-independent-audit-2026-10-23.json) records the verified scope and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-037f4347aa864e41**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
