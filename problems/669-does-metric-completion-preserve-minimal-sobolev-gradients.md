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

## Application

Minimal upper gradients measure the local variation used in Sobolev energies and nonlinear potential theory. Exact preservation would allow completion of the underlying space without changing this energy density on the original domain.

## References

1. Anders Björn and Jana Björn, *Poincaré inequalities and Newtonian Sobolev functions on noncomplete metric spaces*, Journal of Differential Equations **266** (2019), 44–69. [Published paper](https://doi.org/10.1016/j.jde.2018.07.029); [latest arXiv version](https://arxiv.org/abs/1705.02253). Definitions 1.1 and 3.5, Theorem 4.1 and Open Problem 4.4; the latter appears on native page 8 of version 2.
2. Anders Björn and Jana Björn, *Corrigendum* to the preceding paper, Journal of Differential Equations **285** (2021), 493–495. [Corrigendum](https://doi.org/10.1016/j.jde.2021.03.008). The corrected completion-measure convention is also stated explicitly in reference 3, Section 4.
3. Anders Björn, Jana Björn and Panu Lahti, *Removable sets for Newtonian Sobolev spaces and a characterization of p-path almost open sets*, Revista Matemática Iberoamericana **39** (2023), 1143–1180. [Published paper](https://doi.org/10.4171/RMI/1419). Page 1145 explicitly retains the uncertainty over whether $`A_0>1`$ is ever necessary; Theorem 5.4 requires a $`p`$-path almost openness hypothesis for its full equivalences.
4. Luigi Ambrosio, Toni Ikonen, Danka Lučić and Enrico Pasqualetto, *Metric Sobolev spaces I: equivalence of definitions* (2024), [arXiv:2404.11190](https://arxiv.org/abs/2404.11190). Definition 2.1 and Theorem 7.1 compare Sobolev definitions on a complete space; they do not establish preservation under passage from a noncomplete space to its completion.

## Status review


**Known cases:** The completion question asks for equality of the minimal gradients, not equivalence of Sobolev definitions on a complete space. Path-almost-open special cases remain stronger assumptions. The 2026 S-gradient/Hajlasz characterization and single-test-plan results do not imply exact preservation for every noncomplete doubling PI space. No matching full resolution located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The completion question asks for equality of the minimal gradients, not equivalence of Sobolev definitions on a complete space. Path-almost-open special cases remain stronger assumptions. The 2026 S-gradient/Hajlasz characterization and single-test-plan results do not imply exact preservation for every noncomplete doubling PI space. No matching full resolution located.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/1705.02253); [comparison source 2](https://doi.org/10.4171/RMI/1419); [comparison source 3](https://arxiv.org/abs/2404.11190); [comparison source 4](https://link.springer.com/article/10.1007/s43034-026-00519-8). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The irrational-line example in reference 1 fails the required Poincaré inequality and does not settle this problem. The 2023 extension theorem and its non-path-open example also leave the universal equality question unresolved. Current searches found no matching complete resolution or announcement. These bounded AI checks are not human peer review or a certificate of openness.

The [source/current review](../FURTHER_problems/_tracking/C161-metric-completion-gradient-Root-precise-gate-20261028/ROOT-EXACT-PRIMARY-CORRECTION-CURRENT-ANNOUNCEMENT-AND-FORMAL-MODEL-PASS.json), [independent source review](../FURTHER_problems/_tracking/C161-METRIC-COMPLETION-GRADIENT-FOUR-EXACT-PRIMARY-PAGES-PIXELS-CANONICAL-MEASURE-FORMULATION-PEER-C-END-20261028.json) and [all-status comparison](../FURTHER_problems/_tracking/C161-metric-completion-gradient-Root-precise-gate-20261028/ROOT-FINAL-SPECIFIC-FIVE-MODEL-SEMANTIC-COMPARISONS-COMPLETE.json) preserve the hypotheses, access limits and checked corpus.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-01e261c83de5a707**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
