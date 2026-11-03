# 586. Freeness of real hyperplane arrangements from their intersection lattice

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`d\geq1`$, let $`\mathcal A`$ be a finite set of distinct linear hyperplanes through the origin in $`\mathbb R^d`$. Its intersection lattice is
```math
L(\mathcal A)=\left\{\bigcap_{H\in\mathcal B}H:
                 \mathcal B\subseteq\mathcal A\right\},
```
ordered by reverse inclusion; the empty intersection is $`\mathbb R^d`$.

Put $`S=\mathbb R[x_1,\ldots,x_d]`$. For each $`H\in\mathcal A`$, choose a nonzero linear form $`\alpha_H`$ with $`H=\ker\alpha_H`$, and define the $`S`$-module
```math
D(\mathcal A)=
\left\{(p_1,\ldots,p_d)\in S^d:
    \sum_{j=1}^d p_j\,\frac{\partial\alpha_H}{\partial x_j}
         \in\alpha_H S \quad\text{for every }H\in\mathcal A\right\}.
```
These are the polynomial vector fields tangent to every hyperplane. The definition is independent of the nonzero scalar choices of $`\alpha_H`$. Call $`\mathcal A`$ **free** when $`D(\mathcal A)`$ is a free $`S`$-module.

For every $`d`$ and every pair $`\mathcal A,\mathcal A'`$ of such real arrangements, does
```math
L(\mathcal A)\cong L(\mathcal A')
\quad\text{and}\quad
D(\mathcal A)\text{ free}
\quad\Longrightarrow\quad
D(\mathcal A')\text{ free}
```
hold?

The isomorphism is an abstract lattice isomorphism. There is no bound on the number of hyperplanes and no supersolvability or generic-position assumption. Both arrangements are over the same fixed field $`\mathbb R`$. This is the real-arrangement form of Terao's freeness conjecture, stated explicitly in [1, Exercise 3.118(d)].

## Application

Freeness describes whether all polynomial vector fields tangent to the arrangement admit a polynomial basis. The question asks whether this algebraic property can be read from incidence data alone, without the continuous geometric parameters specifying a realization.

## References

1. R. P. Stanley, *Enumerative Combinatorics*, Volume 1, second-edition author draft, version of 15 July 2011, Section 3.11 and Exercise 3.118(a),(d), native PDF pages 321–322 and 433–434; commentary on native page 500. [Author PDF](https://math.mit.edu/~rstan/ec/ec1.pdf). The locators refer to this exact author draft.
2. C. Anghel and R. Stan, *Terao's freeness conjecture for arrangements of 15 and 16 lines*, arXiv:2610.25868v1, 19 October 2026, Conjecture 1.1, Main Theorem and Corollary 1.2. [Preprint](https://arxiv.org/abs/2610.25868v1).
3. A. Dimca and P. Pokora, *A nine-line counterexample to a conjecture on the minimal degree of Jacobian relations*, arXiv:2607.01985v2, 20 August 2026, introduction and Section 2. [Preprint](https://arxiv.org/abs/2607.01985v2).
4. P. Pokora, *On the Numerical Terao Conjecture*, arXiv:2608.05662v3, 24 August 2026, Conjecture 1.1 and Theorem 4.1. [Preprint](https://arxiv.org/abs/2608.05662v3).

5. A. Dimca and P. Pokora, *On a generalized Terao Conjecture for line arrangements*, arXiv:2609.33584v2, 2 October 2026, Conjecture 1.1 and Theorems 1.2–1.7. [Preprint](https://arxiv.org/abs/2609.33584v2).
6. M. Janasz and P. Pokora, *On homological properties of some Cynk-Szemberg octic hyperplane arrangements*, J. Korean Math. Soc. 63(4), 753–771 (2026), DOI:10.4134/JKMS.j250358; arXiv:2502.17031v4, 14 January 2026, Introduction and Definitions 2.1–2.4. [Latest preprint](https://arxiv.org/abs/2502.17031v4).
7. L. Giordani, T. Möller, P. Mücksch and G. Röhrle, *On connected subgraph arrangements* (2026), Theorems 1.2–1.4. [Publisher](https://doi.org/10.1007/s13366-026-00858-6).

## Status review


**Known cases:** The October 15/16-line theorem handles only small complex rank-three arrangements. Numerical/generalized variants and conic-line counterexamples do not give a real free/nonfree hyperplane pair with the same full intersection lattice.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The October 2026 preprint [2] still states the general freeness conjecture as open. Its theorem concerns at most 16 central planes in $`\mathbb C^3`$; it does not cover arbitrary arrangements in arbitrary dimension.

The counterexample in [3] concerns the minimal degree of Jacobian relations. Its two arrangements are both nonfree, so it does not give a free/nonfree pair with the same intersection lattice. The numerical counterexample in [4] uses lines together with a smooth conic, and equality of weak singularity counts; these differ from the hyperplanes and full intersection-lattice isomorphism required here.

The generalized invariant in [5] has results for small line arrangements, while [6] treats a special class of octic arrangements. The original version of [6] gives a conditional construction: a plane counterexample would yield higher-dimensional counterexamples. It supplies no unconditional free/nonfree pair. The projective-uniqueness theorem in [7] establishes combinatorial freeness for connected subgraph arrangements, a particular class.

Targeted searches checked Terao/freeness/intersection-lattice aliases and current papers, including announced counterexamples, through 24 October 2026. The live Prove2Me discovery page and indexed site searches returned no matching freeness statement in the inspected extent. This is a bounded search record, not an exhaustive proof of absence or a certification of the cited proofs.


### Online recheck, 2026-10-30

The October 15/16-line theorem handles only small complex rank-three arrangements. Numerical/generalized variants and conic-line counterexamples do not give a real free/nonfree hyperplane pair with the same full intersection lattice.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.25868); [status source 2](https://arxiv.org/abs/2609.33584); [status source 3](https://arxiv.org/abs/2502.17031). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-04c7ffcd86c88af0** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
