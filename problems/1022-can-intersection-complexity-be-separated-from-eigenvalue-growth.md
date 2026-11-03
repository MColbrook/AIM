# 1022. Can intersection complexity be separated from eigenvalue growth?

**Area:** Spectral geometry and embedded hypersurfaces
**Status:** ✅ SOLVED
**Last checked:** 2026-11-03

## Problem statement

Fix an integer $`n\ge2`$. For a smooth compact connected embedded hypersurface $`\Sigma^n\subset\mathbb R^{n+1}`$ without boundary, give $`\Sigma`$ its induced Riemannian metric. Let
```math
0=\lambda_0(\Sigma)<\lambda_1(\Sigma)\le\lambda_2(\Sigma)\le\cdots
```

be the eigenvalues of the nonnegative Laplace–Beltrami operator $`-\mathrm{div}_\Sigma\nabla_\Sigma`$, with multiplicity. Define its intersection index by
```math
i(\Sigma)=\sup_{\ell\pitchfork\Sigma}\#(\ell\cap\Sigma),
```

where the supremum is over transverse affine lines, and assume $`i(\Sigma)<\infty`$.

Do there exist a constant $`A_n>0`$ and a continuous function $`F_n:[0,\infty)\to\mathbb R`$, both chosen for this dimension and independent of $`\Sigma`$ and $`k`$, such that
```math
\lambda_k(\Sigma)\mathrm{Vol}_n(\Sigma)^{2/n}
\le F_n(i(\Sigma))+A_n k^{2/n}
\qquad(k\ge1)?
```


The coefficient of $`k^{2/n}`$ must depend only on the dimension. No prescribed sharp Weyl coefficient is required.

## Application

This asks whether the complexity of an embedded surface can enter a spectral estimate through an additive term while the coefficient governing the growth of higher frequencies stays uniform.

## Known results and scope

Colbois, Dryden and El Soufi [3, Theorem 1.2] prove the multiplicative estimate
```math
\lambda_k(\Sigma)\mathrm{Vol}_n(\Sigma)^{2/n}
\le c(n)i(\Sigma)^{2/n}k^{2/n}.
```

It gives the desired type of bound for convex hypersurfaces, whose intersection index is two, but its coefficient still depends on the index in the general case.

Pétiard explicitly asks the additive question in [1, p. 3] and repeats it in [2, §1.5, printed p. 17]. His counterexample concerns the different isoperimetric ratio
$`I(\Sigma)=|\Sigma|/|\Omega|^{n/(n+1)}`$, where $`\partial\Omega=\Sigma`$; it does not settle this intersection-index question.

Bounds involving min-conformal volume [4] or intrinsic packing, volume growth and injectivity data [5] use additional geometric quantities. They do not, as stated, give the requested function of $`i(\Sigma)`$ alone.

## References

1. L. Pétiard, [*Counter-example to a Kröger type spectral inequality*](https://arxiv.org/abs/1706.09189), arXiv:1706.09189v1, 2017, pp. 1–3, especially the question on p. 3.
2. L. Pétiard, [*Isoperimetric inequalities for Laplace and Steklov problems on Riemannian manifolds*](https://libra.unine.ch/server/api/core/bitstreams/cb35ac23-61a8-402a-9fdb-a1eb4d47c041/content), PhD thesis, Université de Neuchâtel, 2019, §1.5, printed pp. 15–18; the question is on printed p. 17 (PDF p. 29).
3. B. Colbois, E. B. Dryden and A. El Soufi, [*Bounding the eigenvalues of the Laplace–Beltrami operator on compact submanifolds*](https://doi.org/10.1112/blms/bdp100), *Bulletin of the London Mathematical Society* 42(1) (2010), 96–108, Theorem 1.2; [primary preprint](https://arxiv.org/abs/0909.5346).
4. A. Hassannezhad, [*Bornes supérieures pour les valeurs propres d’opérateurs naturels sur les variétés riemanniennes compactes*](https://www.applis.univ-tours.fr/theses/2012/asma.hassannezhad_4233.pdf), PhD thesis, Université François Rabelais de Tours, 2012, Theorem 1.1.1, Corollary 1.1.2 and Theorem 2.1.1.
5. B. Colbois and A. Girouard, [*Metric upper bounds for Steklov and Laplace eigenvalues*](https://aif.centre-mersenne.org/articles/10.5802/aif.3742/), *Annales de l’Institut Fourier* 76(4) (2026), 1519–1536, DOI 10.5802/aif.3742; [arXiv:2108.03101v2](https://arxiv.org/abs/2108.03101), Corollaries 4 and 12.
6. M. J. Colbrook, [*A counterexample to an additive intersection-index eigenvalue bound*](../research/solutions/1022-additive-intersection-index-counterexample/aim1022.pdf), 3 November 2026. [TeX source](../research/solutions/1022-additive-intersection-index-counterexample/aim1022.tex), [package and reproduction](../research/solutions/1022-additive-intersection-index-counterexample/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-spectral-batch/1022-review.md).

## Status review

**Outcome:** Counterexample.

**Reviewed result, 2026-11-03:** Smooth embedded hypersurfaces violate every proposed dimension-only additive separation of intersection index and eigenvalue growth. The [manuscript](../research/solutions/1022-additive-intersection-index-counterexample/aim1022.pdf) and [individual audit](../research/solution_reviews/2026-11-03-spectral-batch/1022-review.md) record the proof, checked references and exact target comparison. Review was performed by Codex (AI).

### Earlier status check, 2026-10-30

The intersection-index term must be additive with a dimension-only coefficient of eigenvalue growth. Existing multiplicative index bounds and other metric spectral estimates do not separate these terms.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original formulation, the thesis passage and the definition of intersection index were checked against primary sources. A bounded search of later results and announcements found no matching complete resolution. The problem was compared with all statuses in the AIM/OpenAI snapshots and the current FURTHER catalogue; the private review records those boundaries. The [source review](../FURTHER_problems/_tracking/focused-intersection-index-additive-spectrum-C162-A-20261028/INTERSECTION-INDEX-EXACT-PRIMARY-CURRENT-982MODELS615P1704-PEER-PASS-NO-ADMISSION-R3.json), [independent review](../FURTHER_problems/_tracking/focused-intersection-index-additive-spectrum-C162-A-20261028/ROOT-INDEPENDENT-PRIMARY-SCALE-INDEX-AND-LATER-THEOREM-REVIEW-PASS.json) and [current all-status comparison](../FURTHER_problems/_tracking/focused-intersection-index-additive-spectrum-C162-A-20261028/ROOT-FRESH-982MODELS615P-1704ROWS-PRECISE-DUPLICATE-RECHECK.json) retain the exact scope and limitations. These are bounded AI checks, not human peer review or a proof certificate.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8bdc8c810db9b75d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
