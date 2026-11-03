# 905. Does Lipschitz affine approximation determine the exact martingale cotype?

**Area:** Banach space geometry and quantitative differentiation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a real Banach space $`(Y,\|\cdot\|_Y)`$ and an exponent $`2\leq q<\infty`$. Suppose that there exist a positive integer $`n`$, an $`n`$-dimensional real normed space $`(X,\|\cdot\|_X)`$, and a finite constant $`C`$ with the following property.

Let $`B_X=\{x:\|x\|_X\leq1\}`$, use Lebesgue measure in fixed linear coordinates on $`X`$, and write $`\mathcal A(X,Y)`$ for the affine maps $`\Lambda(x)=Tx+b`$, with $`T:X\to Y`$ linear and $`b\in Y`$. Every compactly supported map $`f:X\to Y`$ satisfying $`\|f(x)-f(y)\|_Y\leq\|x-y\|_X`$ obeys
```math
\int_X\int_0^\infty
\inf_{\Lambda\in\mathcal A(X,Y)}
\left(\frac{1}{|tB_X|}\int_{x+tB_X}
\|f(y)-\Lambda(y)\|_Y^q\,dy\right)
\frac{dt}{t^{q+1}}\,dx
\leq C\,|\mathrm{supp}f|.
```

Here $`|E|`$ denotes Lebesgue volume, and $`\mathrm{supp}f`$ is the closure of the set where $`f\ne0`$. There is no bound on the Lipschitz constant of the affine approximants.

Must $`Y`$ have **martingale cotype $`q`$**? Explicitly, must there be a finite constant $`m`$ such that, for every probability space with filtration $`(\mathcal F_k)_{k=1}^N`$ and every finite $`Y`$-valued martingale $`(M_k)_{k=1}^N`$ in $`L^q`$,
```math
\left(\sum_{k=1}^{N-1}\mathbb E\|M_{k+1}-M_k\|_Y^q\right)^{1/q}
\leq m\max_{1\leq k\leq N}
\left(\mathbb E\|M_k\|_Y^q\right)^{1/q}?
```

The martingale condition is $`\mathbb E[M_{k+1}\mid\mathcal F_k]=M_k`$. Equivalently, does $`Y`$ admit an equivalent norm whose modulus of uniform convexity has power type $`q`$? The exponent must remain the same $`q`$; replacing it by $`q+\varepsilon`$ does not answer the question.

## Application

Quantitative differentiation measures how well Lipschitz maps resemble affine maps on balls of different sizes. This question asks whether a precise analytic approximation estimate detects the corresponding power of uniform convexity in the target space. Such estimates are used in quantitative embedding and discretization problems, including the approach to Bourgain's discretization theorem developed in the source.

## Known results and scope

Hytönen–Naor's Theorem 9 proves that the assumed estimate implies superreflexivity, meaning existence of some equivalent uniformly convex norm. Their results also give, for Banach lattice targets, martingale cotype $`q+\varepsilon`$ for every $`\varepsilon>0`$. The question concerns attainment of the exact exponent.

Hytönen–Merikoski characterize martingale cotype $`q`$ by a stronger local approximation estimate controlled by a Sobolev $`W^{1,q}`$ norm. Their Remark 3 explicitly distinguishes the unresolved Hytönen–Naor question: the support-volume bound using a global Lipschitz constant is weaker than that Sobolev bound. Substituting the stronger bound would change the problem.

The current OpenAI announcement that nontrivial Markov type implies superreflexivity is a qualitative renorming statement; superreflexivity already follows here from the source theorem. Ryoo's later real-valued Dorronsoro theorem on Carnot groups and vector-valued heat estimates assuming power-type uniform convexity also have different hypotheses and conclusions.

## References

1. T. Hytönen and A. Naor, *Heat flow and quantitative differentiation*, J. Eur. Math. Soc. 21 (2019), 3415–3466, [DOI](https://doi.org/10.4171/JEMS/906). Eligible source: [arXiv:1608.01915v1](https://arxiv.org/pdf/1608.01915v1), Question 10 and Theorem 9, p. 10; martingale definitions pp. 5–6; Proposition 33 and discussion pp. 30–32. The [author's 2017 version](https://web.math.princeton.edu/~naor/homepage%20files/UAAP-heat-flow.pdf) retains Question 10.
2. T. Hytönen and J. Merikoski, *Vector-Valued Local Approximation Spaces*, J. Fourier Anal. Appl. 25 (2019), 299–320, published online 2018, [DOI](https://doi.org/10.1007/s00041-018-9598-2). [arXiv:1612.09502v3](https://arxiv.org/pdf/1612.09502v3), Theorems 1, 3–4 and Remark 3, pp. 3–5.
3. OpenAI, *Nontrivial Markov Type Forces Superreflexivity* (2026), [preprint](https://github.com/openai/math/blob/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf), Theorem 1.1, p. 1. Included to distinguish its announced qualitative conclusion from the exact exponent requested here.
4. S.-Y. Ryoo, *Quantitative nonembeddability of groups of polynomial growth into uniformly convex spaces*, [arXiv:2207.11305v2](https://arxiv.org/pdf/2207.11305v2) (2025), Theorem 34, p. 22, and Theorems 55–57, p. 38.

## Status review


**Known cases:** The Lipschitz support-volume estimate implies qualitative superreflexivity, while the exact-q martingale characterization uses a stronger Sobolev-controlled approximation inequality. Qualitative Markov-type renorming and Banach-lattice q-plus-epsilon progress do not attain the specified exponent from this weaker hypothesis.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The Lipschitz support-volume estimate implies qualitative superreflexivity, while the exact-q martingale characterization uses a stronger Sobolev-controlled approximation inequality. Qualitative Markov-type renorming and Banach-lattice q-plus-epsilon progress do not attain the specified exponent from this weaker hypothesis.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 2026-10-24 against the original statement and definitions, the later author version, selected current primary theorems, official version histories, author publication listings, targeted Prove2Me searches, and all-status AIM/FURTHER comparisons. No matching full resolution or announcement was located. The review preserves the distinction between exact martingale cotype, weaker qualitative renorming, and the stronger Sobolev hypothesis. It covers selected primary passages and does not certify every cited proof or exhaust the literature.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6403776313aba0f9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
