# 856. Can every interior Neumann–Steklov eigenvalue pair be realized by a planar domain?

**Area:** Spectral geometry and shape optimization
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D\subset\mathbb R^2`$ be the unit disk. For a nonempty bounded connected open set $`\Omega\subset\mathbb R^2`$ with Lipschitz boundary, write $`|\Omega|`$ for its area and $`P(\Omega)`$ for its total boundary length, including boundaries of any holes. Let $`\mu_1(\Omega)`$ and $`\sigma_1(\Omega)`$ be the first positive eigenvalues of
```math
-\Delta u=\mu u,\quad \partial_\nu u=0,
\qquad
\Delta v=0,\quad \partial_\nu v=\sigma v,
```

respectively. Both spectra are counted with multiplicity from their zero eigenvalue at index $`0`$.

Prove or disprove that for every pair
```math
0<x<8\pi,\qquad 0<y<\pi\mu_1(D)
```

there exists such a domain $`\Omega`$ satisfying
```math
P(\Omega)\sigma_1(\Omega)=x,\qquad
|\Omega|\mu_1(\Omega)=y.
```

There is no convexity or simple connectivity restriction. The question concerns exact simultaneous attainment.

## Application

These two scale invariant quantities describe the first bulk Neumann mode and the first Steklov boundary mode. Determining their joint range would show how independently these normalized frequencies can be prescribed by changing a planar shape and its topology.

## Known results and scope

Henrot and Michetti [1, Section 5.1, Theorem 5.1] prove that the **closure** of the attainable diagram is the full rectangle
```math
[0,8\pi]\times[0,\pi\mu_1(D)].
```

Their constructions approximate pairs; they do not establish exact realization of every interior pair.

Conjecture 1 in the published paper [1, p. 1436] asks for the exact diagram when disconnected Lipschitz open sets are also allowed:
```math
(0,8\pi)\times(0,\pi\mu_1(D))
\;\cup\;\{(0,0)\}
\;\cup\;\{(2\pi,\pi\mu_1(D))\}.
```

Disconnected sets give the origin. The disk is the only shape attaining the top Neumann boundary; the Steklov upper boundary is excluded by a strict inequality. Thus the remaining question is precisely the positive interior realization problem above.

The original July 2021 version already asks for interior attainment, but its displayed diagram incorrectly includes the two zero axes. The revised and published versions correct those axes. We use the corrected formulation. The author's 2022 thesis retains this question as Conjecture 3.1 [2, p. 80].

The more recent results of Acampora, Amato and Cristoforoni [3, Theorems 1.3–1.4] concern the ratio of eigenvalues on collapsing convex domains and associated one dimensional profiles. They do not settle joint attainment on arbitrary planar Lipschitz domains.

## References

1. A. Henrot and M. Michetti, [*A comparison between Neumann and Steklov eigenvalues*](https://ems.press/content/serial-article-files/33905?nt=1), *Journal of Spectral Theory* **12** (2022), 1405–1442, [DOI 10.4171/JST/429](https://doi.org/10.4171/JST/429), Section 5.1, Theorem 5.1 and Conjecture 1. Original source: [arXiv:2107.10075v1](https://arxiv.org/abs/2107.10075v1), submitted 21 July 2021; [revised author manuscript](https://cvgmt.sns.it/media/doc/paper/5203/HM_CompNeummStekSub.pdf), 3 March 2022.
2. M. Michetti, [*Steklov and Neumann eigenvalues: inequalities, asymptotic and mixed problems*](https://docnum.univ-lorraine.fr/public/DDOC_T_2022_0109_MICHETTI.pdf), doctoral thesis, Université de Lorraine, defended 13 September 2022, Section 3.5.1, Conjecture 3.1, p. 80.
3. P. Acampora, V. Amato and E. Cristoforoni, [*Estimates on the Neumann and Steklov principal eigenvalues of collapsing domains*](https://arxiv.org/pdf/2307.12889v2), *Communications in Contemporary Mathematics* **28** (2026), 2550027, [DOI 10.1142/S0219199725500270](https://doi.org/10.1142/S0219199725500270). The version checked is arXiv:2307.12889v2, revised 3 March 2025.

## Status review


**Known cases:** The known closure of the joint attainable diagram does not imply every interior point is attained exactly. Collapsing convex-domain ratio estimates and one-dimensional profile bounds have different hypotheses and conclusions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known closure of the joint attainable diagram does not imply every interior point is attained exactly. Collapsing convex-domain ratio estimates and one-dimensional profile bounds have different hypotheses and conclusions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded searches through 24 October 2026 found no complete proof, counterexample or announced resolution of exact interior joint attainment. The closure theorem and convex thin-domain ratio estimates have different conclusions. Current AIM/OpenAI index entries and admitted FURTHER statements were checked for equivalent targets; no match was found. This is a literature and duplicate check, not a proof that no solution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-e460bb55f648870f**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
