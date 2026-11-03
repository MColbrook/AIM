# 1003. Continuing stochastic Ricci flow through zero total area

**Area:** Rough paths and singular stochastic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(\Sigma,g)`$ be a connected closed orientable smooth Riemannian surface. Fix $`0<\gamma<2`$, $`\mu>0`$, distinct marked points $`x_i\in\Sigma`$ and real charges $`\alpha_i<Q`$, where
```math
Q=\frac2\gamma+\frac\gamma2,\qquad
\bar\alpha=\sum_i\alpha_i,\qquad
0<\bar\alpha-Q\chi(\Sigma)<\gamma.
```

Here $`\chi`$ is the Euler characteristic. Let $`m`$ be the finite Liouville area-measure law with these vertex insertions, as constructed in Dubédat–Shen §4.2: the field law $`\nu_g^\alpha`$ is pushed forward by its Gaussian multiplicative chaos area map $`X\mapsto M_\gamma(X)=:e^{\gamma X}:_g\,dV_g`$.

Write $`\mathcal X=\mathcal M_+(\Sigma)\setminus\{0\}`$, where $`\mathcal M_+(\Sigma)`$ denotes finite nonnegative Borel measures with the weak topology. Fix the particular $`m`$-symmetric stochastic Ricci diffusion $`A`$ constructed by the closed Dirichlet form in their Theorem4.3. For cylinder functions $`F(a)=q(a(f_0),\ldots,a(f_k))`$, $`f_0=1`$, its defining form is the closure of
```math
\mathcal E(F,G)=\gamma^2\int_{\mathcal X}
\sum_{i,j}(\partial_iq)(\partial_jr)\,a(f_i h_j)\,m(da),
```

where $`G(a)=r(a(h_0),\ldots,a(h_l))`$, the spatial test functions are smooth, and the smooth cylinder functions have compact support with total mass bounded away from zero. In particular, this process is killed upon reaching the globally zero measure. Use the source's quasi-everywhere convention for its starting states.

Does there exist a conservative continuous strong Markov extension $`\widetilde A`$ to $`\overline{\mathcal X}=\mathcal X\cup\{0\}`$ whose part process on $`\mathcal X`$ agrees with $`A`$, up to its usual exceptional-set equivalence, and such that for every finite $`T`$,
```math
\int_0^T\mathbf1_{\{\widetilde A_t(\Sigma)=0\}}\,dt=0
\quad\text{almost surely}?
```

Thus the full spatial area measure must resume after collapse, spending zero time at the zero measure. The family is nonempty: on a flat torus, one charge $`\alpha_1=\gamma/2`$ gives the mass-process Bessel dimension $`\delta=1`$.

## Application

This asks whether a stochastic model of two-dimensional random geometry can continue through complete area collapse while retaining its stochastic Ricci dynamics. A symmetric conservative construction would also support equilibrium sampling of the finite inserted Liouville area law; symmetry is not an extra requirement in the displayed existence question.

## References

1. J. Dubédat and H. Shen, *Stochastic Ricci Flow on Compact Surfaces*, International Mathematics Research Notices **2022**(16), 12253–12301, [DOI](https://doi.org/10.1093/imrn/rnab015); [arXiv1904.10909v2](https://arxiv.org/pdf/1904.10909v2), §4.2, Theorem4.3 and §5 Question6 (PDFp36). The [published manuscript](https://par.nsf.gov/servlets/purl/10326369) retains Question6 on PDFp43.

## Status review


**Known cases:** The spatial measure-valued process must resume after collapse and spend zero time at zero. A CIR/squared-Bessel continuation of total area alone does not construct its spatial excursions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The spatial measure-valued process must resume after collapse and spend zero time at zero. A CIR/squared-Bessel continuation of total area alone does not construct its spatial excursions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The scalar total area has generator
```math
\gamma^2v\,\partial_{vv}
+\bigl[\gamma(\bar\alpha-Q\chi)-\mu\gamma^2v\bigr]\partial_v,
\qquad \delta=\frac{2(\bar\alpha-Q\chi)}\gamma\in(0,2).
```

Its squared-Bessel/CIR continuation through zero is known. This alone does not construct the required spatial measure-valued excursions. The source explicitly asks for that continuation; extending the cylinder core to include zero is the stated difficulty. The separate all-starting-states and strong-Feller questions are not included here.

Proof, counterexample and announcement searches checked on17October2026 found no complete resolution. All-status AIM, current OpenAI overview and FURTHER comparisons found no duplicate. Prove2Me matches concerned other notions of conformal factors, zero mass and Liouville theory. Exact source extents, published-version access limits and comparisons are retained in the [source packet](../FURTHER_problems/_tracking/parallel/rough-filtering/srf-zero-area-reflection.json) and [independent review](../FURTHER_problems/_tracking/srf-zero-area-coordinator-review.json). Negative searches do not certify openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e1c1cbb962a421af**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
