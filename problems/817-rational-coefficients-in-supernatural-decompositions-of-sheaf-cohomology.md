# 817. Rational coefficients in supernatural decompositions of sheaf cohomology

**Area:** Algebraic geometry / cohomology of coherent sheaves
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`K`$ be a field, let $`n\geq1`$, and let $`\mathcal F\ne0`$ be a coherent sheaf on $`\mathbb P^n_K`$. Its cohomology table has entries
```math
\gamma_{i,t}(\mathcal F)=\dim_K H^i(\mathbb P^n_K,\mathcal F(t)),
\qquad 0\leq i\leq n,\quad t\in\mathbb Z.
```


For a strictly decreasing integer sequence $`z=(z_1>\cdots>z_s)`$, $`0\leq s\leq n`$, put $`z_0=+\infty`$ and $`z_{s+1}=z_{s+2}=\cdots=-\infty`$. Define the normalized supernatural table
```math
\gamma^z_{i,t}=
\begin{cases}
\displaystyle\prod_{j=1}^{s}|t-z_j|,&0\leq i\leq s,\ z_i>t>z_{i+1},\\
0,&\text{otherwise}.
\end{cases}
```

The empty product is one. This is the normalization in which the supernatural sheaf has degree $`s!`$.

Order root sequences coordinatewise after padding with $`-\infty`$. Eisenbud–Schreyer prove that there is a unique chain $`Z`$ of such sequences and unique positive real coefficients $`q_z`$ with
```math
\gamma(\mathcal F)=\sum_{z\in Z}q_z\gamma^z,
```

where the sum converges in each entry.

**Must every $`q_z`$ be rational, including when $`\mathcal F`$ is not pure-dimensional?**

Here pure-dimensional means that all associated subvarieties have the same dimension. The question concerns the coefficients in this unique chain decomposition. It does not require a finite sum or a common denominator.

## Application

These tables record the dimensions of all twisted sheaf-cohomology groups and refine the Hilbert polynomial. The question asks whether their canonical expansion in explicit building blocks always uses rational weights. The decomposition can involve infinitely many terms, so rationality would not by itself give a finite classification or algorithm. Its significance is in the numerical structure of coherent sheaves and Boij–Söderberg theory.

## References

1. D. Eisenbud and F.-O. Schreyer, [*Cohomology of coherent sheaves and series of supernatural bundles*](https://doi.org/10.4171/JEMS/212), *Journal of the European Mathematical Society* **12** (2010), 703–722. Introduction, Theorem 0.2 and Question 1, printed pp. 703–704; Algorithm 0.4, p. 706. [Author version](https://arxiv.org/abs/0902.1594).
2. D. Erman and S. V. Sam, [*Supernatural analogues of Beilinson monads*](https://doi.org/10.1112/S0010437X16007703), *Compositio Mathematica* **152** (2016), 2545–2562. [Version 2](https://arxiv.org/html/1506.07558v2), Theorem 1.8 and Proposition 5.1.
3. S. B. Iyengar, L. Ma and M. E. Walker, [*Lim Ulrich sequences and Boij–Söderberg cones*](https://doi.org/10.1017/fms.2023.108), *Forum of Mathematics, Sigma* **11** (2023), e115. Section 3, especially Theorem 3.4 and its proof.

## Status review


**Known cases:** Finite rational decompositions of graded local cohomology tables in bounded dimension and pure Betti-table results are different cones. Rational approximation of a real cohomology-table decomposition does not establish rationality of each unique chain coefficient for a general non-pure coherent sheaf.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Finite rational decompositions of graded local cohomology tables in bounded dimension and pure Betti-table results are different cones. Rational approximation of a real cohomology-table decomposition does not establish rationality of each unique chain coefficient for a general non-pure coherent sheaf.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original Question 1 in [1] explicitly asks for rationality beyond the pure-dimensional case. Theorem 0.2 proves rationality of every coefficient attached to a top-dimensional summand, and of all coefficients when the sheaf is pure-dimensional.

Theorem 1.8 of [2] concerns vector bundles whose finite rational decomposition uses a particular collection of supernatural bundles. It assumes rational coefficients and does not settle the non-pure case. Proposition 5.1 gives a general inequality on transformed cohomology tables rather than equality sufficient to recover such a decomposition.

Theorem 3.4 of [3] compares closures of cones in positive characteristic. Its proof uses positive real coefficients and rational approximation of them; approximation does not show that the canonical coefficients themselves are rational.

Bounded searches through 24 October 2026 located no matching proof, counterexample or complete announced solution. The source's official arXiv history shows only its 2009 version; the published 2010 statement supplies the eligible witness. Selected source and comparison statements were checked, with no full audit of their proofs. The observed Prove2Me homepage and targeted indexed searches produced no matching claim; this is not a review of the whole website.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-96345eb794be9f0e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
