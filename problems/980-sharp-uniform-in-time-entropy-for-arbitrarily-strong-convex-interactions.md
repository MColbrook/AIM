# 980. Sharp uniform-in-time entropy for arbitrarily strong convex interactions

**Area:** Interacting diffusions and mean-field approximation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Fix $`d\ge1`$ and $`\sigma>0`$. Let $`U,W\in C^\infty(\mathbb R^d)`$ have globally bounded derivatives of every order at least two. Suppose that $`W(x)=W(-x)`$ and, for some finite $`M,L`$ and $`\alpha>0`$,

```math
\alpha I_d\preceq D^2U(x)\preceq M I_d,
\qquad 0\preceq D^2W(x)\preceq L I_d
\qquad(x\in\mathbb R^d).
```

There is no upper restriction on $`L/\alpha`$. For every integer $`n\ge2`$, let $`B^1,\ldots,B^n`$ be independent standard $`d`$-dimensional Brownian motions, independent of initial values with joint law $`\mu_0^{\otimes n}`$, where $`\mu_0=\mathcal N(0,I_d)`$. Consider

```math
dX_t^{i,n}=-\left[\nabla U(X_t^{i,n})+
\frac1n\sum_{j=1}^n\nabla W(X_t^{i,n}-X_t^{j,n})\right]dt
+\sqrt2\sigma\,dB_t^i,
\qquad 1\le i\le n.
```

Let $`\mu_t=\mathrm{Law}(\bar X_t)`$ solve the McKean–Vlasov equation

```math
d\bar X_t=-\left[\nabla U(\bar X_t)+
\int_{\mathbb R^d}\nabla W(\bar X_t-y)\,\mu_t(dy)\right]dt
+\sqrt2\sigma\,dB_t,
\qquad \bar X_0\sim\mu_0,
```

and put $`P_t^{n,k}=\mathrm{Law}(X_t^{1,n},\ldots,X_t^{k,n})`$. Does there exist a finite constant $`C=C(d,\sigma,U,W)`$, independent of $`n,k,t`$, such that

```math
\sup_{t\ge0}H\!\left(P_t^{n,k}\,\middle|\,\mu_t^{\otimes k}\right)
\le C\left(\frac{k}{n}\right)^2
\qquad(n\ge2,\ 1\le k\le n)?
```

Here $`H(\nu\mid\eta)=\int\log(d\nu/d\eta)\,d\nu`$ when $`\nu\ll\eta`$, and $`+\infty`$ otherwise. Evenness gives $`\nabla W(0)=0`$; the displayed particle normalization is $`1/n`$, including the zero diagonal term.

This is a smooth, Gaussian-initialized instance of the question of removing the small-interaction assumption from sharp uniform-in-time propagation of chaos. It is not asserted to be the full generality of the source question.

## Application

In granular-media and mean-field particle simulations, a small group of simulated particles is used to approximate independent samples from a nonlinear diffusion. The estimate would control their distributional dependence throughout long simulations, including when the attractive convex interaction is much stronger than the confining curvature.

## References

1. Daniel Lacker and Luc Le Flem, *Sharp uniform-in-time propagation of chaos*, Probability Theory and Related Fields **187** (2023), 443–480. [DOI](https://doi.org/10.1007/s00440-023-01192-x); [author version](https://arxiv.org/abs/2205.12047v2), §2.3, Corollary2.7 and discussion/Remark2.8, physical page9. These identify the interaction-strength limitation and a solvable linear Gaussian example.
2. Manuel Arnese and Daniel Lacker, *Sharp propagation of chaos for mean field Langevin dynamics, control, and games* (2026). [Primary text](https://arxiv.org/html/2603.10988v1), equations(1.1)–(1.3), Assumption(UiT), Theorem2.8 and §2.3. The latter explicitly leaves sharp rates without small interaction open even for convex pairwise interactions; Remark2.11 corrects a smallness threshold in the 2023 proof.
3. Zhenjie Ren and Songbo Wang, *Size of chaos for Gibbs measures of mean field interacting diffusions*, Probability Theory and Related Fields (2025). [DOI](https://doi.org/10.1007/s00440-025-01435-z); [accepted version](https://arxiv.org/abs/2411.14236v3), Proposition5, displacement-convex case, physical page9; Perspectives, page14. Their arbitrary-strength sharp estimate concerns stationary Gibbs measures.

## Status review


**Known cases:** Arbitrarily strong convex interactions and uniform time sharp local entropy are required. The 2026 primary explicitly retains the interaction-strength restriction; stationary Gibbs estimates do not cover transient marginals.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Arbitrarily strong convex interactions and uniform time sharp local entropy are required. The 2026 primary explicitly retains the interaction-strength restriction; stationary Gibbs estimates do not cover transient marginals.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The cited 2026 source still states the broader smallness-removal question as open. Checked 17 October 2026. An independent selected-primary audit confirmed the exact forward entropy, Gaussian initialization, current 1/n normalization and uniformity in time and marginal size. It also checked that stationary sharp estimates and dynamic global bounds do not give this local square rate.

Known uniform-in-time global entropy bounds yield local rates of order $`k/n`$ by subadditivity; this loses the requested square. Sharp estimates under small interaction and sharp equilibrium estimates do not establish the displayed dynamic assertion. The target is forward relative entropy at every time, with nonstationary independent Gaussian initialization.

The May2026 revision of Wang's *Large-scale concentration and relaxation for mean-field Langevin particle systems* ([arXiv:2508.16428v2](https://arxiv.org/abs/2508.16428v2)), Theorem7, gives global modulated-free-energy control rather than the requested local square rate. Tangpi–Touzi's [arXiv:2510.19211v3](https://arxiv.org/abs/2510.19211v3), Theorem3.7, gives a synchronous-coupling mean-square rate of order $`1/n`$; Zhang's [arXiv:2601.10076v3](https://arxiv.org/abs/2601.10076v3) concerns stationary Rényi divergence and retains weak interaction.

Current AIM entries148 and149 concern deterministic Coulomb/kinetic limits;404 and405 concern vanishing-viscosity mean-field games. The admitted extended ensemble-filter endpoint concerns common observations and random covariance feedback. These are different targets. Current OpenAI catalogue descriptions and the Prove2Me contexts located by the supplied aliases contained no equivalent problem or resolution. Catalogue comparisons do not certify mission proof bodies.

[Detailed review packet](../FURTHER_problems/_tracking/parallel/rough-filtering/convex-sharp-entropy-review.json).

The [independent audit](../FURTHER_problems/_tracking/parallel/continuum/cross-convex-sharp-entropy-review.json) also examined the potentially resolving Monmarché–Ren–Wang theorem [arXiv:2401.07966v3](https://arxiv.org/abs/2401.07966v3); its inspected statement retains a high-temperature or small-interaction condition. The [fresh catalogue comparison](../FURTHER_problems/_tracking/parallel/rough-filtering/sharp-entropy-prove2-0091-review.json) covers all 52 matching listing windows, grouped without losing matched text. These dated searches found no matching complete result or announcement.

The original Lacker–Le Flem author version and the Ren–Wang accepted version were read in full for discovery; their publisher-version parity gaps remain explicit in the source packet. Later comparisons have selected extents recorded there. The source is eligible through registered journal J119; its May2022 arXiv submission is outside the W001 discovery cutoff. These checks do not certify every cited proof or every mission proof body.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-775c225f97fb32da**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
