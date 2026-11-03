# 855. Does Pu’s sharp systolic bound hold for every nonfree two-complex?

**Area:** Systolic geometry and geometric topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a finite connected two-dimensional simplicial complex whose fundamental group is not free. Equip each two-simplex with a compatible piecewise smooth Riemannian metric $`g`$. Let $`\mathrm{sys}_{\pi_1}(X,g)`$ be the length of its shortest noncontractible closed curve, and let $`\mathrm{area}(X,g)`$ be the sum of the areas of its two-simplices.

**Must every such $`(X,g)`$ satisfy**

```math
\frac{\mathrm{sys}_{\pi_1}(X,g)^2}{\mathrm{area}(X,g)}\leq\frac{\pi}{2}\,?
```


Equivalently, the systolic area $`\sigma(X)=\inf_g\mathrm{area}(X,g)/\mathrm{sys}_{\pi_1}(X,g)^2`$ should be at least $`2/\pi`$. The real projective plane attains this constant, so it cannot be improved universally.

## Application

The systole measures the shortest loop detecting nontrivial topology. A sharp universal bound would show that no singular two-dimensional complex with nonfree fundamental group can pack such a loop more efficiently than the projective plane.

## Known results and scope

Rudyak and Sabourau [1, Question 1.5] pose precisely this extension of Pu’s inequality and prove the weaker universal bound $`\mathrm{sys}_{\pi_1}^2/\mathrm{area}\leq16/\pi`$ [1, Theorem 1.4]. Babenko and Moulla [2, printed pp. 201–202] restate the sharp target as open and explain its equivalent group-level formulation. Babenko’s later survey [3, Conjecture 3.6] again calls the $`2/\pi`$ lower bound unverified; it reports a universal lower bound $`\sigma(X)\geq1/4`$. Results for special classes of groups [4] do not establish the bound for every nonfree fundamental group. The survey’s additional strictness conjecture for most groups is stronger and is outside the present question.

## References

1. Y. B. Rudyak and S. Sabourau, [*Systolic invariants of groups and 2-complexes via Grushko decomposition*](https://www.numdam.org/item/10.5802/aif.2369.pdf), *Annales de l’Institut Fourier* **58** (2008), no. 3, 777–800, doi:10.5802/aif.2369; Theorem 1.4 and Question 1.5, printed p. 780.
2. I. Babenko and T. Moulla, [*The Karoubi–Weibel complexity for groups*](https://ems.press/content/serial-article-files/47666?nt=1), *L’Enseignement Mathématique* **70** (2024), 197–230, doi:10.4171/LEM/1041; printed pp. 201–202.
3. I. K. Babenko, [*Differential geometry on finitely presented groups and related combinatorial invariants*](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=10232&what=fullteng), *Russian Mathematical Surveys* **80** (2025), no. 2, 183–226, doi:10.4213/rm10232e; Conjecture 3.6.
4. E. Borghini, [*A systolic inequality for 2-complexes of maximal cup-length and systolic area of groups*](https://arxiv.org/abs/1909.12720), *Journal of Geometric Analysis* **34** (2024), article 253; special-class results.

## Status review


**Known cases:** Known universal systolic-area lower bounds and cup-length special cases do not reach the sharp 2/pi bound for every nonfree two-complex. The real projective plane establishes sharpness if the inequality holds, not the universal upper estimate on systolic ratio.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Known universal systolic-area lower bounds and cup-length special cases do not reach the sharp 2/pi bound for every nonfree two-complex. The real projective plane establishes sharpness if the inequality holds, not the universal upper estimate on systolic ratio.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source, later-result and duplicate audit](../FURTHER_problems/_tracking/pu-sharp-systolic-two-complex-status-2026-10-21.json) checks the exact constants, later open restatements, related partial results and matching AIM/FURTHER entries. Bounded searches found no complete proof, counterexample or announced resolution through 21 October 2026; they cannot exclude unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e1d9a5c67a240d20**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
