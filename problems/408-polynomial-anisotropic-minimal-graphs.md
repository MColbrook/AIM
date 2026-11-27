# 408. Polynomial anisotropic minimal graphs in dimensions four and five

**Area:** Quasilinear elliptic PDEs / crystalline surface energy

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-11-27

## Problem statement

Does there exist $`n\in\{4,5\}`$, a non-affine real polynomial $`u`$ on $`\mathbb R^n`$, and a positive even integrand $`\Phi\in C^{2,1}(S^n)`$ whose positively one-homogeneous extension to $`\mathbb R^{n+1}\setminus\{0\}`$ has uniformly convex level sets, such that

```math
\mathop{\mathrm{div}}\nolimits\big(D F(\nabla u)\big)=0\quad\text{on }\mathbb R^n,\qquad F(p)=\Phi((-p,1))?
```

Here uniform convexity means that $`D^2\Phi(\nu)`$ restricted to $`\nu^\perp`$ is positive definite with a positive lower bound uniform over $`\nu\in S^n`$.

## Application

Anisotropic surface energies describe orientation-dependent interface tension in crystals. A polynomial equilibrium would provide an exact nonplanar model in the lowest dimensions where Bernstein rigidity can fail.

## References

1. C. Mooney, *Bernstein theorems for nonlinear geometric PDEs*, survey (2024), §7.2, polynomial solutions in lower dimensions. [Author PDF](https://www.math.uci.edu/~mooneycr/BernsteinTheorems_v5.pdf).
2. C. Mooney, *Entire solutions to equations of minimal surface type in six dimensions*, Journal of the European Mathematical Society 24 (2022), 4353–4361, §1 and Theorem 1.1. [DOI](https://doi.org/10.4171/JEMS/1202); [Author PDF](https://www.math.uci.edu/~mooneycr/Bernstein_6D_JEMS.pdf).
3. C. Mooney and Y. Yang, *The anisotropic Bernstein problem*, Inventiones mathematicae 235 (2024), 211–232, construction of nonpolynomial four-dimensional examples. [Publisher manuscript](https://par.nsf.gov/servlets/purl/10511787).

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The six-dimensional polynomial construction uses a C2,1 integrand, so that regularity is fixed explicitly here. The four-dimensional Bernstein counterexamples have subquadratic growth and do not supply a polynomial. September 2026 arXiv:2609.08972 proves a lower growth gap; August 2026 arXiv:2608.29117 concerns integrands close to isotropic area. Neither settles polynomial existence for arbitrary uniformly elliptic integrands in dimensions four or five. No matching resolution was located through 22 September 2026.

**Proposed resolution (2026-11-27):** Affine rigidity for entire polynomial graphs in the stated class in both dimensions. Theorem 1 gives the complete claim in the [manuscript](../research/solutions/408-polynomial-anisotropic-minimal-graphs/paper.pdf). The [target comparison and review scope](../research/solutions/408-polynomial-anisotropic-minimal-graphs/TARGET-COMPARISON.md) identify the proof's coverage and the AI-assisted review. Independent mathematical review is requested.
