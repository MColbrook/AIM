# 893. Weak L2 boundedness for the parabolic Carleson operator

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a complex Schwartz function $`f`$ on $`\mathbb R^2`$, define
```math
\mathcal C_{\mathrm{par}}f(x,y)=\sup_{a,b\in\mathbb R}
\left|\mathrm{p.v.}\int_{\mathbb R}
f(x-t,y-t^2)e^{i(at+bt^2)}\,\frac{dt}{t}\right|.
```

The principal value removes a symmetric neighborhood of zero. Both modulation coefficients vary independently.

Does there exist an absolute constant $`C<\infty`$ such that, for every such $`f`$ and $`\lambda>0`$,
```math
\lambda^2\left|\{(x,y):\mathcal C_{\mathrm{par}}f(x,y)>\lambda\}\right|
\le C\|f\|_{L^2(\mathbb R^2)}^2?
```

Here $`|\cdot|`$ is planar Lebesgue measure. No additional supremum over truncation radii is imposed.

## Application

The estimate controls the area on which singular integration along parabolic trajectories, with independent oscillatory modulations, greatly amplifies a planar signal.

## References

- J. Roos, *Bounds for anisotropic Carleson operators*, J. Fourier Anal. Appl. **25** (2019), 2324-2355, [DOI](https://doi.org/10.1007/s00041-018-09657-7), [2017 primary](https://arxiv.org/abs/1710.10962), equation (2.4).
- L. Becker, *Maximal Polynomial Modulations of Singular Radon Transforms*, J. Funct. Anal. **286** (2024), 110299, [DOI](https://doi.org/10.1016/j.jfa.2023.110299), [primary v2](https://arxiv.org/html/2210.17263v2), **Open Problem 1**.
- M. Hsu and V. Lie, *On the resonant Carleson-Radon transform in all dimensions. The degree one resonant case* (2026), [primary v1](https://arxiv.org/html/2606.27219v1), Problem 2, equation (1.16) and Remark 1.12.

## Status review


**Known cases:** Hsu-Lie treat a restricted resonant modulation subspace and retain the full two-parameter parabolic problem. Polynomial Carleson boundedness on the line and parabolic PDE Carleson-measure estimates are different operators. No matching weak-L2 endpoint theorem was located.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Hsu-Lie treat a restricted resonant modulation subspace and retain the full two-parameter parabolic problem. Polynomial Carleson boundedness on the line and parabolic PDE Carleson-measure estimates are different operators. No matching weak-L2 endpoint theorem was located.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

**Partial progress; checked 28 October 2026.** Mollified kernels and restricted modulations are understood. The June 2026 paper explicitly retains the full two-parameter problem; its main theorem does not cover this modulation space. No matching complete resolution, announcement or AIM/private duplicate was found.

Roos supplies the precutoff boundedness question; Becker states this exact weak endpoint. Multiplication of the input by a linear planar phase gives the displayed quadratic phase along the parabola.

Review evidence: [owner](../FURTHER_problems/_tracking/focused-full-modulation-parabolic-Carleson-weakL2-C226-C-20261028/OWNER-EXACT-TWO-PARAMETER-PARABOLIC-CARLESON-WEAK-L2-PRIMARY-2026-RESONANCE-SCOPE-AND-DUPLICATE-PROPOSAL.json), [independent model review](../FURTHER_problems/_tracking/focused-full-modulation-parabolic-Carleson-weakL2-C226-C-20261028/A-INDEPENDENT-TWO-PARAMETER-WEAK-L2-MODULATION-AND-2026-RESTRICTED-SUBSPACE-MODEL-PEER-PASS.json), [coordinating review](../FURTHER_problems/_tracking/focused-full-modulation-parabolic-Carleson-weakL2-C226-C-20261028/ROOT-EXACT-WEAK-ENDPOINT-CURRENT-RESONANCE-AND-LATER-HELD-ROW-SEMANTIC-FINAL-REVIEW.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-16c3c3561677865d**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
