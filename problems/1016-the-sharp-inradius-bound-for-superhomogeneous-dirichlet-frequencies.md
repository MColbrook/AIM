# 1016. The sharp inradius bound for superhomogeneous Dirichlet frequencies

**Area:** Spectral theory and spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-11-03

## Problem statement

Fix $`N\ge2`$, $`1<p<\infty`$, and a superhomogeneous exponent $`q>p`$ in the range
```math
\begin{cases}
 q<\dfrac{Np}{N-p},&p<N,\\
 q<\infty,&p=N,\\
 q\le\infty,&p>N.
 \end{cases}
```

For a nonempty bounded open convex set $`\Omega\subset\mathbb R^N`$, define its ordinary Euclidean inradius and Dirichlet Poincaré–Sobolev frequency by
```math
R_\Omega=\sup\{r>0:\exists x,\ B_r(x)\subset\Omega\},\qquad
 \lambda_{p,q}(\Omega)=
 \inf_{\substack{u\in C_c^\infty(\Omega)\\u\ne0}}
 \frac{\int_\Omega|\nabla u|^p\,dx}
      {\|u\|_{L^q(\Omega)}^p}.
```

Determine the exact constant
```math
C_{\mathrm{opt}}(N,p,q)=
 \inf_{\substack{\Omega\subset\mathbb R^N\\
                  \Omega\text{ nonempty, bounded, open, convex}}}
 R_\Omega^{\,p-N+Np/q}\lambda_{p,q}(\Omega),
 \qquad \frac1\infty=0.
```


Scaling permits the equivalent constraint $`R_\Omega=1`$. The target is the optimal universal **lower-bound constant**, with no volume, perimeter or capacitary-inradius factor. Neither attainment by a bounded domain nor a particular minimizing shape is presumed.

## Application

The constant gives the best domain-independent control of a nonlinear Dirichlet frequency from the radius of the largest inscribed ball. Such bounds connect Sobolev inequalities and nonlinear eigenvalue estimates with geometric design constraints.

## References

- L. Brasco, *On principal frequencies and inradius in convex sets*, **Bruno Pini Mathematical Analysis Seminar** 9(1) (2018), 78–101. [Published article](https://doi.org/10.6092/issn.2240-2829/8945); [published PDF](https://mathematicalanalysis.unibo.it/article/download/8945/8866/28804), Proposition 6.3, equation (15), p. 99, and Open problems 1, p. 100.
- G. Pisante and F. Prinari, *Sharp Makai-type inequalities for the best Poincaré–Sobolev constants* (2026), [arXiv:2604.11973v1](https://arxiv.org/html/2604.11973), Theorem 1.1 and Section 1.4.
- F. Bozzola and L. Brasco, *The Role of Topology and Capacity in Some Bounds for Principal Frequencies*, **Journal of Geometric Analysis** 34 (2024), 299. [Published article](https://doi.org/10.1007/s12220-024-01742-2), Theorems 1.2–1.3.
1. M. J. Colbrook, [*Critical inradius asymptotics and a supremum-norm bound for convex domains*](../research/solutions/1016-inradius-critical-asymptotics/aim1016.pdf), 3 November 2026. [TeX source](../research/solutions/1016-inradius-critical-asymptotics/aim1016.tex), [package and reproduction](../research/solutions/1016-inradius-critical-asymptotics/README.md), and [independent AI review](../research/solution_reviews/2026-11-03-spectral-batch/1016-review.md).

## Status review

**Known cases:** For $`p=N`$, the critical large-$`q`$ asymptotic is $`q^{N-1}C_{\mathrm{opt}}(N,N,q)\to |S^{N-1}|(eN^2/(N-1))^{N-1}`$. A separate explicit lower bound is proved for $`q=\infty,\ p\ge N+1`$; it is not asserted sharp.

**Remaining target:** Determine the exact optimal constant at fixed finite parameters and in the other admissible regimes. The supremum-norm bound is not proved sharp and does not cover $`N<p<N+1`$.

**Reviewed result, 2026-11-03:** The critical large-q asymptotic is determined uniformly over convex domains; a separate explicit supremum-norm lower bound holds for p at least N+1. The [manuscript](../research/solutions/1016-inradius-critical-asymptotics/aim1016.pdf) and [individual audit](../research/solution_reviews/2026-11-03-spectral-batch/1016-review.md) record the proof, checked references and exact target comparison. Review was performed by Codex (AI).

### Earlier status check, 2026-10-30

The sharp constant uses only ordinary inradius and q>p. The 2026 sharp Makai-type results impose q<=p and different geometric factors; extremal functions on a fixed domain do not solve optimization over convex shapes.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. Brasco proves a positive bound and explicitly asks for its sharp constant. The question here selects the $`q>p`$ component of the source's two-part question.

The 2026 “complete picture” of sharp geometric inequalities is explicitly restricted to $`q\le p`$ and combinations of two geometric quantities. Later general-domain bounds and existence results for extremal functions do not identify this optimal constant over convex shapes. No matching general determination or complete announcement was found. Particular parameter cases may be known; the full parameter-dependent determination is the target.

Semantic checks against the AIM/OpenAI all-status corpus and developing collection found no equivalent problem. These are dated searches, not a proof that no unlocated result exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-357f10178e95f713**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
