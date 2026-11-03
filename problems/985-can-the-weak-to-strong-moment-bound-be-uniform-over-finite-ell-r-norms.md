# 985. Can the weak-to-strong moment bound be uniform over finite $`\ell_r`$ norms?

**Area:** Probability, asymptotic convex geometry and log-concave measures
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`F`$ be a finite-dimensional normed space that embeds linearly and isometrically into $`\ell_r`$ for some $`1\le r<\infty`$, and let $`X`$ be an $`F`$-valued log-concave random vector. For $`p\ge1`$, set

```math
\sigma_p(X;F)=\sup_{\varphi\in F^*,\,\|\varphi\|_*\le1}
                 \bigl(\mathbb E|\varphi(X)|^p\bigr)^{1/p}.
```


**Does there exist one absolute constant $`C`$, independent of $`r`$, $`F`$, $`p`$ and $`X`$, such that**

```math
\bigl(\mathbb E\|X\|^p\bigr)^{1/p}
\le C\bigl(\mathbb E\|X\|+\sigma_p(X;F)\bigr)?
```


The question is stated in the Geometric Tomography report of the 2020 BIRS proceedings [1, printed p. 29]. It asks whether the known coefficient proportional to $`r`$ can be replaced by an absolute one. It does not assume that $`X`$ is centered or isotropic.

## Application

An absolute constant would control strong moments, and hence norm tails, of log-concave vectors from their mean norm and the moments of linear observations uniformly across these spaces. It would remove the loss as $`r`$ grows.

## Known results and scope

Latała and Strzelecka proved the displayed inequality with a coefficient $`C_2r`$ for every finite $`r`$ [2, Theorem 2]. Their Conjecture 1 asks for an absolute coefficient for every finite-dimensional norm. In fact, the uniform finite-$`r`$ question would imply that general conjecture: approximate any finite-dimensional norm by a finite maximum of dual functionals, then by their $`\ell_r`$ norm and let $`r\to\infty`$. This equivalence is a direct approximation observation, not a claim made in [1].

Hmadi and Liakopoulos [3, pp. 3–4] still describe the all-norm comparison as open. Their 2026 estimate improves the dimension dependence but retains a dimension-dependent coefficient. The adjacent question in [1] about making the Euclidean first-moment coefficient exactly one is a different target.

## References

1. Banff International Research Station, [*2020 Proceedings*](https://www.birs.ca/files/publications/proceedings/birs_2020_proceedings.pdf), Geometric Tomography (20w5037), report of Rafał Latała's presentation, printed p. 29 (PDF p. 33).
2. R. Latała and M. Strzelecka, [*Weak and strong moments of $`\ell_r`$-norms of log-concave vectors*](https://arxiv.org/pdf/1501.01649v2), *Proceedings of the American Mathematical Society* **144** (2016), no. 8, 3597–3608, Conjecture 1 and Theorem 2. [DOI](https://doi.org/10.1090/proc/13003).
3. A. Hmadi and D.-M. Liakopoulos, [*Moment comparisons, Sudakov inequalities and entropy of centroid bodies*](https://arxiv.org/pdf/2608.10853v1), arXiv:2608.10853v1 (2026), pp. 3–4 and Theorem 1.3.

## Status review


**Known cases:** The constant must be independent of r as well as dimension and moment. The August 2026 bounds and established r-dependent theorem do not give the requested absolute constant.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The constant must be independent of r as well as dimension and moment. The August 2026 bounds and established r-dependent theorem do not give the requested absolute constant.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [independent bounded source audit](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/latala-strong-weak-moments-native33-bounded-audit-20261023.json) and [coordinator check](../FURTHER_problems/_tracking/birs-uniform-logconcave-moments-coordinator-audit-2026-10-23.json) record the exact proceedings wording, its proven $`r`$-dependent predecessor, later partial bound, status and duplicate searches. The searches do not certify that every later result has been found. The proceedings receipt covers one bounded page passage, not the whole volume.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ae598b3340e45dac**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
