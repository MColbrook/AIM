# 1026. Steklov zeros in a fixed boundary collar

**Area:** Spectral theory and spectral geometry
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Let $`d\ge2`$ and let $`\Omega\subset\mathbb R^d`$ be a bounded connected Lipschitz domain. A real weak Steklov eigenfunction of positive eigenvalue $`\sigma`$ is a nonzero $`u\in H^1(\Omega;\mathbb R)`$ satisfying
```math
\int_\Omega \nabla u\cdot\nabla v\,dx
 =\sigma\int_{\partial\Omega}\mathrm{Tr}u\mathrm{Tr}v\,d\mathcal H^{d-1}
 \qquad(v\in H^1(\Omega;\mathbb R)).
```

It is harmonic in the interior. Use its harmonic representative to define
$`Z_u=\{y\in\Omega:u(y)=0\}`$, and write
```math
\Omega_\delta=\{x\in\Omega:\mathrm{dist}(x,\partial\Omega)<\delta\}.
```


**Problem.** Do there exist constants $`\delta_\Omega>0`$ and $`C_\Omega>0`$, depending only on the fixed domain, such that for every such eigenpair and every $`x\in\Omega_{\delta_\Omega}`$,
```math
B(x,C_\Omega/\sigma)\cap Z_u\ne\varnothing?
```

The collar width must be independent of the eigenvalue. The assertion concerns every real eigenfunction, including arbitrary directions in a multiple eigenspace. Balls may meet the exterior, but their required zeros lie inside $`\Omega`$.

## Application

These harmonic modes describe media with a boundary spectral load. The proposed estimate identifies a region where sign oscillations persist at the boundary wavelength even when the mode's amplitude is small. It would help specify the spatial resolution needed to capture nodal interfaces near a boundary.

## References

1. S. Decio, *Nodal sets of Steklov eigenfunctions near the boundary: Inner radius estimates*, International Mathematics Research Notices **2022** (21), 16709–16729, [doi:10.1093/imrn/rnab198](https://doi.org/10.1093/imrn/rnab198). The precise proposed strengthening appears in Remark (ii) following Theorem 1, [arXiv:2102.05549v2, p. 3](https://arxiv.org/pdf/2102.05549v2#page=3).
2. O. Bruno and J. Galkowski, *Domains without dense Steklov nodal sets*, Journal of Fourier Analysis and Applications **26** (2020), article 45, [doi:10.1007/s00041-020-09753-7](https://doi.org/10.1007/s00041-020-09753-7); [primary author manuscript](https://www.homepages.ucl.ac.uk/~ucahalk/BandLimitedSteklov.pdf).
3. M. Mukherjee, *Wavelength-scale optional stopping, critical Feynman–Kac gauges, and capacitary spectral inequalities*, [arXiv:2608.15650v1](https://arxiv.org/html/2608.15650v1), §8.2–8.3, especially Theorems 8.3 and 8.5.

4. G. Xie and C. Zhang, [*Sharp Bounds for Nodal Sets of Steklov Eigenfunctions on Smooth Surfaces*](https://arxiv.org/abs/2610.28391), arXiv:2610.28391v2 (1 November 2026), Theorem 1.2 and its proof in §4.3, especially Lemmas 4.4–4.5. [Primary manuscript](https://arxiv.org/pdf/2610.28391v2).

## Status review

**Resolution update (3 November 2026):** Solved on the basis of an **unverified counterexample announcement**. Xie–Zhang’s Theorem 1.2 and its construction in §4.3 give one fixed bounded simply connected smooth Euclidean planar domain and a sequence of real, ordinary Steklov eigenfunctions with eigenvalues tending to infinity. Their entire interior nodal sets lie in boundary neighborhoods whose widths tend to zero. The conformal map and the resulting Euclidean domain are fixed throughout the sequence; this is not a varying-domain or weighted-boundary counterexample.

For any proposed fixed collar, choose an interior point in it with positive boundary distance. For all sufficiently late members of this sequence, every zero remains at least half that distance from the point, whereas the proposed ball radius tends to zero. This contradicts the displayed assertion, already in the smooth planar subclass of Lipschitz domains.

[Claimed solution](https://arxiv.org/pdf/2610.28391v2) · [Dated statement comparison and fixed-collar implication](../research/solution-status-audit-2026-11-03/lane-d/1026.json). The current version, theorem hypotheses and the implication for this local formulation were checked. The external proof has not been independently verified end-to-end here; no Lean verification or human peer review is asserted.

### Earlier status record



**Known cases:** The collar width is fixed independently of frequency. Boundary-centered nodal density and estimates in shrinking collars do not give this fixed-width assertion; the known global non-density examples do not decide a sufficiently small collar.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The collar width is fixed independently of frequency. Boundary-centered nodal density and estimates in shrinking collars do not give this fixed-width assertion; the known global non-density examples do not decide a sufficiently small collar.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Decio proves wavelength density for balls centered exactly on the boundary and explicitly suggests the fixed-collar extension above. The global density conjecture has counterexamples, but the cited construction leaves a sufficiently small fixed collar undecided. The 2026 norm estimates use collars whose widths shrink as $`\sigma^{-1}`$; they do not assert the displayed fixed-collar zero-density estimate.

Checks through 17 October 2026 have not located a complete resolution of this statement. All-status AIM and current announcement comparisons distinguish it from interior nodal-volume estimates, amplitude decay, and boundary nodal-component counts. The review record retains precise version and access limits; this is a literature check, not a proof of openness. [Review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/collar-density-review.json).

The independent selected-primary audit confirmed the full Lipschitz formulation. All15 returned windows from the186-page combined catalogue scan were read; none stated an equivalent target. These are listing-description checks, without certification of mission proofs. The final21-page IMRN body has not been compared with the19-page author version.

[Independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-collar-density-review.json), [catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/collar-density-prove2-0115-review.json) and [coordinator review](../FURTHER_problems/_tracking/collar-density-coordinator-review-2026-10-17.json) retain exact assumptions, versions and bounded search evidence.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b3f3a912668a85e3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
