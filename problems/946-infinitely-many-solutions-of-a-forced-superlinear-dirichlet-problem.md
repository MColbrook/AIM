# 946. Infinitely many solutions of a forced superlinear Dirichlet problem

**Area:** PDEs and materials
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge3`$, let $`\Omega\subset\mathbb R^n`$ be a smooth bounded domain, and let
```math
1<p<\frac{n+2}{n-2}.
```

For every $`w\in L^2(\Omega)`$, does the Dirichlet problem
```math
-\Delta u=|u|^{p-1}u+w\quad\text{in }\Omega,
\qquad u=0\quad\text{on }\partial\Omega
```

have infinitely many distinct weak solutions in $`H^1_0(\Omega)`$?

Here a weak solution satisfies
```math
\int_\Omega\nabla u\cdot\nabla v\,dx
 =\int_\Omega (|u|^{p-1}u+w)v\,dx
 \qquad\text{for every }v\in H^1_0(\Omega).
```

The subcritical exponent makes this weak formulation well-defined. The conjecture concerns every forcing $`w`$, without symmetry or smallness assumptions, throughout the subcritical range and for arbitrary smooth bounded domains. “Infinitely many” is the requested conclusion; no additional prescribed energy growth or nodal pattern is imposed.

## Application

The equation models a nonlinear equilibrium subject to an external forcing. In the unforced problem, symmetry supports the construction of infinitely many equilibria. The conjecture asks whether their multiplicity survives arbitrary square-integrable forcing.

## Known progress

The source explains that infinitely many solutions are known for every $`w\in L^2(\Omega)`$ when $`1<p<n/(n-2)`$. Its own construction supplies solutions under an additional gluing condition; it does not establish that condition for every smooth bounded domain.

Molle and Passaseo's 2023 Theorem 2.1 proves the full subcritical range for every forcing when $`\Omega`$ is a cube. Their introduction discusses extensions to domains admitting particular reflection-symmetric, two-colourable tessellations. This geometric result leaves the arbitrary smooth-domain question above open. Cubes are cited as a related domain class; their corners are not being treated as smooth boundary.

A 2026 preprint of Chong Li and Shujie Li announces infinitely many solutions under an Ambrosetti–Rabinowitz condition and additional assumptions, including $`f(x,t)=o(t)`$ as $`t\to0`$. This fails for arbitrary nonzero additive forcing. Their Remark 1.3 explicitly distinguishes the external-force model. Its stated theorem therefore does not settle this target; this comparison does not certify its proof.

## Status review


**Known cases:** The 2023 result restricts the domain to cubes. Li-Li Remark 1.3 explicitly distinguishes its AR nonlinearities from the additive-forcing Bahri-Lions model; it does not settle this all-domain L2 forcing assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2023 result restricts the domain to cubes. Li-Li Remark 1.3 explicitly distinguishes its AR nonlinearities from the additive-forcing Bahri-Lions model; it does not settle this all-domain L2 forcing assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The eligible 2021 statement, equation and limits of its construction were checked in native PDF pages 1–3. The complete 2023 publisher HTML introduction and Theorem 2.1 were read. Its scope is explicitly cubic domains; the author repository confirms that restriction. The author's research and publication list, updated August 2026, and targeted searches for a later or announced general solution did not reveal a matching resolution as of this review.

An author-hosted PDF returned an access denial, and the publisher PDF route did not return a validated native PDF. These gaps are recorded; the 2023 theorem comparison uses the available primary publisher HTML. This review does not certify either paper's full proof.

The all-status AIM/OpenAI index and the current FURTHER findings were checked. The retrieved MEMS extremal-solution regularity problem, Ising conformal-universality problem and embedded self-shrinker problem have different equations and conclusions.

## References

1. R. Molle and D. Passaseo, *Infinitely many solutions for elliptic equations with non-symmetric nonlinearities*, [arXiv:2112.02298v1](https://arxiv.org/abs/2112.02298v1), 2021. Published in *Calculus of Variations and Partial Differential Equations* **61** (2022), article 115.
2. R. Molle and D. Passaseo, *On the Bahri–Lions conjecture for elliptic equations with non-symmetric nonlinearities*, *Calculus of Variations and Partial Differential Equations* **62** (2023), article 177, [doi:10.1007/s00526-023-02507-5](https://link.springer.com/article/10.1007/s00526-023-02507-5), especially the introduction and Theorem 2.1.
3. [Riccardo Molle's research and publication list](https://riccardomollemath.github.io/research/), updated August 2026; [author repository record for the 2023 article](https://art.torvergata.it/handle/2108/323744).

4. C. Li and S. Li, *A proof for the conjecture on superlinear problems with Ambrosetti–Rabinowitz condition*, [arXiv:2601.14825v1](https://arxiv.org/abs/2601.14825v1), 2026, assumptions $`(f_1^\prime),(f_2),(f_3)`$, Theorem 1.1 and Remark 1.3.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-6e4f1a923de86fa6**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
