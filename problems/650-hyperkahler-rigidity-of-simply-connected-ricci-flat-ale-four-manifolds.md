# 650. Hyperkähler rigidity of simply connected Ricci-flat ALE four-manifolds

**Area:** Riemannian geometry / mathematical relativity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a smooth connected simply connected complete noncompact Riemannian four-manifold with $`\mathrm{Ric}_g=0`$. Suppose that it is **asymptotically locally Euclidean (ALE)**: there are a compact set $`K\subset M`$, $`R>0`$, a finite subgroup $`\Gamma\subset\mathrm{SO}(4)`$ acting freely on $`S^3`$, and a diffeomorphism

```math
\Phi:(\mathbb R^4\setminus\overline{B_R})/\Gamma\longrightarrow M\setminus K
```

such that, for some $`\tau>0`$ and every integer $`k\ge0`$,

```math
\left|\nabla_{g_0}^{k}(\Phi^*g-g_0)\right|_{g_0}
 =O(r^{-\tau-k}),\qquad r\longrightarrow\infty,
```

where $`g_0`$ is the Euclidean quotient metric and $`r`$ its radial coordinate.

**Must $`(M,g)`$ be hyperkähler?** Here this means that the given metric admits global parallel orthogonal complex structures $`I,J,K`$ satisfying

```math
I^2=J^2=K^2=-\mathrm{Id},\qquad IJ=K=-JI.
```

The compatible orientation may be chosen. No complex structure, spin structure, symmetry or inclusion $`\Gamma\subset\mathrm{SU}(2)`$ is assumed. The flat case is included.

This is the four-dimensional conjecture in Bando–Kasue–Nakajima's Remark 1.8(3). Their equivalent intrinsic setting assumes Euclidean lower volume growth and finite $`\int_M|\mathrm{Rm}|^2`$. The ALE assumptions above give both conditions, and their Theorem 1.5 gives ALE coordinates in the converse direction.

## Application

Ricci-flat ALE spaces model bubbles in degenerating four-dimensional Einstein metrics and appear as gravitational instantons in Euclidean quantum gravity. The assertion would reduce this entire simply connected class to the hyperkähler spaces classified by Kronheimer, without imposing complex geometry in advance.

## References

1. S. Bando, A. Kasue and H. Nakajima, *On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth*, Invent. Math. **97** (1989), 313–349, [doi:10.1007/BF01389045](https://doi.org/10.1007/BF01389045), Theorem 1.5 and Remark 1.8(3), pp.314–315. A [public course collection](https://www.math.stonybrook.edu/Courses/MAT683/201001/MAT683S10.pdf) contains the digitized article beginning at PDF page353.
2. B. Araneda and J. Lucietti, *All toric Hermitian ALE gravitational instantons*, J. Geom. Anal. **36** (2026), article345, [published paper](https://doi.org/10.1007/s12220-026-02579-7); [latest arXiv revision, 13 October 2026](https://arxiv.org/abs/2510.09291v2), Conjecture1.1, Theorem1.2 and Definition3.1.
3. P. Ghosh, *Mass and rigidity in almost Kähler geometry*, [arXiv:2603.08627v2](https://arxiv.org/abs/2603.08627v2), Theorems1.15–1.16. This assumes that the given metric is almost Kähler.
4. M. B. Law, *An analytical characterization of Eguchi–Hanson space and its higher-dimensional analogs*, [arXiv:2604.23410v1](https://arxiv.org/abs/2604.23410v1), Theorem1.2. This imposes a particular end group and an additional bound on the Lichnerowicz kernel.

## Status review


**Known cases:** The current October ALE revision assumes both toric and Hermitian structure. Almost-Kahler and prescribed-end/kernel cases also add hypotheses absent from the general simply connected Ricci-flat ALE question.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The latest toric-Hermitian paper explicitly retains the general conjecture. Its classification requires a compatible Hermitian structure and torus symmetry. The almost-Kähler theorem requires a symplectic form compatible with the given metric. Neither hypothesis is assumed here. The analytical Eguchi–Hanson theorem also has additional end-group and kernel restrictions.

Simply connectedness matters: finite quotients can be locally hyperkähler without admitting a global hyperkähler triple. The proposed question concerns the given Ricci-flat metric, rather than existence of a different special-holonomy metric on the same manifold.

Dated searches and comparisons with the AIM collection, relevant OpenAI primary statements and the current FURTHER list are recorded in the [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/ale-hyperkahler-review.json). The original article's question and surrounding hypotheses were visually checked; the owner subsequently completed the pinned 37-page article. Current papers were reviewed for the selected statements above, without independent certification of all their proofs. The scoped catalogue comparison, independent selected-primary audit and coordinator review passed.

[Independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-ale-hyperkahler-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/ale-hyperkahler-duplicate-navigation.json), [catalogue review](../FURTHER_problems/_tracking/parallel/complex-bayesian/ale-hyperkahler-prove2-0159-review.json) and [coordinator review](../FURTHER_problems/_tracking/ale-hyperkahler-coordinator-review-2026-10-18.json) preserve the exact hypotheses, reading extents and remaining version gaps. This is a dated literature assessment, not a guarantee that no solution exists.


### Online recheck, 2026-10-30

The current October ALE revision assumes both toric and Hermitian structure. Almost-Kahler and prescribed-end/kernel cases also add hypotheses absent from the general simply connected Ricci-flat ALE question.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2510.09291); [status source 2](https://arxiv.org/abs/2603.08627); [status source 3](https://arxiv.org/abs/2604.23410). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-aad8c03d2e3c83bd** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
