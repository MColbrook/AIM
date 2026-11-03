# 708. The critical opening for asymptotic Borel surjectivity

**Area:** Complex analysis and asymptotic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M=(M_p)_{p\ge0}`$, $`M_0=1`$, be strongly regular: positive and logarithmically convex, with constants $`A,B>0`$ such that
```math
M_{p+q}\le A^{p+q}M_pM_q,\qquad
\sum_{q\ge p}\frac{M_q}{(q+1)M_{q+1}}\le B\frac{M_p}{M_{p+1}}.
```

Set $`m_p=M_{p+1}/M_p`$ and
```math
\gamma(M)=\sup\{a>0:(m_p/(p+1)^a)_p\text{ is almost increasing}\}.
```

Almost increasing means $`c_p\le Kc_q`$ whenever $`p\le q`$, for a fixed $`K`$.

On the logarithm's Riemann surface put $`S_\alpha=\{z:|\arg z|<\pi\alpha/2\}`$, with $`0<|z|<\infty`$. Prescribe $`\widehat f=\sum a_pz^p`$ satisfying $`|a_p|\le CA^pM_p`$. Define three holomorphic classes:

- $`\widetilde{\mathcal A}_M`$: for each bounded proper subsector $`T`$ of $`S_\alpha`$, some $`C_T,A_T>0`$ satisfy
  ```math
|f(z)-\sum_{p<N}a_pz^p|\le C_TA_T^NM_N|z|^N\quad(z\in T,\ N\ge0).
```

- $`\widetilde{\mathcal A}^{u}_M`$: that estimate holds throughout $`S_\alpha`$ with one pair of constants.
- $`\mathcal A_M`$: some $`C,A>0`$ satisfy $`|f^{(p)}(z)|\le CA^p p!M_p`$ throughout $`S_\alpha`$.

Let $`\mathcal S`$ denote the openings $`\alpha>0`$ for which the coefficient map onto all prescribed series is surjective. Is
```math
\mathcal S(\widetilde{\mathcal A}_M)=(0,\gamma(M)],\qquad
\mathcal S(\widetilde{\mathcal A}^{u}_M)=\mathcal S(\mathcal A_M)=(0,\gamma(M))
```

always true? At the critical opening this asks for nonuniform surjectivity and uniform non-surjectivity.

## Application

The endpoint controls how far a divergent formal expansion can be realized by an analytic solution in a sector.

## References

1. J. JimÃ©nez-Garrido, J. Sanz and G. Schindl, [*Injectivity and surjectivity of the asymptotic Borel map in Carleman ultraholomorphic classes*](https://arxiv.org/pdf/1805.01153), Definitions 2.1â€“2.2 and 4.1, Section 2.3, Remark 4.20 and Table 4, p.30. *Journal of Mathematical Analysis and Applications* **469** (2019), 136â€“168; [DOI](https://doi.org/10.1016/j.jmaa.2018.09.011).
2. The same authors, [*Surjectivity of the asymptotic Borel map in Carlemanâ€“Roumieu ultraholomorphic classes defined by regular sequences*](https://doi.org/10.1007/s13398-021-01119-y), *RACSAM* **115** (2021), 181, end of Section 3.
3. J. JimÃ©nez-Garrido, I. Miguel-Cantero, J. Sanz and G. Schindl, [*Surjectivity of the asymptotic Borel map in Carleman ultraholomorphic classes defined by sequences with shifted moments*](https://doi.org/10.1186/s13660-026-03485-w), *Journal of Inequalities and Applications* **2026**, 85, Theorem 2.10 and Section 4.

## Status review


**Known cases:** The critical opening, Roumieu quantifiers and three different asymptotic classes are retained. Interior/exterior bounds, rational-index exclusions and Beurling statements do not settle both unrestricted endpoint decisions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The critical opening, Roumieu quantifiers and three different asymptotic classes are retained. Interior/exterior bounds, rational-index exclusions and Beurling statements do not settle both unrestricted endpoint decisions.

Additional comparison sources: [comparison source 1](https://arxiv.org/pdf/1805.01153); [comparison source 2](https://doi.org/10.1016/j.jmaa.2018.09.011); [comparison source 3](https://doi.org/10.1007/s13398-021-01119-y); [comparison source 4](https://doi.org/10.1186/s13660-026-03485-w). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Interior/exterior bounds are known. The uniform and derivative endpoints are excluded for rational $`\gamma(M)`$; important subclasses admit nonuniform realizations at the endpoint. The 2021 article repeats the general conjecture, while the 2026 theorem retains the endpoint bracket. Its Beurling results use different quantifiers and do not settle this Roumieu question.

The [coordinating review](../FURTHER_problems/_tracking/focused-Borel-map-critical-opening-C191-A-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, current-resolution, announcement and semantic duplicate checks, with independent normalization review. Bounded checks do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-98eccdb3a0a69c54**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
