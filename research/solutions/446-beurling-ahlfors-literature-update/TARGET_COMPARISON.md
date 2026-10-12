# Comparison with AIM 446

Target: [446. The sharp Beurling–Ahlfors bound for planar elliptic systems](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/446-beurling-ahlfors-sharp-norm.md), repository revision c9929805cece044705abaaebe1cebddac1ba11a6.

Manuscript: [A note on the sharp Beurling–Ahlfors bound](paper/beurling_ahlfors_update.pdf), by Kaiwen Jin, October 12, 2026.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| Plane identified with the complex numbers; planar Lebesgue measure | Section 1 fixes the complex coordinates, Wirtinger derivatives, and area measure. | Same domain and measure. |
| Disk principal value with kernel $-1/(\pi z^2)$ | Equation (1) is the target definition. Section 3 proves the distribution identities and identifies their convolution with the pointwise disk limit. | Same kernel, sign, and truncation. The limit exists at every point for the stated inputs. |
| Every complex $f\in C_c^\infty(\mathbb C;\mathbb C)$ | Theorem 1 and Section 3 use the unrestricted Cauchy potential of an arbitrary such input. | All complex smooth compactly supported inputs, including nonzero-mean inputs. |
| Every real $1<p<\infty$ | Sections 2–3 establish the estimate for $p>2$; Section 4 proves the $p=2$ identity and the estimate for $1<p<2$ by complex duality. | Full open exponent interval. |
| Constant exactly $p^*-1$, where $p^*=\max\{p,p/(p-1)\}$ | Theorem 1, equation (2); Lemma 3 gives the scalar majorant, and Section 4 gives the conjugate-exponent constant. | Uniform in the input; depends only on $p$. |
| Matching upper bound for the known lower bound | Theorem 1 proves the requested upper bound. The cited primary paper also states the operator norm equality in Corollary 2, equation (4). | The entire upper-bound question is covered. |
| Public dependency sufficient to support the central implication | Theorem 2 of the note quotes Agazzi et al., Theorem 1, on arbitrary real matrices and smooth periodic two-component fields. Sections 2–4 supply the subsequent transfer. | Versioned public dependency: arXiv:2609.28311v2, Theorem 1 and its proof in Section 2. |

The unrestricted field and matrix range in the imported theorem is essential: a special class of real, radial, or Hessian inputs would not give this argument. No such restriction is made here. The cutoff estimate in Section 3 holds for every fixed exponent greater than 1 even when the potential itself is not square integrable.

The primary result is due to Agazzi and collaborators; the note supplies an attributed exposition of the transfer to the frozen AIM formulation. The primary paper is a preprint. This correspondence does not itself constitute independent verification or a catalogue-status decision.
