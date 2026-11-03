# 1014. Is every second p-Laplacian nodal line in a disk a diameter?

**Area:** Nonlinear spectral geometry
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`\Omega=\{x\in\mathbb R^2:|x|<1\}`$ and fix $`1<p<\infty`$. A second Dirichlet eigenfunction $`u\in W^{1,p}_0(\Omega)\setminus\{0\}`$ satisfies

```math
-\mathrm{div}(|\nabla u|^{p-2}\nabla u)=\lambda_{2,p}|u|^{p-2}u \quad\text{in }\Omega.
```


Must the interior nodal set $`\{x\in\Omega:u(x)=0\}`$ be a diameter of the disk, for **every** such second eigenfunction? The claim is known when $`p=2`$. For general $`p`$, numerical plots suggest a straight line through the center, but proving that the eigenfunction is nonradial or that its nodal set reaches the boundary does not establish this shape.

## Application

The second mode describes the lowest sign-changing vibration of a nonlinear membrane. Its nodal line separates the two regions of opposite displacement. The conjecture asks whether rotational symmetry of the disk forces this interface to be straight despite the nonlinear eigenvalue equation.

## References

1. B. Kawohl and J. Horák, [*On the geometry of the p-Laplacian operator*](https://www.aimsciences.org/article/doi/10.3934/dcdss.2017040), *Discrete and Continuous Dynamical Systems - S* **10** (2017), 799–813, Section 4, p. 805. The authors explicitly call the disk-diameter statement an open conjecture.
2. B. Kawohl, [*Variations on the p-Laplacian*](https://www.mi.uni-koeln.de/mi/Forschung/Kawohl/kawohl/variationsPLap.pdf), Section 5, Conjecture (a), states the same problem directly for $`1<p<\infty`$.
3. V. Bobkov, [*On the nodal set conjecture for the p-Laplacian in circularly symmetric domains*](https://arxiv.org/html/2602.01210v1), arXiv:2602.01210v1 (2026). The result concerns whether the nodal set meets the boundary; it does not assert the diameter shape.
4. T. V. Anoop, P. Drábek and Sarath Sasi, [*On the structure of the second eigenfunctions of the p-Laplacian on a ball*](https://doi.org/10.1090/proc/12902), *Proceedings of the American Mathematical Society* **144** (2016), 2503–2512. This proves nonradiality, which does not determine the nodal-line shape.

## Status review


**Known cases:** Every second eigenfunction must have a diameter nodal line. The February 2026 boundary-contact theorem and earlier nonradiality results do not fix its shape.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Every second eigenfunction must have a diameter nodal line. The February 2026 boundary-contact theorem and earlier nonradiality results do not fix its shape.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Anoop–Drábek–Sarath established that a second disk eigenfunction is not radial. Bobkov's 2026 boundary-contact theorem is also weaker than the displayed conjecture. A [bounded exact-source, announcement and semantic-duplicate review](../FURTHER_problems/_tracking/disk-p-laplacian-second-nodal-diameter-status-2026-10-21.json) found no complete proof or counterexample and no equivalent AIM/FURTHER problem. The review does not certify the absence of unindexed work.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-2163930443d0ffb9**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
