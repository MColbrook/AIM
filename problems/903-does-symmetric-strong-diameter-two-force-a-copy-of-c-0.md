# 903. Does symmetric strong diameter two force a copy of $`c_0`$?

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a nonzero real Banach space with its given norm and closed unit ball $`B_X`$. For $`x^*\in X^*`$ with $`\|x^*\|=1`$ and $`\alpha>0`$, write
```math
S(x^*,\alpha)=\{x\in B_X:x^*(x)>1-\alpha\}.
```

Assume that $`X`$ has the **symmetric strong diameter two property**: for every finite family of slices $`S_1,\ldots,S_m`$ and every $`\varepsilon>0`$, there are $`x_i\in S_i`$ and a single $`y\in B_X`$ such that
```math
\|y\|>1-\varepsilon,\qquad x_i+y\in S_i,\quad x_i-y\in S_i\quad(1\le i\le m).
```


Must $`X`$ contain a closed linear subspace isomorphic to real $`c_0`$, the space of real null sequences with the supremum norm? Equivalently, must there exist a bounded linear map $`J:c_0\to X`$ and constants $`0<a\le b<\infty`$ satisfying
```math
a\|z\|_\infty\le\|Jz\|_X\le b\|z\|_\infty\qquad(z\in c_0)?
```

Neither an isometric nor a complemented copy is required. There are no separability, lattice or dual-space assumptions. The premise uses all norm-dual slices, rather than only weak-star slices or a stronger sequential/transfinite variant.

## Application

The question links the geometry of the unit ball, expressed by a common direction in finitely many slices, to a concrete infinite-dimensional linear subspace. It would clarify which structural consequences follow from this diameter property without changing the given norm.

## References

1. R. Haller, J. Langemets, V. Lima and R. Nadel, *Symmetric strong diameter two property*, Mediterranean Journal of Mathematics **16** (2019). [DOI](https://doi.org/10.1007/s00009-019-1306-1); [primary preprint](https://arxiv.org/abs/1804.01705). Definition 1.1 and Question 6.1.
2. S. Ciaci, *Transfinite geometric properties of the unit ball in Banach spaces*, University of Tartu dissertation (2024), Section 3.4, Problem 3.1, p. 58. [University primary text](https://dspace.ut.ee/server/api/core/bitstreams/97f34bef-7753-42db-83f4-0fcc87b29ff1/content). It explicitly retains the ordinary finite-slice question.

## Status review


**Known cases:** Almost-square spaces satisfy a stronger property, while the converse renorming theorem starts with an existing c0 copy. Weak-star or local diameter-two properties do not supply ordinary all-slice symmetric strong diameter two. The c0-absorbing OpenAI example does not assert this premise for its given norm.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Almost-square spaces satisfy a stronger property, while the converse renorming theorem starts with an existing c0 copy. Weak-star or local diameter-two properties do not supply ordinary all-slice symmetric strong diameter two. The c0-absorbing OpenAI example does not assert this premise for its given norm.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 30 October 2026. The original definition and question, the 2024 thesis question, and relevant 2024 and 2026 primary comparison statements were read. Almost-square spaces form a stronger known class. The converse renorming result starting with a copy of $`c_0`$ does not prove the implication asked here. Results about weak-star slices or the local diameter two property do not supply this premise.

Bounded current searches found no matching proof, counterexample or complete announcement. Semantic checks against AIM, current saved OpenAI announcements and private findings found no equivalent target. In particular, the announcement of a space without linear $`c_0`$ that absorbs $`c_0`$ bi-Lipschitz does not assert the required slice property for its given norm. These checks are not a proof of openness; no complete proof audit or published-body parity is claimed.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4f4f1df6c82d9c76**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
