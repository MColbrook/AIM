# 182. A single critical activity for the continuum Widom–Rowlinson model

**Area:** Probability, continuum statistical mechanics, and phase transitions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`d\geq2`$. Consider two species of particles in $`\mathbb R^d`$, represented by locally finite point configurations $`(\omega_1,\omega_2)`$. Particles of the same species do not interact. Particles of different species satisfy the hard-core exclusion
```math
|x-y|>1\qquad(x\in\omega_1,\ y\in\omega_2).
```

Both species have the same activity $`\lambda>0`$. A Gibbs state means a Dobrushin–Lanford–Ruelle state: conditional on the configuration outside any bounded measurable region, the particles inside have the law of two independent Poisson processes of intensity $`\lambda`$, conditioned on the exclusion both within the region and across its boundary. Let $`\mathcal G_d(\lambda)`$ denote the set of all such Gibbs states, without a translation-invariance restriction.

**Does there exist a single $`\lambda_c(d)\in(0,\infty)`$ such that**
```math
\#\mathcal G_d(\lambda)=1\quad\text{for }0<\lambda<\lambda_c(d),
 \qquad
 \#\mathcal G_d(\lambda)>1\quad\text{for }\lambda>\lambda_c(d)?
```

The question makes no assertion at $`\lambda=\lambda_c(d)`$.

Grimmett states this question immediately after Theorem 11.46. That theorem gives constants $`0<\lambda_1\leq\lambda_2<\infty`$ such that uniqueness holds below $`\lambda_1`$ and multiple Gibbs states exist above $`\lambda_2`$. The missing conclusion is that the two regimes are separated by one critical activity. Although the section heading includes “lattice gas,” this question concerns the continuum model described before the separate lattice model.

## Application

This model describes demixing of two mutually excluding particle species. A single critical activity would identify one onset of phase coexistence as the common particle activity increases.

## References
1. G. Grimmett, *The Random-Cluster Model*, Springer, 2006, §11.6, Theorem 11.46 and the following open problem, printed pp. 337–338 in the [author's corrected/reprint copy](https://www.statslab.cam.ac.uk/~grg1000/books/rcm1-1.pdf). The retained author file is identified separately; no original publisher byte or layout parity is asserted.
2. D. Dereudre and P. Houdebert, *Sharp phase transition for the continuum Widom–Rowlinson model*, Annales de l'Institut Henri Poincaré, Probabilités et Statistiques **57** (2021), 387–407, [DOI:10.1214/20-AIHP1082](https://doi.org/10.1214/20-AIHP1082); the selected native text checked here is [arXiv:1807.04988v5](https://arxiv.org/abs/1807.04988v5), dated 2 June 2020. Proposition 2.5 identifies the two-color Gibbs states with area-interaction Gibbs states, with the symmetric case corresponding to $`z=\beta=\lambda`$. Section 3.2.1 explicitly leaves the single-threshold question on this diagonal open. Theorem 1 proves sharpness of a percolation transition with $`\beta`$ fixed; Theorem 2 and Corollary 3.1 give partial uniqueness results. These statements do not establish the displayed diagonal threshold.
3. B. Jahnel and D. Kamecke, *Phase transitions for the Widom–Rowlinson model in random environments*, [arXiv:2505.05319v1](https://arxiv.org/abs/2505.05319v1) (2025), Theorem 2.1 and Corollary 2.2. The homogeneous corollary proves nonuniqueness for sufficiently large activity; it does not identify a single threshold separating all smaller and larger activities.

4. B. Jahnel, D. Kamecke and C. Külske, *Lattice random-field Widom–Rowlinson models*, [arXiv:2605.18744v1](https://arxiv.org/abs/2605.18744v1) (2026). The official title and abstract identify a lattice model with a random field; no full native-body review of this comparator is claimed.

## Status review


**Known cases:** The fixed-temperature continuum percolation sharpness theorem does not locate a unique Gibbs-state threshold on the symmetric diagonal z=beta=lambda. Large-activity coexistence and random-field lattice results leave the full diagonal uniqueness/nonuniqueness assertion unresolved.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Bounded searches through 24 October 2026 located no matching complete published or announced resolution. The fixed-temperature percolation theorem and the sufficient large-activity coexistence results above were checked in their native statements. The 2026 paper *Lattice random-field Widom–Rowlinson models* concerns a lattice model with disorder, as identified by its official title and abstract; it is a different target. Independent current-status and all-status AIM/FURTHER/OpenAI semantic comparisons found no matching target or resolution. Indexed Prove2Me results and the returned live homepage subset were also inspected; these checks do not cover every mission.


### Online recheck, 2026-10-30

The fixed-temperature continuum percolation sharpness theorem does not locate a unique Gibbs-state threshold on the symmetric diagonal z=beta=lambda. Large-activity coexistence and random-field lattice results leave the full diagonal uniqueness/nonuniqueness assertion unresolved.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/1807.04988); [status source 2](https://arxiv.org/abs/2505.05319); [status source 3](https://arxiv.org/abs/2605.18744). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-4cd0cb59eed5bed5** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
