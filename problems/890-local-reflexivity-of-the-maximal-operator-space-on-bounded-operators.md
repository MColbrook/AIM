# 890. Local reflexivity of the maximal operator space on bounded operators

**Area:** Operator spaces and functional analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`H=\ell_2(\mathbb N;\mathbb C)`$ and let
```math
X=\mathrm{MAX}(\mathcal B(H)).
```

Here $`\mathcal B(H)`$ first has its usual operator norm as a Banach space, and $`\mathrm{MAX}`$ gives it the largest operator-space matrix norms compatible with that norm. Equivalently, every bounded linear map from $`X`$ to any $`\mathcal B(K)`$ is completely bounded with the same norm. These matrix norms generally differ from the usual ones on the $`C^*`$-algebra $`\mathcal B(H)`$.

**Does there exist a finite constant $`\lambda\geq1`$ for which $`X`$ is $`\lambda`$-locally reflexive?** Precisely, for every finite-dimensional subspace $`E\subset X^{**}`$, with its inherited operator-space structure, must there be a net of linear maps $`u_\alpha:E\to X`$ such that
```math
\sup_\alpha\|u_\alpha\|_{\mathrm{cb}}\leq\lambda,
\qquad
j_Xu_\alpha(e)\longrightarrow e
\quad\text{in }\sigma(X^{**},X^*)\quad(e\in E)?
```

Here $`j_X:X\to X^{**}`$ is the canonical embedding and
$`\|u\|_{\mathrm{cb}}=\sup_{r\geq1}\|\mathrm{id}_{M_r}\otimes u\|`$.
The constant is independent of $`E`$; the approximating net may depend on $`E`$. The bidual carries its canonical operator-space structure. No norm-separability assumption on $`X`$ is imposed.

Pisier's Theorem 18.13 makes this a test case for local reflexivity of all maximal operator spaces, with a uniform finite constant. Asking for $`\lambda=1`$ is a stronger version; the question above asks whether any finite constant works.

## Application

Banach-space local reflexivity approximates finite-dimensional pieces of a bidual without controlling all matrix levels at once. This problem asks whether such simultaneous control survives for the maximal operator-space structure. The equivalent lifting properties in the cited sources connect it to bounded liftings through quotient $`C^*`$-algebras.

## References

1. G. Pisier, [*Introduction to Operator Space Theory*](https://bpb-us-e1.wpmucdn.com/sites.northeastern.edu/dist/4/7815/files/2024/07/Pisier.pdf), Cambridge University Press, London Mathematical Society Lecture Note Series **294** (2003). See the question in the Introduction, printed p. 9; the maximal structure in Chapter 3, equations (3.3)-(3.4); Definition 18.1; and Theorem 18.13, especially (ii)-(iii).
2. N. Ozawa, [*On the lifting property for universal $`C^*`$-algebras of operator spaces*](https://jot.theta.ro/jot/archive/2001-046-003/2001-046-003-007.pdf), *Journal of Operator Theory* **46** (2001), 579-591, Proposition 3.1(C2) and its proof. The source attributes the maximal-space conjecture to T. Oikhberg.
3. G. Pisier, [*Seemingly injective von Neumann algebras*, arXiv:2010.13743v4](https://arxiv.org/html/2010.13743v4), 19 December 2021, Section 8, especially Definitions 8.2-8.3 and the discussion following them. This gives the explicit completely bounded approximation convention used above.
4. G. Pisier and J. Roydor, [*Operator space theory from the maximal viewpoint*, arXiv:2610.21929v2](https://arxiv.org/html/2610.21929v2), 17 October 2026, Sections 2 and 4. Its local-reflexivity statements concern maximally bounded maps and impose an additional identification hypothesis.

## Status review


**Known cases:** Pisier-Roydor v2 introduces maximally bounded maps and maximal tensor norms. Its maximal local-reflexivity statements do not prove completely bounded approximations for MAX(B(H)) with a uniform finite constant. Ordinary operator-space local reflexivity and this new mb notion remain distinct.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Pisier-Roydor v2 introduces maximally bounded maps and maximal tensor norms. Its maximal local-reflexivity statements do not prove completely bounded approximations for MAX(B(H)) with a uniform finite constant. Ordinary operator-space local reflexivity and this new mb notion remain distinct.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source question concerns the maximal matrix norms on an underlying Banach space. The 2026 paper's maximal-tensor-product theory uses a different class of maps and does not establish the completely bounded approximation property above. The existing FURTHER problem about local reflexivity implying exactness for an ordinary $`C^*`$-algebra has different hypotheses and conclusion. Searches through the checked date found no matching proof, counterexample or announced solution. The [dated audit](../FURTHER_problems/_tracking/MAX-local-reflexivity-independent-peer-2026-10-23.json) records the independent statement comparison, exact constant convention, current searches and access limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-03f54527a60e84c3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
