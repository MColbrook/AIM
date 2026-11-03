# 667. Does Cameron–Martin coercivity ensure a strong posterior mode?

**Area:** Bayesian inverse problems and infinite-dimensional probability
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a real separable Banach space, let $`\mu_0`$ be a centred nondegenerate Gaussian Borel probability measure on $`X`$, and let $`(E,\|\cdot\|_E)`$ be its Cameron–Martin Hilbert space. Let $`\Phi:X\to\mathbb R`$ be continuous. Assume separately that

```math
0<Z:=\int_X e^{-\Phi(x)}\,\mu_0(dx)<\infty,
\qquad \mu(dx):=Z^{-1}e^{-\Phi(x)}\mu_0(dx).
```

For $`h\in E`$, define the posterior Onsager–Machlup functional

```math
I(h):=\Phi(h)+\frac12\|h\|_E^2.
```

Suppose there are constants $`A\in\mathbb R`$ and $`c>0`$ such that

```math
A+I(h)\ge c\|h\|_E^2\qquad\text{for every }h\in E.
```

Must $`\mu`$ have a **strong mode**? Explicitly, with closed balls in the given $`X`$ norm,

```math
B_r(x):=\{z\in X:\|z-x\|_X\le r\},
\qquad M_r:=\sup_{x\in X}\mu(B_r(x)),
```

must there exist $`x_*\in X`$ for which

```math
\lim_{r\downarrow0}\frac{\mu(B_r(x_*))}{M_r}=1?
```

This is the question immediately preceding Proposition 4.1 of [1]. Retain the uniform positive quadratic margin $`c`$ in its coercivity assumption. No global lower bound or uniform continuity of $`\Phi`$ is imposed.

## Application

Function-valued Bayesian inverse problems often estimate an unknown by minimizing a penalized likelihood. The question asks whether energy coercivity suffices to connect that variational estimate with asymptotically maximal posterior probability of small uncertainty balls.

## References

1. H. Lambley, [*Strong maximum a posteriori estimation in Banach spaces with Gaussian priors*](https://doi.org/10.1088/1361-6420/ad07a4), **Inverse Problems 39** (2023), 125010. [Latest author version, arXiv:2304.13622v3](https://arxiv.org/html/2304.13622v3), Definition 2.1, Lemma 2.2 and §4.1, especially the question before Proposition 4.1. The author PDF places the question on printed p.11; the published PDF places it on p.13.
2. I. Klebanov, H. Lambley and T. J. Sullivan, [*Classification of small-ball modes and maximum a posteriori estimators in metric spaces*](https://arxiv.org/abs/2306.16278v4), revised 14 August 2025. [PDF](https://arxiv.org/pdf/2306.16278v4), §5.4, Theorem 5.10, Examples 6.11–6.12 and Remark 6.13(a), printed pp.27–31 and 42–46.

## Status review


**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The uniform positive Cameron-Martin quadratic margin is retained. The current v4 small-ball classification has the previously checked counterexamples, whose Onsager-Machlup functions fail this coercivity. Weak modes and strong modes under the stronger ambient lower bound do not settle the proposed general strong-mode conclusion. Fresh author, primary-record and indexed announcement searches found no matching complete result.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2304.13622); [comparison source 2](https://arxiv.org/abs/2306.16278); [comparison source 3](https://wrap.warwick.ac.uk/id/eprint/180555/7/WRAP-Strong-maximum-posteriori-estimation-Banach-spaces-23.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known cases:** [1, Theorem 1.1] obtains strong modes under the stronger condition that, for every $`\eta>0`$, some $`K(\eta)`$ satisfies $`\Phi(x)\ge K(\eta)-\eta\|x\|_X^2`$ for all $`x\in X`$. Proposition 4.1 establishes weak modes under the assumptions above. A weak mode compares its small-ball mass with each fixed centre separately; the strong-mode definition compares with the supremum over all centres at each radius. Lemma 2.2 says that if one strong mode exists, every weak mode is strong.

**Later counterexamples:** The continuous Gaussian reweightings in [2, Examples 6.11–6.12] distinguish weak and strong modes. Remark 6.13(a) explicitly says their Onsager–Machlup functionals fail the displayed coercivity condition, so those counterexamples do not resolve this question.

Targeted searches through 16 October 2026 and comparison with the imported OpenAI announcement overview located no matching complete resolution. The closest retained AIM entry, 660, concerns exact small-ball ratios for non-Gaussian product priors and is a different target. The complete Prove2Me listing snapshot was compared using named aliases and relevant posterior contexts; no equivalent target was located. The simultaneous FURTHER candidates are distinct. The dated search record is evidence of a bounded review, not proof that no solution exists.

The [review packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/gaussian-posterior-coercivity-review.json) and [catalogue comparison](../FURTHER_problems/_tracking/prove2me-catalogue-review.json) record reading extents and limitations.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b6812e2054a22dd3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
