# 814. Smooth classification of four-manifolds with conformal curvature ratio below eight

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`M`$ be a smooth, closed, connected, oriented four-manifold with a smooth Riemannian metric $`g`$. Its Schouten tensor is
```math
P_g=\frac12\left(\mathrm{Ric}_g-\frac{R_g}{6}g\right).
```

For an endomorphism $`A`$, write $`\sigma_2(A)`$ for the second elementary symmetric polynomial of its eigenvalues. Assume
```math
Y(M,[g])>0,\qquad
 \int_M\sigma_2(g^{-1}P_g)\,dV_g>0.
```

Here $`[g]`$ is the conformal class and
```math
Y(M,[g])=\inf_{\widetilde g\in[g]}
 \mathrm{Vol}(M,\widetilde g)^{-1/2}
 \int_M R_{\widetilde g}\,dV_{\widetilde g}
```

is its Yamabe constant.

Regard the Weyl tensor $`W_g`$ as an endomorphism of two-forms, with its Hilbert–Schmidt norm, and define
```math
\beta(M,[g])=
 \frac{\int_M\|W_g\|_{\mathrm{End}(\Lambda^2)}^2\,dV_g}
      {\int_M\sigma_2(g^{-1}P_g)\,dV_g}.
```

If $`\beta(M,[g])<8`$, must $`M`$ be diffeomorphic to $`S^4`$, $`\mathbb{CP}^2`$, or $`\mathbb{CP}^2`$ with the opposite orientation?

No Einstein, sectional-curvature, simple-connectivity or Betti-number assumption is imposed. The conclusion concerns the smooth manifold, not an isometry or conformal classification of the given metric. The endpoint $`\beta=8`$ is excluded.

## Application

The question asks how far an integral, conformally invariant curvature bound determines smooth four-dimensional topology. It would extend a known conformal sphere theorem beyond its first critical curvature ratio.

## References

- S.-Y. A. Chang, M. Gursky and S. Zhang, *A conformally invariant gap theorem characterizing $`\mathbb{CP}^2`$ via the Ricci flow*, **Mathematische Zeitschrift** 294 (2020), 721–746. [Published article](https://doi.org/10.1007/s00209-019-02331-8); [arXiv:1809.05918v1](https://arxiv.org/html/1809.05918), Conjecture 1.2 and equation (1.13), with conventions in equations (1.1)–(1.6).

## Status review


**Known cases:** The known beta less than four sphere theorem and gap results requiring nonzero positive second Betti number or extra curvature assumptions do not supply the complete smooth classification for beta less than eight under the stated conformal assumptions alone.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The known beta less than four sphere theorem and gap results requiring nonzero positive second Betti number or extra curvature assumptions do not supply the complete smooth classification for beta less than eight under the stated conformal assumptions alone.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked **30 October 2026**. The original paper proves the sphere conclusion for $`\beta<4`$ and a gap above four under an additional positive second-Betti-number condition. It also restricts the intersection form below eight. These results do not establish the full smooth classification stated here.

Current searches found no matching general resolution or complete announcement. The closest reviewed announcement classifies Einstein metrics with nonnegative sectional curvature, or assumes nonnegative sectional curvature and a separate small-energy bound. Those hypotheses are absent here. The current AIM/OpenAI all-status corpus and developing collection contained no equivalent target in the semantic comparisons. These dated checks do not guarantee that no unlocated result exists.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-92845684f419166a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
