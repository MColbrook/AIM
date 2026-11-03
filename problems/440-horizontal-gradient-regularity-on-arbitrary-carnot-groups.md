# 440. Horizontal gradient regularity on arbitrary Carnot groups

**Area:** Partial differential equations and regularity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix a finite-dimensional Carnot group $`G`$, a positive inner product on its first Lie-algebra layer $`V_1`$, and $`1<q<\infty`$. Thus $`G`$ is connected and simply connected, with stratified nilpotent Lie algebra $`V_1\oplus\cdots\oplus V_s`$, where $`[V_1,V_j]=V_{j+1}`$ and $`s`$ is any finite step. Let $`X_1,\ldots,X_m`$ be the associated orthonormal left-invariant horizontal fields, $`\mu`$ Haar measure, and $`d_{CC}`$ their Carnot–Carathéodory distance.

For any open $`\Omega\subset G`$, consider a real scalar function $`u`$ with $`u,X_1u,\ldots,X_mu\in L^q_{\mathrm{loc}}(\Omega)`$, satisfying
```math
\int_\Omega |Xu|^{q-2}\sum_{j=1}^{m}(X_ju)(X_j\phi)\,d\mu=0
\qquad(\phi\in C_c^\infty(\Omega)),
```

where $`Xu=(X_1u,\ldots,X_mu)`$ and the flux is zero at $`Xu=0`$.

Does there exist $`\alpha\in(0,1)`$, depending only on the fixed group, inner product and $`q`$, such that **every** such solution has a locally Hölder continuous horizontal gradient with respect to $`d_{CC}`$? Precisely, can representatives be chosen so that for each compact $`K\subset\Omega`$,
```math
|Xu(x)-Xu(y)|\leq C_{u,K}\,d_{CC}(x,y)^\alpha
 \qquad(x,y\in K)
```

with finite $`C_{u,K}`$?

## Application

The horizontal energy $`\int|Xu|^q`$ models nonlinear potentials with derivatives restricted to admissible directions. Regularity of the associated horizontal field underpins nonlinear capacity and geometric analysis in these constrained spaces.

## References

- F. Dragoni, N. Garofalo and P. Salani, *Starshapedeness for fully-nonlinear equations in Carnot groups*, J. London Math. Soc. **99** (2019), 901–918, [DOI](https://doi.org/10.1112/jlms.12198). [Primary v2](https://arxiv.org/html/1804.00765v2), **§3.2**, equation (17) and subsequent open question.
- L. Capogna, G. Citti and X. Zhong, *Regularity theory of quasilinear elliptic and parabolic equations in the Heisenberg group*, Vietnam J. Math. **52** (2024), 807–827, [DOI](https://doi.org/10.1007/s10013-023-00644-0). [Primary v2](https://arxiv.org/html/2212.10605v2), **§8(i)**.
- G. Citti and S. Mukherjee, *Regularity of quasi-linear equations with Hörmander vector fields of step two*, Adv. Math. **408** (2022), 108593, [DOI](https://doi.org/10.1016/j.aim.2022.108593). [Primary v4](https://arxiv.org/html/2110.04377v4), **Theorem 1.3**.

- S. Zheng and Z. Feng, *Regularity of subelliptic p-harmonic systems with subcritical growth in Carnot group*, J. Differential Equations **258** (2015), 2471–2494, [DOI](https://doi.org/10.1016/j.jde.2014.12.020), restricted-exponent/Cordes setting.

## Status review


**Known cases:** The arbitrary-step, all-exponent horizontal-gradient assertion remains beyond step-two/Heisenberg and restricted-exponent Riemannian-approximation theorems. Current searches found no complete arbitrary-Carnot resolution.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

**Partial progress; the universal question remains open in searches checked 28 October 2026.** Linear $`q=2`$, Euclidean, Heisenberg and all step-two cases are known. Restricted-exponent/Cordes results provide further partial cases. The 2023 survey explicitly retains the general Carnot-group problem; searches found no complete general resolution or announced solution.

The conclusion concerns the **horizontal** gradient and the control metric. It does not require full Euclidean differentiability, vector-valued system regularity, boundary regularity or a sharp exponent. AIM 124 concerns regularity of minimizing horizontal curves, a different object. All-status AIM and private semantic checks found no equivalent target.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-general-Carnot-q-harmonic-horizontal-gradient-C217-C-20261028/OWNER-EXACT-SCALAR-HORIZONTAL-Q-HARMONIC-CC-GRADIENT-HOLDER-ALL-CARNOT-GROUPS-PRIMARY-PARTIALS-CURRENT-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-general-Carnot-q-harmonic-horizontal-gradient-C217-C-20261028/A-INDEPENDENT-SCALAR-HORIZONTAL-GRADIENT-CC-METRIC-AND-STEP2-SCOPE-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-general-Carnot-q-harmonic-horizontal-gradient-C217-C-20261028/ROOT-EXACT-SCALAR-CARNOT-HORIZONTAL-GRADIENT-PRIMARY-PARTIALS-CURRENT-FINAL-REVIEW.json).


### Online recheck, 2026-10-30

The arbitrary-step, all-exponent horizontal-gradient assertion remains beyond step-two/Heisenberg and restricted-exponent Riemannian-approximation theorems. Current searches found no complete arbitrary-Carnot resolution.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2212.10605); [status source 2](https://arxiv.org/abs/2110.04377); [status source 3](https://doi.org/10.6092/issn.2240-2829/10589). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-99602011c336bf91** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
