# 851. Can a small $`C^1`$ perturbation make any prescribed orbit asymptotic to a hyperbolic periodic orbit?

**Area:** Smooth dynamical systems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a compact smooth manifold, $`f\in\mathrm{Diff}^1(M)`$, $`x\in M`$, and $`\mathcal U`$ any $`C^1`$ neighborhood of $`f`$. Does there exist $`g\in\mathcal U`$ and a hyperbolic periodic orbit $`\mathcal O`$ of $`g`$ such that $`x\in W^s_g(\mathcal O)`$?

Crovisier additionally asks whether $`g`$ can be chosen so that the closures of the forward $`f`$- and $`g`$-orbits of $`x`$ are arbitrarily close in Hausdorff distance, and whether $`\mathcal O`$ is arbitrarily close to $`\omega_f(x)`$. These are stronger requests; a result for almost every $`x`$, generic $`f`$, or a special class of surfaces would not answer the stated universal question.

## Application

The usual $`C^1`$ closing and connecting lemmas control finite pieces of trajectories. An asymptotic version would control their limiting behavior and, as Crovisier notes, imply density of stable and unstable manifolds of hyperbolic periodic orbits for generic $`C^1`$ diffeomorphisms. It is also linked in the source to the tolerance-stability conjecture.

## References

- S. Crovisier, [*Perturbation de la dynamique de difféomorphismes en topologie $`C^1`$*](https://www.numdam.org/item/AST_2013__354__R1_0/), *Astérisque* **354** (2013), Question 5.12, printed p. 50 (PDF p. 61).
- S. Crovisier, [*Periodic orbits and chain-transitive sets of $`C^1`$-diffeomorphisms*](https://doi.org/10.1007/s10240-006-0002-4), *Publ. Math. IHÉS* **104** (2006), 87–141, Problem 1 on printed p. 94. This is an earlier formulation of the same question.
- S. Crovisier and E. Pujals, [*Strongly dissipative surface diffeomorphisms*](https://doi.org/10.4171/CMH/438), *Comment. Math. Helv.* **93** (2018), 377–400. Its closing result concerns a restricted class of surface maps and does not provide the universal prescribed-point stable-capture assertion.

## Status review


**Known cases:** The ergodic/asymptotic closing statements give frequency-one closability or exponent approximation for almost every point, rather than stable capture of every prescribed point after an arbitrarily small C1 perturbation. Generic and dissipative-surface results do not cover the universal statement.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The ergodic/asymptotic closing statements give frequency-one closability or exponent approximation for almost every point, rather than stable capture of every prescribed point after an arbitrarily small C1 perturbation. Generic and dissipative-surface results do not cover the universal statement.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Crovisier posed this explicitly in 2006 and repeated it in 2013. Bounded searches through 22 October 2026 compared later primary work on special dissipative maps and partial hyperbolicity. A 2019 talk entitled “An asymptotic closing lemma and its applications” could easily be mistaken for a resolution, but [Hayashi's own 2018](https://www.ms.u-tokyo.ac.jp/activity/documents/AnnualReport2018.pdf) and [2019](https://www.ms.u-tokyo.ac.jp/activity/documents/AnnualReport2019.pdf) research summaries describe a frequency-one strongly-closable-points result and Lyapunov-exponent approximation, rather than stable capture of every prescribed point or the two Hausdorff controls. No exact later complete theorem or announced counterexample was located; this is a bounded check, not exhaustive certification. The [source-body receipt](../FURTHER_problems/_tracking/parallel/continuum/cached-broad-books-body-continuation-0273-review.json), [independent current-scope comparison](../FURTHER_problems/_tracking/parallel/continuum/crovisier-asterisque354-question5-12-current-scope-independent-2026-10-22.json), [coordinator status addendum](../FURTHER_problems/_tracking/crovisier-asymptotic-closing-status-2026-10-22.json) and [duplicate check](../FURTHER_problems/_tracking/crovisier-asymptotic-closing-duplicates-2026-10-22.json) record the limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dcb91827f27e16b8**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
