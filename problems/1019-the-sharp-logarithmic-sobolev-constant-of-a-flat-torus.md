# 1019. The sharp logarithmic Sobolev constant of a flat torus

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`T=\mathbb R^n/\Lambda`$ be any flat torus of dimension $`n\geq2`$, with normalized Riemannian volume measure $`\mu`$ and Dirichlet form $`\mathcal E(f,f)=\int_T|\nabla f|^2\,d\mu`$. Write

```math
\lambda(T)=\inf_{\mathrm{Var}_\mu(f)>0}\frac{\mathcal E(f,f)}{\mathrm{Var}_\mu(f)},\qquad
\alpha(T)=\inf_{\mathrm{Ent}_\mu(f^2)>0}\frac{\mathcal E(f,f)}{\mathrm{Ent}_\mu(f^2)},
```


where $`\mathrm{Ent}_\mu(f^2)=\int_T f^2\log(f^2/\int_Tf^2\,d\mu)\,d\mu`$. Is $`\alpha(T)=\lambda(T)/2`$ for **every** full-rank lattice $`\Lambda`$? If equality fails, determine the sharp $`\alpha(T)`$ in terms of the lattice [1, printed p. 242, (Q1)].

## Application

The constant $`\alpha`$ gives the sharp logarithmic Sobolev inequality and the corresponding hypercontractivity rate of heat flow, while $`\lambda`$ controls $`L^2`$ relaxation. Equality is known for rectangular products through the circle inequality and tensorization [1, Section 1.2]; the question concerns arbitrary, including skew, lattices. A later problem about uniform comparison $`c\lambda\leq\alpha`$ on all flat tori is weaker and does not determine this sharp identity [2, Section 3.4]. Recent sharp results for **finite cycles and the circle** concern discrete or one-dimensional spaces [3], not arbitrary skew tori of dimension at least two.

## References

1. G.-Y. Chen, W.-W. Liu and L. Saloff-Coste, [*The logarithmic Sobolev constant of some finite Markov chains*](https://www.numdam.org/item/10.5802/afst.1183.pdf), *Ann. Fac. Sci. Toulouse Math.* **17** (2008), no. 2, 239–290, DOI: [10.5802/afst.1183](https://doi.org/10.5802/afst.1183), equations (1.1)–(1.3), printed p. 242, (Q1).
2. L. Saloff-Coste, [*Analysis on compact Lie groups of large dimension and on connected compact groups*](https://pi.math.cornell.edu/~lsc/papers/hulancoll.pdf), *Colloq. Math.* **118** (2010), no. 1, 183–199, DOI: [10.4064/cm118-1-10](https://doi.org/10.4064/cm118-1-10), Section 3.4, Problem 11 and rectangular-torus discussion.
3. L. Chen, N. Lam and G. Lu, [*Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*](https://arxiv.org/abs/2610.05347), preprint (2026), abstract.

## Status review


**Known cases:** Every full-rank lattice is needed. Rectangular products, finite cycles and complete modified log-Sobolev inequalities do not determine the ordinary sharp log-Sobolev constant for arbitrary skew tori.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every full-rank lattice is needed. Rectangular products, finite cycles and complete modified log-Sobolev inequalities do not determine the ordinary sharp log-Sobolev constant for arbitrary skew tori.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [bounded audit](../FURTHER_problems/_tracking/flat-torus-log-sobolev-status-2026-10-22.json) checks the exact original continuous-torus question, a later author survey, targeted proof/counterexample announcements, and local semantic duplicates through 22 October 2026. No all-flat-tori determination was located.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7efe90517bc81620**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
