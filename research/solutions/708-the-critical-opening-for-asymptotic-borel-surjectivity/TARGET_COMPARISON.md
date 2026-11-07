# AIM 708: target comparison

**Decision:** Partially resolved.

**Established:** Both uniform critical endpoints are excluded for every strongly regular sequence.

**Scope / remaining target:** The nonuniform critical endpoint inclusion remains unresolved here.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 708. The critical opening for asymptotic Borel surjectivity

**Area:** Complex analysis and asymptotic analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M=(M_p)_{p\ge0}`$, $`M_0=1`$, be strongly regular: positive and logarithmically convex, with constants $`A,B>0`$ such that
```math
M_{p+q}\le A^{p+q}M_pM_q,\qquad
\sum_{q\ge p}\frac{M_q}{(q+1)M_{q+1}}\le B\frac{M_p}{M_{p+1}}.
```

Set $`m_p=M_{p+1}/M_p`$ and
```math
\gamma(M)=\sup\{a>0:(m_p/(p+1)^a)_p\text{ is almost increasing}\}.
```

Almost increasing means $`c_p\le Kc_q`$ whenever $`p\le q`$, for a fixed $`K`$.

On the logarithm's Riemann surface put $`S_\alpha=\{z:|\arg z|<\pi\alpha/2\}`$, with $`0<|z|<\infty`$. Prescribe $`\widehat f=\sum a_pz^p`$ satisfying $`|a_p|\le CA^pM_p`$. Define three holomorphic classes:

- $`\widetilde{\mathcal A}_M`$: for each bounded proper subsector $`T`$ of $`S_\alpha`$, some $`C_T,A_T>0`$ satisfy
  ```math
|f(z)-\sum_{p<N}a_pz^p|\le C_TA_T^NM_N|z|^N\quad(z\in T,\ N\ge0).
```

- $`\widetilde{\mathcal A}^{u}_M`$: that estimate holds throughout $`S_\alpha`$ with one pair of constants.
- $`\mathcal A_M`$: some $`C,A>0`$ satisfy $`|f^{(p)}(z)|\le CA^p p!M_p`$ throughout $`S_\alpha`$.

Let $`\mathcal S`$ denote the openings $`\alpha>0`$ for which the coefficient map onto all prescribed series is surjective. Is
```math
\mathcal S(\widetilde{\mathcal A}_M)=(0,\gamma(M)],\qquad
\mathcal S(\widetilde{\mathcal A}^{u}_M)=\mathcal S(\mathcal A_M)=(0,\gamma(M))
```

always true? At the critical opening this asks for nonuniform surjectivity and uniform non-surjectivity.
