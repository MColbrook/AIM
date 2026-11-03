# 1067. Does De Giorgi minimization recover the p-Laplacian telegraph equation?

**Area:** Nonlinear waves and variational evolution
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`n\ge1`$, $`p,q>1`$ with $`p\ne2`$, and put
```math
V=\{v\in L^2(\mathbb R^n):\nabla v\in L^p(\mathbb R^n),\ v\in L^q(\mathbb R^n)\},\qquad
W(v)=\int_{\mathbb R^n}\left(\frac{|\nabla v|^p}{p}+\frac{|v|^q}{q}\right)dx.
```

For arbitrary real $`w_0,w_1\in V`$, let $`w_\varepsilon`$ minimize
```math
F_\varepsilon(w)=\int_0^\infty e^{-t/\varepsilon}
\left[\frac{\varepsilon^2}{2}\|w_{tt}(t)\|_2^2+W(w(t))+
\frac{\varepsilon}{2}\|w_t(t)\|_2^2\right]dt
```

over $`H^2_{\mathrm{loc}}([0,\infty);L^2(\mathbb R^n))`$ with $`w(0)=w_0`$, $`w_t(0)=w_1`$ and finite functional.

Does every sequence $`\varepsilon_j\downarrow0`$ have a subsequence whose minimizers converge weakly in $`H^1_{\mathrm{loc}}([0,\infty);L^2)`$ to a distributional solution of
```math
w_{tt}=\mathrm{div}(|\nabla w|^{p-2}\nabla w)-|w|^{q-2}w-w_t?
```

Retain the prescribed initial traces, with velocity interpreted in $`V'`$, and require
```math
E(t)+\int_0^t\|w_t(s)\|_2^2ds\le E(0)\quad\text{for a.e. }t>0,
\qquad E(t)=\tfrac12\|w_t(t)\|_2^2+W(w(t)).
```

The flux must be $`|\nabla w|^{p-2}\nabla w`$, rather than a measure-valued replacement. This is the unforced model explicitly given in Serra–Tilli, Problem 2 and Examples 4 and 8. Their Theorem 2.5 already provides minimizers, subsequential compactness, initial traces and the energy bound. The missing conclusion is the limiting PDE.

## Application

The equation describes a nonlinear restoring force, a defocusing potential and velocity damping. The question tests whether global space-time minimization constructs the causal wave evolution.

## References

1. E. Serra and P. Tilli, [*A minimization approach to hyperbolic Cauchy problems*](https://ems.press/content/serial-article-files/32146), J. Eur. Math. Soc. **18** (2016), 2019–2044. [DOI](https://doi.org/10.4171/JEMS/637). Problem 2, Theorem 2.5 and Examples 4 and 8.
2. L. Tentarelli and P. Tilli, [*An existence result for dissipative nonhomogeneous hyperbolic equations via a minimization approach*](https://arxiv.org/html/1804.11107), latest v2 (2018), Theorem 2.5, Remark 2.6 and Example 2; J. Differential Equations **266** (2019), 5185–5208. [DOI](https://doi.org/10.1016/j.jde.2018.10.023).
3. U. Stefanelli, [*The Weighted Inertia-Energy-Dissipation Principle*](https://arxiv.org/html/2407.20933), v1 (2024), §§4.5–4.7; published 2025. [DOI](https://doi.org/10.1142/S0218202525400019).
4. G. Akagi, V. Bögelein, A. Marveggio and U. Stefanelli, [*Weighted Inertia-Dissipation-Energy approach to doubly nonlinear wave equations*](https://arxiv.org/html/2401.08856), J. Funct. Anal. **289** (2025), 111067. [DOI](https://doi.org/10.1016/j.jfa.2025.111067).

## Status review


**Known cases:** The missing step is identification of the nonlinear spatial p-Laplacian flux in the minimizer limit. Compactness, traces and energy bounds are known. The 2025 doubly nonlinear result has quadratic spatial energy; added spatial damping changes the equation.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The missing step is identification of the nonlinear spatial p-Laplacian flux in the minimizer limit. Compactness, traces and energy bounds are known. The 2025 doubly nonlinear result has quadratic spatial energy; added spatial damping changes the equation.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2018 source retains this flux-identification question. The 2024 survey describes a linear highest-order spatial operator in the established theory. The 2025 doubly nonlinear wave result also retains a quadratic spatial-gradient energy; its nonlinearities concern damping and the lower-order potential.

Strong spatial damping $`\Delta w_t`$ is a different model. No uniqueness, full-sequence convergence, energy equality or finite-horizon substitution is requested here.

The [existing undamped p-wave entry](413-energy-admissible-weak-solutions-of-the-undamped-hyperbolic-p-laplacian-from-smooth-data.md) asks ordinary weak existence on bounded Dirichlet domains. This entry instead asks convergence of a specified variational approximation for the source-stated weakly damped whole-space model. No equivalence is claimed.

The [coordinating review](../FURTHER_problems/_tracking/focused-DeGiorgi-pLap-telegraph-causal-limit-C174-A-20261028/ROOT-FINAL-SCIENTIFIC-REVIEW.json) records primary, current-announcement and all-status duplicate checks, together with a separate mathematical formulation review. These bounded searches do not prove continued openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-f911b8259b87aede**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
