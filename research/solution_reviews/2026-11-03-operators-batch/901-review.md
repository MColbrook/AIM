# AIM 901: mathematical review

**Final status:** Solved. **Reviewed:** 3 November 2026, by Codex (AI), separately from the author.

[Canonical problem](../../../problems/901-finite-dimensional-detection-of-almost-periodic-banach-cocycles.md) · [PDF manuscript](../../solutions/901-almost-periodic-cocycle-quotients/aim901.pdf) · [source and reproduction](../../solutions/901-almost-periodic-cocycle-quotients/README.md).

The audit compares the complete supplied argument with the current target at revision 5d7e26e8444eb98de91988454564e45e011107c4. The original archive's earlier review assertions were not accepted as evidence.

## AIM 901 independent proof review

**Verdict: PASS FULL TARGET.** The supplied proof establishes finite-dimensional quotient detection under all hypotheses of the current canonical statement. In particular, it deals with a quotient of the whole Banach space, unboundedness of the quotient cocycle, and compact-open closure of coboundaries. It does not confuse a finite set of irreducible representation types with a finite-dimensional range.

Review date: 3 November 2026 UTC. Input: the complete original `report/sections/901.tex`, the current canonical problem, and the relevant primary literature. Exact file hashes are recorded in `verdicts.json`. All TeX line locators refer to the original submitted file.

### Hypotheses and the compact acting group

The target allows arbitrary locally compact Hausdorff $`G`$, arbitrary real Banach $`V`$, and a strongly continuous representation whose vector orbits are norm relatively compact. Compact generation, countability, reflexivity, and separability are absent. The proof consistently uses nets where compactness or closure might not be sequential.

At lines 24–40, every orbit is bounded. The uniform boundedness principle on the Banach space $`V`$ therefore gives a single finite $`M=\sup_g\|\pi(g)\|`$, without any assumption on the topology or cardinality of $`G`$. Since inverses are also elements of the same group, they obey the same bound.

The product of all compact vector-orbit closures is compact. Its closure of the representation image consists of linear operators: linearity passes to pointwise norm limits, and the uniform bound passes to the limit as well. The induced topology is precisely the strong operator topology. On this uniformly bounded collection, multiplication is jointly continuous by the displayed estimate. If a net $`\pi(g_\alpha)`$ tends strongly to $`k`$, compactness of the inverses supplies a subnet converging to $`l`$; joint continuity gives both $`kl=I`$ and $`lk=I`$. Thus the strong closure is a group, not just a compact semigroup of possibly noninvertible contractions. Inversion is continuous: on a compact Hausdorff group with continuous multiplication the inverse graph is closed, or equivalently one can use the same inverse-subnet argument. This proves every assertion about $`K`$ used later.

Integration of the strongly continuous $`K`$-action against a continuous scalar function is legitimate even for nonmetrizable $`K`$ and nonseparable $`V`$. After application to a fixed vector, the integrand has compact norm image in a Banach space; that image is metrizable and separable, and the function is Bochner integrable. The integral has norm at most $`M`$ times the scalar $`L^1`$ norm.

### Isotypic projections and central approximations

The matrix coefficient convention at lines 44–65 is internally correct. For the representation $`\tau`$ itself, Schur orthogonality makes $`E_{ij}^\tau`$ the ordinary matrix unit with row $`i`$, column $`j`$. Consequently the displayed expansion of $`\rho(k)P_\tau`$ has the correct index order. For a general Banach representation the same convolution identities give bounded idempotents, disjoint isotypic ranges, and central $`P_\tau`$.

If $`U`$ is a finite sum of these ranges, the restrictions of the representation belong to the finite-dimensional operator span of the corresponding $`E_{ij}^\tau`$. Their coefficients are continuous in $`k`$. Hence $`k\mapsto\rho(k)|_U`$ is operator-norm continuous, even when $`U`$ itself has infinite Banach multiplicity. This is the crucial distinction at lines 62–65.

The construction of $`R_\alpha`$ at lines 67–80 works for every compact Hausdorff group. Such a group has a neighborhood basis at the identity consisting of conjugation-invariant neighborhoods: compactness makes the inner conjugation action uniformly continuous near the identity. A nonnegative continuous bump can be placed in such a neighborhood and averaged under conjugation; it remains central, supported there, and can be normalized to integral one. Peter–Weyl uniform approximation followed by conjugation averaging produces central trigonometric polynomials, which are finite linear combinations of characters. Their integrated operators are therefore finite linear combinations of the $`P_\tau`$, with conjugate representation types merely relabeled if required by the coefficient convention.

