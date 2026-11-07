# AIM 669: target comparison

**Decision:** Solved.

**Established:** A doubling metric measure space supporting a Poincar\'e inequality has a function with source minimal gradient at most $1$ and completion gradient $\sqrt2$. The completion complement is nonmeasurable.

**Scope / remaining target:** The conclusion concerns exactly the catalogue target; no historical priority claim is made.

Canonical revision: 1e564633494c109edfd3ec46da1366adcff925a5.

# 669. Does metric completion preserve minimal Sobolev gradients?

**Area:** Nonlinear potential theory on metric spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`1<p<\infty`$. Equip a possibly noncomplete metric space $`X`$ with a positive complete Borel measure $`\mu`$, finite and nonzero on every ball. Write $`\widehat X`$ for its metric completion. On Borel subsets $`E\subset\widehat X`$, define $`\widehat\mu(E)=\mu(E\cap X)`$, then complete this measure.

Choose a ball $`B_0\subset X`$. Assume constants $`C_D,C_P<\infty`$ and $`\lambda\ge1`$ give, for every ball $`B\subset B_0`$,

```math
\mu(2B)\le C_D\mu(B),\qquad
\fint_B|v-v_B|\,d\mu\le C_P r_B\left(\fint_{\lambda B}g^p\,d\mu\right)^{1/p}
```


for every integrable $`v`$ on $`\lambda B`$ and every upper gradient $`g`$ of $`v`$. Here $`v_B=\fint_Bv\,d\mu`$; an upper gradient controls endpoint differences by its line integral along each rectifiable curve. A $`p`$-weak upper gradient allows a curve family of zero $`p`$-modulus as exceptions.

For open $`\Omega\subset B_0`$, set

```math
\Omega^\wedge=\widehat X\setminus\overline{X\setminus\Omega}^{\,\widehat X}.
```


Let $`u\in D^p(\Omega)`$, the measurable pointwise-defined functions admitting an upper gradient in $`L^p(\Omega)`$. The extension theorem supplies $`\widehat u\in D^p(\Omega^\wedge)`$ agreeing with $`u`$ outside a set of zero Sobolev $`C_p^X`$-capacity in $`\Omega`$, with

```math
g_{\widehat u,\Omega^\wedge}\le A_0 g_{u,\Omega}\quad\mu\text{-a.e. on }\Omega.
```


The subscripts specify where the minimal $`p`$-weak upper gradients are computed. **Can this extension always preserve the gradient exactly, with $`A_0=1`$? Or is there an example satisfying all these hypotheses where equality fails on a set of positive $`\mu`$-measure?** This is Björn–Björn’s Open Problem 4.4.

No assumption that $`\Omega`$ is $`p`$-path almost open in $`\widehat X`$ is imposed. Under that additional assumption, equality is known. The completion complement need not be measurable; only its inner $`\widehat\mu`$-measure is always zero.
