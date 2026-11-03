# 319. Generic stabilization by static output feedback

**Area:** Feedback control and real algebraic geometry

**Status:** 🔵 OPEN

**Last checked:** 2026-09-17

## Problem statement

For positive integers $`m,p`$, put $`n=mp`$ and consider all real matrix triples

```math
\mathcal A_{m,p}
=\mathbb R^{n\times n}\times\mathbb R^{n\times m}
\times\mathbb R^{p\times n}.
```

A triple $`(A,B,C)`$ describes the continuous-time system

```math
\dot x=Ax+Bu,\qquad y=Cx,
```

with $`n`$ state coordinates, $`m`$ inputs and $`p`$ measured outputs. A static output-feedback controller is a constant real matrix $`K\in\mathbb R^{m\times p}`$ implementing $`u=Ky`$. It gives the closed-loop matrix $`A+BKC`$.

Call a real matrix **Hurwitz** when every eigenvalue has strictly negative real part, and define

```math
\mathcal S_{m,p}
=\{(A,B,C)\in\mathcal A_{m,p}:
\text{ there exists }K\in\mathbb R^{m\times p}
\text{ for which }A+BKC\text{ is Hurwitz}\}.
```

**Determine exactly which pairs $`(m,p)`$ make $`\mathcal S_{m,p}`$ dense in $`\mathcal A_{m,p}`$ in the ordinary Euclidean topology.**

The set $`\mathcal S_{m,p}`$ is already open: a stabilizing gain continues to stabilize sufficiently small perturbations of its plant. Thus density means that an open dense set of plants admits some stabilizing gain, which may depend on the plant. The gain has no prescribed magnitude or sparsity, but it must be constant in time and use only the measured output. The question concerns real gains and continuous-time stability.

This is the critical-dimension case of the Byrnes–Anderson generic-stabilization question, explicitly posed in Eremenko's 2010 note. It asks for a dimension classification valid for all positive integer pairs, beyond known cases. It does not ask merely for an algorithm deciding stabilization of one given triple: real-algebraic decision procedures already provide that in principle.

## Application

A static controller directly mixes available sensor signals into actuator inputs, without maintaining an observer or other internal controller state. The classification would identify when the numbers of inputs and outputs generically suffice to stabilize a linear plant at the threshold $`mp=n`$, where the number of freely chosen gain coefficients equals the state dimension. It describes a basic capability of this controller architecture; it does not by itself provide a well-conditioned design method, small gains or robustness guarantees for every plant.

## References

