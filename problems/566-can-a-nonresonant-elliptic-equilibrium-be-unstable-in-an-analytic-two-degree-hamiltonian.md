# 566. Can a nonresonant elliptic equilibrium be unstable in an analytic two-degree Hamiltonian?

**Area:** Geometry and topology
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Does there exist a real-valued, real-analytic Hamiltonian defined near $`0\in\mathbb R^4`$, with canonical coordinates $`z=(x_1,x_2,y_1,y_2)`$, of the form
```math
H(x,y)=\frac{\omega_1}{2}(x_1^2+y_1^2)
        +\frac{\omega_2}{2}(x_2^2+y_2^2)+O(\|z\|^3),
```

where
```math
k_1\omega_1+k_2\omega_2\ne0
 \quad\text{for every }(k_1,k_2)\in\mathbb Z^2\setminus\{0\},
```

such that the origin is **Lyapunov unstable** for
```math
\dot x_j=\partial_{y_j}H,\qquad
 \dot y_j=-\partial_{x_j}H,\qquad j=1,2?
```


Instability means that some fixed neighbourhood $`U`$ of the origin, with closure inside the domain of $`H`$, is exited in positive time by orbits starting arbitrarily close to the origin. The local flow is followed until exit.

The frequency vector and Hamiltonian are existential choices. No particular arithmetic class of frequencies, global extension, genericity, KAM condition or normal-form convergence property is required. Necessarily $`\omega_1\omega_2<0`$: a definite quadratic part would give stability by conservation of energy.

## Application

This asks whether linear nonresonance and analyticity can still permit nonlinear escape in the smallest nontrivial autonomous Hamiltonian phase space. It distinguishes actual long-time stability from the finite-time control provided by normal-form estimates.

## References

- B. Fayad, *Lyapunov unstable elliptic equilibria*, **Journal of the American Mathematical Society** 36 (2023), 81–106. [Published article](https://doi.org/10.1090/jams/997); [author-hosted published copy](https://webusers.imj-prg.fr/~bassam.fayad/F_unstable.pdf), Section 2.1, p. 84; [arXiv:1809.09059v3](https://arxiv.org/abs/1809.09059v3).
- F. Trujillo, *Lyapunov instability in KAM stable Hamiltonians with two degrees of freedom*, **Journal of Modern Dynamics** 19 (2023), 363–383. [Published article](https://doi.org/10.3934/jmd.2023010). Its examples are Gevrey-smooth.
- B. Fayad, J. Paradela, M. Saprykina and T. M. Seara, *On the density of Lyapunov unstable elliptic equilibria* (2026), [arXiv:2609.03722v1](https://arxiv.org/html/2609.03722v1), Theorems A–B and Section 6.

## Status review

Checked **30 October 2026**. Fayad's published paper explicitly leaves the two-degree question open. Its analytic instability examples start in three degrees of freedom; its divergent Birkhoff normal forms in two degrees do not establish instability. Trujillo's two-degree constructions have weaker regularity. The September 2026 analytic density results require at least five degrees; their two-degree parameter families supply intermediate periodic-orbit constructions rather than the equilibrium requested here.

No matching complete resolution or announcement was found in current searches or the semantic comparison with the AIM/OpenAI all-status corpus and developing collection. These checks are dated and may miss an unlocated result.


### Online recheck, 2026-10-30

Analytic unstable elliptic equilibria are constructed in higher degrees of freedom; two-degree examples cited here have weaker regularity. The September 2026 density theorem requires at least five degrees and does not provide this analytic two-degree example.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2609.03722); [status source 2](https://doi.org/10.1090/jams/997); [status source 3](https://doi.org/10.3934/jmd.2023010). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-159aaf6648ffaa2c** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
