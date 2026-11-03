# 1012. Bishop's mean-eigenvalue conjecture for three regions on the sphere

**Area:** Spectral geometry and shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D_1,D_2,D_3`$ be pairwise disjoint nonempty connected open subsets of the round unit sphere $`\mathbb S^2`$. Define the first Dirichlet eigenvalue by
```math
\lambda_1(D)=\inf_{0\ne u\in H^1_0(D)}
\frac{\int_D|\nabla_{\mathbb S^2}u|^2\,dS}{\int_D|u|^2\,dS},
```

where $`H^1_0(D)`$ is the closure of $`C_c^\infty(D)`$ in the spherical $`H^1`$ norm.

Must every such triple satisfy
```math
\lambda_1(D_1)+\lambda_1(D_2)+\lambda_1(D_3)\ge\frac{45}{4}?
```

Equivalently, is the smallest possible **mean** eigenvalue $`15/4`$, attained by the Y-partition into three equal spherical lunes of opening $`2\pi/3`$?

In spherical coordinates, each lune has a positive ground state proportional to
```math
(\sin\theta)^{3/2}\sin(3\phi/2),\qquad 0<\phi<2\pi/3,
```

with eigenvalue $`(3/2)(5/2)=15/4`$. The competitors have no prescribed area, symmetry or interface. Their union need not exhaust the sphere. Only the optimal value and Y-partition's minimality are asked; no uniqueness assertion for arbitrary open representatives is added.

## Application

The sum of the ground-state energies measures the total lowest vibration energy of three separated regions on a spherical shell. The conjecture identifies the optimal division without imposing equal areas in advance.

## References

1. B. Helffer, T. Hoffmann-Ostenhof and S. Terracini, [*On spectral minimal partitions: the case of the sphere*](https://arxiv.org/html/0903.3326), Conjecture 1.2 and Eqs.(1.2)–(1.8); *Around the Research of Vladimir Maz'ya III*, International Mathematical Series **13** (2010), 153–178. [DOI](https://doi.org/10.1007/978-1-4419-1345-6_6).
2. V. Bonnaillie-Noël, B. Helffer and T. Hoffmann-Ostenhof, [*Nodal domains, spectral minimal partitions, and their relation to Aharonov–Bohm operators*](https://arxiv.org/html/1711.01174), §6.2 (2017).
3. R. Ognibene and B. Velichkov, [*Structure of the free interfaces near triple junction singularities in harmonic maps and optimal partition problems*](https://arxiv.org/html/2412.00781v5), §1.2, Problem 1.5 and Corollary 3.6, v5 (7 September 2026).
4. M. Sundqvist, [*The Y-partition is the optimal three-partition for the disc and the harmonic oscillator*](https://arxiv.org/html/2609.21964), §1.4 (18 September 2026).

## Status review


**Known cases:** The objective is the mean, not the maximum, of three first eigenvalues on the sphere. The 2026 disk/oscillator and triple-junction results explicitly distinguish these objectives and do not prove the sum bound.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The objective is the mean, not the maximum, of three first eigenvalues on the sphere. The 2026 disk/oscillator and triple-junction results explicitly distinguish these objectives and do not prove the sum bound.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The known spherical theorem minimizes the **maximum** of the three eigenvalues. It does not establish the conjectured lower bound on their mean. The September 2026 papers explicitly distinguish these objectives; the new disc and harmonic-oscillator results also concern the maximum.

The [coordinating review](../FURTHER_problems/_tracking/focused-Bishop-spherical-mean-three-partition-C210-C-20261028/ROOT-INDEPENDENT-UNIT-SPHERE-MEAN-VS-MAX-PRIMARY-LATEST-AND-SEMANTIC-FINAL-REVIEW.json) and [independent model review](../FURTHER_problems/_tracking/focused-Bishop-spherical-mean-three-partition-C210-C-20261028/A-INDEPENDENT-UNIT-SPHERE-MEAN-NORMALIZATION-OPEN-DOMAIN-BRIDGE-AND-MAX-SCOPE-MODEL-PEER.json) check normalization, current sources and semantic duplicates. The regular-domain formulation extends to arbitrary open cells by Dirichlet Rayleigh approximation, without extending an equality classification. No matching mean-value resolution or complete announcement was located.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-11b7e75a12da58cf**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
