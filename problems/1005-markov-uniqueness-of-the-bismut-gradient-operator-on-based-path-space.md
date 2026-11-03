# 1005. Markov uniqueness of the Bismut-gradient operator on based path space

**Area:** Geometric stochastic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be any smooth compact connected Riemannian manifold without boundary, of dimension at least two. Fix $`x_0\in M`$ and $`T>0`$. Let $`C_{x_0}M`$ be the continuous paths $`\sigma:[0,T]\to M`$ starting at $`x_0`$, equipped with Brownian-motion measure $`\mu`$, with Brownian generator $`\frac12\Delta_M`$. There is no terminal endpoint constraint.

For almost every path, let $`{\parallel}_t:T_{x_0}M\to T_{\sigma(t)}M`$ be stochastic Levi–Civita parallel translation. The Bismut tangent space is

```math
\mathcal H_\sigma=\{v_t={\parallel}_t h_t:h\in H^1([0,T];T_{x_0}M),\ h_0=0\}.
```


Use its damped inner product

```math
\langle v,w\rangle_{\mathcal H_\sigma}
=\int_0^T\left\langle\frac{D v_t}{dt}+\frac12\mathrm{Ric}^{\#}_{\sigma(t)}v_t,
\frac{D w_t}{dt}+\frac12\mathrm{Ric}^{\#}_{\sigma(t)}w_t\right\rangle\,dt.
```


Let $`\mathrm{Cyl}`$ consist of real smooth cylindrical functions $`F(\sigma)=f(\sigma(t_1),\ldots,\sigma(t_k))`$, where $`f\in C^\infty(M^k)`$. Restrict the ordinary differential of $`F`$ to $`\mathcal H_\sigma`$. Its closure gives $`d:D^{2,1}\subset L^2(\mu)\to L^2\Gamma\mathcal H^*`$. Write $`d^*`$ for the Hilbert-space adjoint, and put $`L_0F=-d^*dF`$ on $`\mathrm{Cyl}`$.

**Question.** For every such $`M,x_0,T`$, is there exactly one symmetric, strongly continuous sub-Markov contraction semigroup on $`L^2(\mu)`$ whose generator extends $`L_0`$? Here sub-Markov means that $`0\le f\le1`$ implies $`0\le P_tf\le1`$.

## Application

This asks whether the natural cylindrical diffusion operator determines a unique symmetric Markov evolution on Brownian path space. It tests a basic analytic foundation of stochastic calculus on curved manifolds.

## References

1. K. D. Elworthy and Xue-Mei Li, [*Geometric stochastic analysis on path spaces*](https://arxiv.org/abs/1911.09764v1), Sections 2.1–2.2, especially physical pp. 11–13 of the inspected 22-page preprint. Related ICM 2006 chapter, vol. III, pp. 575–594, [DOI](https://doi.org/10.4171/022-3/30); final-edition body parity remains pending.
2. K. D. Elworthy and Xue-Mei Li, [*Itô maps and analysis on path spaces*](https://www.xuemei.org/Ito-map.pdf), *Mathematische Zeitschrift* **257** (2007), 643–706, [DOI](https://doi.org/10.1007/s00209-007-0145-0), Sections 2.2–2.3 and Theorem 6.9, printed p. 679. The final theorem specifies precisely the operator and extension class used here.
3. K. D. Elworthy and Xue-Mei Li, [*Intertwining and the Markov uniqueness problem on path spaces*](https://arxiv.org/abs/1911.10969v1), Problems 1–3 and the correction of an earlier claimed proof; related 2006 chapter in *Stochastic Partial Differential Equations and Applications—VII*, pp. 89–95.
4. K. D. Elworthy and Y. Yang, [*The vanishing of L2 harmonic one-forms on based path spaces*](https://arxiv.org/html/1204.0120v2), particularly Lemma 3.5 and its intrinsic-filtration hypothesis; selected comparison only.

## Status review


**Known cases:** The precise symmetric sub-Markov extension class and damped Bismut operator are retained. The authors corrected an earlier uniqueness claim, and subsequent weak derivative identities with intrinsic-filtration premises do not settle the general question.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The precise symmetric sub-Markov extension class and damped Bismut operator are retained. The authors corrected an earlier uniqueness claim, and subsequent weak derivative identities with intrinsic-filtration premises do not settle the general question.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The exact question is equivalent, by reference [2], Theorem 6.9, to equality of the weak and minimal cylindrical Sobolev domains. The compact Levi–Civita setting supplies that theorem's additional condition. Existence of one closed Dirichlet form does not prove uniqueness of its Markov extensions. This question concerns Markov uniqueness, with the damped metric above; essential self-adjointness is stronger.

Regularity of conditional expectation of arbitrary driving-Wiener Sobolev functions onto the full Itô-map sigma algebra would imply the desired equality. Reference [3] corrects an earlier claimed proof of that stronger regularity statement. Finite-chaos results and the later intrinsic-time projection lemma in [4] do not give that full projection statement.

Results for different Gibbs measures, polymer measures, loop measures or stochastic-heat forms with L2 tangent directions do not, by their inspected statements, establish uniqueness for this H1 Bismut operator. The recorded bounded current searches found no matching complete resolution or announcement. They are not a proof that none exists.

The [source review](../FURTHER_problems/_tracking/parallel/rough-filtering/path-space-markov-uniqueness-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/continuum/cross-path-space-markov-uniqueness-review.json), [current comparisons](../FURTHER_problems/_tracking/path-space-markov-current-comparisons-2026-10-19.json), [semantic comparisons](../FURTHER_problems/_tracking/path-space-markov-duplicates-review-2026-10-19.json), [catalogue review](../FURTHER_problems/_tracking/path-space-markov-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/path-space-markov-coordinator-review-2026-10-19.json) record the evidence and limits. These are AI checks, not human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-faa29cb4dcef7e56**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
