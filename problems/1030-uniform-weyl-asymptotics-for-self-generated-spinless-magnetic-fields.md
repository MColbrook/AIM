# 1030. Uniform Weyl asymptotics for self-generated spinless magnetic fields

**Area:** Semiclassical spectral theory and magnetic Schrödinger operators
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a real potential $`V\in L^{5/2}(\mathbb R^3)`$, and write $`V_+=\max\{V,0\}`$. For $`h>0`$ and $`\beta\ge0`$, define
```math
E^{\rm S}(\beta,h,V)
=\inf_{A\in H^1(\mathbb R^3;\mathbb R^3)}
\left\{
\mathrm{Tr}\bigl(( -ih\nabla+A)^2-V\bigr)_-
+\beta\int_{\mathbb R^3}|\mathrm{curl}A|^2\,dx
\right\}.
```

Here $`t_-=\min\{t,0\}`$: the trace is the signed sum of the negative eigenvalues, using the variational/Friedrichs formulation of Appendix A in [1]. The operator acts on scalar $`L^2(\mathbb R^3)`$.

Prove or disprove
```math
\lim_{h\downarrow0}\ \sup_{\beta\ge0}
\left|
h^3E^{\rm S}(\beta,h,V)
+\frac{1}{15\pi^2}\int_{\mathbb R^3}V_+(x)^{5/2}\,dx
\right|=0.
```

The potential is fixed before taking the limit. Uniformity is required over the field-energy penalty, including $`\beta=0`$; no quantitative remainder or uniformity over potentials is requested.

## Application

This would show that optimizing a self-generated magnetic field leaves the leading semiclassical energy of spinless noninteracting fermions unchanged, even when the field-energy penalty becomes arbitrarily small.

## References

1. László Erdős, Søren Fournais and Jan Philip Solovej, *Stability and semiclassics in self-generated fields*, Journal of the European Mathematical Society **15** (2013), no. 6, 2093–2113. [DOI](https://doi.org/10.4171/JEMS/416), [publisher PDF](https://ems.press/content/serial-article-files/31927?nt=1), [author preprint](https://arxiv.org/abs/1105.0506v3). Equation (1), equation (6), Theorem 2.2 and Remark 3, printed pages 2094–2098; Appendix A, printed pages 2107–2108.

## Status review


**Known cases:** Uniformity includes zero magnetic-field penalty for the scalar spinless operator. The known beta-h large asymptotics and spin-dependent Pauli results do not cover this all-penalty endpoint.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Uniformity includes zero magnetic-field penalty for the scalar spinless operator. The known beta-h large asymptotics and spin-dependent Pauli results do not cover this all-penalty endpoint.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Theorem 2.2 of [1] proves the stated leading term when $`\beta h\to\infty`$. Remark 3 explicitly conjectures uniformity for $`\beta\in[0,\infty)`$ in the spinless case. Equation (6) gives a universal lower bound with a nonsharp constant, and choosing $`A=0`$ gives the nonmagnetic upper comparison.

Monotonicity gives
```math
E^{\rm S}(0,h,V)\le E^{\rm S}(\beta,h,V)
\le \mathrm{Tr}(-h^2\Delta-V)_-.
```

Consequently, the all-$`\beta`$ assertion is equivalent to the corresponding leading limit at $`\beta=0`$, using the usual nonmagnetic Weyl asymptotics. This equivalence is an elementary inference from the definition. The Pauli analogue has different behaviour and is outside this problem.

No matching complete published or announced resolution was located in the bounded searches on 24 October 2026. Comparisons included later self-generated-field asymptotics, Scott-correction results, Lieb–Thirring bounds and planar constant-field estimates. A full later monograph chapter was inaccessible; the audit retains this search gap. These checks do not certify that no unindexed result exists.

The [planar variable-field Dirichlet eigenvalue problem](424-does-the-sharp-liyau-bound-hold-for-varying-magnetic-fields.md) is related but has a different dimension, domain, spectral target and quantification. AIM 018 asks for the sharp nonmagnetic three-dimensional Lieb–Thirring inequality; the OpenAI announcement on sharp one-dimensional matrix inequalities also has a different target. All-status catalogue and FURTHER comparisons found no equivalent existing statement.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f195e30a22b0b5bd**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
