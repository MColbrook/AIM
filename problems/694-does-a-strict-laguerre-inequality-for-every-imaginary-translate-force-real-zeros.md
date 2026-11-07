# 694. Does a strict Laguerre inequality for every imaginary translate force real zeros?

**Area:** Entire functions and zero distribution
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-07

## Problem statement

Let $`f`$ be a real entire function in the class $`S(A)`$ of Csordas and Escassut for some finite $`A\geq0`$. Thus $`f`$ has their genus-at-most-one canonical-product form, possibly multiplied by $`e^{-az^2+bz}`$ with $`a\geq0`$ and $`b\in\mathbb R`$, and all its zeros lie in the horizontal strip $`|\mathrm{Im}z|\leq A`$. For real $`\mu`$, put

```math
f_\mu(x)=f(x+i\mu)+f(x-i\mu),\qquad
L[g]\,(x)=(g'(x))^2-g(x)g''(x).
```


If $`L[f_\mu]\,(x)>0`$ for **every** real $`x`$ and **every nonzero** real $`\mu`$, must all zeros of $`f`$ be real, equivalently must $`f`$ belong to the Laguerre–Pólya class? This is Conjecture 3.5 of the source. The precise canonical-product and convergence assumptions are those of its Definition 1.1; the horizontal-strip condition alone is not the complete definition of $`S(A)`$.

## Application

The question asks whether a family of ordinary differential inequalities on imaginary translates can detect the nonreal zeros of a real entire function. A positive result would turn a necessary real-zero test into a characterization for this class.

## References

- G. Csordas and A. Escassut, [*The Laguerre inequality and the distribution of zeros of entire functions*](https://www.numdam.org/item/10.5802/ambp.210.pdf), *Annales Mathématiques Blaise Pascal* **12** (2005), 331–345, Definitions 1.1–1.2, Conjecture 3.5, Remark 3.6, Theorem 5.1 and Proposition 5.4. [DOI](https://doi.org/10.5802/ambp.210).
- G. Csordas and A. Vishnyakova, [*The generalized Laguerre inequalities and functions in the Laguerre–Pólya class*](https://doi.org/10.2478/s11533-013-0269-x), *Central European Journal of Mathematics* **11** (2013), 1643–1650, Theorems 2.3 and 3.2. Those criteria use all-order real or complex inequalities rather than just the inequality above.
- D. A. Cardon, [*Extended Laguerre inequalities and a criterion for real zeros*](https://arxiv.org/abs/0911.1122), Theorem 2.1. Its shifted-product criterion requires a family of coefficient inequalities.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/694-does-a-strict-laguerre-inequality-for-every-imaginary/main.pdf). The strict translated Laguerre criterion is proved when the Gaussian coefficient is positive.

**Known cases:** The strict translated Laguerre criterion is proved when the Gaussian coefficient is positive.

**Remaining target:** The case of Gaussian coefficient zero remains unresolved here.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/694-review.md) checks the complete argument against this exact target and records the primary-source comparisons. The verified restricted results do not resolve the remaining target, so this entry remains partially resolved. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



**Previously recorded known cases:** The strict ordinary Laguerre inequality for every nonzero shift is essential. Known results with finitely many nonreal zeros, extra real-zero density, or all higher Laguerre inequalities impose additional conditions. No matching general resolution of Conjecture 3.5 was located.

**Previously recorded remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The strict ordinary Laguerre inequality for every nonzero shift is essential. Known results with finitely many nonreal zeros, extra real-zero density, or all higher Laguerre inequalities impose additional conditions. No matching general resolution of Conjecture 3.5 was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the conclusion for functions with only finitely many nonreal zeros and for some classes with sufficiently dense real zeros. Its Proposition 5.4 adds an inequality for the imaginary part of $`f(x+i\mu)`$; the conjecture assumes only the inequality for the real part. Later all-order and complex Laguerre criteria therefore do not directly settle this precise implication. Bounded searches through 22 October 2026 found no matching complete proof, counterexample or announcement. This negative search is not exhaustive.

The [source-bound body receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal-primary-body-second-pass-0683-J322-remote-pdf-body-review.json), [later-scope audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/journal0688-ambp210-conjecture35-bounded-scope-status-review.json), [independent current review](../FURTHER_problems/_tracking/csordas-escassut-cosine-laguerre-2026-10-22-status.json) and [duplicate review](../FURTHER_problems/_tracking/csordas-escassut-cosine-laguerre-2026-10-22-duplicates.json) record what was checked and its limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6eeb9e3bb6903144**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
