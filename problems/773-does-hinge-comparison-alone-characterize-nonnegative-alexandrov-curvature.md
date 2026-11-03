# 773. Does hinge comparison alone characterize nonnegative Alexandrov curvature?

**Area:** Metric geometry and synthetic curvature
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,d)`$ be a complete geodesic metric space: every pair of points can be joined by a distance-minimizing geodesic. For any $`p,x,y\in X`$ with $`p\ne x,y`$, choose any two unit-speed minimizing geodesics
```math
\alpha:[0,a]\to X,\qquad \beta:[0,b]\to X,
\qquad a=d(p,x),\quad b=d(p,y),
```

from $`p`$ to $`x`$ and $`y`$, respectively. Suppose their joint-limit angle exists:
```math
\theta(\alpha,\beta)=
\lim_{\substack{s\downarrow0\\t\downarrow0}}
\arccos\!\left(
\frac{s^2+t^2-d(\alpha(s),\beta(t))^2}{2st}
\right).
```

Assume, for **every such choice** of points and geodesics, that
```math
\theta(\alpha,\beta)\ge
\widetilde\theta_p(x,y):=
\arccos\!\left(
\frac{d(p,x)^2+d(p,y)^2-d(x,y)^2}
{2d(p,x)d(p,y)}
\right).
```


Must $`X`$ have Alexandrov curvature bounded below by zero, denoted $`\mathrm{CBB}(0)`$? Explicitly, must every $`p,x_1,x_2,x_3\in X`$ with $`p\ne x_i`$ satisfy
```math
\widetilde\theta_p(x_1,x_2)+
\widetilde\theta_p(x_2,x_3)+
\widetilde\theta_p(x_3,x_1)\le2\pi?
```


This is Open Question 8.51 in the current author version of [1]. It already appears as Open Question 7.9.1 in the 2019 first version [2]. The assumptions concern all minimizing-geodesic choices and the actual joint limit, rather than only a limiting upper angle. No local compactness, finite dimension, manifold structure or reference measure is imposed.

## Application

Synthetic curvature compares the metric geometry of a space with Euclidean triangles. This problem asks whether the angle test on each hinge already forces the usual four-point lower-curvature condition.

## Known results and scope

The lower angle comparison holds in $`\mathrm{CBB}(0)`$ spaces. A converse is known if one also assumes the adjacent-angle estimate: when two hinges share one side and their other sides together form a minimizing geodesic, their angles have sum at most $`\pi`$ [1, Theorem 8.14(c)]. Removing that additional hypothesis is exactly the question. The source notes that even spaces homeomorphic to $`S^2`$ or $`\mathbb R^2`$ may be considered; those restrictions are not imposed here.

On 1 July 2026, Petrunin described a related pointwise local hinge-comparison question as longstanding open and referred explicitly to Question 8.51 [3]. That answer concerns a local variant, so it is corroboration rather than a claimed equivalence of the two formulations. Results about curvature measures on surfaces of bounded integral curvature, or distributional sectional curvature on finite-dimensional RCD spaces, have additional hypotheses and do not directly settle the stated metric-space problem.

## References

1. S. Alexander, V. Kapovitch and A. Petrunin, *Alexandrov geometry: foundations*, Graduate Studies in Mathematics 236, AMS, 2024; [publisher record](https://doi.org/10.1090/gsm/236), [official book page](https://anton-petrunin.github.io/book/), [current author PDF](https://anton-petrunin.github.io/book/arXiv.pdf). Definitions in Chapters 6 and 8, Theorem 8.14(c), Open Question 8.51, native pages 107–108. The exact author-PDF hash and source windows are recorded in the owner audit.
2. S. Alexander, V. Kapovitch and A. Petrunin, *Alexandrov geometry: preliminary version no. 1*, [arXiv:1903.08539v1](https://arxiv.org/abs/1903.08539v1), submitted 20 March 2019, Open Question 7.9.1, printed page 84 (native PDF page 90). Later versions renumber the question.
3. A. Petrunin, [answer to “Pointwise hinge comparison implies local Alexandrov CBB”](https://mathoverflow.net/a/512790), MathOverflow, 1 July 2026. The answer refers to the book question and to the footnote to 4.1.5 in Burago, Burago and Ivanov, *A Course in Metric Geometry*.

4. OpenAI, [Gigli’s distributional curvature characterization of Alexandrov spaces](https://github.com/openai/math/blob/main/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf), manuscript dated September 2026, Theorems 1.1 and 6.3. This announced characterization assumes finite-dimensional RCD structure, Hausdorff reference measure and distributional sectional curvature; the selected statement comparison does not certify its proof.
5. M. Marot, [On two notions of curvature on singular surfaces](https://arxiv.org/abs/2511.08138v4), v4, 6 August 2026, Theorem 1 and Proposition 4. Its surface and adjacent-angle hypotheses differ from the question here.

## Status review


**Known cases:** All geodesic choices and joint-limit angles are required, without properness, local compactness, dimension or measure assumptions. Adjacent-angle comparison and analytic RCD characterizations add substantive hypotheses; the current Alexandrov foundations source retains the hinge-only question.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

All geodesic choices and joint-limit angles are required, without properness, local compactness, dimension or measure assumptions. Adjacent-angle comparison and analytic RCD characterizations add substantive hypotheses; the current Alexandrov foundations source retains the hinge-only question.

Additional comparison sources: [comparison source 1](https://doi.org/10.1090/gsm/236); [comparison source 2](https://anton-petrunin.github.io/book/); [comparison source 3](https://anton-petrunin.github.io/book/arXiv.pdf); [comparison source 4](https://arxiv.org/abs/1903.08539v1); [comparison source 5](https://mathoverflow.net/a/512790); [comparison source 6](https://github.com/openai/math/blob/main/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/main.pdf); [comparison source 7](https://arxiv.org/abs/2511.08138v4). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Owner source, announcement and all-status duplicate checks are recorded in the companion audit. The exact statements and the missing adjacent-angle hypothesis were checked against source text and native page images. No matching complete resolution or duplicate was located in bounded searches through 23 October 2026.

The independent review also checked the closest announced RCD characterization against its native main and final theorem statements. Its additional analytic and measure hypotheses do not establish the stated hinge-only target. These are bounded source and literature checks; no exhaustive absence claim, website-wide completion or formal proof certification is implied.

The [independent scope review](../FURTHER_problems/_tracking/hinge-only-CBB0-independent-peer-2026-10-23.json) and [duplicate review](../FURTHER_problems/_tracking/hinge-only-CBB0-duplicate-review-2026-10-23.json) record the final checks and their limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-1f0bf4e715d8b6b3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
