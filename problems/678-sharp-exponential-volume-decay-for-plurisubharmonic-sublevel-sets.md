# 678. Sharp exponential volume decay for plurisubharmonic sublevel sets

**Area:** Complex analysis and potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each integer $`n\ge2`$, does there exist a constant $`C_n`$ with the following property? Let $`\Omega\subset\mathbb C^n`$ be any bounded hyperconvex domain, let $`\varphi\in\mathcal F(\Omega)`$, and put

```math
\mu=\left(\int_\Omega(dd^c\varphi)^n\right)^{1/n}>0,
\qquad dd^c=\frac{i}{\pi}\partial\bar\partial.
```

Is it true that, for every $`s>0`$,

```math
\mathrm{Vol}_{2n}\{z\in\Omega:\varphi(z)<-s\}
\le C_n\mathrm{diam}(\Omega)^{2n}
\exp\!\left(-\frac{2ns}{\mu}\right)?
```

Here hyperconvex means that the domain has a continuous negative plurisubharmonic exhaustion. The Cegrell class $`\mathcal F(\Omega)`$ consists of decreasing limits $`\varphi_j\downarrow\varphi`$ with $`\varphi_j\in\mathcal E_0(\Omega)`$ and uniformly bounded total Monge–Ampère masses. The class $`\mathcal E_0`$ consists of bounded negative plurisubharmonic functions with boundary limit zero and finite total Monge–Ampère mass. The measure for $`\varphi`$ is its Cegrell Monge–Ampère measure.

## Application

The estimate would sharpen control of the volume occupied by large negative potentials. It is related to optimal exponential integrability and Moser–Trudinger and Brezis–Merle inequalities for complex Monge–Ampère equations.

## References

- S. Dinew, V. Guedj and A. Zeriahi, [*Open problems in pluripotential theory*](https://arxiv.org/pdf/1511.00705v1), Question 35 and Theorem 5.1, p. 17; *Complex Variables and Elliptic Equations* 61(7) (2016), 902–930, DOI 10.1080/17476933.2015.1121481.
- P. Åhag, U. Cegrell, S. Kołodziej, H. H. Phạm and A. Zeriahi, [*Partial pluricomplex energy and integrability exponents of plurisubharmonic functions*](https://arxiv.org/pdf/0804.3954v3), Theorem A, Theorem 4.1 and Corollary 4.2; *Advances in Mathematics* 222(6) (2009), 2036–2058, DOI 10.1016/j.aim.2009.07.002.
- R. J. Berman and B. Berndtsson, [*Moser–Trudinger type inequalities for complex Monge–Ampère operators and Aubin's “hypothèse fondamentale”*](https://www.numdam.org/item/10.5802/afst.1704.pdf), *Annales de la Faculté des Sciences de Toulouse* 31(3) (2022), 595–645, DOI 10.5802/afst.1704.

## Status review


**Known cases:** Question 35 removes the polynomial prefactor while retaining the critical exponential rate and diameter/mass dependence. Real Monge-Ampere torsion, complex energy-integrability and complex-Sobolev capacity results do not imply that critical weak-tail estimate. No matching complete resolution or announcement located in the fresh named-question and broader venue searches.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Question 35 removes the polynomial prefactor while retaining the critical exponential rate and diameter/mass dependence. Real Monge-Ampere torsion, complex energy-integrability and complex-Sobolev capacity results do not imply that critical weak-tail estimate. No matching complete resolution or announcement located in the fresh named-question and broader venue searches.

Additional comparison sources: [comparison source 1](https://www.math.univ-toulouse.fr/~zeriahi/DGZ-arXiv2015.pdf); [comparison source 2](https://www.numdam.org/item/10.5802/afst.1704.pdf); [comparison source 3](https://arxiv.org/abs/2602.13968). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The established bound has the additional factor $`(1+s/\mu)^{n-1}`$. The question retains its exact exponential rate and removes that factor. The one-dimensional analogue is known. Estimates with a smaller exponential rate, extra symmetry, or an integrated exponential bound with a different dependence on the mass do not automatically establish the displayed inequality.

The survey uses $`\lambda`$ for the mass parameter in its preceding theorem and $`\mu`$ in Question 35. The normalization above follows the original Åhag–Cegrell–Kołodziej–Phạm–Zeriahi paper, where $`\mu^n`$ is the total mass. This removes the survey's notational ambiguity.

Literature searches through 16 October 2026 found no matching complete resolution. The completed catalogue comparison found no matching announcement in the returned contexts. This is a literature review, not a guarantee that no solution exists.

Berman–Berndtsson Theorem 1.6 improves a subcritical integrated exponential bound, and is sharp in its stated sense for complex dimension two. This does not by itself give the displayed critical weak-tail estimate. The [2026 complex-Sobolev capacity estimates](https://arxiv.org/abs/2602.13968v1) concern a different norm and retain domain-dependent, suboptimal constants.

Review evidence: [dated mathematical scope and current-status packet](../FURTHER_problems/_tracking/parallel/complex-bayesian/sharp-sublevel-volume-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-15ce012b8d4d1662**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
