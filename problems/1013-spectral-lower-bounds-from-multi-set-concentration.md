# 1013. Spectral lower bounds from multi-set concentration

**Area:** Spectral geometry and concentration of measure
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For each integer $`k\ge2`$, does a constant $`c_k>0`$ depending only on $`k`$ have the following property?

Let $`(M,g)`$ be a complete smooth connected Riemannian manifold without boundary, and let $`\mu=e^{-V}dv_g`$ be a probability measure with smooth $`V`$ and

```math
\mathrm{Ric}_g+\mathrm{Hess}_gV\ge0.
```

Define the variational levels

```math
\lambda^{(k)}=\inf_{\substack{L\subset H^1(\mu)\\\dim L=k+1}}
\ \sup_{0\ne f\in L}\frac{\int_M|\nabla f|^2\,d\mu}{\int_M f^2\,d\mu},
\qquad \lambda^{(0)}=0.
```

No discrete-spectrum assumption is imposed. Put

```math
\Delta_k=\{(a_1,\ldots,a_k)\in[0,1]^k:
 s=\textstyle\sum_i a_i\le1,\quad a_i+s\ge1\ \text{for every }i\}.
```

Suppose some $`a>0`$ satisfies this condition: for **every** positively separated Borel tuple $`A_1,\ldots,A_k`$ with $`(\mu(A_i))_i\in\Delta_k`$, setting $`A=\bigcup_iA_i`$ and $`A_r=\{x:d(x,A)<r\}`$ gives

```math
\mu(A_r)\ge1-(1-\mu(A))
 \exp[-\min(ar^2,\sqrt a\,r)]
\quad\left(0<r\le\tfrac12\min_{i\ne j}d(A_i,A_j)\right).
```

**Must $`\lambda^{(k)}\ge c_k a`$?**

This is the positive universal-function question in [1, §5.2]. Rescaling $`g`$ to $`ag`$ normalizes $`a`$ to one, divides Rayleigh quotients by $`a`$ and preserves weighted nonnegative Ricci curvature. Thus a positive bound at $`a=1`$ is equivalent to this formulation. No constant uniform in $`k`$, or sharp value, is requested. The case $`k=1`$ is known.

## Application

This would turn concentration of several substantial separated pieces into a quantitative obstruction to having too many low-energy scalar modes, extending the usual first-gap concentration principle.

## References

1. N. Gozlan and R. Herry, *Multiple sets exponential concentration and higher order eigenvalues*, Potential Anal. 52 (2020), 203–221. [DOI](https://doi.org/10.1007/s11118-018-9743-1); [primary v1, §§1.1–1.2, Proposition 4.1 and §5.2](https://arxiv.org/html/1804.06133v1).
2. K. Funano, *Estimates of eigenvalues of Laplacian by a reduced number of subsets*, [primary preprint, Theorem 1.1 and §4](https://arxiv.org/html/1601.07581v1).
3. K. Funano and Y. Sakurai, *Upper bounds for higher-order Poincaré constants*, [primary v3, Theorem 1.1](https://arxiv.org/html/1907.03617v3).

## Status review


**Known cases:** The assertion is an inverse spectral lower bound from multi-set concentration. Existing subset comparisons and higher-order Poincare estimates give a different direction; no matching converse found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The assertion is an inverse spectral lower bound from multi-set concentration. Existing subset comparisons and higher-order Poincare estimates give a different direction; no matching converse found.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The cited subset estimates give spectral upper bounds; they do not establish this inverse lower bound from the prescribed concentration profile. Recent convex-domain Dirichlet comparisons also change the setting and hypothesis. The separate forward Gaussian-profile question in §5.1 is not this converse. No equivalence with a uniform adjacent-eigenvalue-ratio conjecture is asserted.

Bounded current-resolution and complete-announcement searches found no matching result. Full nearest-statement comparisons used 1,163 private findings and 1,704 retained public all-status entries, then the distinct curvature and translator dispositions. Boundary shape optimization, Hodge gaps and coefficient inverse problems differ. Published identity is checked; complete published/preprint body parity is not claimed. See the [owner/current review](../FURTHER_problems/_tracking/focused-inverse-multiset-eigenvalue-C259-A-20261029/OWNER-EXACT-CD0-MULTISET-CONCENTRATION-INVERSE-KTH-MINMAX-LOWER-BOUND-PRIMARY-CURRENT-SEMANTIC-PROPOSAL.json) and [independent model peer](../FURTHER_problems/_tracking/focused-inverse-multiset-eigenvalue-C259-A-20261029/C-INDEPENDENT-COMPLETE-WEIGHTED-CD0-DELTAK-PREFACTOR-HALFSEPARATION-AND-SCALING-MODEL-PEER-PASS.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-187d304a434b816d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
