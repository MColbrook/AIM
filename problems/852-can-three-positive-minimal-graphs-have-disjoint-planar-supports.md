# 852. Can three positive minimal graphs have disjoint planar supports?

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D_1,\ldots,D_k`$ be nonempty, connected, unbounded open subsets of $`\mathbb R^2`$, with $`D_i\cap D_j=\varnothing`$ for $`i\ne j`$. Suppose that each real function $`u_i\in C^2(D_i)\cap C^0(\overline{D_i})`$ satisfies

```math
\mathrm{div}\!\left(\frac{\nabla u_i}{\sqrt{1+|\nabla u_i|^2}}\right)=0
\quad\text{in }D_i,
\qquad u_i>0\quad\text{in }D_i,
\qquad u_i=0\quad\text{on }\partial D_i.
```

Must $`k\le2`$? Equivalently, prove that no such triple exists, or construct one. Disjointness concerns the base domains in the plane. No growth, gradient, curvature, simple-connectivity or boundary-smoothness assumption is imposed.

The bound would be sharp: the two half-planes $`D_\pm=\{\pm x_1>0\}`$ support $`u_\pm=\pm x_1`$. Their gradients are constant, so they satisfy the equation and the stated boundary conditions.

## Application

The minimal-surface equation describes equilibria of isotropic surface-area energy. The conjecture asks how many disjoint planar regions can support positive equilibrium graphs whose finite boundary lies at height zero. It concerns continuous geometric PDEs and unbounded interfaces.

## References

1. V. G. Tkachev, [*Disjoint minimal graphs*](https://arxiv.org/abs/0807.3694), arXiv:0807.3694v1 (2008), Section 1, equations (1.1)–(1.3), the Meeks conjecture preceding Theorem 1.1, and Theorem 1.2. Published in *Annals of Global Analysis and Geometry* **35** (2009), 139–155, [doi:10.1007/s10455-008-9127-7](https://doi.org/10.1007/s10455-008-9127-7).
2. A. Weitsman, [*Remarks on the disjoint minimal graphs conjecture*](https://arxiv.org/abs/2610.15736), arXiv:2610.15736v1 (2026), Introduction and Theorems 1–2.
3. A. Benedetti and B. Nelli, [*On Meeks' conjecture on disjoint minimal graphs*](https://arxiv.org/abs/2610.20508), arXiv:2610.20508v1 (2026), Theorems 2.1, 2.4 and 3.1.

## Status review


**Known cases:** The two October 2026 papers remain partial: one treats growth properties for simply connected supports, the other specified slope regimes. These conditions do not exhaust arbitrary hypothetical triples. Vanishing-curvature-at-infinity results impose another omitted hypothesis.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The two October 2026 papers remain partial: one treats growth properties for simply connected supports, the other specified slope regimes. These conditions do not exhaust arbitrary hypothetical triples. Vanishing-curvature-at-infinity results impose another omitted hypothesis.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Tkachev proves the unconditional upper bound three. The remaining question is whether two is the sharp universal bound. Bounded searches of current literature, announced solutions and all-status AIM/FURTHER/OpenAI statements found no matching complete resolution or duplicate.

The October 2026 papers provide substantial partial results. Weitsman derives necessary growth properties for a hypothetical triple on simply connected domains. Benedetti–Nelli exclude families satisfying specified large-slope or small-slope conditions. These hypotheses do not cover every family in the statement above: unspecified solution-dependent linear-growth bounds do not imply the fixed threshold conditions. Neither an unrestricted topology reduction nor an exhaustive growth dichotomy is assumed here.

The original arXiv statement and the current theorem hypotheses were read and independently compared. The final 2009 publication body and Meeks' original chapter formulation were not reconciled; the precise target above is supported by the reviewed 2008 and 2026 primary statements. Those edition gaps remain recorded. This status check does not certify complete proofs of the cited partial results.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dd4bee6d9fc6af13**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
