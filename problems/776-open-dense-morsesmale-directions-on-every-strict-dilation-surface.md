# 776. Open dense Morse–Smale directions on every strict dilation surface

**Area:** Geometry, topology and dynamical systems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a connected compact oriented surface without boundary, equipped with a dilation structure and a finite set $`\Sigma`$ of conical singularities. Away from $`\Sigma`$, its complex coordinate changes have the form $`z\mapsto az+b`$, where $`a>0`$ and $`b\in\mathbb C`$. At a singularity, the local model is obtained from a Euclidean cone of angle $`2\pi k`$, $`k\in\mathbb N_{>0}`$, by cutting along a ray and identifying the two sides by a positive homothety. Regular marked points are allowed.

Call the structure **strict** if it is not a translation structure, equivalently if its linear holonomy is nontrivial. Positive real linear parts preserve directions, so each $`\theta\in S^1`$ determines a straight-line directional foliation $`\mathcal F_\theta`$.

Does every such strict $`X`$ admit an open dense set $`U_X\subset S^1`$ for which $`\mathcal F_\theta`$ is Morse–Smale for every $`\theta\in U_X`$?

Here Morse–Smale has the source's directional meaning: trajectories terminate at a conical singularity or accumulate on hyperbolic closed geodesics. A regular closed geodesic is hyperbolic when its dilation holonomy is different from one. The condition may be imposed in both time orientations by replacing $`U_X`$ with $`U_X\cap(-U_X)`$.

The surface is fixed before directions are varied. The question concerns every strict surface, without a genericity assumption in moduli space or an assumption that a horizon saddle connection exists. Full measure of $`U_X`$ is a stronger question.

## Application

Dilation surfaces describe suspensions of affine interval exchange transformations. The conjecture asks whether attracting and repelling periodic behavior is typical as the direction changes on each fixed geometric system.

## Known progress

Tahar proves the conclusion for surfaces with a horizon saddle connection and relates it to density of hyperbolic closed-geodesic directions. The later theorem that ordinary closed-geodesic directions are dense does not distinguish flat from hyperbolic cylinders.

A 2025 announcement by Apisa, Bainbridge and Wang treats generic surfaces in moduli space. Apisa's Toulouse slides also state a conull-surface result in a single-zero stratum, with most directions Morse–Smale. These quantifiers leave possible exceptional fixed surfaces. Schmidhuber's decomposition theorem permits periodic, Morse–Smale, minimal and Cantor-like components; it does not settle the generic-direction question.

## References

1. G. Tahar, *Horizon saddle connections and Morse–Smale dynamics of dilation surfaces*, [arXiv:2107.11745v1](https://arxiv.org/abs/2107.11745v1), Conjecture 1.3; [latest v2](https://arxiv.org/abs/2107.11745v2), revised 9 February 2023. Published in *Journal of Modern Dynamics* **19** (2023), 417–431, [doi:10.3934/jmd.2023012](https://doi.org/10.3934/jmd.2023012), Conjecture 1.3 and Theorems 1.4–1.5, printed p. 418; Definition 2.1 and local models, pp. 419–420.
2. A. Boulanger, S. Ghazouani and G. Tahar, *Closed geodesics in dilation surfaces*, [arXiv:2110.06061v3](https://arxiv.org/abs/2110.06061v3), Theorem 1.1 and Section 1.4, Problem 1.4. Published in *Geometry & Topology* **29** (2025), 2217–2250, [doi:10.2140/gt.2025.29.2217](https://doi.org/10.2140/gt.2025.29.2217).
3. A. S. Schmidhuber, *On the structure of foliations on dilation surfaces*, [arXiv:2401.00951v1](https://arxiv.org/abs/2401.00951v1), Theorem 1.1, Definition 4.8, Conjecture 4.9 and Section 7.2.
4. P. Apisa, *Twisted holomorphic 1-forms, dynamics, and the framed mapping class group*, [Toulouse slides, 9 April 2025](https://indico.math.cnrs.fr/event/12317/contributions/13222/attachments/5626/9707/Dilation_Surfaces_Talk__Toulouse_Version_.pdf), logical slides 7 and 9.

## Status review


**Known cases:** The surface is fixed and arbitrary before choosing directions. Dense closed-geodesic directions, a dynamical decomposition, genericity in moduli, or a horizon-saddle-connection hypothesis do not give an open dense Morse-Smale set on every strict dilation surface.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The surface is fixed and arbitrary before choosing directions. Dense closed-geodesic directions, a dynamical decomposition, genericity in moduli, or a horizon-saddle-connection hypothesis do not give an open dense Morse-Smale set on every strict dilation surface.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2107.11745v1); [comparison source 2](https://arxiv.org/abs/2107.11745v2); [comparison source 3](https://doi.org/10.3934/jmd.2023012); [comparison source 4](https://arxiv.org/abs/2110.06061v3); [comparison source 5](https://doi.org/10.2140/gt.2025.29.2217); [comparison source 6](https://arxiv.org/abs/2401.00951v1); [comparison source 7](https://indico.math.cnrs.fr/event/12317/contributions/13222/attachments/5626/9707/Dilation_Surfaces_Talk__Toulouse_Version_.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the eligible original question, published definitions and main statements, current primary comparison sources, and the all-status AIM/FURTHER duplicate index. No matching proof, counterexample or announced resolution was located in the bounded searches. Selected native windows and explicit access gaps are retained in the review records; no whole-paper proof audit or exhaustive literature claim is made.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2d7140961f89a282**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
