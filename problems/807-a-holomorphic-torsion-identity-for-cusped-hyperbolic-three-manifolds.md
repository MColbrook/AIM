# 807. A holomorphic torsion identity for cusped hyperbolic three-manifolds

**Area:** Hyperbolic geometry and topological invariants
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-03

## Problem statement

Let $`M_0`$ be an oriented complete hyperbolic three-manifold of finite volume, with curvature $`-1`$ and $`h\ge1`$ torus cusps. Choose peripheral bases $`(m_i,l_i)`$. Write $`u=0`$ for the complete point of the local complex deformation space $`D(M_0)`$. For nearby, possibly incomplete structures $`M_u`$, write $`v_i=\tau_i(u)u_i`$ for the holomorphic peripheral logarithm relation; $`\mathrm{Im}\tau_i(0)>0`$.

For $`n\ge3`$, let

```math
T_n(u)=\mathcal T(M_u,\rho_u^{\,2(n-1)},\{m_i\}),
\qquad E(u)=\exp(2\pi f(u)).
```

Here $`\rho_u^{\,k}`$ is the $`k`$th symmetric power of a lift of the holonomy, of dimension $`k+1`$; even $`k`$ makes the representation independent of the lift. The complex Reidemeister torsion uses Park's convention and the homology bases induced by the meridians. The Yoshida function $`f`$ is normalized as in [1, §6.2], with $`\pi^2f(0)=\mathrm{Vol}(M_0)+2\pi^2i\mathrm{CS}(M_0)`$ modulo $`i\pi^2\mathbb Z`$. Thus $`E`$ is the holomorphic, branch-independent function in Theorem 6.2.

Use **exactly** the deformation Zograf product $`F_n(M_u)`$ of [1, equation (6-3)]: it is formed from primitive loxodromic holonomy conjugacy classes deforming loxodromic classes of the complete structure, with factors $`1-q_\gamma(u)^m`$, $`m\ge n`$. Newly loxodromic classes are excluded. Its complex-length multiplier at the complete structure is $`q_\gamma(0)=\exp[-(\ell_\gamma+i\theta_\gamma)]`$. This definition does not assert a fixed primitive-class indexing in $`\pi_1(M_0)`$ under Dehn filling.

Set $`\eta(\tau)=e^{\pi i\tau/12}\prod_{m\ge1}(1-e^{2\pi im\tau})`$. **Is there a neighborhood $`V`$ of $`0`$ such that, for every integer $`n\ge3`$, some constant $`c_{M_0,n}`$ with $`|c_{M_0,n}|=1`$ satisfies**

```math
T_n(u)^{-12}\prod_{i=1}^h\eta(\tau_i(u))^{-24}
=c_{M_0,n}\,E(u)^{6n^2-6n+1}F_n(M_u)^{12}
\qquad(u\in V)?
```

The constant may depend on $`M_0,n`$, but not on $`u`$. This is the even symmetric-power conjecture [1, Conjecture 1.2]; the odd representation formula is a separate question.

## Application

The identity would determine the complex phase relating torsion, complex volume, cusp modular data and the complex lengths of closed geodesics throughout a local deformation family.

## References

1. J. Park, *Reidemeister torsion, complex volume and the Zograf infinite product for hyperbolic 3-manifolds*, Geometry & Topology **23** (2019), 3687–3734, [DOI](https://doi.org/10.2140/gt.2019.23.3687), [published text](https://msp.org/gt/2019/23-7/gt-v23-n7-p10-p.pdf), Conjecture 1.2 and §6.2. The earlier cusped manuscript is [arXiv:1712.08270v1](https://arxiv.org/abs/1712.08270v1).

## Status review


**Known cases:** The final Geometry and Topology paper retains the holomorphic cusped identity as Conjecture 1.2 (p. 3689). Closed-manifold torsion formulas and the absolute-value identity at the complete cusped structure do not provide the phase-sensitive holomorphic identity throughout the deformation neighborhood.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The final Geometry and Topology paper retains the holomorphic cusped identity as Conjecture 1.2 (p. 3689). Closed-manifold torsion formulas and the absolute-value identity at the complete cusped structure do not provide the phase-sensitive holomorphic identity throughout the deformation neighborhood.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 2026-10-29. The published paper retains this conjecture and proves its absolute-value counterpart at the complete structure. That single-point modulus statement does not establish constancy of the holomorphic quotient on a deformation neighborhood. Closed-manifold identities do not supply the missing cusp statement.

Bounded primary-source, latest-version, proof and announcement searches found no matching complete resolution. All-status AIM/OpenAI and FURTHER semantic comparisons found no equivalent target. The [owner review](../FURTHER_problems/_tracking/focused-cusped-hyperbolic-torsion-phase-Park-C244-C-20261029/OWNER-EXACT-EVEN-SYMMETRIC-POWER-CUSP-TORSION-HOLOMORPHIC-PHASE-PRIMARY-PUBLISHED-CURRENT-DUPLICATE-PROPOSAL.json) and [coordinating review](../FURTHER_problems/_tracking/focused-cusped-hyperbolic-torsion-phase-Park-C244-C-20261029/ROOT-PUBLISHED-EVEN-CUSP-PHASE-NORMALIZATION-PRODUCT-SCOPE-AND-CURRENT-FINAL-REVIEW.json) retain the independent model check and the source-product qualification.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-7c1a12d538ddaacd**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
