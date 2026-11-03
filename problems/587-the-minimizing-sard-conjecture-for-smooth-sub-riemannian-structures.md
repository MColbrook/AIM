# 587. The minimizing Sard conjecture for smooth sub-Riemannian structures

**Area:** Geometric control and sub-Riemannian geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a smooth connected $`n`$-dimensional manifold without boundary, with $`n\geq3`$. Let $`\Delta\subset TM`$ be a smooth constant-rank distribution of rank $`2\leq m<n`$, whose iterated Lie brackets span every tangent space. Equip $`\Delta`$ with a smooth positive-definite inner product $`g`$.

A horizontal curve is an absolutely continuous curve $`\gamma`$ with $`\dot\gamma(t)\in\Delta_{\gamma(t)}`$ almost everywhere. Let $`d_g`$ be the associated Carnot--Carathéodory distance, obtained by minimizing the length $`\int |\dot\gamma|_g\,dt`$ of horizontal curves, and assume that $`(M,d_g)`$ is complete.

For $`x\in M`$, let $`\Omega_x`$ be the Hilbert manifold of horizontal $`W^{1,2}`$ curves $`\gamma:[0,1]\to M`$ with $`\gamma(0)=x`$. The endpoint map is
```math
E_x:\Omega_x\longrightarrow M,\qquad E_x(\gamma)=\gamma(1).
```

A curve is **singular**, or **abnormal**, when the differential $`D_\gamma E_x`$ is not surjective. Define
```math
\mathrm{Abn}_{\min}(x)=
\left\{\gamma(1):\ \gamma\in\Omega_x,\quad
D_\gamma E_x\text{ is not surjective},\quad
\int_0^1 |\dot\gamma(t)|_g^2\,dt=d_g(x,\gamma(1))^2\right\}.
```

The energy equality selects constant-speed, globally length-minimizing curves on the unit time interval.

**Must $`\mathrm{Abn}_{\min}(x)`$ have measure zero for every smooth positive volume density on $`M`$, for every such structure and every $`x\in M`$?**

The measure here is ordinary manifold volume, equivalently Lebesgue measure in smooth coordinate charts. The question includes singular minimizers that are also normal; it is not restricted to strictly abnormal curves. No analyticity, equiregularity, genericity, or additional regularity of minimizing curves is assumed.

## Application

For a system with nonholonomic constraints, a singular path can evade the usual first-order endpoint tests. This question asks how much volume can be occupied by destinations of such paths when they also minimize travel length. It concerns the exceptional set relevant to sub-Riemannian distance geometry and optimal motion planning.

## References

1. A. A. Agrachev, *Some open problems*, [arXiv:1304.2590v2, 12 April 2013](https://arxiv.org/abs/1304.2590v2), Section III, second question, concerning optimal singular curves. This establishes eligibility before February 2022.
2. Z. Badreddine and L. Rifford, *Measure contraction properties for two-step analytic sub-Riemannian structures and Lipschitz Carnot groups*, Annales de l'Institut Fourier **70** (2020), no. 6, 2303–2330. [DOI:10.5802/aif.3362](https://doi.org/10.5802/aif.3362), Section 2.1, Definition 2.1. Gives the complete-structure formulation and the displayed energy condition.
3. L. Rifford, *Subdifferentials and minimizing Sard conjecture in sub-Riemannian geometry*, Journal de l'École polytechnique — Mathématiques **10** (2023), 1195–1244. [DOI:10.5802/jep.242](https://doi.org/10.5802/jep.242), introduction, Theorem 1.1 and Corollaries 1.2–1.4.
4. A. Lerario, L. Rizzi and D. Tiberio, *A sub-Riemannian endpoint map with no regular values*, [arXiv:2609.05991v1, 5 September 2026](https://arxiv.org/abs/2609.05991v1), Section 6, Proposition 6.1.
5. B. Wang and I. Zelenko, *An equiregular counterexample to the Sard conjecture for sub-Riemannian endpoint maps*, [arXiv:2610.24080v1, 16 October 2026](https://arxiv.org/abs/2610.24080v1), introduction following Theorem 1.3.

6. A. Belotto da Silva, A. Parusiński and L. Rifford, *The analytic minimal rank Sard Conjecture*, [arXiv:2208.01392v2, 13 January 2025](https://arxiv.org/html/2208.01392v2), Theorem 1.1 and Corollary 1.2. These require real analyticity and the stated splittability condition.

## Status review


**Known cases:** Known Goh-rank/corank/generic cases and analytic variants do not settle arbitrary smooth minimizing Sard. The September and October endpoint-map counterexamples explicitly distinguish nonminimizing abnormal curves from this minimizing assertion.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Reviewed independently on 23 October 2026 against the exact primary definitions, current announcement scopes and all-status problem statements.

Rifford's 2023 paper proves the minimizing Sard property under a sufficient condition on the Goh-rank of minimizing curves. Its corollaries include pre-medium-fat distributions almost everywhere, in particular smooth bracket-generating distributions of corank at most two, and generic distributions. These hypotheses leave the stated general smooth problem open.

AIM 123 concerns endpoints of **all** singular curves, without the length-minimizing restriction. The September 2026 counterexample to that assertion explicitly proves in Proposition 6.1 that its structure satisfies the minimizing Sard property for every smooth sub-Riemannian metric. The October equiregular counterexample explicitly states after Theorem 1.3 that it does not address minimizing Sard. Neither announcement is a counterexample to this question. AIM 124 asks for continuous velocity of minimizing curves, a different conclusion.

The bounded current literature search did not locate a proof, counterexample or announced complete resolution of the displayed minimizing assertion. The current OpenAI manuscript map and the inspected Prove2Me analysis and calculus-of-variations pages yielded no matching target. These comparisons do not certify the complete proofs of the cited announcements or the whole Prove2Me catalogue. Exact primary passages, source-byte pins, search queries and duplicate comparisons are recorded in the accompanying evidence and owner receipts.


### Online recheck, 2026-10-30

Known Goh-rank/corank/generic cases and analytic variants do not settle arbitrary smooth minimizing Sard. The September and October endpoint-map counterexamples explicitly distinguish nonminimizing abnormal curves from this minimizing assertion.

Comparators and current-status sources: [status source 1](https://doi.org/10.5802/jep.242); [status source 2](https://arxiv.org/abs/2609.05991); [status source 3](https://arxiv.org/abs/2610.24080). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-0e6d1b6203869b84** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
