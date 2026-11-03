# 933. Bounded point interpolation in Hardy spaces of Dirichlet series

**Area:** Function spaces and interpolation theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For $`1<p<\infty`$, $`p\ne2`$, characterize the bounded sequences $`S=(s_j)`$ of distinct points in $`\{s\in\mathbb C:\mathrm{Re}s>1/2\}`$ that interpolate for the Hardy space $`\mathscr H^p`$ of ordinary Dirichlet series. Also obtain quantitative estimates for the interpolation constant $`M_{\mathscr H^p}(S)`$ as the points approach the critical line $`\mathrm{Re}s=1/2`$ [1, concluding question in Section 9].

Here $`\mathscr H^p`$ is the completion of Dirichlet polynomials in the mean-value $`p`$-norm. In the source's definition, interpolation means that for each data sequence $`(a_j)`$ with
```math
\sum_j |a_j|^p\,\|\delta_{s_j}\|^{-p}<\infty,
  \qquad \|\delta_{s_j}\|=\zeta(2\mathrm{Re}s_j)^{1/p},
```

there is an $`f\in\mathscr H^p`$ with $`f(s_j)=a_j`$ and norm bounded by $`M_{\mathscr H^p}(S)`$ times the displayed weighted $`\ell^p`$ norm [1, Section 4.1].

## Application

Point interpolation controls how well functions in $`\mathscr H^p`$ can match prescribed values near their critical boundary. The original paper identifies the missing sequence characterization and constants as obstacles to sharper approximation-number estimates for composition operators.

## Known results and scope

The bounded-sequence case for $`\mathscr H^2`$ is characterized by a local interpolation theorem [2]. The 2016 paper gives an $`\mathscr H^1`$ bound through squaring an $`\mathscr H^2`$ interpolant and finite-sequence estimates away from the critical line [1, Section 4]. Those do not give the requested uniform characterization and near-boundary estimates for $`1<p<\infty`$, $`p\ne2`$. A 2026 preprint announces a solution of the **different local embedding inequality** also listed at the end of [1]; its stated results do not answer this point-interpolation question [3].

## References

1. F. Bayart, H. Queffélec and K. Seip, [*Approximation numbers of composition operators on $`H^p`$ spaces of Dirichlet series*](https://aif.centre-mersenne.org/item/10.5802/aif.3019.pdf), *Annales de l'Institut Fourier* **66** (2016), no. 2, 551–588, Sections 4.1 and 9. [DOI](https://doi.org/10.5802/aif.3019).
2. J.-F. Olsen and K. Seip, [*Local interpolation in Hilbert spaces of Dirichlet series*](https://arxiv.org/abs/math/0608506), *Proceedings of the American Mathematical Society* **136** (2008), 203–212.
3. B. Chen, X. Fang, F. Guo, S. Hou, Y. Shao and Q. Zhou, [*The Local Embedding Problem for Hardy Spaces of Dirichlet Series*](https://arxiv.org/abs/2609.11560v2), arXiv preprint (2026), Theorem 1.1 and Corollary 1.2.

## Status review


**Known cases:** The July 2026 Maletzki theorem is for the bounded Dirichlet-series algebra H-infinity. It does not give the weighted finite-p interpolation characterization or its boundary constants; the recent local embedding result is also a different assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The July 2026 Maletzki theorem is for the bounded Dirichlet-series algebra H-infinity. It does not give the weighted finite-p interpolation characterization or its boundary constants; the recent local embedding result is also a different assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The [source, later-result and duplicate audit](../FURTHER_problems/_tracking/hardy-dirichlet-interpolating-sequences-status-2026-10-21.json) separates point interpolation from local norm embedding and from interpolation between function spaces. No complete solution or announced settlement of the exact point-sequence task was found in bounded searches through 21 October 2026.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-eaa457344ff9ca20**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
