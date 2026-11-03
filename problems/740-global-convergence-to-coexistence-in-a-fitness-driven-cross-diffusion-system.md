# 740. Global convergence to coexistence in a fitness-driven cross-diffusion system

**Area:** Population dynamics and degenerate parabolic systems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge2`$, and let $`\Omega\subset\mathbb R^d`$ be a bounded connected smooth domain. Let $`A=(a_{ij})`$ be a constant symmetric positive-definite matrix, and let $`m(x)=(m_i(x))`$ be smooth up to the boundary. Impose the structural condition (5.1) of [1]: for every proper subset $`I=\{i_1<\cdots<i_r\}\subset\{1,\ldots,N\}`$, every $`j\notin I`$, and every $`x\in\overline\Omega`$,
```math
\det\begin{pmatrix}
 A_{II}&m_I(x)\\
 A_{jI}&m_j(x)
\end{pmatrix}\ge\kappa>0.
```

For $`I=\varnothing`$, this means $`m_j(x)\ge\kappa`$. Put $`u^\infty=A^{-1}m`$ and
```math
E(u)=\frac12\int_\Omega (u-u^\infty)\cdot A(u-u^\infty)\,dx.
```


Given $`u_i^0\ge0`$ in $`L^2(\Omega)`$, with $`\int_\Omega u_i^0\,dx>0`$ for every species, consider
```math
\partial_tu_i=-\nabla\cdot(u_i\nabla f_i)+u_if_i,\qquad
f=m-Au,\qquad
u_i\partial_\nu f_i=0,\qquad u(0)=u^0.
```


**Can the global weak solutions of [1, Theorem 1] be chosen so that**
```math
E(u(t))\le e^{-\gamma t}E(u^0)\qquad(t\ge0)
```

for some $`\gamma>0`$, without the subcritical-initial-entropy condition?

Here retain [1, Definition 2.1] and the entropy-dissipation admissibility (2.3). In particular,
```math
u\in C_w([0,\infty);L^2(\Omega)^N)
 \cap L^2_{\mathrm{loc}}([0,\infty);H^1(\Omega)^N)
 \cap L^\infty(0,\infty;L^2(\Omega)^N),\quad u_i\ge0,
```

the equation holds against $`C^1(\overline\Omega)^N`$ spatial tests in time distributions, and
```math
E(u(t_1))+\sum_i\int_{t_0}^{t_1}\int_\Omega
u_i(|\nabla f_i|^2+|f_i|^2)\,dx\,dt\le E(u(t_0))
```

for almost every $`0\le t_0\le t_1`$, including $`t_0=0`$.

The rate may depend on the data and coefficients. The question asks for a suitable global solution for every datum; it does not add uniqueness or quantify over arbitrary non-admissible weak solutions.

## Application

The source proves the estimate when the initial entropy lies below the minimum entropy of its finitely many partial-extinction equilibria. It explicitly conjectures that excluding an initially absent species should suffice for global convergence. Establishing persistence away from the extinction states is the missing step in its argument. The biological question is whether all initially present populations ultimately coexist at the ideal free distribution.

## References

1. S. Kondratyev, L. Monsaingeon and D. Vorotnikov, [A fitness-driven cross-diffusion system from population dynamics as a gradient flow](https://doi.org/10.1016/j.jde.2016.05.012), *Journal of Differential Equations* **261**(5) (2016), 2784–2808. [Author manuscript](https://arxiv.org/abs/1603.06431), Section 2 after Theorem 2, Definition 2.1, equations (2.1)–(2.4) and (5.1); the same conjecture appears near the end of Section 5. The [Coimbra author preprint](https://www.mat.uc.pt/preprints/ps/p1608.pdf), printed pages 5–6, displays the constant-matrix convention immediately before Theorem 2.

## Status review


**Known cases:** The fitness-driven model fixes symmetric positive-definite constant interactions with spatially varying resources and entropy-admissible weak solutions. The known subcritical-entropy estimate and different adaptive competition models do not remove that threshold for every positive-mass datum.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The fitness-driven model fixes symmetric positive-definite constant interactions with spatially varying resources and entropy-admissible weak solutions. The known subcritical-entropy estimate and different adaptive competition models do not remove that threshold for every positive-mass datum.

Additional comparison sources: [comparison source 1](https://doi.org/10.1016/j.jde.2016.05.012); [comparison source 2](https://arxiv.org/abs/1603.06431); [comparison source 3](https://www.mat.uc.pt/preprints/ps/p1608.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Primary equations, structural condition, weak-solution class and theorem/conjecture hypotheses were checked. The constant matrix is the setting explicitly adopted immediately before Theorem 2; spatially varying resources remain allowed. Exact-model, latest-version and announced-solution searches through 27 October 2026 found no matching complete resolution. No matching target was found in the existing further-problem list or all-status AIM/OpenAI comparison. This is a bounded literature review, not a proof of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e03b2670b8eeca1c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
