# 1007. Embedded eigenvalues in asymptotically flat twisted strips

**Area:** Spectral geometry and waveguides
**Status:** 🟠 SOLUTION CLAIMED
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

## Status review

### Counterexample submitted, 2026-11-03

**Siavash Sadeghi** proposes a negative resolution of the full point-spectrum target. For every half-width, a sufficiently small positive oscillatory twist, decaying at infinity, produces an eigenvalue strictly between the first two transverse thresholds. The construction retains all transverse modes and selects a matching phase by a continuity argument.

The [proof PDF](../research/solutions/siavash-sadeghi-1007/twisted-strip-counterexample.pdf) and [editable source](../research/solutions/siavash-sadeghi-1007/twisted-strip-counterexample.tex) are accompanied by a [full target comparison](../research/solutions/siavash-sadeghi-1007/RESOLUTION_REPORT.md), [fresh mathematical audit](../research/solutions/siavash-sadeghi-1007/MATHEMATICAL_AUDIT.md), [reproduction record](../research/solutions/siavash-sadeghi-1007/REPRODUCTION_RECORD.md), and [dated submission search](../research/solutions/siavash-sadeghi-1007/TARGET_AUDIT.md).

Codex (AI) reviewed the complete supplied proof and re-derived its key estimates on 3 November 2026; no substantive defect was identified. Exact symbolic checks support the algebra, not the complete analytic proof. Further independent mathematical review remains pending, and no human peer review or formal verification is claimed. The scale threshold and selected phase are given by existence, not by certified numerical values. The separate resonance question is outside this entry.

The earlier status reviews below describe the evidence available at their dates.

### Online recheck, 2026-10-30

The asymptotically flat nontrivially twisted strip has all Corollary 5.3 hypotheses and only eigenvalues strictly above threshold are asked. Other waveguide geometries and the known Hardy threshold exclusion do not settle embedded point spectrum here.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The published paper retains the exact question. Targeted later-primary, proof, counterexample and announcement searches through 23 October 2026 found no matching complete answer for the stated strip class. A semantic check found no matching AIM or admitted FURTHER problem; AIM 095 concerns a different perturbed-periodic Schrödinger setting. These checks are bounded and cannot establish absence of all results. The [source and status audit](../FURTHER_problems/_tracking/arxiv2139-two-candidate-independent-audit-2026-10-23.json) records the verified scope and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-037f4347aa864e41**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
