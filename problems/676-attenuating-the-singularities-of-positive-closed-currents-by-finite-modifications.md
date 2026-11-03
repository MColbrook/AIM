# 676. Attenuating the singularities of positive closed currents by finite modifications

**Area:** Complex analysis and Kähler geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`X`$ be a connected compact Kähler manifold of complex dimension $`n\ge3`$, let $`T`$ be a positive closed real $`(1,1)`$-current on $`X`$, and let $`\varepsilon>0`$.

Is there a finite composition of blowups along smooth complex centers $`\pi:Y\to X`$ and a finite effective real divisor $`D=\sum_{j=1}^N a_jD_j`$, with $`a_j\ge0`$ and simple normal crossing support, such that

```math
\pi^*T=[D]+R,\qquad R\ge0,\quad dR=0,
\qquad \sup_{y\in Y}\nu(R,y)<\varepsilon?
```

Here $`[D_j]`$ is integration over the irreducible divisor $`D_j`$, and $`\nu(R,y)`$ is the usual point Lelong number, measuring the logarithmic singularity of a local plurisubharmonic potential. Use a normalization in which a simple logarithmic pole along a smooth divisor has Lelong number one. Pullback is defined using local potentials. Simple normal crossings means that the divisor support is locally a union of coordinate hyperplanes. The empty divisor is allowed.

Both the modification and the divisor may depend on $`T`$ and $`\varepsilon`$. There is no bound prescribed on the number of blowups. One finite modification must control the residual Lelong numbers at **every point**, rather than only generic points of divisors or a finite selection of valuations.

The corresponding statement is known for compact complex surfaces. Currents with everywhere zero Lelong number need no modification, and analytic logarithmic singularities can be resolved. The question permits general nonanalytic singularities. It is the explicitly closed-current, compact Kähler subclass of the survey's higher-dimensional question; no equivalence with arbitrary nonclosed Hermitian backgrounds is asserted.

## Application

Lelong numbers measure concentration of singular positive currents. Separating divisorial concentrations from a uniformly mild remainder would help describe singular Hermitian metrics and their intersection theory.

## References

1. S. Dinew, V. Guedj and A. Zeriahi, *Open problems in pluripotential theory*, Complex Variables and Elliptic Equations **61** (2016), 902–930. [DOI](https://doi.org/10.1080/17476933.2015.1121481), [primary preprint](https://arxiv.org/pdf/1511.00705v1), Section 5.1 and Question 34 on pp. 16–17.
2. V. Guedj, *Desingularization of quasiplurisubharmonic functions*, International Journal of Mathematics **16** (2005), 555–560. [DOI](https://doi.org/10.1142/S0129167X05002953), [published primary PDF](https://www.math.univ-toulouse.fr/~guedj/fichierspdf/IJM2005.pdf), Theorem 1.1.
3. M. Xia, *Transcendental b-divisors I—Correspondence with currents*, [arXiv:2603.14348v1](https://arxiv.org/pdf/2603.14348v1), Theorem 4.11 and Corollaries 4.12–4.15; selected comparison only.

## Status review


**Known cases:** The primary survey asks for one finite modification controlling every residual Lelong number. Xia b-divisor/cohomological approximation permits varying models or representatives and is not this exact fixed-current attenuation. The OpenAI zero-Lelong results concern special nef adjoints and boundary hypotheses, not arbitrary positive closed currents. No matching complete general theorem found.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The primary survey asks for one finite modification controlling every residual Lelong number. Xia b-divisor/cohomological approximation permits varying models or representatives and is not this exact fixed-current attenuation. The OpenAI zero-Lelong results concern special nef adjoints and boundary hypotheses, not arbitrary positive closed currents. No matching complete general theorem found.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/2603.14348v1); [comparison source 2](https://www.math.univ-toulouse.fr/~zeriahi/DGZ-arXiv2015.pdf); [comparison source 3](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 17 October 2026. Current searches found no matching higher-dimensional resolution or complete announcement. The 2026 b-divisor approximation results concern cohomological representatives and varying models; the selected statements do not provide the displayed uniform estimate for the pullback of the original fixed current on one finite model. Fixed-modification multiplier-ideal estimates have a modification-dependent Jacobian error and cannot simply be treated as uniform after resolving varying ideals.

The primary survey and six-page surface paper were read in full by the source reviewer, with a separate selected-primary implication audit. All-status AIM/OpenAI and Prove2Me listing-description comparisons found no equivalent target. These are bounded status checks, not certification of every later proof or an exhaustive absence theorem. Exact passages and limits are retained in the [source review](../FURTHER_problems/_tracking/parallel/complex-bayesian/desingularization-review.json) and [independent audit](../FURTHER_problems/_tracking/parallel/rough-filtering/cross-desingularization-review.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-129ac77e20d498bf**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
