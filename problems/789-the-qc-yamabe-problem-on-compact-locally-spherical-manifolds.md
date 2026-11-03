# 789. The qc Yamabe problem on compact locally spherical manifolds

**Area:** Sub-Riemannian geometry; nonlinear subelliptic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq1`$, and let $`M`$ be a smooth, closed, connected manifold of dimension $`4n+3`$, equipped with a quaternionic-contact structure and a fixed **globally defined** contact form $`\eta=(\eta_1,\eta_2,\eta_3)`$. Its horizontal distribution is $`H=\ker\eta`$, with the compatible horizontal metric $`g_\eta`$. In dimension seven, assume the Reeb-field condition required for the canonical Biquard connection, as specified in [4, §2].

Assume the structure is **locally qc conformal to the standard quaternionic-contact sphere**: every point has a neighborhood qc-conformally equivalent to an open subset of $`S^{4n+3}`$ with its standard structure. No global spherical identification or locally 3-Sasakian representative is assumed.

Write $`Q=4n+6`$, let $`\mathrm{Scal}_\eta`$ be the scalar curvature of the Biquard connection, and use the traced-Hessian horizontal sub-Laplacian
```math
\Delta_\eta u=\mathrm{tr}_{g_\eta}(\nabla du).
```

Must there exist $`u\in C^\infty(M)`$, $`u>0`$, and a constant $`C\in\mathbb R`$ such that
```math
4\frac{Q+2}{Q-2}\,\Delta_\eta u
-\mathrm{Scal}_\eta\,u
=-C\,u^{(Q+2)/(Q-2)}?
```
Equivalently, must the conformal contact form
```math
\bar\eta=u^{4/(Q-2)}\eta
```
have constant qc scalar curvature $`C`$? Any positive smooth solution suffices; minimization of the Yamabe functional is not required.

## Source and scope

The eligible source used here is Ivanov–Minchev–Vassilev [1], **native PDF p. 2 / printed p. 1042**: the paragraph posing the general compact qc Yamabe problem and the displayed equation immediately afterward. Native p. 5 / printed p. 1045 specifies the globally defined contact-form convention. The locally spherical restriction isolates the branch outside the later non-locally-spherical existence theorem [3]; it is a labelled residual of the original general question.

The all-dimensional classification of solutions conformal to the **standard sphere**, discussed in [1, native pp. 3–4], has a later resolution [4] and is separate from the existence question stated here.

## Application

This problem asks whether a qc conformal class admits a constant-scalar-curvature normalization. It links the geometry of horizontal distributions to a critical nonlinear equation for a subelliptic operator.

## References

1. **Stefan Ivanov, Ivan Minchev and Dimiter Vassilev**, *Extremals for the Sobolev inequality on the seven-dimensional quaternionic Heisenberg group and the quaternionic contact Yamabe problem*, Journal of the European Mathematical Society **12**(4) (2010), 1041–1067. [DOI: 10.4171/JEMS/222](https://doi.org/10.4171/JEMS/222). [Eligible source, native p. 2](https://ems.press/content/serial-article-files/31733?nt=1#page=2); definitions also native p. 5.
2. **Wei Wang**, *The Yamabe problem on quaternionic contact manifolds*, Annali di Matematica Pura ed Applicata **186** (2007), 359–380; first published online in 2006. [DOI: 10.1007/s10231-006-0010-5](https://doi.org/10.1007/s10231-006-0010-5). Strict-Yamabe-inequality existence criterion; also stated precisely in [3, introduction].
3. **Stefan Ivanov and Alexander Petkov**, *The qc Yamabe problem on non-spherical quaternionic contact manifolds*, Journal de Mathématiques Pures et Appliquées **118** (2018), 44–81. [DOI: 10.1016/j.matpur.2018.06.011](https://doi.org/10.1016/j.matpur.2018.06.011). [arXiv:1612.02406v1](https://arxiv.org/html/1612.02406v1), Theorem 1.1 and the preceding strict-inequality criterion.
4. **Stefan Ivanov, Ivan Minchev and Dimiter Vassilev**, *Solution of the qc Yamabe equation on a 3-Sasakian manifold and the quaternionic Heisenberg group*, Analysis & PDE **16**(3) (2023), 839–860. [DOI: 10.2140/apde.2023.16.839](https://doi.org/10.2140/apde.2023.16.839). [arXiv:1504.03142v1](https://arxiv.org/html/1504.03142v1), Theorems 1.1 and 1.3; §2 gives the seven-dimensional Reeb condition.
5. **Yun Shi and Wei Wang**, *On conformal qc geometry, spherical qc manifolds and convex cocompact subgroups of $`\mathrm{Sp}(n+1,1)`$*, Annals of Global Analysis and Geometry **49** (2016), 271–307. [DOI: 10.1007/s10455-015-9492-y](https://doi.org/10.1007/s10455-015-9492-y). [arXiv:1509.05961v1](https://arxiv.org/html/1509.05961v1), introduction and Proposition 3.5: scalar-sign classification and the separate qc positive-mass conjecture.
6. **Giuseppe Pipoli**, *Nonhomogeneous expanding flows in hyperbolic spaces*, Annals of Global Analysis and Geometry **62** (2022), 847–867. [DOI: 10.1007/s10455-022-09873-x](https://doi.org/10.1007/s10455-022-09873-x), Lemma 2.4. Its qc clause concerns the standard sphere with an $`S^3`$-invariant conformal factor.

## Status review


**Known cases:** Non-locally-spherical qc Yamabe existence is already known and is excluded from this residual target. The strict Yamabe-constant criterion and globally locally-3-Sasakian representatives do not supply a positive smooth solution for every locally spherical class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Non-locally-spherical qc Yamabe existence is already known and is excluded from this residual target. The strict Yamabe-constant criterion and globally locally-3-Sasakian representatives do not supply a positive smooth solution for every locally spherical class.

Additional comparison sources: [comparison source 1](https://doi.org/10.4171/JEMS/222); [comparison source 2](https://ems.press/content/serial-article-files/31733?nt=1#page=2); [comparison source 3](https://doi.org/10.1007/s10231-006-0010-5); [comparison source 4](https://doi.org/10.1016/j.matpur.2018.06.011); [comparison source 5](https://arxiv.org/html/1612.02406v1); [comparison source 6](https://doi.org/10.2140/apde.2023.16.839); [comparison source 7](https://arxiv.org/html/1504.03142v1); [comparison source 8](https://doi.org/10.1007/s10455-015-9492-y). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Known progress.** Let $`\lambda(M,[\eta])`$ be the infimum of the qc Yamabe quotient
```math
\frac{\displaystyle\int_M
 \left(4\frac{Q+2}{Q-2}|\nabla_H v|^2+
       \mathrm{Scal}_\eta v^2\right)\,dV_\eta}
 {\left(\displaystyle\int_M v^{2Q/(Q-2)}\,dV_\eta\right)^{(Q-2)/Q}},
 \qquad v\in C^\infty(M),\quad v>0,
