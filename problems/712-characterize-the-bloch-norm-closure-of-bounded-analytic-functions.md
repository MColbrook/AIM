# 712. Characterize the Bloch-norm closure of bounded analytic functions

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb D=\{z\in\mathbb C:|z|<1\}`$, and define the Bloch space
```math
\mathcal B=\left\{f\in\mathrm{Hol}(\mathbb D):
 \|f\|_{\mathcal B}:=|f(0)|+
 \sup_{z\in\mathbb D}(1-|z|^2)|f'(z)|<\infty\right\}.
```

Let $`H^\infty(\mathbb D)`$ be the bounded holomorphic functions on $`\mathbb D`$.

Find an intrinsic necessary-and-sufficient condition on $`f\in\mathcal B`$ for
```math
\inf_{g\in H^\infty(\mathbb D)}\|f-g\|_{\mathcal B}=0.
```

The aim is a characterization of this closed subspace, rather than a restatement of the existence of bounded analytic approximants. A derivative-seminorm convention gives the same closure question, since approximants can be adjusted by constants.

## Application

The answer would identify exactly which Bloch functions can be approximated by bounded analytic functions while controlling their hyperbolically weighted derivatives. This is a boundary approximation problem in analytic function-space theory.

## References

- A. Nicolau and O. Soler i Gibert, *Approximation in the Zygmund Class*, [arXiv:1809.11126v1](https://arxiv.org/html/1809.11126v1), §7, Problem 3, preprint p. 25. The original question is attributed there to J. M. Anderson, J. Clunie and C. Pommerenke, *On Bloch functions and normal functions*, **Journal für die reine und angewandte Mathematik** 270 (1974), 12–37.
- A. Limani and A. Nicolau, *Bloch functions and Bekollé–Bonami weights*, [arXiv:2009.10445v1](https://arxiv.org/html/2009.10445v1), introduction and Theorem 1.4.
- X. Zhu and R. Yang, *The closure of the analytic type tent spaces in the weighted-type space and generalized weighted composition operators*, **Mathematical Inequalities & Applications** 28(4) (2025), 705–723. [Primary PDF](https://files.ele-math.com/articles/mia-28-41.pdf), p. 706; DOI [10.7153/mia-2025-28-41](https://doi.org/10.7153/mia-2025-28-41).

## Status review


**Known cases:** Finite Hardy-exponent and BMO closure characterizations do not cover H-infinity. The Limani-Nicolau weight counterexample refutes a proposed characterization rather than supplying the missing general one.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Finite Hardy-exponent and BMO closure characterizations do not cover H-infinity. The Limani-Nicolau weight counterexample refutes a proposed characterization rather than supplying the missing general one.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/1809.11126v1); [comparison source 2](https://arxiv.org/html/2009.10445v1); [comparison source 3](https://files.ele-math.com/articles/mia-28-41.pdf); [comparison source 4](https://doi.org/10.7153/mia-2025-28-41). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. Zhu–Yang explicitly retain this problem as unresolved. Characterizations for finite-exponent Hardy spaces, analytic BMO and related spaces do not answer the $`H^\infty`$ question. Limani–Nicolau disprove a proposed weight criterion; they do not provide the missing characterization.

Current searches found no matching complete resolution announcement. Semantic comparisons with all-status AIM/OpenAI records and the developing collection distinguished Bloch surface conjectures, magnetic Bloch laws and Bloch-to-Bergman inclusion constants. No equivalent target was located. This is a dated, bounded check.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-aff7be7b7056ada6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
