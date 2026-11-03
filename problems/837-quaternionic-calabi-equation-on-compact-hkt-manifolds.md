# 837. Quaternionic Calabi equation on compact HKT manifolds

**Area:** Geometry and topology
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`n\ge1`$ and let $`M`$ be a compact connected smooth manifold without boundary of real dimension $`4n`$. Give $`M`$ integrable hypercomplex structures $`I,J,K`$ and a positive hyperhermitian metric $`g`$. Use the right-action convention of reference 2: write

```math
\omega_L(X,Y)=g(XL,Y),\qquad
\Omega=\omega_J-i\omega_K,\qquad
\partial\Omega=0.
```

Here Dolbeault types and operators are taken with respect to $`I`$. The final condition is the HKT condition. On differential forms set $`(J\eta)(X_1,\ldots,X_k)=\eta(X_1J,\ldots,X_kJ)`$ and

```math
\partial_J=J^{-1}\bar\partial J.
```

A $`(2,0)`$-form $`\eta`$ is q-real when $`J\bar\eta=\eta`$, and is strictly q-positive when $`\eta(Z,\bar ZJ)>0`$ for every nonzero $`I`$-$`(1,0)`$ vector $`Z`$.

Fix a nowhere-vanishing $`I`$-holomorphic $`(2n,0)`$-form $`\Theta`$, with its q-positive choice: $`\Theta=h\Omega^n`$ for a smooth positive real function $`h`$. For **every** real $`f\in C^\infty(M)`$ satisfying

```math
\int_M(e^f-1)\Omega^n\wedge\overline\Theta=0,
```

does there exist a real $`\varphi\in C^\infty(M)`$ such that

```math
(\Omega+\partial\partial_J\varphi)^n=e^f\Omega^n,
\qquad \Omega+\partial\partial_J\varphi>0?
```

The inequality means strict q-positivity. No local flatness or compatible hyperKähler or locally conformally hyperKähler metric is assumed. Uniqueness modulo real constants is already known; the unresolved target is existence. One can select a representative by imposing $`\int_M\varphi\Omega^n\wedge\overline\Theta=0`$.

## Application

This asks whether a quaternionic volume density can be prescribed within a fixed HKT potential class. It is the hypercomplex analogue of the Calabi problem and would produce canonical HKT metrics in geometric settings where the holomorphic volume form is available.

## References

1. S. Alesker and M. Verbitsky, [Quaternionic Monge–Ampère equation and Calabi problem for HKT-manifolds](https://arxiv.org/html/0802.4202v3), Israel Journal of Mathematics **176** (2010), 109–138; arXiv:0802.4202v3 (27 July 2008), Conjectures 1.5 and 5.1, Corollary 4.10 and Remark 4.11. The latest author version explicitly includes the compatibility condition.
2. S. Dinew and M. Sroka, [On the Alesker–Verbitsky Conjecture on HyperKähler Manifolds](https://doi.org/10.1007/s00039-023-00648-5), Geometric and Functional Analysis **33** (2023), 875–911, Conjecture 1.2 and equation (1.3); §§2.1–2.2 give the operator, metric and positivity conventions used here. See Theorem 1.1 and Remark 6.1 for the compatible-hyperKähler case.
3. G. Gentili, A. Trusiani and L. Vezzoni, [Continuous solutions to the quaternionic Monge–Ampère equation on locally flat HKT manifolds](https://arxiv.org/html/2609.21528v1), arXiv:2609.21528v1 (18 September 2026), Introduction and Theorem 1.1.
4. G. Gentili and L. Vezzoni, [HKT geometry on locally conformally hyperkähler manifolds](https://arxiv.org/html/2610.07897v1), arXiv:2610.07897v1 (6 October 2026), Theorem 1.1 and Remark 3.4.

## Status review


**Known cases:** The September 2026 theorem gives continuous solutions with local flatness, and the October 2026 smooth result requires a compatible locally conformally hyperKahler metric. The hyperKahler case is also known; none supplies smooth existence on every HKT manifold in the displayed holomorphic-volume class.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The September 2026 theorem gives continuous solutions with local flatness, and the October 2026 smooth result requires a compatible locally conformally hyperKahler metric. The hyperKahler case is also known; none supplies smooth existence on every HKT manifold in the displayed holomorphic-volume class.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 26 October 2026. Dinew–Sroka establish smooth existence when the hypercomplex structure admits a compatible hyperKähler metric; the initial HKT metric may be different. The September 2026 theorem gives continuous solutions under local flatness. The October 2026 theorem establishes smooth existence with an additional compatible locally conformally hyperKähler metric. Its extra scalar on the right-hand side becomes zero under the displayed holomorphic-volume compatibility, while its additional geometric assumption remains.

These results do not establish smooth existence for the full stated HKT class. Current literature, revision, complete announcement and all-status duplicate checks found no matching complete resolution. Selected primary definitions and theorem scopes were checked independently; this is a bounded literature assessment, not certification of all cited proofs.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-bcc1ff6354cd2f52**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
