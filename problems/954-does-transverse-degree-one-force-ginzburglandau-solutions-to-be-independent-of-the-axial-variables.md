# 954. Does transverse degree one force Ginzburg–Landau solutions to be independent of the axial variables?

**Area:** Nonlinear elliptic equations and vortex models
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`N\ge3`$, write a point of $`\mathbb R^N`$ as $`(z,t)\in\mathbb R^2\times\mathbb R^{N-2}`$. Let $`u\in C^2(\mathbb R^N;\mathbb C)`$ solve the classical complex-valued Ginzburg–Landau equation
```math
\Delta u+(1-|u|^2)u=0 \qquad\text{in }\mathbb R^N.
```

Assume that its modulus approaches one as the transverse coordinate goes to infinity, **uniformly in all axial variables**:
```math
\lim_{R\to\infty}
\sup_{\substack{|z|\ge R\\t\in\mathbb R^{N-2}}}
\bigl||u(z,t)|-1\bigr|=0.
```


This uniform limit makes $`u`$ nonzero whenever $`|z|`$ is sufficiently large. For such an $`R`$ and any $`t`$, define the transverse degree to be the winding number of the phase on the circle:
```math
q=\deg\left(
S^1\ni e^{i\theta}\longmapsto
\frac{u(Re^{i\theta},t)}{|u(Re^{i\theta},t)|}\in S^1
\right).
```

Continuity and homotopy invariance make this integer independent of the sufficiently large radius $`R`$ and of $`t`$.

If $`q\in\{-1,+1\}`$, must there exist a function $`v:\mathbb R^2\to\mathbb C`$ such that
```math
u(z,t)=v(z)\qquad\text{for every }(z,t)\in\mathbb R^2\times\mathbb R^{N-2}?
```


This is the residual degree-one question stated after condition (1.18) in [1], including both signs. There is no assumption of stability, local or global minimality, periodicity, finite energy, or an energy growth bound. The requested conclusion is independence of the axial variables; a separate radial classification of $`v`$ is not part of the question.

## Application

The equation describes stationary states of the complex Ginzburg–Landau energy without an applied magnetic field. Zeros of the complex field represent vortices, and phase winding records their net charge. In three dimensions, the question asks whether a configuration of total transverse charge one whose modulus becomes uniformly constant away from its axis must be a straight planar profile extended along that axis. This addresses the geometry of entire critical configurations, including configurations that need not minimize the energy [1, introduction].

## Known results and scope

The same assertion without the restriction $`q=\pm1`$ is false. Dávila, del Pino, Medina and Rodiac construct nontrivial helical solutions in three dimensions satisfying the uniform modulus limit. Their Theorem 1 has total transverse degree $`n\ge2`$. The mixed-sign construction in their Theorem 2 has one negative and $`n-1`$ positive filaments, with $`n\ge5`$, hence total degree $`n-2\ge3`$. These results leave the stated degree-one question open in the source.

Sandier and Shafrir prove that a local minimizer $`u:\mathbb R^3\to\mathbb R^2`$ is constant if
```math
\liminf_{R\to\infty}\frac{E(u;B_R)}{R\log R}<2\pi,
\qquad
E(u;B_R)=\int_{B_R}
\left(\frac12|\nabla u|^2+\frac14(1-|u|^2)^2\right).
```

Their conjectural classification of all nonconstant local minimizers and this theorem both concern a more restricted variational class [2, introduction and Theorem 1.1]. They do not establish axial independence for every critical solution in the problem above.

Later constructions for a coupled two-component Ginzburg–Landau system [3] have a different target space and coupling. Their recalled scalar helical examples have at least two units of total degree; they do not settle the scalar residual question here.

Degree-one travelling vortex helices for the Gross–Pitaevskii equation [4] solve an equation with a nonzero travelling-wave term. For the nonstraight helices in its Theorem 1, that term does not vanish; these profiles therefore do not supply stationary counterexamples to the equation here.

## References

