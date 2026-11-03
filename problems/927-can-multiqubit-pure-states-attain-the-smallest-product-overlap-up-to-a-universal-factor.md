# 927. Can multiqubit pure states attain the smallest product overlap up to a universal factor?

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a unit vector $`\psi\in(\mathbb C^2)^{\otimes N}`$, define its maximal product-state overlap by
```math
\Lambda(\psi)=\sup_{\|u_1\|=\cdots=\|u_N\|=1}
\bigl|\langle\psi,u_1\otimes\cdots\otimes u_N\rangle\bigr|.
```

Does there exist a numerical constant $`C<\infty`$, **independent of the number of qubits $`N`$**, such that for every $`N\ge1`$ some unit vector $`\psi_N\in(\mathbb C^2)^{\otimes N}`$ satisfies
```math
\Lambda(\psi_N)^2\le C\,2^{-N}?
```

Equivalently, can the complex Hilbert–Schmidt unit sphere contain order-$`N`$ tensors with injective norm bounded by $`\sqrt C\,2^{-N/2}`$ uniformly in $`N`$? No explicit construction is required by the existence question.

## Application

The overlap measures how close a multipartite pure state is to a fully separable product state. A positive answer would remove the polynomial loss in the available random-state estimate and match the elementary $`2^{-N}`$ lower scale up to a constant. This is a sharp scaling question for geometric entanglement and complex injective tensor norms.

## References

1. Guillaume Aubrun and Alexander Müller-Hermes, [*Asymptotic Tensor Powers of Banach Spaces*](https://doi.org/10.5802/aif.3736), *Annales de l'Institut Fourier* **76** (2026), no. 3, 1341–1368, §4.1, especially Lemma 4.3 and the paragraph after its proof on printed pp. 1354–1355. The proved complex estimate retains a $`\sqrt{N\log N}`$ numerator at fixed local dimension 2; the authors explicitly say that the constant-numerator improvement is unknown even there.
2. Lisa T. Weinbrenner and Otfried Gühne, [*Quantifying entanglement from the geometric perspective*](https://doi.org/10.1209/0295-5075/adffb5), *Europhysics Letters* **151** (2025), no. 6, adffb5, “Asymptotic behaviour” section. This independently formulates the stated $`\Lambda^2(\psi_N)\le C2^{-N}`$ question and distinguishes it from the $`N^2 2^{-N}`$ random-state bound.
3. Guillaume Aubrun and Stanisław J. Szarek, *Alice and Bob Meet Banach: The Interface of Asymptotic Geometric Analysis and Quantum Information Theory*, American Mathematical Society, 2017, Problem 8.27, cited by both papers above. The book's exact problem page was not independently inspected in this review.

## Status review


**Known cases:** A dimension-independent constant multiplying 2^-N is needed, rather than its exponential root limit or polynomial losses. The 2026 tensor norm article and 2025 geometric-entanglement discussion retain this distinction; no matching constant bound found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

A dimension-independent constant multiplying 2^-N is needed, rather than its exponential root limit or polynomial losses. The 2026 tensor norm article and 2025 geometric-entanglement discussion retain this distinction; no matching constant bound found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 journal paper proves the limiting tensor radius but explicitly leaves the finite-order constant-numerator bound open; taking an $`N`$-th root loses the polynomial factor and therefore does not answer this question. The 2025 review independently labels the same multiqubit inequality open. A targeted literature and announcement search on 21 October 2026 found no subsequent resolution, and a semantic comparison found no duplicate in AIM or existing FURTHER pages. This bounded status assessment does not establish unsolvedness as a theorem.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c77f7a7a604d2997**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