The approximating polynomial need not be nonnegative. Positivity is used for the concentrating bump; the $`L^1`$ approximation error and the bound $`\|R_\alpha\|\le2M`$ control its replacement. Directing neighborhoods and approximation errors together gives strong convergence to the identity. A finite net in any norm-compact subset of $`V`$, together with that uniform operator bound, proves (901.2). None of these operators is asserted to have finite rank. No approximation property of $`V`$ has been inserted.

### Finite-dimensional quotients really separate points

The lemma at lines 89–132 addresses quotients explicitly. For $`\ell\in U^*`$, the family $`\ell\circ\rho(k)|_U`$ spans a finite-dimensional space because the corresponding operators lie in a finite-dimensional span. Its common annihilator $`W_\ell`$ is closed and $`K`$-invariant, and $`U/W_\ell`$ is finite dimensional. If $`u\ne0`$, Hahn–Banach provides a functional with $`\ell(u)\ne0`$, so this family of quotients separates $`u`$. This argument does not rely on $`U^*`$ having almost-periodic orbits in general; only the finite-type restriction is used.

The quotient maps needed in the theorem are maps from $`V`$, rather than merely from $`U`$. If $`P_U`$ is the finite central isotypic projection, then $`qP_U:V\to U/W_\ell`$ is bounded, onto, and equivariant. Its kernel is a closed invariant subspace of $`V`$ of exactly that finite codimension. The quotient norm and any norm on the finite-dimensional image are equivalent. Therefore boundedness of the canonical quotient cocycle implies boundedness of $`qP_Ub`$, and unboundedness in such an image implies the required unboundedness in $`V/\ker(qP_U)`$. The sentence after the lemma correctly implements this extension.

### Exact coboundaries on nontrivial finite types

The Haar average of the representation on a sum of nontrivial types is zero. Operator-norm continuity with finite-dimensional operator span makes that integral an operator-norm limit of finite convex combinations of the $`K`$-operators. Density of $`\pi(G)`$ in $`K`$, in that operator-norm representation, allows those convex combinations to use actual $`g_j\in G`$. Hence one can arrange $`A=\sum_jt_j\pi(g_j)|_U`$ with $`\|A\|<1`$, as at (901.3). The inverse $`(I-A)^{-1}`$ is then bounded by its Neumann series.

For any finite-dimensional quotient $`F`$ under consideration, its linear action has compact closure, inherited from $`K`$. A $`G`$-invariant closed subspace is automatically $`K`$-invariant by strong closure, so this inheritance also holds for any such quotient, not just the explicit separating family. Averaging an inner product over the compact image gives a Euclidean isometric linear action. If (qc(G)) is bounded, the associated affine action has a bounded orbit. The unique Euclidean circumcenter of that orbit is fixed, since the affine action permutes the orbit and preserves distances. Thus $`qc(g)=(I-\pi_F(g))w`$ for every $`g`$.

Applying $`q`$ to the prescribed vector

```math
v=(I-A)^{-1}\sum_jt_jc(g_j)
```

gives $`(I-A_F)qv=(I-A_F)w`$. The quotient norm satisfies $`\|A_F\|\le\|A\|<1`$, so $`qv=w`$. Every separating quotient kills $`c(g)-(I-\pi(g))v`$, which forces this residual vector to vanish. The lemma therefore proves an exact coboundary on $`U`$. It does not try to infer a Banach fixed point from an arbitrary bounded affine orbit in infinite dimension.

### Compact-open closure and the real case

The contrapositive at lines 140–157 assumes boundedness of every finite-dimensional invariant quotient image of $`b`$. The trivial component $`P_0b`$ is a vector-valued homomorphism. Scalar functionals, composed with $`P_0`$, give equivariant quotients onto the scalar field whenever nonzero. Each resulting scalar homomorphism is bounded and hence zero by $`h(g^n)=nh(g)`$. Separating scalar functionals imply $`P_0b=0`$.

For each nontrivial type, the preceding lemma applies to $`P_\tau b`$, because each required quotient extends to $`V`$. Each $`P_\tau b`$ is an exact coboundary. Every finite linear combination $`R_\alpha b`$ is then also a single coboundary; linear combinations of primitives supply its primitive. The primitive norms need not be uniformly bounded and the argument does not assume that they are.