- [Christopher I. Byrnes and Brian D. O. Anderson, *Output feedback and generic stabilizability*, SIAM Journal on Control and Optimization 22(3) (1984), 362–380](https://doi.org/10.1137/0322024). The accessible [earlier manuscript in NASA report CR-166441](https://ntrs.nasa.gov/api/citations/19830010078/downloads/19830010078.pdf) has §2, Question 2 and Theorems 1–3, printed pp. 113–115, and the counterexample in §4. These are report page numbers, not journal pagination.
- [Alexandre Eremenko, *Stabilizability by static output feedback*, 20 October 2010](https://www.math.purdue.edu/~eremenko/dvi/gpolep.pdf), model on p. 1, Question on p. 2 and equivalent geometric formulation on pp. 3–4; also listed under polynomial matrices on his [expert problem page](https://www.math.purdue.edu/~eremenko/uns1.html).
- [Alexandre Eremenko and Andrei Gabrielov, *Pole placement by static output feedback for generic linear systems*, SIAM Journal on Control and Optimization 41(1) (2002), 303–312](https://www.math.purdue.edu/~gabriea/feedback_siam.pdf), §1, Theorem A, Theorem 1.1 and the stabilization question on p. 306.
- [Matthias Franke, *Eigenvalue assignment by static output feedback—on a new solvability condition and the computation of low gain feedback matrices*, International Journal of Control 87(1) (2014), 64–75](https://doi.org/10.1080/00207179.2013.822102); [accepted manuscript](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/ae917e07-970e-4d22-a0d5-f4842c9fbb08/content), Lemma 2.2, Theorem 2.3, Remark 5 and §5.
- [Klaus Röbenack and Rick Voßwinkel, *Eigenvalue Placement by Quantifier Elimination – the Static Output Feedback Problem*, Acta Cybernetica 24 (2020), 409–427](https://cyber.bibl.u-szeged.hu/index.php/actcybern/article/download/4054/3995), §§3–5.
- [Adrian Ilka and Nikolce Murgovski, *Novel Results on Output-Feedback LQR Design*, IEEE Transactions on Automatic Control 68(9) (2023), 5187–5200](https://research.chalmers.se/publication/533170/file/533170_Fulltext.pdf), Theorems 1–2.
- [Laura Menini, Corrado Possieri and Antonio Tornambè, *Exact certificates for the solvability of stabilization problems through numerical algebraic geometry*, Automatica 182 (2025), 112523](https://doi.org/10.1016/j.automatica.2025.112523), accessible publisher-indexed introduction and Theorem 3 excerpt.
- [Johan Löfberg, *Static output-feedback stabilization is NP-hard*, arXiv:2609.16886v1, 15 September 2026](https://arxiv.org/html/2609.16886v1), §1, Theorem 1.1. Preprint.
- [Abdulrahman H. Bajodah and Hassen Mibar, *Static output feedback pole placement via parameter-dependent Ackermann and Greville matrix formulae*, ISA Transactions 167, Part B (2025), 1660–1670](https://doi.org/10.1016/j.isatra.2025.09.017), accessible publisher-indexed formulation and introduction.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The September 17, 2026 search covered generic stabilizability/stabilisability, static output feedback, pole assignment, the critical equality, original and later authors, recent claims, corrections and withdrawals. The [evidence record](../research/expansion-2026-09/candidates/generic-static-output-feedback-stabilization.json) records source access and theorem comparisons. Eremenko's maintained problem list still includes the question. That item has no individual 2026 review date; the dated formulation is from 2010. Byrnes–Anderson and the independent Eremenko–Gabrielov work explicitly distinguish stabilization from full pole assignment.

Known cases include a positive answer when $`m=1`$ or $`p=1`$ and a negative answer at $`(m,p)=(2,2)`$, where a nonempty open family is not stabilizable. Further positive cases occur when the smaller of $`m,p`$ is $`2`$ and the larger is $`2^r-1`$ for an integer $`r\ge2`$, by the odd-degree criterion. Away from the critical equality, $`n<mp`$ permits generic real pole assignment. The complete critical classification is the target, with all dimension pairs counted as one problem.

Eremenko–Gabrielov prove failure of generic arbitrary pole assignment when both $`m,p`$ are even. Omitting some prescribed spectra does not establish that all Hurwitz spectra are unavailable; their paper separately leaves the stabilization question open. Franke's necessary-and-sufficient condition concerns the pole-placement map of an individual plant. Röbenack–Voßwinkel's reference to a solved pole-placement problem points to that result; their quantifier-elimination tests likewise do not classify all critical dimension pairs.

Ilka–Murgovski's 2023 LQR Theorems 1–2 also give plant-dependent Riccati conditions and convergence under existence hypotheses. The 2025 Menini–Possieri–Tornambè exact-certificate paper treats parameters of a specified polynomial; its publisher-indexed theorem excerpt was checked, but full-text access failed. Neither accessible result gives the requested all-pairs criterion.

The publication refresh also checked Löfberg's September 15, 2026 hardness claim. Theorem 1.1 constructs individual single-input plants with state dimension $`D=6(q+r)`$ from instances with $`r`$ elements and $`q`$ constraints, and with $`r`$ outputs. Thus $`D>r`$, outside the critical equality for those plants. Its worst-case decision-complexity conclusion does not classify the generic critical-dimensional locus. This comparison does not certify the new reduction's proof.

Later results on descriptor-system controllability and time-delayed feedback use different admissible inputs or controllers. The reviewed 2025 Ackermann/Greville paper describes plant-dependent algebraic conditions; only its publisher excerpt was accessible, and no general dimension-classification claim was found there. These limits, and the older dates of the explicit status sources, remain recorded in the audit.

This differs from the [Belgian chocolate threshold](../cut_problems/problems/308-belgian-chocolate-threshold.md), which concerns a particular scalar plant family and stable dynamic controllers of unrestricted finite order. The [Witsenhausen benchmark](134-witsenhausen-exact-optimum.md) instead asks for an optimal cost in a decentralized stochastic control problem.

Resolution searches and duplicate checks were refreshed immediately before the September 17, 2026 batch integration. Review was a separated adversarial self-pass; no independent agent or human review is claimed.
