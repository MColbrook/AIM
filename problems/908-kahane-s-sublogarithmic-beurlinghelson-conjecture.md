# 908. Kahane's sublogarithmic Beurling–Helson conjecture

**Area:** Harmonic analysis and Wiener-algebra composition operators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathbb T=\mathbb R/(2\pi\mathbb Z)`$. For a continuous function $`f`$ on $`\mathbb T`$, write

```math
\widehat f(k)=\frac1{2\pi}\int_0^{2\pi}f(t)e^{-ikt}\,dt,\qquad
  \|f\|_{A(\mathbb T)}=\sum_{k\in\mathbb Z}|\widehat f(k)|.
```


For every continuous circle map $`\varphi:\mathbb T\to\mathbb T`$, does

```math
\|e^{in\varphi}\|_{A(\mathbb T)}=o(\log |n|)
  \quad\text{as }|n|\to\infty
```


imply $`\varphi(t)=\nu t+\varphi(0)`$ modulo $`2\pi`$ for some $`\nu\in\mathbb Z`$? The condition is required for **all sufficiently large positive and negative integers** $`n`$. Nonlinear piecewise-linear maps can have norm of order $`\log|n|`$, so the proposed little-$`o`$ threshold is sharp in scale.

## Application

The question asks how slowly the Fourier-series norm of powers of a circle map may grow before the map must be affine. A positive answer would extend the classical bounded-norm Beurling–Helson rigidity theorem to the proposed sharp threshold for changes of variable in the Wiener algebra.

## References

1. V. Lebedev, [*Absolutely convergent Fourier series. An improvement of the Beurling–Helson theorem*](https://arxiv.org/html/1112.4892), arXiv:1112.4892v3 (2012), Introduction and theorem. The introduction defines the norm, states Kahane's conjecture and describes the piecewise-linear boundary examples.
2. T. Sanders, [*The quantitative Beurling–Helson theorem*](https://arxiv.org/html/2604.07324), arXiv:2604.07324v1 (2026), Introduction, Theorem 1.4. It restates the conjecture and proves the affine conclusion under the stronger $`O(\log^{1/8-\varepsilon}|n|)`$ bound for any $`\varepsilon>0`$.

## Status review


**Known cases:** The primary current Sanders theorem still assumes O(log-to-the-one-eighth-minus-epsilon) Fourier norm growth, which is stronger than little-o of log. The full sharp sublogarithmic threshold has not been matched by a complete proof or counterexample.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The primary current Sanders theorem still assumes O(log-to-the-one-eighth-minus-epsilon) Fourier norm growth, which is stronger than little-o of log. The full sharp sublogarithmic threshold has not been matched by a complete proof or counterexample.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2604.07324). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 theorem does not settle the little-$`o(\log|n|)`$ hypothesis. Current searches for an exact-threshold proof, counterexample or announcement, and semantic comparisons with the AIM and FURTHER lists, found none through 2026-10-21. The [review receipt](../FURTHER_problems/_tracking/kahane-beurling-helson-status-2026-10-21.json) gives the checked scope and limits; it does not certify the absence of unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-74082b8169c81216**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
