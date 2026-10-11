# Target comparison for AIM 412

Target: [Sharp vanishing-viscosity control time for downstream transport](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/412-positive-transport-sharp-uniform-control-time.md),
revision c9929805cece044705abaaebe1cebddac1ba11a6.
Manuscript: [Downstream transport control: a literature resolution of AIM 412](manuscript.pdf),
12 October 2026.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| Interval (0,L), L>0; constant positive speed M>0; positive viscosity | Equation (1), p. 1; Proposition 1, pp. 1--2 | Same model and all fixed positive L,M |
| Equation y_t+M y_x−epsilon y_xx=0, control at x=0, zero data at x=L | Equation (1); backward-adjoint boundary calculation before (6), p. 2 | Same sign, actuator and downstream boundary |
| Arbitrary unit L2 initial states; L2 boundary controls; transposition solutions | Equation (2), p. 1; terminal identity (6) and the normalized initial state, p. 2 | Uses an admissible unit initial state for each viscosity, as permitted by the supremum |
| Worst minimal control norm, with an infimum over null controls and supremum over initial states | Equation (2); estimate (7) and following paragraph, p. 2 | Applies to every null control; no attainment or supremum/limit interchange is assumed |
| Every fixed T>L/M should have cost tending to zero as viscosity tends to zero | Corollary 3, p. 2: T=3L/(2M)>L/M has cost tending to infinity | Complete negative answer to this universal yes/no assertion |
| Arbitrary physical length and positive speed | Scaling in Proposition 1: tau=MT/L, delta=epsilon/(ML); identities (4)--(5), p. 2 | Covers every fixed L,M>0; retains the factor M in the squared flux norm |
| A limit through all sufficiently small positive viscosities | Lemma 2 and (4)--(7) | A positive viscosity-independent terminal bound and flux tending to zero imply full divergence, not only a subsequential obstruction |
| Public imported theorem | Lemma 2, pp. 1--2, citing Koike--Laheurte Theorem 4.1, primary PDF pp. 16--18 | Ordinary attributed primary preprint theorem, with the needed normalized positive adjoint equation and smooth finite-mode witnesses |

The precise external input is
[Koike--Laheurte, arXiv:2609.35355v1](https://arxiv.org/pdf/2609.35355v1).
Its Theorem 1.3, PDF p. 4, also states the positive-speed divergence below
2L/M. The note proves the relevant implication directly from Theorem 4.1
for the official transposition formulation.

The note does not settle the critical time T=2L/M, which the source leaves
open on PDF p. 5. This is not an unproved part of the original displayed
assertion's negation: one admissible time suffices, and Corollary 3 supplies
such a time for every positive L,M.

This comparison was prepared from the finished manuscript and the public
official statement. Independent mathematical review of the literature
resolution and its target correspondence is requested.
