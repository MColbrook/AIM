# 811. The strong maximal-rank conjecture for linear series on a general curve

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Work over $`\mathbb C`$. Fix integers $`g,r,d\ge1`$ and $`k\ge2`$, and put
```math
s=g-d+r,\qquad \rho=g-(r+1)(g-d+r).
```

Assume
```math
s\ge0,\qquad 0\le\rho<r-2.
```

Let $`C`$ be a general smooth connected projective curve of genus $`g`$, and write
```math
W_d^r(C)=\{L\in\mathrm{Pic}^d(C):h^0(C,L)\ge r+1\},
```

where $`\mathrm{Pic}^d(C)`$ parametrizes degree-$`d`$ line bundles and $`h^0`$ is the complex dimension of the space of global sections. Under these hypotheses $`W_d^r(C)`$ has dimension $`\rho`$, and its line bundles have exactly $`r+1`$ sections and are very ample. Thus the linear series are complete.

For each $`L\in W_d^r(C)`$, consider multiplication of sections
```math
\mu_{k,L}:\mathrm{Sym}^k H^0(C,L)\longrightarrow H^0(C,L^{\otimes k}).
```

The source and target have dimensions
```math
a=\binom{r+k}{k},\qquad b=kd+1-g.
```

Let
```math
\Sigma_k(C)=
\{L\in W_d^r(C):\mathrm{rank}\mu_{k,L}<\min(a,b)\},
\qquad e=\rho-1-|a-b|.
```


**Must $`\Sigma_k(C)`$ be empty when $`e<0`$, and nonempty of Krull dimension $`e`$ when $`e\ge0`$?**

This is the original Aprodu--Farkas strong maximal-rank conjecture [1]. Generality concerns the curve: for each fixed admissible quadruple, the assertion is to hold on a nonempty Zariski open subset of its moduli space. The failure locus includes all the specified line bundles on that curve. The assertion does not require the locus to be irreducible or smooth.

## Application

The map describes which degree-$`k`$ polynomials restrict to sections on each projective embedding of $`C`$. The conjecture predicts the size of the exceptional family of embeddings. Such loci produce cycles in moduli spaces of curves and help determine their birational geometry.

## Known progress

Larson's maximal-rank theorem [3] treats a general linear series on a general curve. For $`\rho=0`$, the monodromy argument in [1] also gives the strong statement. The nonspecial range $`s=0`$ is settled by [1, Proposition 5.7]. Several further quadratic cases are known, including the range $`d\le g+1`$ reviewed in [5].

For $`k=2`$, the conjecture holds for $`(g,r,d)=(13,5,16),(22,6,25),(23,6,26)`$ [2,4,5]. The maps in the first case are surjective for every relevant line bundle; those in the other two cases are injective. In all three cases $`e=-1`$.

Robu [6] studies quadratic maps over a broader parameter range. Its examples $`(g,r,d)=(7,4,10)`$ and $`(4,4,8)`$ have $`\rho=2`$ and $`4`$, respectively, outside the strict bound $`\rho<r-2=2`$. They do not refute the formulation above. Existence of an expected-dimension component in other ranges does not determine the dimension of the entire failure locus.

## References

1. M. Aprodu and G. Farkas, *Koszul cohomology and applications to moduli*, in *Grassmannians, Moduli Spaces and Vector Bundles*, Clay Mathematics Proceedings **14** (2011), 25--50. [arXiv:0811.3117v1](https://arxiv.org/abs/0811.3117v1), Conjecture 5.4 and its preceding numerical setup; [author version](https://www.mathematik.hu-berlin.de/~farkas/clay4.pdf), PDF pp. 22--23. The complex-field convention is stated in Section 2.2.
2. I. Vogt, *Recent advances in Brill--Noether theory and the geometry of Brill--Noether curves*, [arXiv:2602.03660v1](https://arxiv.org/pdf/2602.03660v1), 2026, Conjecture 3.15 and Theorem 3.16, pp. 10--11.
3. E. Larson, *The Maximal Rank Conjecture*, [arXiv:1711.04906v2](https://arxiv.org/pdf/1711.04906v2), 2018, Theorem 1.2, p. 2.
4. G. Farkas, D. Jensen and S. Payne, *The nonabelian Brill--Noether divisor on M13 and the Kodaira dimension of R13*, Geometry & Topology **28**(2) (2024), 803--866, [DOI 10.2140/gt.2024.28.803](https://doi.org/10.2140/gt.2024.28.803). Theorem 1.5, printed p. 807, [published PDF](https://msp.org/gt/2024/28-2/gt-v28-n2-p08-p.pdf).
5. F. Liu, B. Osserman, M. Teixidor i Bigas and N. Zhang, *The strong maximal rank conjecture and moduli spaces of curves*, Algebra & Number Theory **18**(8) (2024), 1403--1464, [DOI 10.2140/ant.2024.18.1403](https://doi.org/10.2140/ant.2024.18.1403). Theorem 1.1 and the scope discussion, printed pp. 1404--1405, [published PDF](https://msp.org/ant/2024/18-8/ant-v18-n8-p01-p.pdf).
6. V. Robu, *The Stratified and the Strong Maximal Rank Conjecture in P3 and P4*, [arXiv:2605.24612v1](https://arxiv.org/pdf/2605.24612v1), 2026, Theorems 1.1--1.3 and Section 2, pp. 1--6.

## Status review


**Known cases:** The May 2026 Robu results address quadrics or existence of certain expected-dimensional components. They do not prove emptiness or the dimension of the entire rank-failure locus for every allowed linear series and every multiplication degree. The strong all-parameters conjecture remains.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The May 2026 Robu results address quadrics or existence of certain expected-dimensional components. They do not prove emptiness or the dimension of the entire rank-failure locus for every allowed linear series and every multiplication degree. The strong all-parameters conjecture remains.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Open in the cited literature; checked 26 October 2026. The 2026 survey explicitly retains the full conjecture. The more recent quadratic results and their parameter restrictions were compared with the original statement. Bounded current-literature, AIM, FURTHER and OpenAI announcement checks located no equivalent listed target or matching complete resolution.

Selected primary formulation and theorem/hypothesis passages were checked. This is a bounded status review, with no independent certification of the complete cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-80ffedebd7cab58b**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
