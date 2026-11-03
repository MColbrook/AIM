# 757. Sharp strain integrability in planar Griffith fracture

**Area:** Fracture mechanics and free-discontinuity problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be bounded and Lipschitz. Fix Lamé coefficients $`\mu>0`$ and $`\lambda+\mu>0`$, and define $`\mathbb C\xi=\lambda\mathrm{tr}(\xi)I+2\mu\xi`$ for symmetric matrices. For a displacement $`u`$ and crack $`K`$, set

```math
e(u)=\tfrac12(Du+Du^T),\qquad
G(u,K;B)=\int_{B\setminus K}\mathbb Ce(u):e(u)\,dx
+\mathcal H^1(K\cap B).
```

Assume $`K\subset\Omega`$ is relatively closed and coral: $`\mathcal H^1(K\cap B(x,r))>0`$ whenever $`x\in K`$ and $`r>0`$. Let $`u\in W^{1,2}_{\mathrm{loc}}(\Omega\setminus K;\mathbb R^2)`$, with locally finite $`G`$.

The pair is a *local minimizer* if, for every ball $`B\Subset\Omega`$,
$`G(u,K;B)\leq G(v,L;B)`$ for every relatively closed $`L\subset\Omega`$ and $`v\in W^{1,2}_{\mathrm{loc}}(\Omega\setminus L;\mathbb R^2)`$ satisfying

```math
L\setminus B=K\setminus B,\qquad
v=u\ \text{a.e. on }\Omega\setminus(K\cup B).
```

Must every such pair satisfy $`e(u)\in L^{4,\infty}_{\mathrm{loc}}(\Omega)`$? Explicitly, for every open $`U\Subset\Omega`$, is

```math
\sup_{s>0}s^4\mathcal L^2\{x\in U\setminus K:|e(u)(x)|>s\}<\infty?
```

The matrix norm is Frobenius. This is the isotropic subclass of the endpoint question in [2]. Crack connectedness and restrictions preserving crack topology are not imposed.

## Application

Griffith's energy balances stored elastic energy against crack length. This question measures how strongly strain can concentrate near a freely formed crack. Since the linear stress is $`\mathbb Ce(u)`$, the same exponent controls stress for fixed material coefficients.

## References

1. C. Labourie and A. Lemenant, [*Regularity improvement for the minimizers of the two-dimensional Griffith energy*](https://arxiv.org/abs/2111.13081v2), [DOI](https://doi.org/10.4171/rlm/1009), §1, final paragraph. Earlier discovery source for the sharp subcritical $`p<4`$ question; first arXiv submission in November 2021.
2. M. Friedrich, C. Labourie and K. Stinson, [*Hausdorff dimension of the singular set for Griffith almost-minimizers in the plane*](https://arxiv.org/abs/2510.08670v1), *Transactions of the American Mathematical Society* **379** (2026), 7789–7818, [DOI](https://doi.org/10.1090/tran/9776). The endpoint is explicit in §1; §2.1 defines competitors and minimizers, and Theorem 2.1(ii) proves some $`p>2`$.
3. C. Labourie, L. Lamberti and A. Lemenant, [*Good access to the crack and integrability of the full gradient for Griffith almost-minimizers in the plane*](https://arxiv.org/abs/2607.19229v1), preprint (2026), Theorems 1.2–1.3 and Corollary 1.4.

## Status review


**Known cases:** The weak-fourth-power strain endpoint concerns isotropic vectorial Griffith minimizers without connected-crack restrictions. The scalar planar Mumford-Shah announcement, some p-greater-than-two integrability and full-gradient L2 estimates do not give it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The weak-fourth-power strain endpoint concerns isotropic vectorial Griffith minimizers without connected-crack restrictions. The scalar planar Mumford-Shah announcement, some p-greater-than-two integrability and full-gradient L2 estimates do not give it.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2111.13081v2); [comparison source 2](https://doi.org/10.4171/rlm/1009); [comparison source 3](https://arxiv.org/abs/2510.08670v1); [comparison source 4](https://doi.org/10.1090/tran/9776); [comparison source 5](https://arxiv.org/abs/2607.19229v1); [comparison source 6](https://github.com/openai/math/blob/main/preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Remaining endpoint:** Known higher integrability gives some $`p>2`$ [2]. The subsequent full-gradient $`L^2`$, finite-trace and geometric results [3] do not yield the stated weak-$`L^4`$ bound. Weak $`L^4`$ implies local $`L^p`$ for every $`p<4`$; these are recorded as one problem family.

**Announcement comparison:** OpenAI's [scalar planar Mumford–Shah announcement](https://github.com/openai/math/blob/main/preprints/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026/Interior-regularity-of-planar-Mumford-Shah-minimizers-September-24-2026.pdf) concerns a different energy. A scalar full-gradient result does not automatically settle vector displacement with symmetric-gradient energy. Source [2] explicitly discusses this distinction.

The [review packet](../FURTHER_problems/_tracking/parallel/continuum/griffith-endpoint-review.json) records source extents, current searches, author updates, all-status AIM duplicate comparisons and the completed Prove2Me listing cross-check. No matching resolution or duplicate was found as of the check date. The individual cited proofs and all Prove2Me proof projects have not been exhaustively audited.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8b60393423ca150f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
