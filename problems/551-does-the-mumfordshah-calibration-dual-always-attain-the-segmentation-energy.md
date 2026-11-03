# 551. Does the Mumford–Shah calibration dual always attain the segmentation energy?

**Area:** Continuous optimization
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be bounded and Lipschitz, and let $`g\in L^\infty(\Omega;[0,1])`$. For $`u\in SBV(\Omega;[0,1])`$, with jump set $`S_u`$, consider the Mumford–Shah segmentation energy

```math
F_g(u)=\frac12\int_{\Omega\setminus S_u}|\nabla u|^2\,dx
       +\mathcal H^1(S_u)
       +\frac12\int_\Omega |u-g|^2\,dx,
\qquad P_g=\inf_u F_g(u).
```


Its calibration dual $`Q_g`$ [1, §5.3] maximizes $`-\int_\Omega\sigma^t(x,0)\,dx`$ over admissible fields $`\sigma=(\sigma^x,\sigma^t)`$ on $`\Omega\times[0,1]`$ satisfying $`\mathrm{div}_{x,t}\sigma=0`$, $`\sigma^x\cdot\nu_\Omega=0`$ on the lateral boundary, and the convex constraints

```math
\frac12|\sigma^x(x,t)|^2\leq\sigma^t(x,t)+\frac12|t-g(x)|^2
\quad\text{a.e.},\qquad
\left|\int_{t_1}^{t_2}\sigma^x(x,s)\,ds\right|\leq1
\quad\text{for a.e. }x\text{ and all }t_1,t_2\in[0,1].
```


Is $`P_g=Q_g`$ for **every** such $`\Omega`$ and $`g`$? This is the explicit conjecture of Bouchitté and Phan [1, p. 220]. Their Proposition 5.1 proves $`P_g\geq Q_g`$ and gives equality whenever a suitable calibration exists for a minimizing image; neither statement establishes the general equality. The admissible-field and trace conventions are those of [1, problem (Q)].

## Application

The primal energy balances smoothness within image regions, the length of boundaries between them, and fidelity to measured grey levels. A zero duality gap would make the calibration dual an exact global certificate for every instance of this continuous segmentation model.

## References

1. G. Bouchitté and M. Phan, [*A duality recipe for non-convex variational problems*](https://comptes-rendus.academie-sciences.fr/mecanique/item/10.1016/j.crme.2017.12.011.pdf), *Comptes Rendus Mécanique* **346** (2018), 206–221, §5.3, especially p. 220, problems (P)/(Q), Proposition 5.1 and the explicit Conjecture; [DOI](https://doi.org/10.1016/j.crme.2017.12.011).
2. C. Labourie and E. Milakis, [*The calibration method for the thermal insulation functional*](https://www.numdam.org/item/10.1051/cocv/2022045.pdf), *ESAIM: Control, Optimisation and Calculus of Variations* **28** (2022), article 50, introduction pp. 1–2. It notes that calibration existence for Mumford–Shah minimizers is not known in general, while studying a different energy.
3. F. Deangelis, [*Solution of the Mumford–Shah conjecture*](https://arxiv.org/abs/2609.26732), arXiv:2609.26732 (2026). Its announced planar classification and interior regularity result has a different conclusion from the calibration-duality equality.

## Status review

The 2015 gapless duality theorem for non-convex **integral** functionals does not include this jump energy; the recent planar regularity announcements also do not establish $`P_g=Q_g`$. A [bounded status and duplicate audit](../FURTHER_problems/_tracking/j302-bouchitte-phan-mumford-shah-calibration-duality-status-2026-10-22.json) through 22 October 2026 found no matching proof, counterexample or announced resolution.


### Online recheck, 2026-10-30

Regularity/classification of planar Mumford–Shah minimizers is not equality with the calibration dual. The source's gapless-duality conjecture for this jump-energy functional remains beyond integral-functional and thermal-insulation calibration results.

Comparators and current-status sources: [status source 1](https://doi.org/10.1016/j.crme.2017.12.011); [status source 2](https://www.numdam.org/item/10.1051/cocv/2022045.pdf); [status source 3](https://arxiv.org/abs/2609.26732). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-ec9bcf83b8c6e1d4** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
