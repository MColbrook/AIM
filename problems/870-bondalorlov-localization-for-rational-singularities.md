# 870. Bondal–Orlov localization for rational singularities

**Area:** Algebraic geometry / derived categories
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`k`$ be a field of characteristic zero, and let $`X`$ be a normal integral quasi-projective variety over $`k`$. Let
```math
p:Y\longrightarrow X
```

be a projective resolution of singularities: $`Y`$ is smooth and $`p`$ is birational. Assume that $`X`$ has rational singularities, expressed by
```math
p_*\mathcal O_Y=\mathcal O_X,\qquad
R^ip_*\mathcal O_Y=0\quad(i>0).
```


Write $`D^b_{\mathrm{coh}}(Z)`$ for the bounded derived category of coherent sheaves on $`Z`$, and set
```math
\mathcal K_p=\{E\in D^b_{\mathrm{coh}}(Y):Rp_*E\simeq0\}.
```

Must the induced functor
```math
\overline{Rp_*}:
D^b_{\mathrm{coh}}(Y)/\mathcal K_p
\longrightarrow D^b_{\mathrm{coh}}(X)
```

be an equivalence of triangulated categories for every such $`X`$ and $`p`$, with no restriction on dimension?

The quotient is the Verdier quotient by the full triangulated subcategory $`\mathcal K_p`$. Thus the assertion requires both full faithfulness and essential surjectivity. It concerns bounded coherent complexes, rather than only perfect complexes or an unbounded category of quasi-coherent sheaves.

## Application

A resolution replaces a singular space by a smooth one. The proposed equivalence would describe exactly which bounded coherent-complex information is lost under this replacement and permit categorical constructions from the smooth resolution to descend to the singular space. This is relevant to the derived-category interpretation of operations in the minimal model program.

## References

1. A. I. Efimov, [*Homotopy finiteness of some DG categories from algebraic geometry*](https://doi.org/10.4171/JEMS/979), *Journal of the European Mathematical Society* **22** (2020), 2879–2942. [Eligible author version](https://arxiv.org/pdf/1308.0135v3), p. 5, Conjecture 1.9 and Theorem 1.10.
2. M. Mauri and E. Shinder, [*Homological Bondal–Orlov localization conjecture for rational singularities*](https://doi.org/10.1017/fms.2023.65), *Forum of Mathematics, Sigma* **11** (2023), e66. [Author version](https://arxiv.org/pdf/2212.06786v2), Conjecture 1.1, Theorem 1.2 and Corollary 1.3.
3. Y. Shen and T. Sun, [*The Bondal–Orlov Localization Conjecture Holds for Threefolds*](https://arxiv.org/abs/2608.22539), preprint (2026), Theorem 1.0.2 and Corollary 1.0.3.

## Status review


**Known cases:** Shen-Sun prove localization with cohomological dimension at most two for the whole pushforward functor. Rational singularities only impose vanishing on the structure sheaf. The threefold theorem and K-theoretic or thick-generation statements do not settle the unrestricted bounded Verdier-quotient equivalence.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Shen-Sun prove localization with cohomological dimension at most two for the whole pushforward functor. Rational singularities only impose vanishing on the structure sheaf. The threefold theorem and K-theoretic or thick-generation statements do not settle the unrestricted bounded Verdier-quotient equivalence.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The pre-2022 source [1] explicitly states the general conjecture. Its theorem proves a special blow-up case with additional conditions on powers of the exceptional ideal.

Mauri–Shinder [2] prove that the image of $`Rp_*`$ generates the target derived category by cones and shifts, and obtain surjectivity on its Grothendieck group. These statements do not establish the displayed quotient equivalence. The projection formula does not supply a bounded preimage of every coherent complex: $`Lp^*F`$ can be unbounded when $`F`$ is not perfect.

Shen–Sun [3] announce the full localization theorem when $`R^ip_*F=0`$ for every coherent $`F`$ and every $`i>2`$. This covers projective resolutions of quasi-projective threefolds and some higher-dimensional cases, but imposes an additional hypothesis absent from the general question. Rationality requires this vanishing only for $`\mathcal O_Y`$, not for every coherent sheaf. The paper's introduction retains the general-dimensional conjecture.

Current targeted searches and comparison with the reviewed AIM, FURTHER and OpenAI catalogue located no matching complete resolution in unrestricted dimension. Selected primary statements and version histories were checked; external proofs were not fully audited.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-fb0797e175f030e3**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
