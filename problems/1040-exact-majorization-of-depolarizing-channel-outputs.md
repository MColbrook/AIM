# 1040. Exact majorization of depolarizing-channel outputs

**Area:** Quantum information and matrix inequalities
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`d\geq2`$, let the depolarizing channel on $`d`$-dimensional matrices be

```math
\mathcal D_{p,d}(X)=(1-p)X+\frac{p}{d}\mathrm{Tr}(X)I_d,
\qquad 0\leq p\leq\frac{d^2}{d^2-1}.
```


For every $`n\geq1`$ and every density matrix $`\rho`$ on $`(\mathbb C^d)^{\otimes n}`$, must the output eigenvalues of $`\mathcal D_{p,d}^{\otimes n}(\rho)`$ be majorized by those for any fixed pure product input? Explicitly, with eigenvalues listed in decreasing order, is

```math
\lambda^\downarrow\!\left(\mathcal D_{p,d}^{\otimes n}(\rho)\right)
\prec
\lambda^\downarrow\!\left(\mathcal D_{p,d}^{\otimes n}
 (|0\rangle\langle0|^{\otimes n})\right)?
```


Here $`x\prec y`$ means that every initial partial sum of the decreasingly ordered entries of $`x`$ is at most the corresponding sum for $`y`$, with equal total sums. The question includes possibly entangled inputs $`\rho`$ and the full completely positive parameter range above. A proof for every $`d,p,n`$, or one counterexample, would decide the conjecture.

## Application

Exact majorization would compare all convex spectral functionals of arbitrary outputs with the pure-product reference output. In classical communication through repeated depolarizing channels, it would give stronger finite-blocklength control than the currently proved approximate majorization. The channel's leading-order classical capacity and the paper's third-order expansion are already established; neither settles this exact spectral question.

## References

1. Z. Song, X. Wang, M. Tomamichel and K. Fang, [*Approximate majorization and high-order capacity of quantum depolarizing channels*](https://arxiv.org/html/2609.37240v1), arXiv:2609.37240v1 (29 September 2026), Introduction, equations (1)–(2), and §5, Discussion. The authors state the exact relation as a conjecture, prove an approximate relation, and identify the exact version as open in the discussion.
2. C. King, [*The capacity of the quantum depolarizing channel*](https://arxiv.org/abs/quant-ph/0204172), *IEEE Transactions on Information Theory* **49** (2003), 221–229. King's established norm and entropy results give important weaker comparisons, as explained in [1, Introduction and Remark 5](https://arxiv.org/html/2609.37240v1).

## Status review


**Known cases:** The conjecture asks exact all-partial-sum majorization for all tensor powers. The September 2026 source still conjectures it; approximate majorization, shifted determinants and bosonic Gaussian-channel majorization are different.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The conjecture asks exact all-partial-sum majorization for all tensor powers. The September 2026 source still conjectures it; approximate majorization, shifted determinants and bosonic Gaussian-channel majorization are different.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The September 2026 source states the conjecture for the entire range $`0\leq p\leq d^2/(d^2-1)`$. Its Theorem 4 compares shifted log determinants; its approximate-majorization bound permits a nonzero spectral defect and does not prove the exact partial-sum inequalities. The authors again call exact majorization open in §5. The current arXiv record lists only v1. Bounded searches on 21 October 2026 for the exact conjecture, a proof, a counterexample and an announcement found no matching complete resolution. A separate bosonic Gaussian-channel majorization theorem concerns a different channel and does not answer this question. Searches of AIM problem statements and admitted FURTHER pages found no equivalent target. These checks do not certify exhaustive absence of a solution.

The [primary-source audit](../FURTHER_problems/_tracking/depolarizing-majorization-primary-2026-10-21.json), [current-status review](../FURTHER_problems/_tracking/depolarizing-majorization-status-2026-10-21.json), and [duplicate/scope review](../FURTHER_problems/_tracking/depolarizing-majorization-duplicates-2026-10-21.json) record the selected evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e6d09869b8647910**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
