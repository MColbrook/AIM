# AIM 180 target comparison

[Problem statement at the frozen AIM revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/180-activated-random-walk-density.md)

Theorem 1 of the manuscript proposes the full limit of the expected stationary sleeper density. The following table maps the original assumptions and conclusion to the proof.

| AIM assumption or conclusion | Where it is used |
| --- | --- |
| Every fixed positive sleep rate | Theorem 1 and section 2 fix an arbitrary real \(\lambda>0\). All later estimates may depend on that fixed rate. |
| Unit-rate nearest-neighbor walk on \(\mathbb Z^2\), lone-particle sleeping, reactivation on arrival | Theorem 1 specifies the continuous-time process. Section 2 identifies its finite stabilization with the legal stack process and checks the finite-jump fixation convention. |
| The iid Poisson all-active infinite-volume threshold | Section 2 applies the finite-box exit criterion below this threshold. Section 3 uses the same Poisson initial law and common stack exhaustion to compare the left pressure slope with the threshold. |
| The squares \(\Lambda_n=[-n,n]^2\cap\mathbb Z^2\), with particles killed on exit | Section 2 translates the domain to side \(L=2n+1\), preserving every jump and kill. Interior killed squares in the proof are used for local comparisons on the original ambient stacks. |
| Independent uniform drive, one particle between stabilizations | Section 2 identifies the stationary law of this irreducible driven chain with the saturated sampler. In sections 4 and 6 the local samplers with fixed deterministic inlets have the same corresponding stationary law. |
| Limit of the expected sleeper count divided by \(|\Lambda_n|\) | Equation (1) proves the lower bound. Section 6 excludes every sequence of odd square sizes whose expected density stays above the threshold by a fixed positive amount. Since \(|\Lambda_n|=(2n+1)^2\), these give exactly the stated limit. |

The upper bound uses a small-field estimate for the stationary logarithmic moment and a finite family of approximations to the actual incoming particle counts. For each fixed inlet profile, the tile test counts are independent. The argument takes a union of the corresponding events before choosing a profile for the ambient sample.
