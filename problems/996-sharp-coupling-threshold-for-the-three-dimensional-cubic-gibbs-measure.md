# 996. Sharp coupling threshold for the three-dimensional cubic Gibbs measure

**Area:** Singular stochastic equations and mathematical physics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mu`$ be the real massive Gaussian free field on $`\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3`$, and let $`u_N=\pi_Nu`$ use the *cube* Fourier cutoff of the source. For $`\sigma\ne0`$, $`A>0`$, and the taming exponent $`\gamma=3`$, use the source's Wick-ordered potential and second renormalization (1.2.9)–(1.2.12):

```math
R_N(u)=-\frac{\sigma}{3}\int_{\mathbb T^3}\! :u_N^3:\,dx
+A\left|\int_{\mathbb T^3}\! :u_N^2:\,dx\right|^3,
\qquad R_N^{\diamond}=R_N+\alpha_N,
\qquad d\rho_N=Z_N^{-1}e^{-R_N^{\diamond}}\,d\mu.
```

Does a sharp coupling $`\sigma_*>0`$ exist such that these measures can be constructed as the unique weak limit for every $`0<|\sigma|<\sigma_*`$ with a suitable sufficiently large $`A=A(\sigma)`$, while the corresponding $`\Phi^3_3`$ measure is non-normalizable for every $`|\sigma|>\sigma_*`$ and every $`A>0`$? If so, determine $`\sigma_*`$ and decide whether the measure is normalizable at $`|\sigma|=\sigma_*`$. The source's precise non-normalizability notion uses a $`\sigma`$-finite reference measure; a bare divergence of a formal partition function would not replace that condition.

The source proves the first assertion only for $`0<|\sigma|<\sigma_0`$ and the second only for $`|\sigma|>\sigma_1`$, where $`0<\sigma_0\leq\sigma_1`$. Its Remark 1.2.5 asks whether these regimes meet at a sharp value and what happens at that value. The question here uses the same cube cutoff and taming as that theorem.

## Application

The $`\Phi^3_3`$ Gibbs measure is an invariant-measure candidate for a three-dimensional stochastic damped nonlinear wave equation. A sharp threshold would say exactly which coupling strengths permit this probability measure and whether the borderline model exists.

## References

1. Tadahiro Oh, Mamoru Okamoto and Leonardo Tolomeo, *Stochastic Quantization of the $`\Phi^3_3`$-Model*, **Memoirs of the European Mathematical Society** **16** (2025), ISBN 978-3-98547-085-3, [DOI](https://doi.org/10.4171/MEMS/16). [Publisher Chapter 1 PDF](https://ems.press/content/book-chapter-files/49916), definitions (1.2.9)–(1.2.12), Theorem 1.2.1, printed pp. 11–12; explicit threshold and endpoint question, Remark 1.2.5, printed p. 15.
2. Niko Nikov, *Phase transitions for fractional $`\Phi^3_d`$ on the torus*, [arXiv:2501.17669v1](https://arxiv.org/html/2501.17669) (2025), Introduction and Theorem 1.2. Its critical fractional extension retains a small-versus-large coupling split.
3. Damiano Greco, Tadahiro Oh, Liying Tao and Leonardo Tolomeo, *Critical threshold for weakly interacting log-correlated focusing Gibbs measures*, [arXiv:2412.09790v2](https://arxiv.org/abs/2412.09790) (2025 revision). Its threshold concerns a different quartic, vanishing-coupling model.
4. Nikolay Barashkov, Kihoon Seong and Philippe Sosoe, *Sharp phase transition in the grand canonical $`\Phi^3`$ measure at critical chemical potential*, [arXiv:2508.08427](https://arxiv.org/abs/2508.08427) (2025; published 2026). It concerns a two-dimensional model and a chemical-potential threshold.

## Status review


**Known cases:** The sharp coupling for the tamed three-dimensional cubic model, including its endpoint, is needed. Small/large coupling split results, fractional extensions and two-dimensional chemical-potential thresholds are different.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The sharp coupling for the tamed three-dimensional cubic model, including its endpoint, is needed. Small/large coupling split results, fractional extensions and two-dimensional chemical-potential thresholds are different.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The publisher's printed pp. 11, 12 and 15 were inspected visually to fix mathematical symbols that the text extractor garbled. The author-hosted final manuscript still asks the same question in its corresponding Remark 1.12. The later fractional model proves only the separated small- and large-coupling regimes. The other threshold papers above concern different dimensions or interactions. Bounded result and announcement searches through 21 October 2026 found no resolution of this exact three-dimensional, fixed-coupling endpoint problem.

Semantic searches found no matching AIM problem or previously admitted FURTHER entry. The [source-bound page receipt](../FURTHER_problems/_tracking/parallel/continuum/cached-broad-books-body-continuation-0247-replacements-review.json) and [detailed review](../FURTHER_problems/_tracking/phi33-sharp-coupling-review-2026-10-21.json) record the checked extents and limits. A bounded search cannot exclude an unindexed result.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2d361e842e464f3a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
