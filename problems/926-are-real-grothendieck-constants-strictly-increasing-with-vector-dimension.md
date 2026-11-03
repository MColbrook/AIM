# 926. Are real Grothendieck constants strictly increasing with vector dimension?

**Area:** Operator inequalities and continuous optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a nonzero real matrix $`A=(a_{ij})`$ of arbitrary finite size $`m`$ by $`n`$ and an integer $`d\ge1`$, define

```math
V_d(A)=\max_{u_i,v_j\in S^{d-1}}
 \left|\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}\langle u_i,v_j\rangle\right|,
\qquad
K_G^{\mathbb R}(d)=
\sup_{\substack{m,n\ge1\\0\ne A\in\mathbb R^{m\times n}}}
\frac{V_d(A)}{V_1(A)}.
```

Here $`S^{d-1}`$ is the unit sphere in $`\mathbb R^d`$. In particular, $`V_1`$ is the maximum over two sign vectors. The size of $`A`$ is unrestricted; $`d`$ bounds the dimension of the vectors. Square matrices give the same definition by padding with zero rows or columns.

Is

```math
K_G^{\mathbb R}(d+1)>K_G^{\mathbb R}(d)
\qquad\hbox{for every integer }d\ge1?
```

The weak inequality follows by embedding $`\mathbb R^d`$ in $`\mathbb R^{d+1}`$. The question concerns strictness throughout the hierarchy, rather than the value of the universal limit.

## Application

These constants quantify the worst loss in replacing vector-valued bilinear optimization by optimization over signs. Their dimension dependence also describes limitations of finite-dimensional correlation models.

## References

- J. Briët, H. Buhrman and B. Toner, *A generalized Grothendieck inequality and entanglement in XOR games*, [arXiv:0901.2009v1](https://arxiv.org/abs/0901.2009v1), 14 January 2009. Definition 1 on p. 1 fixes the vector-dimensional constant; the paragraph following Theorem 3 on p. 2 explicitly leaves its strict increase open.
- S. Designolle, T. Vértesi and S. Pokutta, *Better bounds on finite-order Grothendieck constants*, [arXiv:2409.03739v4](https://arxiv.org/abs/2409.03739v4), revised 5 October 2026; published as *Better bounds on finite-order Grothendieck constants with applications to Bell nonlocality*, [Physical Review A 113, 022401 (2026)](https://doi.org/10.1103/m5mn-c5dx). Section II, Eq. (5), distinguishes ordinary and generalized constants; Sections III–V give bounds.
- B. Bagchi and G. Misra, *On Grothendieck constants*, [author-hosted primary text](https://www.isibang.ac.in/~gm/gmhomefiles/papers/kgc2.pdf), 26 April 2008, p. 1. Its fixed-matrix-size constants are a different sequence; their failure of strict monotonicity does not answer the question above.

## Status review


**Known cases:** The dimension is vector order with unrestricted matrix size. Fixed matrix-size equalities and dimension-witness ratios are different quantities. The October 2026 finite-order estimates do not establish strictness at every adjacent order.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The dimension is vector order with unrestricted matrix size. Fixed matrix-size equalities and dimension-witness ratios are different quantities. The October 2026 finite-order estimates do not establish strictness at every adjacent order.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper proves nontrivial generalized ratios $`K_G(n\mapsto m)>1`$ and binary-outcome dimension witnesses, while explicitly separating those results from this question. A strict improvement $`V_{d+1}(A)>V_d(A)`$ for some matrix does not itself compare the two worst-case suprema relative to $`V_1`$. Recent finite-order bounds and announcements of improvements to the universal real constant did not supply a resolution of the whole hierarchy in the searches performed.

AIM 027 asks for the exact universal limit $`K_G`$; that related problem does not state the adjacent strictness question. The all-status findings, saved pages and current public catalogue comparison located no matching formulation. This is a bounded literature check, not a certification that no solution exists or human peer review.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c4e00fc43141e067**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
