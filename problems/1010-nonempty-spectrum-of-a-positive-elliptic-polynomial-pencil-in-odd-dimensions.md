# 1010. Nonempty spectrum of a positive-elliptic polynomial pencil in odd dimensions

**Area:** Spectral theory and partial differential equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`d\ge5`$ be odd. Let $`P\in\mathbb R[x_1,\ldots,x_d]`$ have degree $`m\ge2`$, with leading homogeneous part satisfying

```math
P_m(x)>0\qquad\text{for every }x\in\mathbb R^d\setminus\{0\}.
```


Must there exist $`\lambda\in\mathbb C`$ and a nonzero complex-valued Schwartz function $`u\in\mathcal S(\mathbb R^d)`$ such that

```math
\bigl[-\Delta+(P(x)-\lambda)^2\bigr]u(x)=0
\qquad (x\in\mathbb R^d)?
```


The quantifier is over every such polynomial, including lower-degree terms. Positivity of $`P_m`$ forces $`m`$ to be even. The equation is linear in $`u`$ and quadratic in the spectral parameter. The question asks for existence of at least one eigenvalue; completeness of generalized eigenfunctions and stronger trace-coefficient conjectures are separate questions.

## Application

This asks whether a confining differential-operator pencil necessarily has nonempty spectrum. Such pencils occur in the study of analytic regularity for differential operators with multiple characteristics and in spectral approaches to damped oscillations.

## References

1. F. Aboud and D. Robert, *Asymptotic expansion for nonlinear eigenvalue problems*, Journal de Mathématiques Pures et Appliquées **93**(2) (2010), 149–162. [Publisher and DOI](https://doi.org/10.1016/j.matpur.2009.08.009); [primary preprint](https://arxiv.org/abs/0903.0919). The formulation is in the introduction, preprint pp. 1–2; Remark 3.4 on p. 6 treats lower-degree terms.
2. F. Aboud, F. Jauberteau and D. Robert, *Numerical approaches to compute spectra of non-self adjoint operators in dimensions two and three*, arXiv:2412.02465v1 (2024). [Primary text](https://arxiv.org/html/2412.02465v1), introduction and conclusion.
3. F. M. Aboud, *Existence of solution for some quasi-homogenous and quasi-elliptic Nonlinear Eigenvalue Problems*, ZANCO Journal of Pure and Applied Sciences **31**(s2) (2019), 70–80. [DOI](https://doi.org/10.21271/ZJPAS.31.s2.9). Theorems 4.1 and 5.1 impose additional hypotheses.

## Status review


**Known cases:** Every positive-elliptic polynomial in every odd dimension at least five must have an eigenvalue. The general trace-expansion method gives only selected polynomial classes; the 2025 numerical paper concerns dimensions two and three.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every positive-elliptic polynomial in every odd dimension at least five must have an eigenvalue. The general trace-expansion method gives only selected polynomial classes; the 2025 numerical paper concerns dimensions two and three.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 27 October 2026. The primary work proves the assertion for $`d=3`$ and selected classes in dimensions 5 and 7, alongside earlier results in even dimensions and dimension 1. The 2024 introduction still states the general conjecture and distinguishes these established cases. Its bounded-domain numerical computations do not prove the whole-space assertion above. The 2019 quasi-elliptic results have additional order and positivity conditions and do not establish this universal odd-dimensional Laplacian statement.

Current and announcement searches located no matching complete resolution. The all-status AIM collection, the indexed OpenAI announcements and the saved FURTHER collection were checked for equivalent models. Negative searches provide bounded evidence. The dated review records exact source versions, comparisons and access limitations; they do not certify every cited proof.

Review evidence: [dated source, current-status and independent comparison record](../FURTHER_problems/_tracking/C134-09030919-polynomial-pencil-root-current-gate-20261027/ROOT-FINAL-FORMULATION-CURRENT-AND-INDEPENDENT-ADMISSION-PASS.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0f69f513463d629e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
