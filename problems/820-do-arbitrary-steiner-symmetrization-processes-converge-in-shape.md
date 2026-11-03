# 820. Do arbitrary Steiner symmetrization processes converge in shape?

**Area:** Convex and geometric analysis
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

For a nonempty compact set $`K\subset\mathbb R^n`$ and a direction $`u\in S^{n-1}`$, let $`S_uK`$ denote its Steiner symmetral in the paper's compact-set convention. Given an arbitrary direction sequence $`(u_m)_{m\ge1}`$, form

```math
K_m=S_{u_m}\cdots S_{u_1}K.
```


**Question (Bianchi–Burchard–Gronchi–Volčič, Open Problem 6.2).** Must every such process *converge in shape*? In the source's usage, this means that there is a sequence of Euclidean isometries $`(I_m)`$, chosen from the direction sequence and usable for **every** nonempty compact initial set $`K`$, for which $`I_mK_m`$ converges in Hausdorff distance. The limit may depend on $`K`$ and need not be a ball.

The original Theorem 2.2 proves this when the squared successive angular increments are summable. With only finitely many distinct directions, its Theorem 6.1 gives ordinary convergence without moving the sets. Neither result addresses every direction sequence.

## Application

The answer would determine whether the known failures of ordinary Steiner-iteration convergence can always be explained by the set's changing position or orientation, or whether some direction sequence changes the shape itself indefinitely.

## References

1. G. Bianchi, A. Burchard, P. Gronchi and A. Volčič, [*Convergence in shape of Steiner symmetrizations*](https://doi.org/10.1512/iumj.2012.61.5087), *Indiana Univ. Math. J.* **61** (2012), no. 4, 1695–1710, Open Problem 6.2; [original arXiv v1 PDF](https://arxiv.org/pdf/1206.2041v1), physical pp. 4 and 11.
2. G. Bianchi and P. Gronchi, [*Symmetrizations*](https://people.dimai.unifi.it/bianchi/lavori/bianchi_gronchi_symmetrizations_preprint_capitolo_book.pdf), in *Convex Geometry*, Lecture Notes in Mathematics 2332 (2023), pp. 233–292, §5.7, printed p. 257. The coauthors explicitly retain the unrestricted question.
3. J. Ulivelli, [*Convergence properties of symmetrization processes*](https://arxiv.org/pdf/2207.05416), *Adv. Appl. Math.* **146** (2023), 102484. The shape-stability comparison concerns conditional processes.

## Status review


**Known cases:** Square-summable angular increments, finitely many directions and finite unions of line segments are conditional positive results. They do not prove shape convergence for every direction sequence simultaneously for all compact initial sets with the source uniform-isometry convention.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

Square-summable angular increments, finitely many directions and finite unions of line segments are conditional positive results. They do not prove shape convergence for every direction sequence simultaneously for all compact initial sets with the source uniform-isometry convention.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The 2023 coauthor survey explicitly says the full question is open. Later conditional convergence and shape-stability results do not assert the all-sequences statement. Targeted proof, counterexample, announcement and semantic-duplicate searches through 2026-10-22 found no exact resolution; this is a bounded search. The adjacent Open Problem 6.3 in the original paper was answered by [Bianchi–Gardner–Gronchi](https://arxiv.org/pdf/1908.03259) and is excluded. The already admitted [minimal-discrepancy question](../cut_problems/FURTHER_problems/geometry-topology/lead-0e792b92b8de2280.md) requires convergence to a ball under a special direction condition, so it is distinct. The [original-source receipt](../FURTHER_problems/_tracking/steiner-shape-all-directions-original-2026-10-22.json) and [status audit](../FURTHER_problems/_tracking/steiner-shape-all-directions-status-2026-10-22.json) record the evidence and limits.

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-97e271959d863311**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
