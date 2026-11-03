# 745. Global positive classical evolution for the non-isothermal binary PNPF system

**Area:** Electrochemistry and nonlinear partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`c>1`$. On $`\mathbb R^3`$, consider positive concentrations $`p,n`$, absolute temperature $`\theta`$, particle velocities $`v_p,v_n`$, and potential $`\phi`$, satisfying
```math
\begin{aligned}
p_t+\nabla\!\cdot(pv_p)&=0,&pv_p&=-\nabla(p\theta)-p\nabla\phi,\\
n_t+\nabla\!\cdot(nv_n)&=0,&nv_n&=-\nabla(n\theta)+n\nabla\phi,\\
-\Delta\phi&=p-n,&\phi(x,t)&\longrightarrow0\quad(|x|\to\infty),\\
c(p+n)\theta_t+c(pv_p+nv_n)\!\cdot\nabla\theta
&=\Delta\theta+p|v_p|^2+n|v_n|^2-p\theta\nabla\!\cdot v_p-n\theta\nabla\!\cdot v_n.
\end{aligned}
```
Assume $`p_0-1,n_0-1,\theta_0-1\in C_c^\infty(\mathbb R^3)`$ and $`\min(p_0,n_0,\theta_0)\ge\eta>0`$. Their amplitude is unrestricted. The initial potential is determined by the decaying Newtonian solution of $`-\Delta\phi_0=p_0-n_0`$.

**Question.** Does the unique local positive classical solution extend for all time? In a continuation formulation, can one establish for every finite $`T`$ both
```math
\sup_{0\le t\le T}\left(\|(p-1,n-1,\theta-1)(t)\|_{H^2}+\|\nabla\phi(t)\|_{L^2}\right)<\infty,
\qquad
\inf_{\mathbb R^3\times[0,T]}\min(p,n,\theta)>0?
```
A finite-time loss of regularity or positivity for such data would answer the question negatively.

## Application

The model describes ionic transport coupled to temperature, including electrothermal heating. Its established global theorem requires sufficiently small perturbations of $`(1,1,1)`$. The arbitrary-data problem is explicitly identified in the source's concluding remarks. The class above fixes a smooth strictly positive subclass of that question.

## References

1. C.-Y. Hsieh, T.-C. Lin, C. Liu and P. Liu, *Global existence of the non-isothermal Poisson–Nernst–Planck–Fourier system*, Journal of Differential Equations **269** (2020), 7287–7310, [DOI](https://doi.org/10.1016/j.jde.2020.05.037). [Primary arXiv v1](https://arxiv.org/pdf/2001.08393v1): equation (11), PDF page 6; normalized coefficients and Theorem 1, page 7; explicit open direction, Section 6, page 19.

2. N. Jiang, Y.-L. Luo and X. Zhang, *Stability of equilibria to the model for non-isothermal electrokinetics*, Communications in Mathematical Sciences **19** (2021), 687–720. [DOI](https://doi.org/10.4310/CMS.2021.v19.n3.a6), [primary preprint](https://arxiv.org/abs/1910.04094).
3. N.-A. Lai, C. Liu and A. Tarfulea, *Positivity of temperature for some non-isothermal fluid models*, [primary preprint](https://arxiv.org/abs/2011.07192).

## Status review


**Known cases:** The PNP-Fourier system here has Joule heating and compression terms, arbitrary positive compact perturbations and free-space electrostatics. Small-equilibrium, passive-heat torus and weak compressible-fluid results do not establish its arbitrary-data positive classical continuation.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The PNP-Fourier system here has Joule heating and compression terms, arbitrary positive compact perturbations and free-space electrostatics. Small-equilibrium, passive-heat torus and weak compressible-fluid results do not establish its arbitrary-data positive classical continuation.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.jde.2020.05.037); [comparison source 2](https://arxiv.org/pdf/2001.08393v1); [comparison source 3](https://doi.org/10.4310/CMS.2021.v19.n3.a6); [comparison source 4](https://arxiv.org/abs/1910.04094); [comparison source 5](https://arxiv.org/abs/2011.07192); [comparison source 6](https://arxiv.org/abs/2608.21640). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. The general small-equilibrium theorem of [Jiang–Luo–Zhang](https://arxiv.org/abs/1910.04094) and the conditional scalar temperature principles of [Lai–Liu–Tarfulea](https://arxiv.org/abs/2011.07192) do not give arbitrary-data classical evolution here. The [August 2026 non-isothermal NPNS theorem](https://arxiv.org/abs/2608.21640) concerns a different torus model with a passive heat equation and requires small temperature variation. No matching resolution was located in bounded current searches; the complete cached Prove2Me listing comparison found no matching announcement. An independent scope audit checked all flux and thermal signs, the positivity assumptions and the free-space electrostatic normalization. Compact charge perturbations need not have zero total charge here: their decaying Newtonian potential has an $`L^2`$ gradient.

The [2022 decay result](https://doi.org/10.1007/s10473-022-0315-5) assumes small perturbations. The [2026 nonconstant-equilibrium paper](https://doi.org/10.1016/j.aml.2025.109833) announces evolution near permanent-charge equilibria, rather than arbitrary positive data; its full theorem body remains an access gap. The precise compact-perturbation data class and continuation bounds above make a subclass of the source's broader arbitrary-data question explicit. They are not claimed as an already proved equivalence theorem.

The pinned 2020 preprint was read in full; parity with the complete published version remains unchecked. Current searches and catalogue comparisons are bounded, and no cited proof is independently certified here. See the [source review](../FURTHER_problems/_tracking/parallel/continuum/pnpf-global-positive-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-pnpf-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0980eccbbd8017d8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
