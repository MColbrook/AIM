# 761. Hilbertianity of almost-everywhere tangents in PI spaces

**Area:** Metric geometry and analysis on singular spaces
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,d,m)`$ be a complete separable metric space with a nonzero Borel measure $`m`$ of full support, finite on bounded sets. Suppose that it is a **PI space** in the source's sense: $`m`$ is doubling, and a weak $`(1,2)`$-Poincaré inequality holds. Explicitly, there are constants $`C_D,C_P<\infty`$ and $`\lambda\ge1`$ such that
```math
m(B_{2r}(x))\le C_Dm(B_r(x)),\qquad
\fint_{B_r(x)}|u-u_{B_r(x)}|\,dm
\le C_Pr\left(\fint_{B_{\lambda r}(x)}\mathrm{lip}(u)^2\,dm\right)^{1/2}
```

for every $`x\in X`$, $`r>0`$, and boundedly supported Lipschitz function $`u`$. Here $`u_B=\fint_Bu\,dm`$ and $`\mathrm{lip}(u)`$ is its pointwise Lipschitz slope.

Assume that $`X`$ is **infinitesimally Hilbertian**: the Sobolev space $`W^{1,2}(X,d,m)`$, defined by relaxation of the squared Lipschitz slope, is Hilbert. Equivalently, its Cheeger energy is a quadratic form.

A pointed measured Gromov–Hausdorff tangent at $`x`$ is any limit
```math
\left(X,\frac{d}{r_j},\frac{m}{m(B_{r_j}(x))},x\right)
\xrightarrow{\mathrm{pmGH}}(Y,d_Y,m_Y,y),
\qquad r_j\downarrow0.
```


Is it true that, for $`m`$-almost every $`x\in X`$, **every** such tangent $`(Y,d_Y,m_Y)`$ is infinitesimally Hilbertian?

No rectifiability or curvature bound is assumed. The target does not require uniqueness of the tangent or that it be isometric to a Hilbert space; it asks for Hilbertianity of its Sobolev space.

## Application

Infinitesimal Hilbertianity expresses a quadratic energy and linear heat flow on a possibly singular space. The question asks whether this analytic structure persists in all geometric limits obtained by magnifying around typical points, under the doubling and Poincaré assumptions used in analysis on nonsmooth spaces.

## Known progress

The source proves the assertion for $`m`$-rectifiable PI spaces (Theorem 1.4). It also constructs a PI example with a non-Hilbertian tangent at an exceptional point (Theorem 1.2). This does not refute an almost-everywhere assertion. Its non-PI example has non-Hilbertian tangents almost everywhere (Theorem 1.1), so the Poincaré assumption matters.

Finite-dimensional RCD spaces satisfy the conclusion through stability of synthetic curvature bounds. Later results establishing universal infinitesimal Hilbertianity under a curve-splitting hypothesis or for metric surfaces do not establish the all-tangents assertion for general PI spaces. Magnabosco–Rigoni construct a different, equivalent metric under a locally Minkowski assumption; Ryborz’s examples have a base space which is itself not infinitesimally Hilbertian. Neither result answers the question for the original infinitesimally Hilbertian PI space.

## References

1. D. Lučić, E. Pasqualetto and T. Rajala, *Non-Hilbertian tangents to Hilbertian spaces*, [arXiv:2111.06777v1](https://arxiv.org/abs/2111.06777v1), Question 1.5 and Theorem 1.4, native p. 4; Sections 2.1 and 2.3, native pp. 5 and 7. Published in *Proceedings of the Royal Society of Edinburgh Section A: Mathematics* **153**(3) (2023), 811–832, [doi:10.1017/prm.2022.18](https://doi.org/10.1017/prm.2022.18).
2. J. Núñez-Zimbrón, E. Pasqualetto and E. Soultanis, *Spaces with Riemannian curvature bounds are universally infinitesimally Hilbertian*, [arXiv:2508.05483v2](https://arxiv.org/abs/2508.05483v2), revised 11 September 2025, Theorem 1.2 and Corollary 1.4. The latest version uses a weak infinitesimal curve-splitting condition.
3. A. Lytchak and E. Soultanis, *Infinitesimally Euclidean metric surfaces*, [arXiv:2610.24626v1](https://arxiv.org/abs/2610.24626v1), submitted 17 October 2026, Theorems 1.1–1.3. These concern metric surfaces with locally finite Hausdorff two-measure.

4. M. Magnabosco and C. Rigoni, *A Canonical Infinitesimally Hilbertian Structure on Locally Minkowski Spaces*, *Potential Analysis* **63** (2025), 999–1031, [doi:10.1007/s11118-025-10196-2](https://doi.org/10.1007/s11118-025-10196-2), Theorem 1.2.
5. V. Ryborz, *The Infinitesimal Structure of Manifolds With Non-continuous Riemannian Metrics*, *Journal of Geometric Analysis* **36** (2026), 313, [doi:10.1007/s12220-026-02556-0](https://doi.org/10.1007/s12220-026-02556-0), Theorem 2.

## Status review


**Known cases:** The inspected non-Hilbertian tangent counterexample explicitly lacks a Poincare inequality. Its Question 1.5 retains the almost-everywhere PI target. Rectifiable PI and curvature-bounded Hilbertian cases do not cover arbitrary PI spaces.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The inspected non-Hilbertian tangent counterexample explicitly lacks a Poincare inequality. Its Question 1.5 retains the almost-everywhere PI target. Rectifiable PI and curvature-bounded Hilbertian cases do not cover arbitrary PI spaces.

Additional comparison sources: [comparison source 1](https://arxiv.org/abs/2111.06777v1); [comparison source 2](https://doi.org/10.1017/prm.2022.18); [comparison source 3](https://arxiv.org/abs/2508.05483v2); [comparison source 4](https://arxiv.org/abs/2610.24626v1); [comparison source 5](https://doi.org/10.1007/s11118-025-10196-2); [comparison source 6](https://doi.org/10.1007/s12220-026-02556-0). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 24 October 2026 against the eligible question, its definitions and counterexamples, current primary comparison statements, the all-status AIM/FURTHER duplicate index, the unchanged checked OpenAI announcement catalogue, and indexed Prove2Me results. The live Prove2Me homepage subset was also inspected; this does not cover every mission. No matching proof, counterexample or announced resolution was located in the bounded searches. Selected native windows, version pins and explicit access gaps are retained; no whole-paper proof audit or exhaustive literature claim is made.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-02921abee874d00d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