```
and let $`\Lambda=\lambda(S^{4n+3})>0`$ be the standard sphere value in the same convention. Wang's criterion [2] gives a positive smooth solution whenever $`\lambda(M,[\eta])<\Lambda`$. This covers **all nonpositive Yamabe classes and many positive classes**, including locally spherical classes satisfying that strict inequality. Ivanov–Petkov [3] establishes the inequality for every compact non-locally-spherical structure, in all dimensions. The standard sphere and classes already containing a compact locally 3-Sasakian representative are also solved [4].

**Remaining target.** The requested conclusion is existence for every compact locally spherical conformal class in the statement, including those not covered by these known results. Local qc conformal flatness alone does not provide a global locally 3-Sasakian representative. A scalar-positive representative supplied by a sign-classification theorem need not have constant scalar curvature. The positive-mass conjecture in [5] is a separate statement; no equivalence with this existence question is asserted.

**Literature check and limits.** Bounded primary-source and announcement searches through **25 October 2026** located no full resolution covering this entire statement. The reviewed theorem statements and selected original pages do not constitute a full proof audit or exhaustive literature search. The 1,702-row all-status AIM/OpenAI index and the observed 887-record FURTHER findings export contained no matching target in the completed bounded comparisons. Cached Prove2Me descriptions yielded no matching qc-Yamabe entry; full live mission clearance remains unverified.

**Source-review extent.** Original native pp. 2–5 and the specified later theorem/definition passages were actually read. No whole-paper, full-source, solution, Lean or additional coverage credit is claimed.

**Admission review:** 25 October 2026. The recorded primary-statement, current-status and semantic duplicate checks were completed before admission. Public AIM-head and complete OpenAI-CONTENTS comparisons were refreshed without a change. The dated, bounded search and access limits above remain part of this assessment.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4f90f0ff635663f0**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
