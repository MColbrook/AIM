# 538. Closed geodesics on complete manifolds of finite volume

**Area:** Riemannian geometry / geodesic dynamics
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`(M^n,g)`$ be a connected smooth noncompact Riemannian manifold without boundary, of dimension $`n\geq3`$. Assume that $`g`$ is geodesically complete and

```math
0<\mathrm{Vol}_g(M)<\infty.
```


Must there exist a nonconstant smooth curve $`\gamma:\mathbb R\to M`$ and a period $`T>0`$ such that

```math
\nabla_{\dot\gamma}\dot\gamma=0,\qquad \gamma(t+T)=\gamma(t)\quad\text{for every }t\in\mathbb R?
```


Thus both position and velocity return. A geodesic loop whose two endpoint velocities differ does not meet the requirement. No curvature bound, topological restriction, finite-end condition, or convexity assumption on the ends is imposed. Self-intersections are allowed.

## Application

This is an existence question for periodic trajectories of free motion in a complete geometric configuration space with finite total volume. It tests how far the familiar periodic-orbit existence theory on compact manifolds extends when trajectories and variational sequences can travel into noncompact ends. No direct experimental application is claimed.

## References

1. K. Burns and V. S. Matveev, *Open problems and questions about geodesics*, Ergodic Theory and Dynamical Systems **41** (2021), 641–684. [Eligible author version](https://arxiv.org/abs/1308.5417), v3, §2.3, Question 2.3.1 and surrounding discussion, physical p.4. Attributes the question to Bangert; the surface case is known.
2. A. Jabbour and S. Sabourau, *Sharp upper bounds on the length of the shortest closed geodesic on complete punctured spheres of finite area*, Revista Matemática Iberoamericana **38** (2022), 1051–1065. [Published paper](https://ems.press/content/serial-article-files/39032), p.1051, introduction. Explicitly retains this question for complete noncompact manifolds of dimension at least three.
3. G. R. Chambers and Y. Liokumovich, *Existence of minimal hypersurfaces in complete manifolds of finite volume*. [Author version](https://arxiv.org/abs/1609.04058), v3, Theorem 1.1 and Corollary 1.3. The higher-dimensional conclusion is a possibly noncompact minimal hypersurface, rather than a closed geodesic.
4. I. Beach, *The Shortest Geodesic Flower on a Manifold with Locally Convex Ends and Finite Volume* (2026). [Preprint](https://arxiv.org/abs/2605.12642), v1, main theorem and Definition 2. Gives a stationary geodesic flower under an additional end condition; a multiedge flower need not contain a smooth periodic geodesic.

## Status review

The finite-area surface case is known, and compact manifolds have a closed geodesic. The question here concerns arbitrary complete noncompact finite-volume manifolds in higher dimensions. Existence of a minimal hypersurface, a geodesic net, or a geodesic loop does not give the requested periodic trajectory automatically. Finite-volume recurrence of the geodesic flow also does not force a periodic orbit.

Literature and announcement searches on 17 October 2026 found no complete resolution of this precise general question. The OpenAI announcement concerning spheres and closed three-manifolds assumes compactness; the recent hyperbolic simple-geodesic announcement assumes constant negative curvature. Neither covers the class above. Independent selected-primary review passed. All 186 cached catalogue pages were checked with six target aliases, with no matches; this checks listing descriptions rather than every mission proof.

[Owner review](../FURTHER_problems/_tracking/parallel/complex-bayesian/finite-volume-geodesic-review.json), [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-finite-volume-geodesic-review.json), [duplicate comparison](../FURTHER_problems/_tracking/parallel/complex-bayesian/finite-volume-geodesic-broad-duplicate-snapshot.json), [catalogue receipt](../FURTHER_problems/_tracking/parallel/complex-bayesian/finite-volume-geodesic-prove2-0133-review.json) and [coordinator review](../FURTHER_problems/_tracking/finite-volume-geodesic-coordinator-review-2026-10-17.json) preserve scope and access limits.


### Online recheck, 2026-10-30

Compact closed-geodesic infinitude, hyperbolic finite-volume theorems and geodesic flowers under end conditions do not imply a smooth periodic geodesic on every complete noncompact finite-volume manifold of dimension >=3.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2605.12642); [status source 2](https://arxiv.org/abs/2608.29855); [status source 3](https://ems.press/content/serial-article-files/39032). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-21974abcf63a0f32** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
