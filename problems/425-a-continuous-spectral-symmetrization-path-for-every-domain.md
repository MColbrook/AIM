# 425. A continuous spectral symmetrization path for every domain

**Area:** Spectral shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\geq2`$ and let $`\Omega\subset\mathbb R^d`$ be a nonempty bounded open set. Write $`\lambda_1(\Omega)`$ for its first Dirichlet eigenvalue. If $`w_\Omega\in H^1_0(\Omega)`$ solves $`-\Delta w_\Omega=1`$, define its torsional rigidity by $`T(\Omega)=\int_\Omega w_\Omega\,dx`$.

Does there always exist a family of bounded open sets $`(\Omega_t)_{0\leq t\leq1}`$, with $`\Omega_0=\Omega`$, $`\Omega_1`$ an equal-volume ball, and $`|\Omega_t|=|\Omega|`$ for **every** $`t`$, such that

```math
\lambda_1(\Omega_t)\ \text{is nonincreasing},\qquad
T(\Omega_t)\ \text{is nondecreasing},
```


and $`t\mapsto\Omega_t`$ is **$`\gamma`$-continuous**? Here $`\gamma`$-continuity means that, whenever $`t_n\to t`$, the zero-extended Dirichlet solutions of $`-\Delta u=f`$ on $`\Omega_{t_n}`$ converge strongly in $`H^1(\mathbb R^d)`$ to the solution on $`\Omega_t`$, for every $`f\in L^2(\mathbb R^d)`$. Equivalently, within a common bounded ambient region one can use the $`L^2`$ distance between the zero-extended torsion functions. This is the topology of the cited paper, not just convergence in volume or of set boundaries.

The question is the general-domain case of Buttazzo's Remark 3.5. It asks for one path satisfying **both** monotonicity conditions throughout. In dimension one, the analogous general statement fails because merging two intervals forces a torsion discontinuity.

## Application

A positive answer would let one continuously round any bounded domain to a ball while preserving material volume and improving both its fundamental Dirichlet frequency and torsional rigidity. Such a path would connect spectral and compliance bounds with continuous shape optimization, beyond the static Faber–Krahn and Saint-Venant inequalities.

## References

1. G. Buttazzo, *On the Continuity of the Continuous Steiner Symmetrization*, **Journal of Convex Analysis** 30 (2023), no. 2, 615–626. [Published PDF](https://journalofconvexanalysis.com/articles/jca30033/jca30033.pdf?v=2), [DOI](https://doi.org/10.68381/jca30033). Introduction, pp. 615–617, specifies fixed volume, both functional directions and the $`\gamma`$ topology; Remark 3.5, p. 623, states the residual general-domain question.
2. G. Buttazzo and A. Pratelli, *An application of the continuous Steiner symmetrization to Blaschke–Santaló diagrams*, **ESAIM: Control, Optimisation and Calculus of Variations** 27 (2021), article 36. [DOI](https://doi.org/10.1051/cocv/2021038), [author manuscript](https://cvgmt.sns.it/media/doc/paper/4894/steiner_aldo201104.pdf). Theorem 1.1 gives the fixed-volume $`\gamma`$-continuous path for polyhedral domains, a dense but restricted class.
3. A. Yu. Solynin, *Continuous symmetrization via polarization*, **St. Petersburg Mathematical Journal** 24 (2013), no. 1, 117–166. [arXiv:1102.1004](https://arxiv.org/abs/1102.1004). This earlier continuous symmetrization result uses continuity properties of boundaries and function rearrangements; the selected passages do not establish this problem's Dirichlet-resolvent $`\gamma`$-continuous path.

## Status review


**Known cases:** The source still leaves general domains open. Polyhedral-domain and nested-domain paths do not simultaneously provide fixed volume, both functional monotonicities and full gamma-continuity for every bounded open domain.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Buttazzo proves or recalls several special cases and a $`\gamma`$-continuous bridge between nested domains. The latter need not preserve volume, and the polyhedral construction does not supply a path from every arbitrary open set. A separate arbitrary-domain eigenvalue path in Bucur–Henrot (2000) has left-continuity rather than the requested full $`\gamma`$-continuity and does not establish both functional directions. Bounded primary, announcement, author and version searches through 20 October 2026 found no exact complete proof or counterexample; this is not a guarantee that no later or unindexed result exists. The closest AIM and FURTHER questions concern static shape inequalities, not this continuous path.

The [selected source review](../FURTHER_problems/_tracking/buttazzo-steiner-primary-review-2026-10-20.json), [current-status review](../FURTHER_problems/_tracking/buttazzo-steiner-current-review-2026-10-20.json), [semantic comparison](../FURTHER_problems/_tracking/buttazzo-steiner-duplicates-review-2026-10-20.json) and [coordinator decision](../FURTHER_problems/_tracking/buttazzo-steiner-coordinator-review-2026-10-20.json) record the exact evidence and its limits. These checks do not certify the papers' proofs.


### Online recheck, 2026-10-30

The source still leaves general domains open. Polyhedral-domain and nested-domain paths do not simultaneously provide fixed volume, both functional monotonicities and full gamma-continuity for every bounded open domain.

Comparators and current-status sources: [status source 1](https://journalofconvexanalysis.com/articles/jca30033/); [status source 2](https://doi.org/10.1051/cocv/2021038). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-c9e4b2cc27a934bf** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
