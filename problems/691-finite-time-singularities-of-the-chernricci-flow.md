# 691. Finite-time singularities of the Chern–Ricci flow

**Area:** Complex analysis, geometric analysis and nonlinear PDEs
**Status:** ✅ SOLVED
**Last checked:** 2026-11-07

## Problem statement

Let $`X`$ be a connected compact complex manifold of complex dimension $`n\ge2`$, with an arbitrary smooth Hermitian metric $`\omega_0`$. Let $`\omega(t)`$ be its maximal smooth Chern–Ricci flow

```math
\partial_t\omega(t)=-\mathrm{Ric}^{\mathrm{Ch}}(\omega(t)),\qquad \omega(0)=\omega_0,
```


on $`[0,T)`$, where $`0<T<\infty`$. In holomorphic coordinates, $`\mathrm{Ric}^{\mathrm{Ch}}(\omega)=-i\partial\bar\partial\log\det(g)`$ for $`\omega=i g_{j\bar k}\,dz_j\wedge d\bar z_k`$.

Define the singular set $`\Sigma`$ as the complement of points admitting a neighborhood $`U`$ on which $`\omega(t)`$ converges locally smoothly, as $`t\uparrow T`$, to a smooth positive Hermitian metric. For each irreducible closed analytic subvariety $`V\subseteq X`$ of positive complex dimension $`k`$, set

```math
\mathrm{Vol}_t(V)=\frac1{k!}\int_V\omega(t)^k,
\qquad
\Sigma_0=\bigcup_{\mathrm{Vol}_t(V)\to0\text{ as }t\uparrow T} V.
```


Integration is over the regular locus of $`V`$, equivalently against its integration current, and $`V=X`$ is allowed. Must

```math
\Sigma=\Sigma_0,
```


and must this common set be a closed complex analytic subvariety of $`X`$? No Kähler, Gauduchon or mass-bound hypothesis is imposed.

## Application

The question asks whether the degeneration of this nonlinear metric flow occurs precisely along collapsing analytic subvarieties. It would extend a geometric description of Kähler–Ricci singularities to Hermitian metrics that need not be closed.

## References

1. V. Tosatti and B. Weinkove, *The Chern–Ricci flow*, [arXiv:2107.12928v3](https://arxiv.org/pdf/2107.12928v3), §6, pp.18–19, Conjecture/Question 6.1. Published in *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* **33** (2022), 73–107, [DOI](https://doi.org/10.4171/RLM/965). The pinned preprint was reviewed.
2. Q.-T. Dang, *Singularities of the Chern–Ricci flow*, *Analysis & PDE* **19** (2026), 449–483, Question 1.1 and Theorem A. [Published PDF](https://msp.org/apde/2026/19-3/apde-v19-n3-p02-s.pdf).
3. Q.-T. Dang, *Hermitian null loci*, [arXiv:2404.01126v2](https://arxiv.org/pdf/2404.01126v2), Theorem C and Theorem 4.7, pp.4 and20–21.

## Status review

### Reviewed manuscript, 2026-11-07

Matthew J. Colbrook provides the following AI-found [manuscript](../research/solutions/691-finite-time-singularities-of-the-chernricci-flow/main.pdf). Counterexample to the analyticity conclusion: the collapsing-subvariety locus is nonanalytic for an admissible Hermitian flow.

The conclusion concerns exactly the catalogue target; no historical priority claim is made.

**Review:** The [separate Codex AI audit](../research/solution_reviews/2026-11-07-complex-analysis/691-review.md) checks the complete argument against this exact target and records the primary-source comparisons. No unresolved mathematical gap was identified in the complete resolution. The results were found by AI; human peer review and formal verification are not claimed.

### Earlier status record (historical)

The following dated record describes the pre-submission state.



**Previously recorded known cases:** The Hermitian null-locus results impose lower-volume and metric or bounded-mass hypotheses. Kähler surface Type I theorems and Chern holonomy flows do not settle arbitrary Hermitian finite-time singularities.

**Previously recorded remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The Hermitian null-locus results impose lower-volume and metric or bounded-mass hypotheses. Kähler surface Type I theorems and Chern holonomy flows do not settle arbitrary Hermitian finite-time singularities.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The inclusion $`\Sigma_0\subseteq\Sigma`$ is elementary. The question is settled when the total volume tends to zero, when the initial metric is Kähler, and for complex surfaces with Gauduchon initial metrics. Reference 3 gives further cases under a positive limiting lower Monge–Ampère mass condition and dimensional or torsion assumptions. Those extra hypotheses do not establish the unrestricted conclusion above.

Current literature and announcement searches on 17 October 2026 found no complete resolution of this target. An independent selected-primary audit checked the locus definitions, the whole-manifold case, the analytic-set conclusion and the hypotheses of the current partial results. In particular, positive actual flow volume is not silently identified with a positive uniform lower Monge–Ampère mass.

All-status AIM/OpenAI and Prove2Me listing-description comparisons found no matching announcement. The two returned catalogue contexts concern a plasma reference and winding bookkeeping. The 2022 published survey and accepted final TAMS edition have not been checked for parity with the pinned preprints; the published 2026 source explicitly retains the general question. These bounded status checks do not certify every cited proof. See the [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/chern-singular-locus-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-chern-singular-locus-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-69298731684a197e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
