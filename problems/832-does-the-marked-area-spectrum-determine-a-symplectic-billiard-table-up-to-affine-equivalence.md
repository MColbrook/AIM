# 832. Does the marked area spectrum determine a symplectic billiard table up to affine equivalence?

**Area:** Symplectic billiards and geometric inverse problems
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a smooth, strictly convex planar domain $`\Omega`$ with everywhere positive boundary curvature, let $`M_\Omega(q)`$ be the maximum area of a simple convex $`q`$-gon inscribed in $`\partial\Omega`$, for each integer $`q\geq 3`$. If two such domains have $`M_{\Omega_1}(q)=M_{\Omega_2}(q)`$ for every $`q\geq3`$, must an affine map carry $`\Omega_1`$ to $`\Omega_2`$?

This sequence is the marked area spectrum of the associated symplectic billiard. Its Mather $`\beta`$-function satisfies $`\beta(1/q)=-2M_\Omega(q)/q`$; knowing the entire $`\beta`$-function supplies at least these values. Affine equivalence here includes reflections; otherwise a reflected asymmetric table would be an immediate obstruction.

## Application

The maximal areas of inscribed periodic polygons encode the billiard dynamics while retaining each polygon's period. The question asks whether this information reconstructs the underlying convex shape. It is a global inverse problem, distinct from rigidity of a continuously varying family near one ellipse.

## References

1. L. Baracco, O. Bernardi and A. Nardi, [*Area spectral rigidity for axially symmetric symplectic billiard tables*](https://www.aimsciences.org/article/doi/10.3934/jmd.2026012?viewType=HTML), *Journal of Modern Dynamics* **22** (2026), 469–488, introduction p. 471 and Definition 2.1 p. 473. The paper poses the general marked-spectrum question explicitly.
2. C. Fierobe, A. Sorrentino and A. Vig, [*Deformational spectral rigidity of axially symmetric symplectic billiards*](https://doi.org/10.1088/1361-6544/ae0c4f), *Nonlinearity* **38** (2025), article 105010. This concerns restricted deformational rigidity.
3. S. Baranzini, M. Bialy and A. Sorrentino, [*Isoperimetric-type inequalities for Mather's $`\beta`$-function of convex billiards*](https://arxiv.org/abs/2509.06915), 2025 preprint. Its pointwise ellipse characterization is a special case rather than general injectivity.

## Status review


**Known cases:** The 2026 spectral-rigidity theorem concerns isospectral families in an axially symmetric near-ellipse class. It does not prove global injectivity of the sequence of maximal polygon areas for arbitrary pairs of strictly convex tables. Hyperbolic marked-area-spectrum rigidity is a different invariant.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2026 spectral-rigidity theorem concerns isospectral families in an axially symmetric near-ellipse class. It does not prove global injectivity of the sequence of maximal polygon areas for arbitrary pairs of strictly convex tables. Hyperbolic marked-area-spectrum rigidity is a different invariant.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2026 theorem proves area-isospectral $`C^1`$ families are equi-affine within an axially symmetric, sufficiently near-ellipse class. It does not compare arbitrary pairs of tables. The 2025 results above also impose special geometry or family hypotheses. The [bounded source, announcement and duplicate review](../FURTHER_problems/_tracking/symplectic-marked-area-rigidity-status-2026-10-21.json) found no general published or announced resolution and no matching AIM or FURTHER entry.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-b4402821c97474be**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
