# 751. Uniqueness at finite energy for a viscous fluid coupled to a full von Kármán plate

**Area:** Fluid–structure interaction
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\mathcal O\subset\mathbb R^3`$ be a bounded cavity with smooth boundary $`\partial\mathcal O=\overline S\cup\overline\Omega`$, where $`\Omega\subset\{x_3=0\}`$ is a bounded smooth planar domain, $`S\subset\{x_3\le0\}`$, and the outward normal on $`\Omega`$ is $`e_3`$. Fix viscosity $`\nu>0`$ and Poisson ratio $`0<\mu<1/2`$. Let $`a:\Omega\times[0,T]\to\mathbb R^2`$ be the in-plane displacement and $`w:\Omega\times[0,T]\to\mathbb R`$ the transverse displacement. Define

```math
P(a,w)=\tfrac12(\nabla a+\nabla a^T)+\tfrac12\nabla w\otimes\nabla w,
\qquad \sigma(a,w)=\mathcal C P(a,w),
```

```math
\mathcal C\epsilon=\frac{2}{1-\mu}\big[\mu\mathrm{tr}(\epsilon)I+(1-\mu)\epsilon\big].
```

Consider the unforced, fixed-domain system with in-plane inertia retained, no rotational inertia and no mechanical plate damping:

```math
v_t-\nu\Delta v+\nabla p=0,\qquad \mathrm{div}v=0\quad\hbox{in }\mathcal O,
```

```math
v=0\ \hbox{on }S,\qquad v=(a_t,w_t)\ \hbox{on }\Omega,
```

```math
a_{tt}-\mathrm{div}\sigma(a,w)=-\nu\big(\partial_3v_{\parallel}+\nabla_{\parallel}v_3\big)|_\Omega,
```

```math
w_{tt}+\Delta^2w-\mathrm{div}(\sigma(a,w)\nabla w)=p|_\Omega-2\nu\partial_3v_3|_\Omega.
```

Impose $`a=0`$, $`w=\partial_{n'}w=0`$ on $`\partial\Omega`$, and $`\int_\Omega w\,dx'=0`$ (hence $`\int_\Omega w_t\,dx'=0`$). Initial data have finite energy:

```math
v_0\in X,\quad a_0\in H^1_0(\Omega)^2,\quad w_0\in H^2_0(\Omega),\quad
(a_1,w_1)\in L^2(\Omega)^2\times\widehat L^2(\Omega),
```

with $`\int_\Omega w_0=0`$ and weak normal-trace compatibility $`v_0\cdot n=w_1`$ on $`\Omega`$. Here $`X=\{v\in L^2(\mathcal O)^3:\mathrm{div}v=0,\ v\cdot n=0\text{ on }S\}`$, $`\widehat L^2`$ denotes zero mean, and $`V=\{v\in H^1(\mathcal O)^3:\mathrm{div}v=0,\ v=0\text{ on }S\}`$.

Is the energy weak solution unique for every such datum and every $`T>0`$? Specifically, require

```math
v\in L^\infty(0,T;X)\cap L^2(0,T;V),\quad
(a,w)\in L^\infty(0,T;H^1_0(\Omega)^2\times H^2_0(\Omega)),
```

```math
(a_t,w_t)\in L^\infty(0,T;L^2(\Omega)^2\times\widehat L^2(\Omega))\cap L^2(0,T;H^{1/2}_*(\Omega)^3),
```

where $`H^{1/2}_*(\Omega)`$ means the trace has an $`H^{1/2}(\mathbb R^2)`$ zero extension. The interface velocity condition holds almost everywhere in time. Set $`(a,w)(0)=(a_0,w_0)`$. The pressure-free weak identity is

```math
\begin{aligned}
-\int_0^T(v,\phi_t)_{\mathcal O}\,dt
+2\nu\int_0^T(D(v),D(\phi))_{\mathcal O}\,dt
-\int_0^T[(a_t,b_t)_\Omega+(w_t,d_t)_\Omega]\,dt\\
+\int_0^T(\Delta w,\Delta d)_\Omega\,dt
+\int_0^T\int_\Omega\sigma(a,w):[\mathrm{sym}\nabla b+\mathrm{sym}(\nabla w\otimes\nabla d)]\,dx'\,dt\\
=(v_0,\phi(0))_{\mathcal O}+(a_1,b(0))_\Omega+(w_1,d(0))_\Omega.
\end{aligned}
```

Here $`(\cdot,\cdot)`$ denotes the $`L^2`$ pairing and $`\mathrm{sym} M=(M+M^T)/2`$. Require this for every solenoidal $`\phi\in L^2(0,T;V)`$ with $`\phi_t\in L^2(0,T;L^2(\mathcal O)^3)`$, $`\phi(T)=0`$ and interface trace $`(b,d)`$, where $`b\in L^2(0,T;H^1_0(\Omega)^2)`$, $`d\in L^2(0,T;\widehat H^2_0(\Omega))`$, and $`(b_t,d_t)\in L^2(0,T;L^2(\Omega)^2\times\widehat L^2(\Omega))`$. Hats denote zero mean. This is the unforced specialization of [2, Definition 2.2]. The interface tractions cancel, so no pressure trace is assumed in this weak class. Also require, for almost every $`t\in[0,T]`$, the energy inequality

```math
\mathcal E(t)+2\nu\int_0^t\|D(v)\|_{L^2(\mathcal O)}^2\,ds\le\mathcal E(0),
```

```math
\mathcal E=\tfrac12\big(\|v\|_2^2+\|a_t\|_2^2+\|w_t\|_2^2+\|\Delta w\|_2^2+\int_\Omega\mathcal C P(a,w):P(a,w)\,dx'\big),\quad D(v)=\tfrac12(\nabla v+\nabla v^T).
```

Uniqueness concerns $`v,a,w`$ in this class, rather than uniqueness only among strong solutions.

## Application

This asks whether a finite-energy initial state predicts a unique motion of a viscous fluid and a plate that can move both along and across its surface. Omitting rotational inertia removes a regularizing term that is often neglected in plate models. A positive answer would justify a deterministic energy-space evolution for this coupled model.

## References

1. I. Chueshov and I. Ryzhkova, *Unsteady interaction of a viscous fluid with an elastic plate modeled by full von Karman equations*, Journal of Differential Equations 254 (2013), 1833–1862, [DOI](https://doi.org/10.1016/j.jde.2012.11.006), [arXiv1112.6094v1](https://arxiv.org/abs/1112.6094v1), Remark 3.5. The preprint title says “shell”. The source covers curved shells; the question here uses the flat, fully dynamic, unforced specialization.
2. I. Ryzhkova, *On an attractor for strong solutions to interactive fluid-plate system without rotational inertia*, [arXiv2307.11262v1](https://arxiv.org/abs/2307.11262v1), introduction, Definition 2.2, Theorem 2.3 and the following paragraph. This gives the precise flat model and explicitly repeats the weak-uniqueness obstruction. The strong solutions and their attractor are different statements.
3. I. Ryzhkova-Gerasymova, *Long time behaviour of strong solutions to interactive fluid-plate system without rotational inertia*, Discrete and Continuous Dynamical Systems-B 23(3) (2018), 1243–1265, [DOI](https://doi.org/10.3934/dcdsb.2018150). Strong well-posedness does not settle the energy weak class.
4. W. Li, A. Miranville, X.-G. Yang and J. Yuan, *Well-posedness for a 2D/3D fluid-shell interaction model*, Electronic Research Archive 33(11) (2025), 7065–7084, [DOI](https://doi.org/10.3934/era.2025312). The primary model fixes its rotational-inertia coefficient to1, so its results do not settle this question.

## Status review


**Known cases:** The target is finite-energy uniqueness of the vectorial full von Karman plate with in-plane inertia, no rotational inertia, coupled to three-dimensional linear Stokes flow. Two-dimensional weak uniqueness, strong solutions, positive rotational inertia and scalar plate discretizations do not establish it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is finite-energy uniqueness of the vectorial full von Karman plate with in-plane inertia, no rotational inertia, coupled to three-dimensional linear Stokes flow. Two-dimensional weak uniqueness, strong solutions, positive rotational inertia and scalar plate discretizations do not establish it.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.jde.2012.11.006); [comparison source 2](https://arxiv.org/abs/1112.6094v1); [comparison source 3](https://arxiv.org/abs/2307.11262v1); [comparison source 4](https://doi.org/10.3934/dcdsb.2018150); [comparison source 5](https://doi.org/10.3934/era.2025312). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Searches through 2026-10-16 found no resolution or announced full solution for this precise class; the dated review packet records scope and catalogue comparisons. This is a question about the vectorial full von Kármán system coupled to linear unsteady Stokes flow, and is distinct from scalar Airy-stress plate equations, from full nonlinear Navier–Stokes uniqueness, and from an inviscid Kutta–Joukowski flow-trace question.

The original source explicitly leaves the zero-rotational-inertia case open in Remark 3.5. The 2018 and 2023 papers repeat the weak-uniqueness question while proving strong-solution results. The 2025 paper uses a positive rotational-inertia coefficient and proves weak uniqueness only for its two-dimensional fluid model. These hypotheses do not settle the class above. Negative searches are dated evidence, not a proof that no resolution exists.

Review evidence: [scope and current-status packet](../FURTHER_problems/_tracking/parallel/continuum/full-vk-weak-uniqueness-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d9c53cc16a3503a4**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
