# 947. Backward Euler convergence for small-BV hyperbolic systems

**Area:** PDEs and materials / hyperbolic conservation laws
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`N\ge2`$ and $`g\in C^\infty(\mathbb R^N;\mathbb R^N)`$ satisfy
$`\|Dg(u)\|_{\mathrm{op}}\le1`$ everywhere, with $`Dg`$ globally Lipschitz.
Set $`F(u)=2u+g(u)`$. Suppose $`DF`$ is strictly hyperbolic near $`0`$, and each characteristic family is genuinely nonlinear or linearly degenerate there. Write $`S_t`$ for the standard small-total-variation admissible semigroup for
```math
u_t+\partial_xF(u)=0,\qquad x\in\mathbb R.
```

For $`h>0`$ and $`v\in L^1(\mathbb R;\mathbb R^N)`$, define $`E_hv`$ to be the unique absolutely continuous $`L^1`$ solution $`w`$ of
```math
w+h\,DF(w)\partial_xw=v\qquad\text{almost everywhere}.
```

The global assumptions on $`g`$ make this step well-defined by Chiri–Zhang's Theorem 2.1.

Is there $`\delta>0`$, depending on $`F`$, such that every
$`u_0\in L^1(\mathbb R;\mathbb R^N)\cap BV(\mathbb R;\mathbb R^N)`$
with $`\mathrm{TV}(u_0)\le\delta`$ satisfies
```math
\lim_{m\to\infty}\left\|E_{t/m}^{\,m}u_0-S_tu_0\right\|_{L^1}=0
\qquad\text{for every fixed }t>0?
```

Here $`E_h^{\,m}`$ means $`m`$ successive implicit time steps; space remains continuous. Uniform BV bounds on the iterates are not assumed, and no convergence rate is requested.

## Application

The question asks whether implicit time stepping selects the standard admissible shock evolution of a nonlinear system, even though each step is uniquely solvable. It connects continuum conservation laws with the reliability of their time approximations.

## References

1. A. Bressan, *Open Questions in the Theory of One Dimensional Hyperbolic Conservation Laws*, in **Nonlinear Conservation Laws and Applications** (2011), pp. 1–22, §4(4), Eq. (4.7), [chapter DOI](https://doi.org/10.1007/978-1-4419-9554-4_1); [author chapter](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/c/168431/files/2023/07/claw-questions.pdf), native p. 15.
2. M. T. Chiri and M. Zhang, *On backward Euler approximations for systems of conservation laws*, **NoDEA** 31 (2024), article 37, [DOI](https://doi.org/10.1007/s00030-023-00920-5). [Accepted manuscript](https://cvgmt.sns.it/media/doc/paper/5361/BackEuler-Revision.pdf), revised 29 December 2023, assumptions (1.7) and Theorem 2.1.
3. A. Bressan, *One Dimensional Hyperbolic Conservation Laws: Past and Future*, [author revision dated 10 September 2024](https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/c/168431/files/2024/09/Erice-revised2024.pdf), §3(7), native pp. 13–14.

## Status review


**Known cases:** Unique implicit steps and individual shock-profile construction do not establish convergence of all small-BV iterates. A-posteriori estimates assume the retained variation control missing in this problem.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Unique implicit steps and individual shock-profile construction do not establish convergence of all small-BV iterates. A-posteriori estimates assume the retained variation control missing in this problem.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2011 source asks about general backward Euler convergence. The displayed normalization specifies the class in reference 2 where every implicit step has a unique $`L^1`$ Carathéodory solution. It is a precise version of that source question; no equivalence of discretizations under a Galilean change is asserted.

Reference 2 establishes fixed-step existence, uniqueness and selected shock profiles. Its estimates do not establish the limit above. Reference 3 still states convergence and uniform BV bounds as open after citing that published work. Known scalar and straight-rarefaction-curve cases do not cover all systems here.

Nearby AIM viscosity, rough-data uniqueness, BV blowup and universal error-rate questions have different approximations or conclusions. No matching complete solution or announcement was located. Final publisher/author byte parity is not certified; the formulation is supported by the primary author chapter, accepted step theorem and later survey. The [owner packet](../FURTHER_problems/_tracking/B296-backward-Euler-small-BV-precise-current-allstatus-owner-C-END-20261026.json) and [independent review](../FURTHER_problems/_tracking/B296-backward-Euler-root-independent-normalized-formulation-current-allstatus-PASS-END-20261026.json) preserve the exact comparisons and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-8d39676ce4d3c66e**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
