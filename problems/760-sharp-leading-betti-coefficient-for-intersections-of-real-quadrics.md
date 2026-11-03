# 760. Sharp leading Betti coefficient for intersections of real quadrics

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix an integer $`k\ge4`$. For each $`n\ge k`$, let
```math
B(k,n)=\max_{q_1,\ldots,q_k}
\sum_{i\ge0}\dim_{\mathbb F_2}H_i(X;\mathbb F_2),
\qquad
X=\{[x]\in\mathbb {RP}^{n}:q_1(x)=\cdots=q_k(x)=0\},
```

where the maximum is over real homogeneous quadratic forms on $`\mathbb R^{n+1}`$. Singular common zero sets and dependent forms are allowed.

Is it true that, for every fixed $`k\ge4`$,
```math
B(k,n)=\frac{2^{k-2}}{(k-1)!}\,n^{k-1}
       +O_k(n^{k-2})
\qquad(n\to\infty)?
```

The homology is ordinary singular homology with coefficients in $`\mathbb F_2`$; the total Betti number of the empty set is zero. The error constant may depend on $`k`$.

## Application

The total Betti number measures the topological complexity of the feasible set of a system of quadratic equations. A sharp bound would quantify how that complexity grows with the number of variables when the number of equations is fixed.

## Known progress

Lerario [1] proves the order of growth $`B(k,n)=\Theta_k(n^{k-1})`$ and conjectures the sharp leading coefficient, expressed there through the topology of a smooth complex complete intersection. The source treats $`k=2`$ and $`k=3`$ separately; the question here retains the higher-codimension cases.

Basu and Rizzie [2] compute the coefficient $`2^{k-2}/(k-1)!`$ and obtain the corresponding bound under their genericity hypotheses. Their Theorem 25 concerns generic real intersections; Theorem 17 gives a weaker bound for arbitrary intersections. Remark 23 distinguishes these scopes. The question above includes singular and non-complete intersections.

## References

1. A. Lerario, *Complexity of intersections of real quadrics and topology of symmetric determinantal varieties*, Journal of the European Mathematical Society 18(2) (2016), 353–379, introduction, pp. 354–356, and §7, p. 375. [DOI](https://doi.org/10.4171/JEMS/592); [published PDF](https://ems.press/content/serial-article-files/32102?nt=1); [original preprint](https://arxiv.org/abs/1211.1444).
2. S. Basu and A. Rizzie, *Multi-degree bounds on the Betti numbers of real varieties and semi-algebraic sets and applications*, Discrete & Computational Geometry 59(3) (2018), 553–620. [DOI](https://doi.org/10.1007/s00454-017-9944-1); [latest checked arXiv version](https://arxiv.org/abs/1507.03958v7), Theorems 17 and 25, Remark 23, and §3.5.2.

## Status review


**Known cases:** The target is the sharp total mod-two Betti coefficient over all real projective intersections, allowing singular and dependent quadrics. Generic complete intersections, random arrangements and algebraic graded Betti tables do not establish the extremal coefficient.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is the sharp total mod-two Betti coefficient over all real projective intersections, allowing singular and dependent quadrics. Generic complete intersections, random arrangements and algebraic graded Betti tables do not establish the extremal coefficient.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/JEMS/592); [comparison source 2](https://ems.press/content/serial-article-files/32102?nt=1); [comparison source 3](https://arxiv.org/abs/1211.1444); [comparison source 4](https://doi.org/10.1007/s00454-017-9944-1); [comparison source 5](https://arxiv.org/abs/1507.03958v7). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The conjecture is explicit in the 2016 source, before the January 2022 cutoff. Searches through 24 October 2026 located no matching complete proof or announced resolution. The genericity distinction in [2] was checked in the current author-linked preprint; final publisher metadata was checked, but its full text was unavailable. This is a bounded literature review, not a proof of continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0155948645c0ed40**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
