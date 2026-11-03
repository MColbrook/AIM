# 729. Uniqueness of free-time controlled transport in Eulerian form

**Area:** Optimal control and continuous optimal transport
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Use hypotheses H0–H6 of [1]. Let $`\mu,\nu`$ be compactly supported probabilities on $`\mathbb R^n`$, with disjoint supports and at least one absolutely continuous marginal. The closed control set is $`A\subset\mathbb R^m`$; $`K\ge0`$ is continuous. Dynamics $`f(q,a)`$ are Lipschitz in $`q`$, continuous in $`a`$, and span $`\mathbb R^n`$ at each $`q`$. Require

```math
\sup_q|f(q,a)|<\infty,\quad |f(q,a)|\le\Gamma_0(1+|a|),\quad
\liminf_{|a|\to\infty}\frac{K(t,q,a)}{|a|}=\infty,
\qquad \liminf_{T\to\infty}\int_0^T\inf_{q,a}K(t,q,a)\,dt=\infty.
```

The smooth Hamiltonian $`H(t,q,p)=\sup_a\{p\cdot f(q,a)-K(t,q,a)\}`$ has the source's asymptotic growth $`H\sim|p|^\beta`$, $`1<\beta<\infty`$, uniformly in $`(t,q)`$. Its maximizing control is unique and continuous. Assume either strict time increase or strict time decrease of $`K`$.

Minimize $`\int_0^\infty\int K\,d\rho_t\,dt`$ over nonnegative finite state–control measures $`\rho_t`$ and a nonnegative stopping measure $`\sigma`$, with spatial marginal $`\nu`$, satisfying [1, (3.1)–(3.2)]:

```math
\int w\,d\sigma=\int w(0,x)\,d\mu(x)
 +\int_0^\infty\int(\partial_t w+f\cdot\nabla_qw)\,d\rho_t\,dt.
```

Here $`\rho_t`$ is weak*-measurable; tests are the source's $`C^1(\mathbb R\times\mathbb R^n)`$ functions with integrals understood. **Is the minimizing pair $`(\rho_t\,dt,\sigma)`$ unique?** Occupation equality includes controls and ignores changes on null time sets. The displayed coercivity is not strengthened to an unstated uniform rate.

## Application

This asks whether endpoint optimality determines the entire mass flow, controls and stopping distribution in a transport problem with an unknown end time.

## References

1. N. Ghoussoub, Y.-H. Kim and A. Z. Palmer, *Optimal Transport with Controlled Dynamics and Free End Times*, SIAM J. Control Optim. 56(5) (2018), 3239–3259. [DOI](https://doi.org/10.1137/18M1178037); [arXiv v2, §§2–5, Remark 5.6](https://arxiv.org/html/1803.10874v2).
2. S. Dweik, N. Ghoussoub and A. Z. Palmer, *Optimal controlled transports with free end times subject to import/export tariffs*. [Primary preprint, §5, Theorem 5.1](https://arxiv.org/pdf/1903.02126).
3. N. Ghoussoub, Y.-H. Kim and A. Z. Palmer, *Optimal Stochastic Transport with Free End Time*. [Primary preprint, Theorem 6.3](https://arxiv.org/html/1909.04814v1).

## Status review


**Known cases:** The deterministic Eulerian occupation-and-stopping pair includes controls. Uniqueness of the endpoint plan, stochastic diffusion results and smoother dual-potential cases do not alone establish uniqueness among all admissible Eulerian pairs.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The deterministic Eulerian occupation-and-stopping pair includes controls. Uniqueness of the endpoint plan, stochastic diffusion results and smoother dual-potential cases do not alone establish uniqueness among all admissible Eulerian pairs.

Additional comparison sources: [comparison source 1](https://doi.org/10.1137/18M1178037); [comparison source 2](https://arxiv.org/html/1803.10874v2); [comparison source 3](https://arxiv.org/pdf/1903.02126); [comparison source 4](https://arxiv.org/html/1909.04814v1). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The source proves the smoother $`C^1`$ dual-potential case and constructs an optimal Eulerian embedding of the unique endpoint plan. Neither assertion establishes uniqueness among all admissible Eulerian pairs. The tariff comparator concerns endpoint plans and stopping maps; the stochastic comparator includes a nonzero Brownian diffusion. A deterministic sink/control superposition argument still needs its exact hypotheses justified.

Bounded resolution and announcement searches found no matching complete result. Full nearest-statement comparisons covered all 1,146 private findings and 1,704 retained public all-status entries. Published metadata was checked; complete published/preprint body parity is not asserted. See the [owner review](../FURTHER_problems/_tracking/focused-free-end-controlled-Eulerian-uniqueness-C247-A-20261029/OWNER-EXACT-DETERMINISTIC-FREE-END-TIME-EULERIAN-MEASURE-UNIQUENESS-PRIMARY-CURRENT-DUPLICATE-PROPOSAL.json) and [final independent gate](../FURTHER_problems/_tracking/focused-free-end-controlled-Eulerian-uniqueness-C247-A-20261029/C-FINAL-CURRENT-AND-1146-PRIVATE-1704-PUBLIC-SEMANTIC-GATE-PENDING-ROOT.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-442aa1806b172de2**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
