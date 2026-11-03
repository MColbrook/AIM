# 891. Exponential coordinate complexity for finite-cotype normed spaces

**Area:** Banach-space geometry and norm approximation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`2\leq q<\infty`$, $`B\geq1`$, and $`D>1`$. For a finite-dimensional real normed space $`E`$, let $`C_q(E)`$ be the least constant in the Rademacher cotype inequality
```math
\left(\sum_{i=1}^{m}\|x_i\|_E^q\right)^{1/q}
 \leq C_q(E)
 \left(\mathbb E_\varepsilon
 \left\|\sum_{i=1}^{m}\varepsilon_i x_i\right\|_E^2\right)^{1/2}
 \quad(m\geq1,\ x_1,\ldots,x_m\in E),
```

where the signs $`\varepsilon_i`$ are independent and uniform on $`\{-1,1\}`$.

Write $`k_E(D)`$ for the least positive integer $`k`$ for which there are real linear functionals $`f_1,\ldots,f_k\in E^*`$ satisfying
```math
\max_{1\leq j\leq k}|f_j(x)|
 \leq\|x\|_E
 \leq D\max_{1\leq j\leq k}|f_j(x)|
 \qquad(x\in E).
```

Thus $`k_E(D)`$ is the smallest coordinate dimension of a linear embedding of $`E`$ into $`\ell_\infty^k`$ with distortion at most $`D`$.

Do there exist $`c=c(q,B,D)>0`$ and $`n_0=n_0(q,B,D)`$ such that
```math
\boxed{\quad k_E(D)\geq \exp(cn)\quad}
```

for every integer $`n\geq n_0`$ and every $`n`$-dimensional real normed space $`E`$ with $`C_q(E)\leq B`$?

The constants must be uniform over this class of norms. The dimension threshold permits the unavoidable small-dimensional exceptions. No assumption on the cotype or type constants of $`E^*`$ is imposed.

## Application

The maximum of finitely many linear measurements gives a polyhedral approximation of a norm. This question asks whether a uniform finite-cotype assumption forces exponentially many such measurements when the multiplicative approximation error is fixed. It connects the geometry of high-dimensional norms with the size of linear-inequality representations.

## References

1. G. Pisier, *Quantum expanders and geometry of operator spaces*, Journal of the European Mathematical Society **16** (2014), 1183–1219, introduction, printed pp. 1185–1186. [Publisher](https://doi.org/10.4171/JEMS/458).
2. G. Pisier, *Random matrices and subexponential operator spaces*, Israel Journal of Mathematics **203** (2014), 223–273, §6, opening paragraphs. The exact cited preprint is arXiv:1212.2053v3 (22 June 2013). [Preprint](https://arxiv.org/abs/1212.2053v3); [published article](https://doi.org/10.1007/s11856-014-1069-0).
3. A. Naor, *Metric dimension reduction: A snapshot of the Ribe program*, Proceedings of the International Congress of Mathematicians 2018, Question 6 and the following real-polytope formulation. [arXiv:1809.02376v1](https://arxiv.org/abs/1809.02376v1).
4. G. Schechtman and N. Tomczak-Jaegermann, *Polylog dimensional subspaces of $`\ell_\infty^N`$*, Geometric Aspects of Functional Analysis, Israel Seminar 2017–2019, Volume II, Lecture Notes in Mathematics **2266** (2020), 325–334. Theorem 1 is cited from arXiv:1812.03678v1 (2018). [Preprint](https://arxiv.org/abs/1812.03678v1); [publication](https://doi.org/10.1007/978-3-030-46762-3_15).
5. H. Huang and K. Tikhomirov, *Cotype of random polytopes*, arXiv:2603.04749v1 (2026), Theorems A–B. [Preprint](https://arxiv.org/abs/2603.04749v1).
6. A. Hmadi, *Dimension-free cotype for isotropic log-concave random polytope spaces*, arXiv:2607.10373v1 (2026), Theorems 1.1–1.2. [Preprint](https://arxiv.org/abs/2607.10373v1).

## Status review


**Known cases:** Finite cotype on the space alone is the target. Existing exponential bounds use nontrivial type of the dual; random polytopes with few vertices do not give few facets while preserving the required cotype constant. The OpenAI cotype-cotype and entropy-duality claims have additional premises or different conclusions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Finite cotype on the space alone is the target. Existing exponential bounds use nontrivial type of the dual; random polytopes with few vertices do not give few facets while preserving the required cotype constant. The OpenAI cotype-cotype and entropy-duality claims have additional premises or different conclusions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Pisier's §6 explicitly asks whether the exponential lower bound holds under a uniformly bounded finite-cotype constant. A uniform nontrivial-type assumption on the dual is a known stronger sufficient hypothesis. The entry states the real finite-dimensional question, consistent with the real formulation of Pisier's dichotomy in Naor's Question 6.

Schechtman and Tomczak-Jaegermann obtain growing almost-isometric $`\ell_\infty`$ sections when $`n/(\log N\log\log N)^2`$ tends to infinity. This is partial progress toward the threshold $`n/\log N`$ associated with the exponential bound.

The 2026 random-polytope theorems establish finite cotype for norms whose unit balls are convex hulls of relatively few random vertices. A small $`\ell_\infty`$ embedding instead corresponds to few facets. Those theorems do not supply the required uniform cotype control for the polar norms.

The nearby OpenAI announcements on [cotype–cotype under the approximation property](https://github.com/openai/math/blob/main/lean/docs/326.md) and [metric-entropy duality](https://github.com/openai/math/blob/main/lean/docs/329.md) were compared at the level of their exact announced statements. The former assumes finite cotype of both a space and its dual; the latter constructs a covering-number inequality between convex bodies and their polars. Neither announced statement supplies the requested coordinate bound or a counterexample with the stated uniform cotype hypotheses. Their full proofs were not audited here.

Checks on 24 October 2026 included the cited primary statements, current version records, Pisier dichotomy and finite-cotype embedding aliases, and all-status AIM/OpenAI/FURTHER comparisons. Prove2Me indexed searches found no matching entry; direct requests timed out, so its live contents were not exhaustively checked. This is a bounded literature check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-07353b9d329f1b19**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
