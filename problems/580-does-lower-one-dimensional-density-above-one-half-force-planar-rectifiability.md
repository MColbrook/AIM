# 580. Does lower one-dimensional density above one half force planar rectifiability?

**Area:** Geometric measure theory
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`E\subset\mathbb R^2`$ be Borel with $`\mathcal H^1(E)<\infty`$. Suppose that for $`\mathcal H^1`$-almost every $`x\in E`$,

```math
\liminf_{r\downarrow0}\frac{\mathcal H^1(E\cap B(x,r))}{2r}>\frac12.
```


**Must $`E`$ be countably $`1`$-rectifiable?** That means all but an $`\mathcal H^1`$-null part of $`E`$ lies in countably many Lipschitz images of intervals. The strict inequality matters: a purely unrectifiable example with lower density exactly $`1/2`$ is known.

## Application

The conjecture seeks a sharp density criterion for recognizing when a set is made up of curves. The best bound stated in the later De Lellis–Glaudo–Massaccesi–Vittone manuscript is $`7/10`$: replacing $`1/2`$ above by $`7/10`$ gives a theorem. The question is whether one can reach the sharp threshold $`1/2`$.

## References

1. C. De Lellis, [*Rectifiable Sets, Densities, and Tangent Measures*](https://www.math.ias.edu/delellis/sites/math.ias.edu.delellis/files/Delellis_note136_corrected.pdf), Zürich Lectures in Advanced Mathematics, EMS (2008), DOI 10.4171/044, Chapter 10, p.111, Conjecture 10.5 (author-hosted corrected PDF).
2. C. De Lellis, F. Glaudo, A. Massaccesi, and D. Vittone, [*Besicovitch's 1/2 Problem and Linear Programming*](https://www.math.ias.edu/delellis/sites/math.ias.edu.delellis/files/Besicovitch_paper-13.pdf), author-hosted manuscript, Introduction, Conjecture 1.1 and Theorem 1.3; see also [arXiv:2404.17536](https://arxiv.org/abs/2404.17536). The manuscript proves the $`7/10`$ threshold and explicitly retains the $`1/2`$ statement as a conjecture.
3. J. Capdevila, [*Besicovitch's example in higher dimensions: a purely unrectifiable set with large lower density*](https://arxiv.org/abs/2607.05206), arXiv:2607.05206 (2026), Introduction. The construction attains equality at $`1/2`$; it does not address the strict threshold above.

## Status review


**Known cases:** Density-threshold improvements are partial and do not reach the strict planar >1/2 criterion. Higher-dimensional examples attain equality at 1/2 and are not counterexamples to the strict planar formulation.

**Remaining target:** Resolve the complete question stated under Problem statement, with all its quantifiers and hypotheses. The restricted results described here do not cover that full target.

The [source, later-result, announcement, and semantic-duplicate review](../FURTHER_problems/_tracking/besicovitch-half-density-planar-status-2026-10-21.json) found no matching complete proof or AIM/FURTHER item. This is a bounded check, not a guarantee against unindexed work.


### Online recheck, 2026-10-30

Density-threshold improvements are partial and do not reach the strict planar >1/2 criterion. Higher-dimensional examples attain equality at 1/2 and are not counterexamples to the strict planar formulation.

Comparators and current-status sources: [status source 1](https://arxiv.org/abs/2404.17536); [status source 2](https://arxiv.org/abs/2607.05206). This bounded search found no matching complete proof, counterexample or complete-solution announcement; it is not a guarantee of continued openness or an independent audit of every cited proof.

## Collection provenance

Promoted from retained further problem **FURTHER-b30906ef8b2eafcc** on 2026-10-30, with its editorial scores unchanged. The [replacement register](../research/catalogue-backfill-2026-10-30/README.md) preserves the former AIM identity for this reused number and the historical research path. Earlier dated AIM-number comparisons above describe the collection at that earlier date.
