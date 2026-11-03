# 106. Payne's Dirichlet–buckling comparison in Euclidean domains

**Area:** Spectral geometry and elastic stability
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\geq2`$ and let $`\Omega\subset\mathbb R^n`$ be a nonempty bounded connected domain with $`C^2`$ boundary. Write $`0<\lambda_1\leq\lambda_2\leq\cdots`$ for the Dirichlet eigenvalues of $`-\Delta`$, counted with multiplicity:
```math
-\Delta\varphi=\lambda\varphi\quad\text{in }\Omega,\qquad
\varphi=0\quad\text{on }\partial\Omega.
```
Write $`0<\Lambda_1\leq\Lambda_2\leq\cdots`$ for the clamped buckling eigenvalues, with multiplicity:
```math
\Delta^2u+\Lambda\Delta u=0\quad\text{in }\Omega,\qquad
u=\partial_\nu u=0\quad\text{on }\partial\Omega.
```
Here $`\nu`$ is the outward unit normal. Precisely, using $`H^j_0(\Omega)`$ for the closure of $`C^\infty_c(\Omega)`$ in $`H^j(\Omega)`$, the two lists are
```math
\lambda_k=\min_{\substack{E\subset H^1_0(\Omega)\\\dim E=k}}
 \max_{0\ne v\in E}\frac{\int_\Omega|\nabla v|^2\,dx}{\int_\Omega |v|^2\,dx},
\qquad
\Lambda_k=\min_{\substack{E\subset H^2_0(\Omega)\\\dim E=k}}
 \max_{0\ne u\in E}\frac{\int_\Omega|\Delta u|^2\,dx}{\int_\Omega|\nabla u|^2\,dx}.
```
Does
```math
\lambda_{k+1}(\Omega)\leq\Lambda_k(\Omega)
\qquad\text{hold for every }k\geq1?
```

This is Payne's planar comparison [1], together with the higher-dimensional Euclidean extension recorded in [2, equation (1.15)]. No convexity or simple-connectivity assumption is imposed. The question concerns these two spectra of the same domain. Both eigenvalue parameters scale as length to the power $`-2`$.

## Application

The domain supports two models: membrane vibrations and buckling of a clamped elastic plate. The comparison would bound successive normalized instability loads from below using the next membrane eigenvalue.

## References

1. L. E. Payne, *Inequalities for eigenvalues of membranes and plates*, Journal of Rational Mechanics and Analysis **4** (1955), 517–529. Historical attribution and the corrected first-index result are discussed in [3, §1].
2. G. Liu, *Some inequalities and asymptotic formulas for eigenvalues on Riemannian manifolds*, [arXiv:0906.2043v1](https://arxiv.org/pdf/0906.2043v1) (2009), equations (1.2), (1.4), (1.15), and Example 4.1.
3. M. Levitin and I. Polterovich, *Payne's conjecture for buckling eigenvalues of odd index*, [arXiv:2609.12235v2](https://arxiv.org/pdf/2609.12235v2) (28 September 2026), Theorem 1 and Remarks 3–5.
4. D. Buoso and P. Freitas, *Sharp inequalities and asymptotics for polyharmonic eigenvalues*, Calculus of Variations and Partial Differential Equations **64** (2025), no. 9, article 295, [DOI: 10.1007/s00526-025-03069-4](https://doi.org/10.1007/s00526-025-03069-4). [arXiv:2506.12791v1, §4](https://arxiv.org/html/2506.12791v1#S4).
5. D. Buoso and V. Lotoreichik, *A note on the failure of Payne's inequality on manifolds with boundary*, [arXiv:2610.20097v1](https://arxiv.org/html/2610.20097v1) (14 October 2026), introduction and §3.
6. G. Liu, *The Payne conjecture for Dirichlet and Buckling eigenvalues*, [arXiv:2109.02561v2](https://arxiv.org/abs/2109.02561v2), withdrawn 23 September 2021; the official notice identifies an error in the proof of Lemma 4.2.

## Status review


**Known cases:** The first-index comparison holds in every Euclidean dimension. In the plane, all odd buckling indices are proved; an even index is also covered when its buckling eigenvalue equals the next one. See the dated results below.

**Remaining target:** Establish or refute the displayed comparison for every remaining even planar index, and for all remaining indices in Euclidean dimensions three and higher, on the full stated class of bounded connected domains.

The first-index inequality $`\lambda_2\leq\Lambda_1`$ is known in every Euclidean dimension; see [3, Remark 5] and [4, Theorem 4.1] with $`m=t=1`$. The same-index inequality $`\lambda_k<\Lambda_k`$ is also known [3, Remark 3]; it does not supply the requested extra index.

The September 2026 preprint [3] establishes
```math
\lambda_{2m}(\Omega)\leq\Lambda_{2m-1}(\Omega)\qquad(m\geq1)
```
for every bounded open planar set, a class larger than the smooth connected domains asked for here. In the plane it also settles an even index $`k`$ when $`\Lambda_k=\Lambda_{k+1}`$, by monotonicity [3, Remark 4]. General even planar indices remain open in the October 2026 primary [5]. The present entry retains the family across dimensions, with these cases explicitly separated from the remaining question.

Dimension one is excluded: intervals violate the comparison at every even buckling index [2, Example 4.1; 3, Remark 4]. The counterexamples in [5] concern intrinsic cylindrical or hemispherical geometries; those are not counterexamples on bounded Euclidean domains with their ordinary metric. The full-proof claim in [6] was withdrawn and is not treated as a resolution.

The existing first-buckling shape optimization and buckling-ratio questions ([AIM 007](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/007-buckling-load-ball.md) and [008](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/008-buckling-eigenvalue-ratio.md)), [Pólya's counting inequalities](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/001-polya-eigenvalue-bound.md), and [Payne's nodal-line problem](https://github.com/MColbrook/AIM/blob/8729eab98bafe409b66c5e39253bf56569a62327/problems/117-convex-higher-dimensional-payne.md) have different targets. No matching full resolution or later complete announcement was located in the checked current literature and AIM, FURTHER, and OpenAI records. This is a bounded formulation and status review, rather than a certification of every cited proof.


### Online recheck, 2026-10-30

The 28 September 2026 version of Levitin and Polterovich proves odd buckling indices in the plane and some even indices with adjacent equal buckling eigenvalues. The 14 October 2026 Buoso-Lotoreichik paper explicitly leaves the general even planar case open; its counterexamples concern intrinsic manifolds, not Euclidean domains. The older all-index proof was withdrawn after an identified Lemma 4.2 error. Fresh searches through 30 October 2026 found no matching complete resolution or announced solution of the stated all-dimensional Euclidean comparison.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2609.12235); [status source 2](https://arxiv.org/html/2609.12235v2); [status source 3](https://arxiv.org/abs/2610.20097); [status source 4](https://arxiv.org/html/2610.20097v1); [status source 5](https://arxiv.org/abs/2109.02561). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ec2b23395e04846f** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
