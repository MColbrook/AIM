# 572. Does mixing force exponential decay for smooth Anosov flows?

**Area:** Hyperbolic dynamics and statistical relaxation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a closed connected smooth Riemannian manifold and let $`\phi^t`$ be a topologically transitive $`C^\infty`$ Anosov flow. Its generator $`X`$ is nowhere zero and there is a continuous invariant splitting
```math
TM=E^s\oplus \mathbb RX\oplus E^u
```

with constants $`A,\lambda>0`$ such that, for all $`t\geq0`$,
```math
\|D\phi^t|_{E^s}\|\leq A e^{-\lambda t},
\qquad
\|D\phi^{-t}|_{E^u}\|\leq A e^{-\lambda t}.
```

Let $`\mu`$ be its unique SRB probability measure: its conditional measures on local unstable leaves are absolutely continuous with respect to the induced Riemannian measures. Assume that $`\mu`$ is mixing, meaning that
```math
\int_M f\,g\circ\phi^t\,d\mu
\longrightarrow
\left(\int_M f\,d\mu\right)\left(\int_M g\,d\mu\right)
```

for every $`f,g\in L^2(\mu)`$.

Must there exist constants $`C,c>0`$, depending on the fixed flow and metric, such that
```math
\left|\int_M f\,g\circ\phi^t\,d\mu
-\int_M f\,d\mu\int_M g\,d\mu\right|
\leq C e^{-ct}\|f\|_{C^1(M)}\|g\|_{C^1(M)}
```

for every pair of real $`C^1`$ observables and every $`t\geq0`$? Here $`\|f\|_{C^1}=\sup_M|f|+\sup_M\|df\|`$, using the fixed Riemannian metric.

Prove this assertion or construct a smooth mixing Anosov flow for which it fails. No contact structure, smooth invariant volume, regularity of the stable holonomies, or codimension-one hypothesis is imposed. The constants need not be uniform over different flows.

## Application

Anosov flows are models of uniformly hyperbolic chaotic evolution. The estimate would bound how quickly correlations between smooth measurements disappear. Such quantitative relaxation estimates support limit theorems and controlled statistical descriptions of deterministic dynamics.

## Known results and scope

The smooth three-dimensional case follows from Tsujii–Zhang's theorem, which proves the stronger conclusion for all equilibrium measures of Hölder potentials. The remaining target permits arbitrary dimension. Butterley–War prove exponential mixing under additional regularity and nonintegrability assumptions, and obtain robust higher-dimensional classes. Melbourne–Varandas' later Theorem 1.2 still assumes $`C^{1+}`$ stable holonomies and joint nonintegrability. These hypotheses are not available for every flow in the question. The codimension-one volume-preserving mixing case in dimension four and higher is also known, as recorded in Melbourne–Varandas, Remark 1.4.

Khoule–Manso–Ndiaye–War announce another class: smooth positive reparametrizations of constant-negative-curvature geodesic flows. This does not encompass all smooth Anosov flows. A 2022 preprint claiming the full codimension-one case was withdrawn because its main proof was incomplete; it is not treated as an established result.

## References

1. O. Butterley and K. War, *Open sets of exponentially mixing Anosov flows*, J. Eur. Math. Soc. 22 (2020), 2253–2285, [DOI](https://doi.org/10.4171/JEMS/964). Eligible source: [arXiv:1609.03512v2](https://arxiv.org/pdf/1609.03512v2), introduction pp. 1–5.
2. M. Tsujii and Z. Zhang, *Smooth mixing Anosov flows in dimension three are exponentially mixing*, Annals of Mathematics 197 (2023), 65–158, [published record](https://annals.math.princeton.edu/2023/197-1/p02). [arXiv:2006.04293v1](https://arxiv.org/pdf/2006.04293v1), Theorem 1.1, p. 3.
3. I. Melbourne and P. Varandas, *Good Inducing Schemes for Uniformly Hyperbolic Flows, and Applications to Exponential Decay of Correlations*, Annales Henri Poincaré 26 (2025), 921–945, published online 2024, [Theorem 1.2 and Remarks 1.3–1.4](https://doi.org/10.1007/s00023-024-01439-w).
4. C. Khoule, M. Manso, A. Ndiaye and K. War, *$`C^0`$-Contact Anosov flows*, [arXiv:2503.00454v1](https://arxiv.org/pdf/2503.00454v1) (2025), Theorems A–B, pp. 3–4.
5. V. Araujo, *Mixing implies exponential mixing among codimension one hyperbolic attractors and Anosov flows*, [arXiv:2209.04907v2](https://arxiv.org/abs/2209.04907v2), withdrawn September 2022. Included only to distinguish its withdrawn claim from verified progress.

## Status review


**Known cases:** The Annals theorem settles dimension three; contact, codimension-one and inducing-scheme results add hypotheses. New examples of exponentially mixing flows and discrete Anosov-map results do not prove exponential mixing for every smooth mixing Anosov flow in all dimensions.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

Checked on 2026-10-24 against the eligible source, later primary theorem statements and announcements, official version histories, and all-status AIM/FURTHER/OpenAI target comparisons. No matching resolution of the general SRB statement was located. The withdrawn claim is explicitly distinguished from known cases. The review covers selected primary material and records retrieval limits; it does not certify every cited proof or exhaust all literature.


### Online recheck, 2026-10-30

The Annals theorem settles dimension three; contact, codimension-one and inducing-scheme results add hypotheses. New examples of exponentially mixing flows and discrete Anosov-map results do not prove exponential mixing for every smooth mixing Anosov flow in all dimensions.

Comparators and current-status sources: [status source 1](https://annals.math.princeton.edu/2023/197-1/p02); [status source 2](https://doi.org/10.1007/s00023-024-01439-w); [status source 3](https://arxiv.org/abs/2503.00454). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-7582f238bcf88f9b** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
