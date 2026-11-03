# 707. Smooth Chern–Ricci collapse on non-Kähler elliptic bundles

**Area:** Complex geometry and geometric partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a connected compact non-Kähler complex surface with a holomorphic elliptic bundle $`f:M\to\Sigma`$, where $`\Sigma`$ is a compact Riemann surface of genus at least two. Here a bundle is locally biholomorphic over the base to $`E\times U`$ for a fixed elliptic curve $`E`$. Let $`\omega_0`$ be an arbitrary smooth positive Gauduchon metric, so $`\partial\bar\partial\omega_0=0`$.

Let $`\omega(t)`$ be the unnormalized Chern–Ricci flow

```math
\partial_t\omega=-\mathrm{Ric}^{\mathrm{Ch}}(\omega),\qquad \omega(0)=\omega_0,
\qquad \mathrm{Ric}^{\mathrm{Ch}}(\omega)=-i\partial\bar\partial\log\det(g).
```

This flow exists for all $`t\ge0`$ in the stated setting. Write $`\omega_\Sigma`$ for the unique Kähler metric on $`\Sigma`$ with $`\mathrm{Ric}(\omega_\Sigma)=-\omega_\Sigma`$. Is it true that

```math
\frac{\omega(t)}t\longrightarrow f^*\omega_\Sigma
\quad\text{in }C^\infty(M),
\qquad
\sup_M\left|\mathrm{Rm}^{\mathrm{Ch}}\!\left(\frac{\omega(t)}t\right)\right|_{\omega(t)/t}\le C
\quad(t\ge t_0)
```

for some finite $`C`$ and $`t_0>0`$? The constants may depend on the bundle and the entire initial metric. The curvature is the full curvature tensor of the Chern connection, measured in the evolving normalized metric. Smooth tensor convergence is measured in any fixed smooth background metric; the limit is semipositive and vanishes in the fibre directions.

The requested conclusions are global smooth convergence and bounded normalized curvature. Uniform convergence and Gromov–Hausdorff convergence are already known. Smooth convergence restricted to individual fibres does not supply all transverse and mixed derivatives. No restriction of $`\omega_0`$ to a special $`\partial\bar\partial`$ class is imposed.

## Application

The problem asks for derivative and curvature control while a nonlinear metric flow collapses elliptic fibres. It would distinguish controlled geometric collapse from curvature blowup in the predicted long-time classification of complex surfaces.

## References

1. V. Tosatti and B. Weinkove, *The Chern–Ricci flow*, Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl. **33** (2022), 73–107. [DOI](https://doi.org/10.4171/RLM/965), [primary preprint v3](https://arxiv.org/pdf/2107.12928v3), Section 4.2 and Conjecture 4.2, pp. 8–10.
2. D. Angella and V. Tosatti, *Leafwise flat forms on Inoue-Bombieri surfaces*, Journal of Functional Analysis **285** (2023), 110015. [DOI](https://doi.org/10.1016/j.jfa.2023.110015), [primary preprint v2](https://arxiv.org/pdf/2106.16141v2), Theorem 1.3 and Section 6, especially Remarks 6.1–6.2.
3. H. Wondo, *Singularity Types for Long-Time Chern-Ricci Flow*, [arXiv:2408.12797v1](https://arxiv.org/pdf/2408.12797v1), Theorem 1.1 and Section 5; selected comparison only.

## Status review


**Known cases:** The May general-type surface theorem has Kodaira dimension two and Gromov-Hausdorff conclusions; this elliptic-bundle question requires global smooth tensor convergence and normalized full-curvature bounds for arbitrary Gauduchon data.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The May general-type surface theorem has Kodaira dimension two and Gromov-Hausdorff conclusions; this elliptic-bundle question requires global smooth tensor convergence and normalized full-curvature bounds for arbitrary Gauduchon data.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/RLM/965); [comparison source 2](https://arxiv.org/pdf/2107.12928v3); [comparison source 3](https://doi.org/10.1016/j.jfa.2023.110015); [comparison source 4](https://arxiv.org/pdf/2106.16141v2); [comparison source 5](https://arxiv.org/pdf/2408.12797v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The full conclusion is known for initial metrics in the specified Vaisman $`\partial\bar\partial`$ class in Reference 2. Its extension for arbitrary Gauduchon data gives fibrewise smoothness, which is weaker than this target. Reference 3 transfers curvature control within one initial $`\partial\bar\partial`$ class and assumes an already controlled reference solution. It does not reach every Gauduchon class. No matching unrestricted result or complete announcement was located in the recorded searches.

Separate primary audits checked those restrictions, the time normalization and the curvature norm. A local counterexample to derivative estimates independent of initial torsion does not disprove this compact global statement, whose constants may depend on the full initial metric. Finite-time singular-locus results and long-time results for general-type surfaces concern different targets.

All-status AIM/OpenAI and Prove2Me listing-description comparisons found no equivalent announcement. The source reviewer read the pinned survey and Angella–Tosatti preprint in full; parity with their published versions remains unchecked. Wondo's paper was read only in the selected passages recorded in the [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/chern-elliptic-collapse-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-chern-elliptic-review.json). These are bounded status checks, not certification of every cited proof.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-983f21a8e62469d9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
