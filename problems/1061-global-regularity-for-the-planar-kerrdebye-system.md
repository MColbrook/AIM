# 1061. Global regularity for the planar Kerr–Debye system

**Area:** Nonlinear waves, fluids and kinetic equations
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`s\ge3`$ be an integer. On $`\mathbb R^2`$, consider the real electric displacement $`D=(D_1,D_2)`$, electric field $`E=(E_1,E_2)`$, magnetic component $`h`$, and susceptibility $`\chi`$, satisfying

```math
\begin{aligned}
\partial_tD_1-\partial_2h&=0,&
\partial_tD_2+\partial_1h&=0,\\
\partial_th+\partial_1E_2-\partial_2E_1&=0,&
\partial_t\chi&=|E|^2-\chi,\\
D&=(1+\chi)E,&\mathrm{div}D&=0.
\end{aligned}
```

For every initial triple

```math
(D_0,h_0,\chi_0)\in H^s(\mathbb R^2;\mathbb R^2)
\times H^s(\mathbb R^2)\times H^s(\mathbb R^2),
\qquad \mathrm{div}D_0=0,\qquad\chi_0\ge0,
```

must the maximal local classical solution extend to every $`t\ge0`$, with $`(D,h,\chi)\in C([0,\infty);H^s)\cap C^1([0,\infty);H^{s-1})`$? Prove this assertion or give admissible data with finite-time loss of this regularity. The norms may grow with time but must remain finite on every finite time interval. No smallness, symmetry, compact support, or equilibrium preparation is assumed.

Here $`E_0=D_0/(1+\chi_0)`$. The equations propagate $`\mathrm{div}D=0`$ and $`\chi\ge0`$. The material constants and the positive response time have been normalized to one by invertible changes of units; no uniform estimate as the response time tends to zero is requested. This is an explicit Sobolev formulation of the whole-plane transverse-magnetic (TM) case of Kanso's broader smooth-continuation question.

## Application

The system models electromagnetic propagation in a nonlinear dielectric with a delayed material response. Global classical continuation would establish whether that response prevents finite-time singularities for arbitrary planar TM pulses.

## References

1. M. Kanso, [*Global existence of small solutions to the Kerr–Debye model for the three-dimensional Cauchy problem*](https://ems.press/content/serial-article-files/44684), *Portugaliae Mathematica* **68** (2011), 389–409, [doi:10.4171/PM/1898](https://doi.org/10.4171/PM/1898). Proposition 1.1 and the explicit open question on p. 394.
2. M. Kanso, [*Sur le modèle de Kerr-Debye pour la propagation des ondes électromagnétiques*](https://theses.fr/2012BOR14587/document), doctoral thesis (2012), equations (1.2.20)–(1.2.21), pp. 7, 17 and 26.
3. T. Dohnal, M. Ionescu-Tira and M. Waurick, [*Well-Posedness and Exponential Stability of Nonlinear Maxwell Equations for Dispersive Materials with Interface*](https://arxiv.org/abs/2301.10099), arXiv:2301.10099v3; *Journal of Differential Equations* **383** (2024), 24–77, [doi:10.1016/j.jde.2023.11.005](https://doi.org/10.1016/j.jde.2023.11.005). Remark 2.14, Corollary 2.30 and Theorem 3.13 in the reviewed preprint.
4. N. Margenberg and M. Bause, [*Well-posedness and exponential stability of dispersive nonlinear Maxwell equations with PML: An evolutionary approach*](https://arxiv.org/abs/2412.05468), arXiv:2412.05468v1 (2024), Section 3, especially pp. 8–9.
5. C. Bresch and R. Schnaubelt, [*Local wellposedness of Maxwell systems with retarded material laws on domains with interfaces*](https://www.waves.kit.edu/downloads/CRC1173_Preprint_2026-55.pdf), CRC 1173 Preprint 2026/55 (20 October 2026), Theorem 5.8.

## Status review


**Known cases:** The target is arbitrary-large-data planar transverse-magnetic Kerr-Debye on R2. The retrieved global Kerr-Debye theorem treats one spatial dimension; 3D small-data and dispersive/interface local theorems do not establish the planar all-data assertion.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The target is arbitrary-large-data planar transverse-magnetic Kerr-Debye on R2. The retrieved global Kerr-Debye theorem treats one spatial dimension; 3D small-data and dispersive/interface local theorems do not establish the planar all-data assertion.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Kanso explicitly leaves the two-dimensional TM global-existence question open. The sufficiently small three-dimensional data theorem and the transverse-electric results concern different hypotheses. A planar solution constant in the third coordinate does not supply finite-energy three-dimensional data.

The later primary results reviewed here give local continuation criteria, require small data, or impose additional Lipschitz assumptions or modifications to the material response. They do not establish arbitrary-data global classical continuation for the displayed system. Bounded searches of current literature and announced results, with all-status AIM/FURTHER/OpenAI statement comparisons, located no complete resolution or duplicate.

The original published question, the thesis's exact TM equations, and selected current theorem hypotheses were independently compared. The stated Sobolev class is our explicit formulation; the source does not prescribe a minimal planar regularity threshold. Full publication/preprint parity and complete proofs of the cited partial results were not audited; those limits remain in the review records.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-d02945c12d33ec4c**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
