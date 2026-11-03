# 787. Are tangent cones of proper lower-curvature spaces length spaces?

**Area:** Metric geometry and synthetic curvature
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\kappa\in\mathbb R`$, and let $`(X,d)`$ be a proper length space with Alexandrov curvature bounded below by $`\kappa`$, denoted $`\mathrm{CBB}(\kappa)`$. Proper means that every closed bounded subset is compact. Length means that distances are infima of lengths of continuous curves. The curvature assumption is the usual four-point comparison with the two-dimensional model of constant curvature $`\kappa`$ [1, Definitions 8.1–8.2]; no finite-dimensionality assumption is imposed.

For $`p\in X`$, define the **canonical metric tangent cone** $`T_pX`$ as follows. Consider constant-speed minimizing geodesic germs $`\gamma`$ starting at $`p`$, including the constant germ. Give these germs the pseudodistance
```math
D(\gamma,\eta)=\lim_{t\downarrow0}
\frac{d(\gamma(t),\eta(t))}{t}.
```

The lower curvature bound ensures that these limits exist. Identify pairs at zero pseudodistance and take the metric completion, with metric $`d_T`$.

Equivalently, let $`\Sigma_pX`$ be the completion of the unit-speed geodesic directions after identifying pairs with zero Alexandrov angle. Then $`T_pX`$ is the Euclidean cone over $`\Sigma_pX`$, with
```math
d_T(r\xi,s\eta)^2=r^2+s^2-2rs\cos\angle(\xi,\eta),
\qquad r,s\ge0,
```

and all points with radial coordinate zero identified. If there are no nonconstant geodesic germs, the germ definition gives the one-point tangent cone.

Must $`T_pX`$ be a length space for **every** $`p\in X`$? Explicitly, for every $`v,w\in T_pX`$ and $`\varepsilon>0`$, must there be a continuous rectifiable curve $`c:[0,1]\to T_pX`$ from $`v`$ to $`w`$ with
```math
\mathrm{Length}_{d_T}(c)\le d_T(v,w)+\varepsilon?
```


This is Open Question 13.41 in the current author version of [1], already present as Open Question 11.7.1 in the 2019 first version [2].

## Application

Tangent cones describe infinitesimal geometry in spaces with singularities and lower curvature bounds. The question asks whether their infinitesimal distances can always be approximated by lengths of curves, which is a basic issue for the geometric calculus developed on these spaces.

## Known results and scope

The source explains that the answer is affirmative for finite-dimensional lower-curvature spaces. For complete length spaces with an Alexandrov **upper** curvature bound, the tangent cone is also a length space [1, Theorem 13.4]. Neither result covers the stated class.

Without properness, an infinite-dimensional example due to Halbeisen has a tangent cone that is not a length space [1, Example 13.6]. That example does not settle the proper case. For infinite-dimensional spaces, a separate known case assumes compactness of the space of directions at the base point [3, Proposition 5.2]. Compactness of $`\Sigma_pX`$ is an additional hypothesis, not part of this question.

The conclusion asks for a length space, without requiring shortest curves to exist or requiring the tangent cone to be proper. The canonical tangent cone above is specified directly; an arbitrary pointed Gromov–Hausdorff blow-up or ultratangent is a different object in this generality. The question should also not be replaced by requiring the entire space of directions to be an intrinsic metric space: even a line has two antipodal directions.

## References

1. S. Alexander, V. Kapovitch and A. Petrunin, *Alexandrov geometry: foundations*, Graduate Studies in Mathematics 236, AMS, 2024; [publisher record](https://doi.org/10.1090/gsm/236), [official book page](https://anton-petrunin.github.io/book/), [current author PDF](https://anton-petrunin.github.io/book/arXiv.pdf). Tangent definitions in Chapter 6, native pages 67–68; Theorem 13.4 and Example 13.6, native pages 188–189; Open Question 13.41, native page 207. The exact current PDF hash is recorded in the owner audit.
2. S. Alexander, V. Kapovitch and A. Petrunin, *Alexandrov geometry: preliminary version no. 1*, [arXiv:1903.08539v1](https://arxiv.org/abs/1903.08539v1), submitted 20 March 2019, Open Question 11.7.1, printed page 165 (native PDF page 171). Later versions renumber the question.
3. A. Mitsuishi and T. Yamaguchi, *Locally Lipschitz contractibility of Alexandrov spaces and its applications*, Pacific Journal of Mathematics **270** (2014), 393–421, [DOI](https://doi.org/10.2140/pjm.2014.270.393), [publisher PDF](https://msp.org/pjm/2014/270-2/pjm-v270-n2-p07-p.pdf). Section 5 and Proposition 5.2, printed pages 412–414.

## Status review


**Known cases:** Halbeisen counterexamples show failure without properness, whereas this canonical tangent-cone question explicitly requires a proper lower-curvature length space. Finite-dimensional or upper-curvature CAT tangent theorems do not cover the remaining class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Halbeisen counterexamples show failure without properness, whereas this canonical tangent-cone question explicitly requires a proper lower-curvature length space. Finite-dimensional or upper-curvature CAT tangent theorems do not cover the remaining class.

Additional comparison sources: [comparison source 1](https://doi.org/10.1090/gsm/236); [comparison source 2](https://anton-petrunin.github.io/book/); [comparison source 3](https://anton-petrunin.github.io/book/arXiv.pdf); [comparison source 4](https://arxiv.org/abs/1903.08539v1); [comparison source 5](https://doi.org/10.2140/pjm.2014.270.393); [comparison source 6](https://msp.org/pjm/2014/270-2/pjm-v270-n2-p07-p.pdf). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The companion owner audit records the exact source windows, native formula images, current announcement searches and all-status semantic duplicate checks. No matching complete resolution was located through 23 October 2026. The existing resolved BKN tangent-cone question concerns asymptotic cones at infinity of finite-dimensional Riemannian manifolds, with different hypotheses and conclusion. Recent finite-dimensional RCD characterizations and regular-point results likewise do not settle the stated class.

Independent source, current-status and all-status semantic duplicate reviews passed for the exact stated target. Bounded checks do not establish exhaustive absence of a solution or complete proof certification.

The [independent scope review](../FURTHER_problems/_tracking/proper-CBB-canonical-tangent-independent-peer-2026-10-23.json) and [duplicate review](../FURTHER_problems/_tracking/proper-CBB-canonical-tangent-duplicate-review-2026-10-23.json) record the final checks and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-4aa863c82444ea30**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
