# 1043. An L³ maximal estimate for planar Zakharov–Kuznetsov flow

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`f\in\mathcal S(\mathbb R^2)`$ define the linear Zakharov–Kuznetsov evolution by

```math
\widehat{U(t)f}(\xi,\eta)=e^{it\xi(\xi^2+\eta^2)}\widehat f(\xi,\eta).
```


Does every $`s>2/3`$ admit a constant $`C_s<\infty`$ such that

```math
\left(\int_{\mathbb R}\left[\sup_{y\in\mathbb R,\,0\le t\le1}
|U(t)f(x,y)|\right]^3\,dx\right)^{1/3}
\le C_s\|f\|_{H^s(\mathbb R^2)}
\qquad\text{for all }f\in\mathcal S(\mathbb R^2)?
```


Here $`\|f\|_{H^s}=\|(1+\xi^2+\eta^2)^{s/2}\widehat f\|_2`$, with a fixed unitary Fourier normalization. The constant is independent of $`f`$. This is [1, Conjecture 4.1], using its space–time maximal norm. The endpoint $`s=2/3`$ is not requested.

## Application

The bound controls dispersive wave amplitudes after maximizing over transverse position and a fixed time interval. The source explains its relevance to a proof of quartic Zakharov–Kuznetsov local well-posedness at low Sobolev regularity.

## References

1. F. Linares and J. P. G. Ramos, [*Maximal function estimates and local well-posedness for the generalized Zakharov–Kuznetsov equation*](https://arxiv.org/html/2005.12485v1), arXiv:2005.12485v1 (26 May 2020), equations (1.3)–(1.5), Proposition 1.1, Theorem 1.2 and §4.1, Conjecture 4.1 (PDF p. 19). Published in *SIAM Journal on Mathematical Analysis* **53**(1) (2021), 914–936, [DOI](https://doi.org/10.1137/20M1344524). The conjecture numbering and formulation here refer to the preprint.
2. S. Correia and P. Leite, [*Sharp local existence and nonlinear smoothing for dispersive equations with higher-order nonlinearities*](https://doi.org/10.1007/s00209-025-03768-w), *Mathematische Zeitschrift* **310**, article 60 (2025), Theorem 1.3.
3. J. Nowicki-Koth, [*Low-regularity global well-posedness theory for the generalized Zakharov–Kuznetsov equation on $`\mathbb R\times\mathbb T`$ and polynomial growth of higher Sobolev norms*](https://arxiv.org/html/2603.24737v1), arXiv:2603.24737v1 (2026), Theorems 1.1–1.2 and Remark 3.4.

## Status review


**Known cases:** The Lx3 Ly,t-infinity linear maximal estimate must hold for every s>2/3. Existing s>3/4 bounds and nonlinear wellposedness/smoothing results do not supply it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The Lx3 Ly,t-infinity linear maximal estimate must hold for every s>2/3. Existing s>3/4 bounds and nonlinear wellposedness/smoothing results do not supply it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 23 October 2026. Source [1] gives this bound for $`s>3/4`$ and a necessary condition $`s\ge2/3`$. Results [2]–[3] concern nonlinear evolution; such results do not imply the conjectured linear estimate.

The [coordinator audit](../FURTHER_problems/_tracking/zk-l3-maximal-coordinator-review-2026-10-23.json) and [independent review](../FURTHER_problems/_tracking/parallel/continuum/author-books-cue-breadth-20261022/zk-maximal-linares-ramos-independent-bounded-check-20261023.json) found no matching later proof, counterexample or announced solution in bounded searches. They compare recent Strichartz and Benjamin–Ono–Zakharov–Kuznetsov results by their actual norms and propagators. The latest arXiv revision is v1. The final SIAM body was unavailable; full published-version parity is not claimed.

The [all-status duplicate audit](../FURTHER_problems/_tracking/zk-l3-maximal-all-status-duplicate-review-2026-10-23.json) distinguishes AIM 356–357's coupled three-dimensional Zakharov system and the [existing cylindrical quartic question](../cut_problems/FURTHER_problems/waves-fluids-kinetics/lead-fb522d0b2c439706.md). This target is a linear estimate on the plane. Dated, bounded checks cannot guarantee that no unindexed resolution exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-09b43f6041aa2e94**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