If $`C\subset G`$ is compact, continuity of $`b`$ makes (b(C)) norm compact. Uniform convergence of $`R_\alpha`$ on that set gives uniform convergence of $`R_\alpha b`$ to $`b`$ on $`C`$. This is exactly compact-open closure by a net. In particular, this conclusion is stronger than merely failing to find a nonzero exact cohomology class, and it does not replace closure by sequential closure.

For real $`V`$, a standard Banach complexification has bounded real-part projection. The complexified orbit of (x+iy) lies in the continuous image of the product of the compact orbit closures of $`x`$ and $`y`$; it is still relatively compact. If complex coboundaries approximate the embedded real $`b`$ on compact subsets, real parts of their primitives produce real coboundaries with the same convergence. Thus nonmembership in the real closure survives complexification.

Restrict the complex finite-dimensional quotient map obtained from the complex theorem to $`V`$, and take its finite-dimensional real image. Its kernel is closed and real invariant. The quotient norm dominates the norm of this bounded quotient map up to its operator norm, so an unbounded image of the real cocycle supplies the required unbounded real quotient. Its dimension is positive because its image of $`b`$ is unbounded. This fills the norm comparison implicit in the last sentence of the proof without changing the argument.

### Additional source corollary

The stated theorem actually proves the asserted extension to arbitrary topological groups: all the uses of compactness occur in $`K`$ or in compact sets used for the compact-open topology. No step uses local compactness of $`G`$. The corollary that every locally compact group has $`\mathcal{AP}_{\mathrm{fd}}`$ follows under the source's definition. Combining it with the verified Cornulier–Tessera Proposition 4.3 gives $`\mathcal{WAP}_{\mathrm{ap}}\Leftrightarrow\mathcal{WAP}_{\mathrm{fd}}`$, so the claimed consequences for their Questions 4.5–4.7 are logically correct.

### Primary references and current status check

The [published Cornulier–Tessera text](https://www.numdam.org/item/10.5802/aif.3363.pdf), *Annales de l'Institut Fourier* 70(5) (2020), 1951–2003, gives Definition 4.1 on printed p. 1971, Lemma 4.2 across pp. 1971–1972, Proposition 4.3 and Question 4.5 on p. 1972, and Questions 4.6–4.7 on p. 1973. Question 4.7 has precisely the finite-codimensional quotient and unbounded projected-cocycle target. The [2017 primary HTML](https://arxiv.org/html/1711.05566v1) has the same numbered statements. These sources identify the question and justify the final corollary; they are not being cited as a preexisting proof of the submitted theorem.

A directly accessible background source is [T. Tao, The Peter-Weyl theorem, and non-abelian Fourier analysis on compact groups, 23 January 2011](https://terrytao.wordpress.com/2011/01/23/the-peter-weyl-theorem-and-non-abelian-fourier-analysis-on-compact-groups/). The opening explicitly assumes compact Hausdorff groups without a metrizability restriction. Theorem 1 gives the regular-representation decomposition; Proposition 6 identifies the finite isotypic spaces as matrix-coefficient spaces. Their $`L^2`$ density already gives the $`L^1`$ approximation needed in the proof, since normalized Haar measure satisfies $`\|f\|_1\le\|f\|_2`$. Conjugation averaging is $`L^1`$ contractive and leaves a finite character sum. This reference can be placed after the Peter–Weyl approximation sentence at original TeX lines 72–75.

The canonical newer reference, [Thom, arXiv 2603.22049v1](https://arxiv.org/html/2603.22049v1), Theorem 1, instead concerns finitely generated groups and uniformly bounded $`c_0`$ representations on superreflexive Banach spaces, with a conclusion about sublinear growth. Those assumptions and conclusion do not supply the unrestricted almost-periodic quotient statement here.

Bounded searches on 3 November 2026 for almost-periodic Banach cocycles, finite-dimensional quotient detection, and the Cornulier–Tessera questions did not locate a separate primary full resolution. An author-hosted older Cornulier–Tessera manuscript is not a later resolution. This search makes no claim about an unindexed theorem or priority.

### Required corrections and remaining target

No substantive correction is required. The verified Tao reference above would make the background easier to trace; its omission is not a mathematical gap. No part of the canonical target remains outside the argument's hypotheses or conclusion.
