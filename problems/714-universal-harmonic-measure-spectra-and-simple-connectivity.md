# 714. Universal harmonic-measure spectra and simple connectivity

**Area:** Geometric function theory and planar potential theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega`$ range over planar domains carrying harmonic measure, with no connectivity restriction, and let $`\omega=\omega_{\Omega,a}`$ be harmonic measure with pole $`a\in\Omega`$. For a finite boundary point $`z`$, define its lower pointwise dimension by
```math
d_\omega(z)=\liminf_{r\downarrow0}
 \frac{\log\omega(B(z,r))}{\log r},
 \qquad
 f_\omega^+(\alpha)=\dim_{\mathrm H}
 \{z\in\partial\Omega:d_\omega(z)\leq\alpha\}.
```

Here $`B(z,r)`$ is a Euclidean disk and $`\dim_{\mathrm H}`$ is Hausdorff dimension. Points outside the support have dimension $`+\infty`$. Equivalently one can use domains on the Riemann sphere; a possible boundary point at infinity does not affect these dimensions.

Set
```math
\Phi(\alpha)=\sup_{\Omega,a} f_{\omega_{\Omega,a}}^+(\alpha),
 \qquad
 \Phi_{\rm sc}(\alpha)=
 \sup_{\substack{\Omega\ \mathrm{simply\ connected}\\a\in\Omega}}
 f_{\omega_{\Omega,a}}^+(\alpha).
```

Is
```math
\Phi(\alpha)=\Phi_{\rm sc}(\alpha)
 \qquad\text{for every }\alpha\geq1?
```


This is [1, Chapter IX, Notes, equation (N.3), pp. 341–342] and the conjecture (1.6) in the inspected author version of [2]. The comparison concerns the suprema over classes of domains, rather than the spectra of each individual domain. The lower local dimension uses a liminf and its sublevel set, rather than only points with an existing exact local exponent.

## Application

Harmonic measure describes where Brownian motion first reaches a boundary and the distribution of flux in a planar Laplace problem. The conjecture asks whether holes can worsen the universal bounds on the size of boundary sets with a specified local concentration of this measure.

## Known progress

The inequality $`\Phi\geq\Phi_{\rm sc}`$ follows from inclusion of the classes. The source reduces the reverse inequality to conformal Cantor sets [2, Section 1.2]. Its Theorem A establishes the corresponding multifractal comparison for polynomial Cantor Julia sets, where all critical points escape to infinity. General conformal Cantor sets need not arise from a polynomial, so this theorem does not finish the stated conjecture.

This question differs from Brennan's integrability conjecture and from the conjectured quadratic formula for the simply connected universal integral-means spectrum. Resolving or disproving a proposed explicit formula within the simply connected class does not establish equality with the unrestricted class.

## References

1. J. B. Garnett and D. E. Marshall, *Harmonic Measure*, Cambridge University Press, 2005, Chapter IX, Notes, pp. 341–342, equations (N.2)–(N.4). [Book DOI](https://doi.org/10.1017/CBO9780511546617).
2. I. Binder, N. Makarov and S. Smirnov, *Harmonic measure and polynomial Julia sets*, *Duke Mathematical Journal* **117**(2) (2003), 343–365. [Journal DOI](https://doi.org/10.1215/S0012-7094-03-11725-1), [inspected author manuscript](https://www.math.utoronto.ca/ilia/Research/bms.pdf), Sections 1.1–1.3, conjecture (1.6), Theorem A. The inspected author manuscript has 18 pages; publisher byte parity is not asserted.

## Status review


**Known cases:** The target compares dimension-sublevel spectra over arbitrary versus simply connected planar domains. Brennan inverse-power integral-means results and particular multiply connected Fatou components do not themselves assert that universal comparison.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target compares dimension-sublevel spectra over arbitrary versus simply connected planar domains. Brennan inverse-power integral-means results and particular multiply connected Fatou components do not themselves assert that universal comparison.

Additional comparison sources: [comparison source 1](https://doi.org/10.1017/CBO9780511546617); [comparison source 2](https://doi.org/10.1215/S0012-7094-03-11725-1); [comparison source 3](https://www.math.utoronto.ca/ilia/Research/bms.pdf); [comparison source 4](https://doi.org/10.1007/s12220-026-02564-0). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Bounded searches on 28 October 2026 found no matching full resolution or complete announcement. The 2026 work of Ferreira and Jové, [*Boundaries of Multiply Connected Fatou Components: A Unified Approach*](https://doi.org/10.1007/s12220-026-02564-0), Theorems A–D, concerns radial extensions, supports and boundary dynamics for Fatou components, rather than the universal multifractal comparison over all planar domains.

The complete retained duplicate corpus comprised 977 findings, 610 formal local problem pages and 1,704 all-status AIM/OpenAI records. Broad target statements were read and compared. The existing chord-arc connectedness problem is a duplicate of another question found in the same book and is excluded from this proposal. DLA growth, coding-tree harmonic-measure singularity, Ising interface limits and gambler's ruin approximation have different models and conclusions. The unchanged public repository heads were checked over HTTPS at 12:52:45 UTC.

The OpenAI family 072 announcement concerns Brennan and inverse-power integral means, including a disproof of a predicted quadratic value. Its announced scope does not state this arbitrary-versus-simply-connected dimension-spectrum comparison. No proof certification of those announcements is claimed.

The [source and current review](../FURTHER_problems/_tracking/B245-two-precise-harmonic-targets-current-gate-C-20261028/MAKAROV-EXACT-LOWER-SUBLEVEL-SPECTRA-977-610-1704-CURRENT-PROPOSAL-AND-BMO-CARLESON-EXCLUSIONS-C-END.json) and [independent review](../FURTHER_problems/_tracking/B245-two-precise-harmonic-targets-current-gate-C-20261028/ROOT-MAKAROV-EXACT-LOWER-SUBLEVEL-ALL-CONNECTIVITY-PRIMARY-PIXELS-CURRENT-SEMANTIC-PASS.json) record the definitions, partial results and bounded checks. No matching full resolution or announcement was located; these AI reviews are not human peer review or a certificate of openness.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b6b883750c63ea08**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
