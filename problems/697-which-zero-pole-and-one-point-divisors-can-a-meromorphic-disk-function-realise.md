# 697. Which zero, pole and one-point divisors can a meromorphic disk function realise?

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`U=\{z\in\mathbb C:|z|<1\}`$. A nonnegative divisor of finite degree on $`U`$ is a finite sum of points of $`U`$ with nonnegative integer multiplicities. Given three such divisors $`D_0,D_\infty,D_1`$, characterize precisely when there is a meromorphic function $`f`$ on $`U`$ whose zero divisor is $`D_0`$, pole divisor is $`D_\infty`$, and divisor of $`1`$-points (zeros of $`f-1`$) is $`D_1`$. Coincident prescriptions that would require $`f`$ to take two distinct values at one point are excluded.

This is the strong interpolation question posed as Problem 1 by Bergweiler and Eremenko. It asks for a complete criterion for arbitrary finite triples, rather than a bound on one of Goldberg's constants or a solution for one small triple.

## Application

The paper links this interpolation question to avoiding graphs of rational functions. That avoidance problem is closely related to simultaneous stabilization of linear systems in feedback control, so a characterization would clarify when a specified collection of forbidden values can be avoided by a single analytic design.

## References

1. W. Bergweiler and A. Eremenko, [*Goldberg's constants*](https://arxiv.org/pdf/1111.2296), *Journal d'Analyse Mathématique* **119** (2013), 365–402, [DOI](https://doi.org/10.1007/s11854-013-0012-3), §1 Problem 1 and Theorem 1.6. The exact question is printed on p. 2; Theorem 1.6 covers only the simplest two-point case.
2. A. Eremenko, [2013 project statement](https://www.math.purdue.edu/~eremenko/dvi/nsf2013q.pdf), section on the strong interpolation question and its relation to avoidance and control.
3. A. Eremenko, [current unsolved-problems index](https://www.math.purdue.edu/~eremenko/uns1.html), Goldberg entry; linked [Goldberg note](https://www.math.purdue.edu/~eremenko/dvi/goldconst.pdf), dated 16 October 2026, discusses related unresolved extremal questions.

## Status review


**Known cases:** The original Bergweiler-Eremenko interpolation problem asks for a criterion for every finite triple of zero, pole and one-point divisors. Special two-point configurations, Goldberg constant estimates and radial-value problems do not give such a characterization.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The original Bergweiler-Eremenko interpolation problem asks for a criterion for every finite triple of zero, pole and one-point divisors. Special two-point configurations, Goldberg constant estimates and radial-value problems do not give such a characterization.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The original paper solves a two-point special case, not the general triple-divisor characterization. A bounded search through 22 October 2026 found no complete later solution or announcement for this exact interpolation question, and no exact AIM or admitted FURTHER duplicate. The [status](../FURTHER_problems/_tracking/goldberg-divisor-interpolation-2026-10-22-status.json) and [duplicate](../FURTHER_problems/_tracking/goldberg-divisor-interpolation-2026-10-22-duplicates.json) audits record the scope of those checks.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-752baacf361ed872**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
