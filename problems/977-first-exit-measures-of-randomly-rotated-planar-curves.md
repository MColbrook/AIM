# 977. First-exit measures of randomly rotated planar curves

**Area:** Probability, geometric measure theory and planar geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\gamma:[0,\infty)\to\mathbb R^2`$ be continuous, with $`\gamma(0)=0`$ and unbounded image. Let $`\Omega\subset\mathbb R^2`$ be nonempty, bounded, open and simply connected. No simplicity or rectifiability of the curve, or regularity of the boundary, is assumed.

For $`z\in\Omega`$ and rotation $`R_\theta`$, define

```math
\tau_z(\theta)=\inf\{t\ge0:z+R_\theta\gamma(t)\notin\Omega\},\qquad
H_z(\theta)=z+R_\theta\gamma(\tau_z(\theta)).
```

Continuity and unboundedness make $`0<\tau_z(\theta)<\infty`$ and $`H_z(\theta)\in\partial\Omega`$. Let $`\mu_z`$ be the law of $`H_z(\Theta)`$ when $`\Theta`$ is uniform on $`[0,2\pi)`$.

Must

```math
\dim_{\mathrm H}\mu_z\le1
\quad\text{for Lebesgue-almost every }z\in\Omega?
```

Here $`\dim_{\mathrm H}\mu=\inf\{\dim_{\mathrm H}E:E\text{ Borel},\ \mu(E)=1\}`$. The full-measure carrier may depend on $`z`$, and the exceptional roots may depend on $`\gamma,\Omega`$.

## Application

This asks how concentrated boundary exit locations must be when the only randomness is the orientation of a prescribed path. It extends a familiar dimension phenomenon for Brownian harmonic measure to a much wider class of paths.

## References

1. I. Benjamini and A. Shamov, [Where does a random process hit a fractal barrier?](https://arxiv.org/pdf/1608.00505v2), §2 and Question2.2, pp.1–2. Published in *Electronic Communications in Probability* **23** (2018), article25, 1–5, DOI [10.1214/18-ECP131](https://doi.org/10.1214/18-ECP131).
2. T. Orponen and A. Rutar, [Visibility problem in the plane](https://arxiv.org/html/2606.06965v2) (2026), Definition1.1 and Question1.4. A nearby question about dimensions of entire visible sets.

## Status review


**Known cases:** The dimension is that of a full carrier of the first-exit probability measure for almost every root. The recent visible-set dimension construction does not control this exit law, and singularity alone is weaker.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The dimension is that of a full carrier of the first-exit probability measure for almost every root. The recent visible-set dimension construction does not control this exit law, and singularity alone is weaker.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

This is the stronger dimension question, rather than the source’s separate singularity conjecture. It concerns the dimension of an exit probability measure, not the whole boundary or its topological support. The 2026 visible-set counterexample in [2] does not directly settle this measure question.

Bounded resolution, announcement and semantic duplicate checks through 29 October 2026 found no matching completion. The latest archived source v2 was read. The published typeset body was inaccessible and was not claimed checked.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-54f55e1377e018e7**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
