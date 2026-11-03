# 889. Uniform and coarse embeddings of $`\ell_2(\ell_1)`$ into intermediate $`L_p`$

**Area:** Nonlinear geometry of Banach spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\ell_2(\ell_1)`$ be the space of sequences $`x=(x_j)_{j\geq1}`$ with $`x_j\in\ell_1`$ and norm
```math
\|x\|_{\ell_2(\ell_1)}=\left(\sum_{j\geq1}\|x_j\|_{\ell_1}^{2}\right)^{1/2}.
```

For each $`2<p<4`$, does $`\ell_2(\ell_1)`$ admit a **uniform embedding** into $`L_p`$? Does it admit a **coarse embedding** into $`L_p`$? The two embedding notions are defined through small-scale and large-scale control, respectively, in [1, Section 3]. This is Question 2 of [1].

**Editorial clarification:** Correct the typographical exponent \|x_j\|_{\ell_1}^{,2} to \|x_j\|_{\ell_1}^{2}; this is the standard squared norm defining ell2(ell1), with no mathematical scope change.

## Application

The answer would locate a transition in the nonlinear geometry of $`L_p`$ spaces and test how the $`\ell_2`$ sum of $`\ell_1`$ blocks behaves under embeddings that need not be linear. It would clarify which metric properties of a Banach space survive a change of target exponent.

## Known results and scope

Naor and Schechtman show that no such uniform or coarse embedding exists for $`1\leq p\leq2`$. For $`p\geq4`$, their Proposition 3.1 constructs an embedding that is both uniform and coarse, with $`\|F_p(x)-F_p(y)\|_p=\|x-y\|_{\ell_2(\ell_1)}^{2/p}`$. The interval $`2<p<4`$ lies between these results. Their proof for $`p\geq4`$ uses a Schoenberg snowflake step whose exponent condition does not cover this interval [1, Section 3].

## References

1. A. Naor and G. Schechtman, [*Pythagorean powers of hypercubes*](https://aif.centre-mersenne.org/item/10.5802/aif.3032.pdf), *Annales de l'Institut Fourier* **66** (2016), no. 3, 1093–1116, Section 3, Proposition 3.1 and Question 2. [DOI](https://doi.org/10.5802/aif.3032).

## Status review


**Known cases:** The known constructions apply for p at least four; the source explicitly asks the intermediate range two less than p less than four. Nonembedding into L1 does not imply nonembedding into Lp above two, and finite-set dimension-reduction results have another domain and target.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known constructions apply for p at least four; the source explicitly asks the intermediate range two less than p less than four. Nonembedding into L1 does not imply nonembedding into Lp above two, and finite-set dimension-reduction results have another domain and target.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source, later-result and duplicate audit](../FURTHER_problems/_tracking/pythagorean-power-lp-embedding-status-2026-10-21.json) records the exact intermediate exponent range. No complete proof, counterexample or announced settlement for that range was found in bounded searches through 21 October 2026.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-02436258f77c2746**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
