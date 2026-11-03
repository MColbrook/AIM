# 405. Uniqueness of divergence-free transport with bounded-deformation velocity

**Area:** Linear transport and nonsmooth flows
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge2`$, $`T>0`$, and let $`b:(0,T)\times\mathbb R^d\to\mathbb R^d`$ be a bounded Borel vector field. Suppose $`\mathrm{div}_x b=0`$ distributionally. For almost every $`t`$, require the symmetric spatial distributional gradient

```math
E_xb_t=\frac{D_xb_t+(D_xb_t)^T}{2}
```

to be a locally finite matrix-valued Radon measure, with

```math
\int_0^T |E_xb_t|(B_R)\,dt<\infty\qquad\text{for every }R>0.
```

No restriction is imposed on its Cantor part or on the time derivative of $`b`$.

For every real $`u_0\in L^1(\mathbb R^d)\cap L^\infty(\mathbb R^d)`$, is there at most one real

```math
u\in L^\infty\big((0,T);L^1(\mathbb R^d)\cap L^\infty(\mathbb R^d)\big)
```

that satisfies

```math
\int_0^T\!\int_{\mathbb R^d}u(\partial_t\varphi+b\cdot\nabla\varphi)\,dx\,dt
+\int_{\mathbb R^d}u_0(x)\varphi(0,x)\,dx=0
```

for every $`\varphi\in C_c^\infty([0,T)\times\mathbb R^d)`$? Uniqueness means equality almost everywhere in space-time. Renormalization and a Lagrangian representation are not extra admissibility requirements.

## Application

The equation models a passive density carried by a prescribed incompressible velocity. This asks whether control of the symmetric derivative alone determines that transport uniquely, including velocities with singular strain. It would extend the available theory of nonsmooth flows beyond fields whose full derivative is a measure.

## References

1. Luigi Ambrosio, [*The flow associated to weakly differentiable vector fields: recent results and open problems*](https://cvgmt.sns.it/media/doc/paper/1217/Ima_proc.pdf), in *Nonlinear Conservation Laws and Applications*, IMA Volumes **153** (2011), 181–193, [chapter DOI](https://doi.org/10.1007/978-1-4419-9554-4_7). Inspected: the 13-page author version recorded in 2009, Sections 1–2, especially the bounded-field setting, solution classes and explicit bounded-deformation question on physical pp. 1–3. Final-version parity remains pending.
2. Marco Inversi, [*Fine dissipative properties of Euler solutions with measure first derivatives*](https://arxiv.org/html/2510.10704v4), latest arXiv revision 18 May 2026, Theorem 1.2 and Section 2.3. This proves an Euler energy-conservation result and explicitly distinguishes the unresolved linear transport problem.
3. Luigi Ambrosio, Stefano Bianchini, Federico Renzi and Federico Vitillaro, [*Non-branching properties of Regular Lagrangian Flows and well posedness of the continuity equation in the class of nonnegative solutions*](https://arxiv.org/html/2610.17129v1), 12 October 2026, Theorem 5.1 and conditions (5.1)–(5.3). The theorem requires spatial special bounded deformation and an additional measure-valued time derivative.

## Status review


**Known cases:** The October regular-Lagrangian-flow theorem requires special BD and extra time regularity. BV theory, Euler energy conservation and fractional-Sobolev counterexamples do not establish uniqueness for every prescribed divergence-free L1-time BD velocity with arbitrary Cantor part.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

This is a divergence-free uniqueness prototype of Ambrosio's broader bounded-deformation extension programme. The field is prescribed; it need not solve the Euler equations. The unknown scalar is arbitrary and need not itself have bounded deformation.

The full-derivative theory for bounded-variation fields does not imply this statement. The October 2026 theorem treats a special bounded-deformation class without a Cantor part and requires time regularity absent here. Its following discussion explicitly raises removal of the time assumption. Inversi's energy-conservation argument uses the Euler nonlinearity and does not supply uniqueness for this scalar equation.

No matching complete solution or announcement was located in the recorded current checks. This is a bounded literature review, not a proof that no resolution exists.

The [source review](../FURTHER_problems/_tracking/parallel/continuum/bd-transport-review.json), [independent selected audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-bd-transport-review.json), [current comparisons](../FURTHER_problems/_tracking/bd-transport-current-comparisons-2026-10-19.json), [semantic comparison](../FURTHER_problems/_tracking/bd-transport-duplicates-review-2026-10-19.json), [catalogue check](../FURTHER_problems/_tracking/bd-transport-catalogue-review-2026-10-19.json) and [coordinator review](../FURTHER_problems/_tracking/bd-transport-coordinator-review-2026-10-19.json) record the evidence and its limits. These are AI checks, not human peer review.


### Online recheck, 2026-10-30

The October regular-Lagrangian-flow theorem requires special BD and extra time regularity. BV theory, Euler energy conservation and fractional-Sobolev counterexamples do not establish uniqueness for every prescribed divergence-free L1-time BD velocity with arbitrary Cantor part.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2610.17129); [status source 2](https://arxiv.org/abs/2510.10704); [status source 3](https://arxiv.org/abs/2610.33993). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-a3505222b6a71a4e** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
