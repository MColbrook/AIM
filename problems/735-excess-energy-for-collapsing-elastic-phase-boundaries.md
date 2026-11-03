# 735. Excess energy for collapsing elastic phase boundaries

**Area:** Nonlinear elasticity and solid–solid phase transitions
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Does there exist an integer $`d\ge2`$, a number $`\kappa>0`$ and a density $`W:\mathbb R^{d\times d}\to[0,\infty)`$ satisfying the conditions below for which
```math
\min\{K_{\mathrm{dp}}^A,K_{\mathrm{dp}}^B\}>2K?
```

Set $`A=I_d`$, $`B=\mathrm{diag}(1,\ldots,1,1+\kappa)`$ and $`\mathcal K=SO(d)A\cup SO(d)B`$. Use Frobenius norms. Require $`W`$ to be continuous, $`W(RF)=W(F)`$ for every $`R\in SO(d)`$, $`W(A)=W(B)=0`$, and
```math
c_1\mathrm{dist}(F,\mathcal K)^2
\le W(F)\le c_2\mathrm{dist}(F,\mathcal K)^2
\qquad(F\in\mathbb R^{d\times d})
```
for some $`c_1,c_2>0`$. Require $`W`$ to be $`C^2`$ on a neighborhood of $`\mathcal K`$ and, for some $`c_3>0`$,
```math
|W(F)-W(G)|\le c_3(1+|F|+|G|)|F-G|
\qquad(F,G\in\mathbb R^{d\times d}).
```
These are the published paper's H1–H7.

Here are the precise cell constants. For a bounded open set $`D\subset\mathbb R^d`$ and $`y\in H^2(D;\mathbb R^d)`$, put
```math
\begin{aligned}
\bar\eta_{\varepsilon,d}&=\varepsilon^{-1+1/(2d)},\\
\mathcal E_\varepsilon(y;D)
&=\varepsilon^{-2}\int_D W(\nabla y)\,dx
+\varepsilon^2\int_D|\nabla^2y|^2\,dx\\
&\quad+\bar\eta_{\varepsilon,d}^{\,2}
 \int_D\bigl(|\nabla^2y|^2-|\partial_{dd}^2y|^2\bigr)\,dx.
\end{aligned}
```
Let $`Q=(-1/2,1/2)^d`$ and $`Q'=(-1/2,1/2)^{d-1}`$. Define the continuous map $`y_0`$ by $`y_0(x)=Ax`$ when $`x_d\ge0`$ and $`y_0(x)=Bx`$ when $`x_d<0`$. Then
```math
K=\inf_{\substack{y_\varepsilon\in H^2(Q;\mathbb R^d)\\
y_\varepsilon\to y_0\ {\rm in}\ L^1(Q)}}
\liminf_{\varepsilon\downarrow0}\mathcal E_\varepsilon(y_\varepsilon;Q).
```

Let $`\mathcal W_d`$ consist of positive families $`(w_\varepsilon)`$ with $`w_\varepsilon\to0`$ and $`\liminf_{\varepsilon\downarrow0}w_\varepsilon/\varepsilon>0`$. Write
```math
z^A=e_d\mathbf1_{\{x_d>0\}},\qquad
z^B=-e_d\mathbf1_{\{x_d>0\}},\qquad D_h=Q'\times(-h,h).
```
For $`M\in\{A,B\}`$, set
```math
K_{\mathrm{dp}}^M
=\sup_{h>0}\ \sup_{(w_\varepsilon)\in\mathcal W_d}
\inf_{\substack{y_\varepsilon\in H^2(D_h;\mathbb R^d)\\
(y_\varepsilon-Mx)/w_\varepsilon\to z^M\ {\rm in\ measure}}}
\limsup_{\varepsilon\downarrow0}\mathcal E_\varepsilon(y_\varepsilon;D_h).
```
All limits use the positive parameter $`\varepsilon\downarrow0`$. There are no prescribed boundary traces in these infima.

An affirmative answer requires both double-profile constants to exceed $`2K`$. This entry asks for one admissible choice of $`(d,\kappa,W)`$; it makes no assertion for every fixed parameter pair. The H1–H7 class is the paper's full linearization setting, chosen explicitly here.

## Application

The constants measure the energy of a single phase boundary and of a pair enclosing a vanishing layer of the other phase. A strict gap would test the additive interface-cost assumption used in the effective elastic model.