1. J. Dávila, M. del Pino, M. Medina and R. Rodiac, [*Interacting helical vortex filaments in the three-dimensional Ginzburg–Landau equation*](https://doi.org/10.4171/JEMS/1175), *Journal of the European Mathematical Society* **24** (2022), 4143–4199. [Published PDF](https://ems.press/content/serial-article-files/33011). The question and condition (1.18) are on printed p. 4148, native PDF p. 6. The same question appears in [arXiv version 2](https://arxiv.org/pdf/1901.02807v2), dated 31 July 2019, native p. 5. The preprint was first submitted on 9 January 2019.
2. E. Sandier and I. Shafrir, [*Small energy Ginzburg–Landau minimizers in $`\mathbb R^3`$*](https://doi.org/10.1016/j.jfa.2017.01.010), *Journal of Functional Analysis* **272** (2017), 3946–3964. [Latest arXiv version](https://arxiv.org/abs/1612.00821), version 2, dated 10 January 2017.
3. L. Duan, Q. Gao and J. Yang, [*The helical vortex filaments of Ginzburg–Landau system in $`\mathbb R^3`$*](https://arxiv.org/abs/2207.11927), arXiv:2207.11927, 25 July 2022. The checked preprint concerns a coupled $`\mathbb C^2`$-valued system, rather than the scalar complex equation above.

4. D. Chiron, [*Vortex helices for the Gross–Pitaevskii equation*](https://math.univ-cotedazur.fr/~chiron/fichierspdf/helixfinal.pdf), equation (2), Theorem 1 and Remark 1, native pp. 2–3. The constructed nonstraight helices have nonzero travelling speed for sufficiently small positive parameter.

## Status review


**Known cases:** The scalar complex equation with uniform transverse degree plus/minus one is required. Higher-degree helices, coupled two-component systems and traveling Gross-Pitaevskii models are not counterexamples.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The scalar complex equation with uniform transverse degree plus/minus one is required. Higher-degree helices, coupled two-component systems and traveling Gross-Pitaevskii models are not counterexamples.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The explicit source question, equation, uniform limit, and degree ranges of the counterexamples were checked in the published paper and in its official 2019 arXiv version 2. These are selected native body passages; no whole-paper reading or byte equality between versions is claimed.

Bounded searches through 23 October 2026 located no matching complete proof, counterexample, or announced resolution of this precise residual question. Current announcements concerning degree-one minimizers on a bounded planar disk, bounded-ball vector-valued minimizers, and nondegeneracy of degree-two or degree-three planar vortices have different hypotheses or conclusions. The checked current OpenAI catalogue descriptions contained no matching target; this is not a claim to have read every linked manuscript.

The all-status duplicate check included the AIM statements, the developing findings, the eight changed statements in the current public AIM snapshot, and all 737 current findings, including the newest admitted statements. The closest existing AIM problem asks for radial classification of higher-degree solutions on the plane. Other nearby entries concern bounded-disk uniqueness, planar $`p`$-Ginzburg–Landau stability for $`p>4`$, and renormalized Coulomb energy. None has the same whole-space axial-independence target.

The companion audit records the selected source windows, dated current queries, exact duplicate comparisons, and access limits. These checks do not certify every cited proof or guarantee the absence of an unlocated solution.

Independent admission evidence: [source and scope review](../FURTHER_problems/_tracking/ginzburg-degree-one-independent-peer-2026-10-23.json), [semantic duplicate review](../FURTHER_problems/_tracking/ginzburg-degree-one-coordinator-duplicate-review-2026-10-23.json), [current searches](../FURTHER_problems/_tracking/ginzburg-degree-one-current-resolution-search-2026-10-23.json), [announcement checks](../FURTHER_problems/_tracking/ginzburg-degree-one-announcements-and-catalogues-2026-10-23.json) and [source versions](../FURTHER_problems/_tracking/ginzburg-degree-one-eligibility-and-latest-versions-2026-10-23.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-c5247c91e7c22a6f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
