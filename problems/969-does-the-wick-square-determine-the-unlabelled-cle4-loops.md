# 969. Does the Wick square determine the unlabelled CLE4 loops?

**Area:** Probability, conformal random geometry and mathematical physics
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`D=\{z\in\mathbb C:|z|<1\}`$, and let $`\Phi`$ be the real Gaussian free field in $`D`$ with zero Dirichlet boundary conditions and covariance given by the Dirichlet Green function of $`-\Delta`$. Thus its covariance has the diagonal singularity
```math
G_D(z,w)=\frac{1}{2\pi}\log\frac1{|z-w|}+O(1).
```


Let $`\Gamma`$ be the **unlabelled, non-nested $`\mathrm{CLE}_4`$** obtained from $`\Phi`$ in the canonical Miller–Sheffield level-line coupling. This is the first layer of loops. To specify the joint law, conditional on the CLE loops with interiors $`(O_j)`$, choose independent fair signs $`(\varepsilon_j)`$ and independent zero-boundary GFFs $`\Phi_j`$ in $`O_j`$. With $`\lambda=\sqrt{\pi/8}`$, the field in $`O_j`$ is
```math
\Phi|_{O_j}=\Phi_j+2\lambda\varepsilon_j.
```

The resulting fields combine, in the sense of random distributions, into $`\Phi`$. In this coupling $`\Gamma`$ and its signs are measurable functions of $`\Phi`$.

Define the Wick square $`\Theta=:\!\Phi^2\!:`$ by mollification. For each $`f\in C_c^\infty(D)`$,
```math
\Theta(f)=\lim_{\epsilon\downarrow0}
\int_D f(z)\bigl(\Phi_\epsilon(z)^2-
\mathbb E[\Phi_\epsilon(z)^2]\bigr)\,dz,
```

where the limit is in $`L^2`$ of the probability space and $`\Phi_\epsilon`$ is a smooth mollification. This is a centered random distribution, rather than a pointwise square.

**Is the collection $`\Gamma`$ almost surely determined by $`\Theta`$?** Equivalently, does
```math
\sigma(\Gamma)\subseteq
\sigma\bigl(\Theta(f):f\in C_c^\infty(D)\bigr)
```

hold after completing both sigma-fields by null events?

The question asks for the unlabelled first-layer loop collection. It does not ask to recover the signs, the full GFF, or the individual Brownian loops.

## Application

The Wick square is the quadratic field observable corresponding, up to normalization, to the renormalized occupation field of a critical Brownian loop-soup. The question asks whether this observable retains the outer-boundary geometry of its clusters. This helps distinguish which parts of a conformally invariant random geometry are encoded by a field and which require extra randomness.

## Known results and scope

Qian–Werner's Proposition 5 constructs a simultaneous coupling of the GFF, its Wick square, the critical Brownian loop-soup and its outermost cluster boundaries. The existence of this coupling is known; the question concerns determination within that coupling.

Aru–Lupu–Sepúlveda's excursion decomposition recovers cluster closures and associated measures from the **full GFF**. This does not itself give recovery from the Wick square.

Lehmkuehler–Qian–Werner prove that the exact trace of the loop-soup is not determined even by the coupled GFF, and construct different traces with the same collection of cluster closures. That result distinguishes a cluster from its closure. It does not by itself decide whether the outer-boundary loops are determined by the Wick square.

The current announcement of a joint Ashkin–Teller scaling limit identifies limiting clusters as recursive local sets of the full limiting GFF. Its selected main statements do not assert reconstruction of $`\Gamma`$ from $`\Theta`$.

## References

1. W. Qian and W. Werner, *Decomposition of Brownian loop-soup clusters*, J. Eur. Math. Soc. 21 (2019), 3225–3253, [DOI](https://doi.org/10.4171/JEMS/902). Eligible source: [arXiv:1509.01180v3](https://arxiv.org/pdf/1509.01180v3), Section 3 and Proposition 5 pp. 9–10, and Section 5.4 p. 23.
2. J. Aru, T. Lupu and A. Sepúlveda, *Excursion decomposition of the 2D continuum GFF*, [arXiv:2304.03150v2](https://arxiv.org/pdf/2304.03150v2) (2023), Theorems 1–2 pp. 2–3, and Theorem 10 with the coupling discussion pp. 7–8.
3. M. Lehmkuehler, W. Qian and W. Werner, *Parity questions in critical planar Brownian loop-soups (or “where did the free planar bosons go?”)*, Probab. Theory Related Fields 195 (2026), 211–246, published online 2025, [DOI](https://doi.org/10.1007/s00440-025-01418-0). [arXiv:2403.07830v2](https://arxiv.org/pdf/2403.07830v2), Results A.1–A.3 pp. 2–3, Theorem 1 p. 9, and the Wick-square definition p. 21.
4. OpenAI, *The joint scaling limit of critical Ashkin–Teller currents* (2026), [preprint](https://github.com/openai/math/blob/main/preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026/main.pdf), Definition 2.1 pp. 6–7 and Theorem 2.3 p. 9.

## Status review


**Known cases:** The target is reconstruction of the unlabelled first CLE4 layer from the centered Wick-square distribution. Excursion decompositions, metric reconstruction from loops, parity identities and Ashkin-Teller scaling limits have different directions/conclusions.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is reconstruction of the unlabelled first CLE4 layer from the centered Wick-square distribution. Excursion decompositions, metric reconstruction from loops, parity identities and Ashkin-Teller scaling limits have different directions/conclusions.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked on 2026-10-24 against the eligible question and coupling, selected current primary statements and official version histories, targeted current and Prove2Me searches, and all-status AIM/FURTHER comparisons. No matching resolution or announcement was located. The review preserves the distinction between the full GFF and its Wick square, and between exact loop traces and outer boundaries. Selected primary passages were checked; every cited proof and the whole literature have not been certified.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-1961823dac27fe7a**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
