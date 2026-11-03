# 827. Do bounded minimal graphs over the hyperbolic disk have radial limits almost everywhere?

**Area:** Geometric analysis and boundary behavior of nonlinear elliptic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D=\{z\in\mathbb C:|z|<1\}`$ carry the complete hyperbolic metric $`g=4|dz|^2/(1-|z|^2)^2`$. Suppose $`u\in C^2(D)`$ is bounded and its graph in $`(D,g)\times\mathbb R`$ is minimal; equivalently,

```math
\mathrm{div}_g\!\left(\frac{\nabla_g u}{\sqrt{1+|\nabla_g u|_g^2}}\right)=0.
```


**Must $`\lim_{r\uparrow1}u(re^{i\theta})`$ exist for Lebesgue-almost every $`\theta\in[0,2\pi)`$?** Boundedness makes any existing limit finite. An entire bounded minimal graph with no radial limit on a set of positive angular measure would refute the conjecture.

## Application

This is a Fatou-type boundary question for the minimal-surface equation in $`\mathbb H^2\times\mathbb R`$. It asks whether bounded solutions have almost-everywhere boundary traces without prescribing regular boundary data.

## Known results and scope

Collin and Rosenberg [1, printed p. 2358] explicitly conjecture this statement. Their Euclidean-disk theorem proves radial limits almost everywhere in the *Euclidean* metric, even for some unbounded solutions. The same paper constructs an *unbounded* hyperbolic minimal graph with radial limits failing almost everywhere; that example does not refute the bounded conjecture. Espinar and Rosenberg [2, Theorem 2.1] treat a class of divergence-form equations under a bounded metric-density hypothesis, which does not hold for the complete Poincaré disk. A later radial-limit lemma at a prescribed polygon vertex [3, Lemma 4] does not address arbitrary bounded entire graphs.

## References

1. P. Collin and H. Rosenberg, [*Asymptotic values of minimal graphs in a disc*](https://aif.centre-mersenne.org/item/10.5802/aif.2610.pdf), *Annales de l'Institut Fourier* **60** (2010), no. 7, 2357–2372, doi:10.5802/aif.2610; conjecture on printed p. 2358.
2. J. M. Espinar and H. Rosenberg, [*Fatou's Theorem and minimal graphs*](https://arxiv.org/pdf/0903.2684), arXiv:0903.2684v3 (2009), Theorem 2.1.
3. J. Castro-Infantes and J. M. Manzano, [*Genus 1 minimal k-noids and saddle towers in $`\mathbb H^2\times\mathbb R`$*](https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/genus-1-minimal-knoids-and-saddle-towers-in-mathbb-h2times-mathbb-r/EEE54DFBB5484163E54D1F4048722DCC), *Journal of the Institute of Mathematics of Jussieu* **22** (2023), no. 5, 2155–2175, doi:10.1017/S1474748021000591, Lemma 4.

## Status review


**Known cases:** The known Fatou theorem on a Euclidean disk and the hyperbolic unbounded counterexample do not answer the bounded complete-hyperbolic-disk target. Metric-density hypotheses in the later PDE theorem fail for the complete Poincare disk; special polygon vertices do not cover arbitrary graphs.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known Fatou theorem on a Euclidean disk and the hyperbolic unbounded counterexample do not answer the bounded complete-hyperbolic-disk target. Metric-density hypotheses in the later PDE theorem fail for the complete Poincare disk; special polygon vertices do not cover arbitrary graphs.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source, later-result and duplicate audit](../FURTHER_problems/_tracking/hyperbolic-minimal-graph-radial-limits-status-2026-10-21.json) distinguishes the bounded hyperbolic conjecture from these related statements. Bounded searches found no complete proof, counterexample or announced resolution through 21 October 2026; they cannot exclude unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a76a0398f1eede42**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