## References

1. E. Davoli and M. Friedrich, *Two-well linearization for solid-solid phase transitions*, Journal of the European Mathematical Society **27** (2025), 615–707. [DOI](https://doi.org/10.4171/JEMS/1385), [published PDF](https://ems.press/content/serial-article-files/49943). H1–H7; equations (3.1)–(3.5), (3.25)–(3.28); conjecture after Proposition 3.17, printed pages 645–646. Online publication: 11 October 2023.
2. J. Deutsch, *A note on the recovery sequence in the double gradient model for phase transitions*, [arXiv:2510.01893v1](https://arxiv.org/html/2510.01893v1), 2 October 2025, §2.1 and Theorem 3.1. Later single-interface result for point wells.
3. E. Davoli, J. Deutsch, M. Friedrich and K. Stinson, *Solid-solid phase transitions with space-dependent wells*, [arXiv:2607.15133v1](https://arxiv.org/html/2607.15133v1), 16 July 2026, §2.1, Remark 2.2 and Theorem 2.6. Later result without frame indifference.

## Status review


**Known cases:** The target is a strict gap above twice the single-interface cell cost for both collapsing double profiles in a frame-indifferent two-well density. The published energy lower bound and equality under extra reduction hypotheses do not settle existence of such a gap; later point-well single-interface results differ.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is a strict gap above twice the single-interface cell cost for both collapsing double profiles in a frame-indifferent two-well density. The published energy lower bound and equality under extra reduction hypotheses do not settle existence of such a gap; later point-well single-interface results differ.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/JEMS/1385); [comparison source 2](https://ems.press/content/serial-article-files/49943); [comparison source 3](https://arxiv.org/html/2510.01893v1); [comparison source 4](https://arxiv.org/html/2607.15133v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known cases.** Proposition 3.16 gives $`\min\{K_{\mathrm{dp}}^A,K_{\mathrm{dp}}^B\}\ge2K`$. Under the additional condition
```math
W(F)\ge W\!\left(I_d+(|Fe_d|-1)e_d\otimes e_d\right)
\qquad(F\in\mathbb R^{d\times d}),
```
Proposition 3.17 gives $`K_{\mathrm{dp}}^A=K_{\mathrm{dp}}^B=2K`$. That extra condition is not imposed on the sought example.

**Source scope.** The authors propose a strict gap for some densities after their compatibility result. This entry states an existential specialization in their H1–H7 class; it does not identify this with a universal fixed-parameter claim. It uses the refined $`K`$ from (3.5), rather than the isotropic $`K_0`$, and preserves the order of the two suprema, the infimum and the limsup in (3.27). Unequal double-profile costs alone would not settle it.

**Later results.** The 2025 point-well theorem gives a conditional periodic formula for a single interface. The 2026 heterogeneous point-well theorem omits frame indifference and imposes a one-dimensional reduction assumption for recovery sequences. Neither supplies nor excludes this strict gap. Their current arXiv histories show only v1.

**Duplicates and announcements.** AIM 155 concerns a three-well quasiconvex hull; AIM 222 concerns force balance; AIM 233 concerns stiffness-tensor closure. The existing FURTHER quadratic two-well relaxation problem asks for equality of convex envelopes. Their statements differ from the cell constants above. All local finding decisions and the AIM/OpenAI duplicate index were searched, with current public catalogue and announcement checks; no equivalent target or matching resolution was located.

**Review limits.** The authoritative 93-page published source was used; its 64-page arXiv v1 was not assumed identical. Selected definitions, statements and native formula images were checked independently; complete proofs were not audited. The search is dated and bounded. Prove2Me timed out, and indexed queries returned no exact match; this does not certify absence from the whole site.

[Source and current-status audit](../FURTHER_problems/_tracking/journal1148-two-well-owner-scope-current-audit-2026-10-23.json) · [Duplicate comparison](../FURTHER_problems/_tracking/two-well-double-profile-duplicate-review-2026-10-23.json).

[Coordinating review](../FURTHER_problems/_tracking/two-well-double-profile-coordinator-review-2026-10-23.json) · [Independent published-source audit](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/davoli-friedrich-double-profile-independent-published-scope-20261023.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-52e41be6f37ecd2d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
