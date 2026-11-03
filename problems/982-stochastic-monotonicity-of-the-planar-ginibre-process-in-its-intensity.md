# 982. Stochastic monotonicity of the planar Ginibre process in its intensity

**Area:** Determinantal point processes and stochastic order
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For every $`\alpha>0`$, let $`\Xi_\alpha`$ be the simple determinantal point process on $`\mathbb C`$ whose kernel, with respect to planar Lebesgue measure $`dA`$, is
```math
K_\alpha(z,w)=\frac{\alpha}{\pi}\exp\!\left(\alpha z\overline w-\frac{\alpha}{2}|z|^2-\frac{\alpha}{2}|w|^2\right).
```
Its intensity is $`\alpha/\pi`$. For every $`0<\alpha<\beta`$, does there exist a coupling of these laws such that
```math
\widetilde\Xi_\alpha\subseteq\widetilde\Xi_\beta\qquad\text{almost surely}?
```
Inclusion means inclusion of their counting measures. Equivalently, is $`\mathbb E F(\Xi_\alpha)\le\mathbb E F(\Xi_\beta)`$ for every bounded increasing Borel function on locally finite configurations, with their usual vague-topology Borel structure? A separate coupling for each pair suffices.

## Application

The Ginibre process models repelling points and arises as an infinite-volume eigenvalue process. An inclusion coupling would let changes in density be compared while keeping existing points, and would transfer bounds for increasing spatial events between densities.

## References

1. Russell Lyons, *Determinantal probability: Basic properties and conjectures*, Proceedings of the International Congress of Mathematicians, Seoul 2014, volume IV, 137–161. [Published chapter](https://rdlyons.pages.iu.edu/pdf/icm-pub.pdf), §3.8, printed p.153, physical p.17; [errata, 30 December 2025](https://rdlyons.pages.iu.edu/errata/icm.pdf).
2. Laurent Decreusefond and Guillaume Moroz, *Optimal transport between determinantal point processes and application to fast simulation* (2021). [Primary text](https://www.vmsta.org/journal/VMSTA/article/211/text), Remark 2 and Theorems 11, 13 and 17; [DOI](https://doi.org/10.15559/21-VMSTA180).
3. Jesper Møller and Eliza O'Reilly, *Couplings for determinantal point processes and their reduced Palm distributions with a view to quantifying repulsiveness* (2021). [Latest author version](https://arxiv.org/abs/1806.07347v6), Theorem 3.3; [DOI](https://doi.org/10.1017/jpr.2020.101).
4. Moritz Otto, *Couplings and Poisson approximation for stabilising functionals of determinantal point processes* (2025). [Published text](https://doi.org/10.1017/S0963548325000082), Theorems 2.1–2.2.

## Status review


**Known cases:** The process intensity varies by spatial scaling; pairwise almost-sure inclusion is needed. Palm couplings, transport/simulation, Poisson approximation and finite Ginibre Poincare formalization do not establish this monotonicity.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The process intensity varies by spatial scaling; pairwise almost-sure inclusion is needed. Palm couplings, transport/simulation, Poisson approximation and finite Ginibre Poincare formalization do not establish this monotonicity.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Lyons explicitly asks this intensity question. His 2025 errata resolves or corrects other parts of the chapter without changing this question. Increasing finite matrix rank at a fixed Gaussian weight is a different comparison.

The inspected transport results use shared eigenfunctions or move configurations of equal size; reduced Palm coupling deletes at most one point. Otto's result approximates a rescaled process of isolated Ginibre points by a Poisson process. None of these inspected statements supplies the displayed coupling. The 2026 non-Hermitian minor-process results concern Gaussian fluctuation limits, also a different target.

Independent thinning retains the wrong pair correlation, while dilation moves points. The standard sufficient operator-order criterion does not directly apply to the nonnested Bargmann–Fock projection ranges. These observations do not disprove monotonicity.

Bounded current searches found no matching complete resolution or announcement. All ten returned catalogue-description windows were read and no equivalent target was identified. Linked mission proofs remain separate obligations. The entire 25-page published source and one-page errata were read for discovery; later comparisons had selected extents. These are AI checks, not human peer review or an exhaustive absence certificate.

The [coordinator review](../FURTHER_problems/_tracking/ginibre-intensity-coordinator-review-2026-10-19.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-ginibre-intensity-monotonicity-review.json), [current checks](../FURTHER_problems/_tracking/ginibre-intensity-current-root-review-2026-10-19.json) and [duplicate comparison](../FURTHER_problems/_tracking/ginibre-intensity-duplicates-review-2026-10-19.json) retain exact scope and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8a57f9407262f2fb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
