# 829. Magnetic flatness from everywhere-collapsed Green directions

**Area:** Magnetic dynamics / geometric rigidity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(M,g)`$ be a closed connected oriented smooth Riemannian surface, let
$`J`$ be rotation by $`\pi/2`$ in its oriented tangent planes, and let
$`f\in C^\infty(M,\mathbb R)`$. The unit-speed magnetic trajectories solve

```math
\nabla_{\dot\gamma}\dot\gamma=f(\gamma)J\dot\gamma.
```

Write $`SM`$ for the unit tangent bundle, $`\varphi_t`$ for this flow and
$`K_g`$ for Gaussian curvature. Set

```math
q(x,v)=K_g(x)-df_x(Jv)+f(x)^2,\qquad (x,v)\in SM.
```

The transverse scalar Jacobi equation along the trajectory from $`z\in SM`$ is

```math
\ddot y(t)+q(\varphi_tz)y(t)=0.
```

Assume this equation has no conjugate points: for every $`z`$, its solution
$`s_z`$ with $`s_z(0)=0`$ and $`\dot s_z(0)=1`$ has $`s_z(t)\ne0`$ for every
$`t\ne0`$. Let $`c_z`$ be the solution with $`c_z(0)=1`$, $`\dot c_z(0)=0`$.
For $`T\ne0`$ define

```math
b_T(z)=-\frac{c_z(T)}{s_z(T)}.
```

Thus the solution starting from $`(y(0),\dot y(0))=(1,b_T(z))`$ vanishes at
time $`T`$. The no-conjugate-points hypothesis gives finite Green limits

```math
r_+(z)=\lim_{T\to+\infty}b_T(z),\qquad
r_-(z)=\lim_{T\to-\infty}b_T(z).
```

These define the two Green lines $`\mathbb R(1,r_+(z))`$ and
$`\mathbb R(1,r_-(z))`$ for the transverse Jacobi cocycle.

**Question.** Does

```math
r_+(z)=r_-(z)\quad\text{for every }z\in SM
```

imply $`q\equiv0`$ on $`SM`$?

The hypothesis is equality at every point, with no curvature sign, no-focal-point,
entropy or action assumption added. The conjugate-point convention is the
transverse scalar equation displayed above. In the source it is expressed using
Green lines in the annihilator of the flow direction in $`T^*(SM)`$.

The conclusion would force $`f`$ to be constant and $`K_g=-f^2`$. It describes
the flat zero-field system or a constant-curvature horocycle magnetic system.

## Application

Magnetic trajectories model charged particles moving at fixed speed on a
curved surface. This asks whether a global degeneracy of transverse focusing
directions certifies a homogeneous geometry and magnetic field.

## References

1. J. Echevarría Cuesta and J. Marshall Reber, *Thermostats without conjugate
   points*, **Ergodic Theory and Dynamical Systems 46** (2026), 1494–1520,
   [DOI](https://doi.org/10.1017/etds.2026.10285),
   [published PDF](https://api.repository.cam.ac.uk/server/api/core/bitstreams/d36a92a8-f0d7-43bd-8514-7ffee7d52b76/content).
   Section 1.3, the magnetic-system question on printed p.1502;
   equations (1.3), (1.9), (2.3)–(2.4), Theorem 1.5 and Corollary 1.10.
2. G. P. Paternain, *Magnetic rigidity of horocycle flows*, **Pacific Journal
   of Mathematics 225** (2006), 301–323,
   [published PDF](https://msp.org/pjm/2006/225-2/pjm-v225-n2-p07-p.pdf),
   [DOI](https://doi.org/10.2140/pjm.2006.225.301).
   The proposition on p.304 requires vanishing Liouville action in addition
   to absence of conjugate points; Theorem B assumes criticality and unique
   ergodicity.
3. A. J. García and G. B. Guglielmo, *A Metric Entropy Formula for Magnetic
   Flows without Conjugate Points*,
   [arXiv:2606.18434v2](https://arxiv.org/html/2606.18434v2),
   Theorem B, Definition 4.2 and Lemma 4.3. The header of the actual v2 text
   orders the authors this way; the repository metadata orders them oppositely.

## Status review


**Known cases:** The 2026 thermostat source still separates the magnetic everywhere-Green-collapse implication from its nonpositive-curvature theorem. The entropy identity uses a no-focal-points condition and the horocycle rigidity theorem imposes an action condition. Neither gives the implication under no conjugate points alone.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 thermostat source still separates the magnetic everywhere-Green-collapse implication from its nonpositive-curvature theorem. The entropy identity uses a no-focal-points condition and the horocycle rigidity theorem imposes an action condition. Neither gives the implication under no conjugate points alone.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The first reference asks exactly the everywhere-collapse implication, without
the nonpositive-curvature hypothesis under which it proves the implication.
Its converse, zero magnetic curvature implies collapse everywhere, is known.
The later entropy theorem uses no focal points to obtain a positive
semidefinite Riccati operator. The older horocycle-rigidity theorem uses an
additional action condition. Neither argument supplies the missing general
implication under the assumptions above.

The precise current-status and duplicate review is recorded in the
[review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/magnetic-green-collapse-review.json).


The [independent selected-primary audit](../FURTHER_problems/_tracking/parallel/complex-bayesian/cross-magnetic-green-collapse-review.json), [catalogue check](../FURTHER_problems/_tracking/parallel/rough-filtering/magnetic-green-prove2me0168-comparison.json) and [coordinator review](../FURTHER_problems/_tracking/magnetic-green-coordinator-review-2026-10-18.json) passed at their recorded extents. The six-alias comparison covered all186 current catalogue listing pages; it does not certify every linked mission proof or every external announcement.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-ac4da1dca26f1eeb**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
