# 922. An integrable weak gradient for the uncentered cube maximal function

**Area:** Harmonic analysis and endpoint Sobolev regularity
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For an integer $`d\geq2`$, let $`W^{1,1}(\mathbb R^d)`$ denote the integrable real functions whose distributional first derivatives are integrable. For $`f`$ in this space, define
```math
M_{\square}f(x)=
\sup_{\substack{x\in Q\\Q\text{ an open axis-parallel cube}}}
\frac{1}{|Q|}\int_Q |f(y)|\,dy .
```

The cubes may have any positive side length and need only contain $`x`$; their centers are unrestricted.

**Does there exist a finite constant $`C_d`$, depending only on $`d`$, such that every $`f\in W^{1,1}(\mathbb R^d)`$ satisfies**
```math
M_{\square}f\in W^{1,1}_{\mathrm{loc}}(\mathbb R^d),
\qquad
\int_{\mathbb R^d}|\nabla M_{\square}f(x)|\,dx
\leq C_d\int_{\mathbb R^d}|\nabla f(x)|\,dx?
```

Here $`\nabla M_{\square}f`$ must be the distributional gradient represented by an $`L^1`$ vector field. Global integrability of $`M_{\square}f`$ itself is not required.

## Application

Maximal averaging replaces each value of a signal by the largest average magnitude seen on an admissible neighborhood. The question asks whether this operation controls total first-order spatial variation at the endpoint Sobolev exponent. It distinguishes a function-valued weak gradient from a derivative measure that can contain singular mass, a basic issue in the regularity theory of maximal operators.

## Known results and scope

Weigt proves that the uncentered cube maximal operator satisfies a dimensional total-variation bound for inputs of bounded variation. Applied to $`|f|`$, this already bounds the total mass of the distributional derivative of $`M_{\square}f`$. What remains is to show that this derivative has no singular part for Sobolev inputs. The current arXiv version and the published article explicitly distinguish these conclusions.

Weigt defines his operator using averages of $`g`$, allowing signed $`g`$. The operator above is his operator applied to $`g=|f|`$. Since $`|f|\in W^{1,1}`$ and $`|\nabla|f||\leq|\nabla f|`$ almost everywhere, his variation estimate applies to this classical absolute-average convention. No equivalence with his operator on arbitrary signed inputs is asserted.

The one-dimensional case is established. The 2025 Lahti–Weigt conditional regularity theorem concerns centered Euclidean balls. OpenAI's 2026 manuscript gives an endpoint gradient theorem for centered disks in the plane. Neither selected statement gives the uncentered cube conclusion above. Pointwise comparability of maximal values for different shapes does not supply comparability of their gradients.

## References

1. O. Saari, *Poincaré inequalities for the maximal function*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze **19** (2019), 1065–1083, [DOI](https://doi.org/10.2422/2036-2145.201705_001). Eligible primary version: [arXiv:1605.05176v2](https://arxiv.org/pdf/1605.05176v2), explicit open question p. 2 and absolute-average uncentered cube definition p. 3. Published counterparts are pp. 1066–1067.
2. J. Weigt, *The variation of the uncentered maximal operator with respect to cubes*, Journal of the European Mathematical Society **27** (2025), 2531–2570, [DOI](https://doi.org/10.4171/JEMS/1575), introduction and Theorem 1.1, pp. 2531–2533. [Current arXiv version, v4](https://arxiv.org/pdf/2109.10747v4), pp. 1–3. The published introduction explicitly leaves the Sobolev weak-gradient question for cubes open.
3. P. Lahti and J. Weigt, *The centered maximal operator removes the non-concave Cantor part from the gradient*, [arXiv:2510.01936v1](https://arxiv.org/pdf/2510.01936v1) (2025), operator definition p. 1 and Theorem 1.2 p. 3. Its conditional upgrade uses centered balls.
4. OpenAI, *An Endpoint Gradient Bound for the Centered Disk Maximal Operator* (2026), [manuscript](https://github.com/openai/math/blob/main/preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/article.pdf), Theorem 1.1 and operator definition p. 1; comparison with cube variation results pp. 2–3. This is an announced planar centered-disk result; its complete proof and formalization have not been checked here.
5. J. Kapulainen, *On continuity of generalized maximal functions*, manuscripta mathematica **177** (2026), article 49, [DOI](https://doi.org/10.1007/s00229-026-01732-4), Sections 1–2 and Theorem 4.5. The theorem proves pointwise continuity for continuous integrable inputs, a different regularity statement.

## Status review


**Known cases:** The cube, uncentered, endpoint W1,1 assertion requires absolute continuity of the BV derivative. The centered planar-disk announcement, fractional maximal estimates and existing BV bound do not settle it.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The cube, uncentered, endpoint W1,1 assertion requires absolute continuity of the BV derivative. The centered planar-disk announcement, fractional maximal estimates and existing BV bound do not settle it.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 2026-10-24 against the eligible primary question and definitions, Weigt's current v4 and published introduction, the selected later primary statements and version histories, targeted solution and announcement searches, current public AIM/OpenAI metadata, the Prove2Me homepage and targeted navigation, and all-status AIM/FURTHER comparisons. No matching resolution or announcement was located. The existing FURTHER problem about the sharp weak-type $`(1,1)`$ constant of the centered square maximal operator concerns maximal values, a different operator and norm.

The 2021 first version of Weigt's paper asserted that a ball-based regularity argument extends to cubes. The current v4 and published article instead explicitly leave the cube weak-gradient question open; the earlier sentence is not used as a current resolution.

The review covers selected primary statements and their scope. It does not certify all cited proofs or establish an exhaustive absence of solutions.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-a785c86819d04640**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
