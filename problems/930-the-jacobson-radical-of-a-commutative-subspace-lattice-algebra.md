# 930. The Jacobson radical of a commutative subspace-lattice algebra

**Area:** Operators, matrices and computation
**Status:** 🟡 PARTIAL
**Last checked:** 2026-10-30

## Problem statement

Let $`H`$ be a complex separable Hilbert space and $`\mathcal L`$ a strongly closed lattice of pairwise commuting orthogonal projections on $`H`$, containing $`0`$ and $`I`$. Define
```math
\mathcal A=\mathrm{Alg}\mathcal L
 =\{T\in B(H):(I-P)TP=0\text{ for every }P\in\mathcal L\}.
```

Let $`X`$ consist of the surjective lattice homomorphisms $`\phi:\mathcal L\to\{0,1\}`$ preserving finite meets and joins. No continuity or preservation of arbitrary joins is required. For $`\phi\in X`$, put
```math
\mathcal I_\phi=
 \left\{T\in\mathcal A:
 \inf_{\substack{Q\le P,\ P,Q\in\mathcal L\\
                  \phi(P)=1,\ \phi(Q)=0}}
 \|(P-Q)T(P-Q)\|=0\right\}.
```

The norm is the operator norm. The interval projection $`P-Q`$ need not belong to $`\mathcal L`$.

Must
```math
\mathrm{rad}\mathcal A=\bigcap_{\phi\in X}\mathcal I_\phi
```

hold for every such lattice? Here $`\mathrm{rad}\mathcal A`$ is the Jacobson radical; equivalently, $`T\in\mathrm{rad}\mathcal A`$ exactly when $`ST`$ is quasinilpotent for every $`S\in\mathcal A`$.

The inclusion $`\bigcap_\phi\mathcal I_\phi\subseteq\mathrm{rad}\mathcal A`$ is known. The question asks for the reverse inclusion, without restricting the lattice's width, atomicity or complete distributivity.

## Application

This asks whether small compressions to intervals characterize the radical of a general algebra defined by invariant subspaces, extending the nest-algebra description to commuting lattices.

## References

- K. R. Davidson, *Nest Algebras*, Pitman Research Notes in Mathematics 191, Longman, 1988, Exercises 6.5–6.6*, printed p. 76 (native p. 84 in the author copy); Definitions 6.3–6.4 and the nest case in Theorem 6.7 provide context.
- A. Hopenwasser, [*The radical of a reflexive operator algebra*](https://msp.org/pjm/1976/65-2/pjm-v65-n2-p10-p.pdf), Pacific Journal of Mathematics 65(2), 1976, [DOI:10.2140/pjm.1976.65.375](https://doi.org/10.2140/pjm.1976.65.375), Section 2, Proposition 4 and the following conjecture.
- K. R. Davidson and J. L. Orr, *The Jacobson Radical of a CSL Algebra*, Transactions of the American Mathematical Society **344** (1994), 925–947, [DOI:10.1090/S0002-9947-1994-1250816-9](https://doi.org/10.1090/S0002-9947-1994-1250816-9). The [author abstract](https://johnorr.uk/research/abstracts.html) describes the completely distributive reduction and width-two results. Its volume “334” is a bibliographic typo.

## Status review


**Known cases:** The 2001 Yang-Gao article explicitly concerns width-two CSLs, not all CSLs. Weak-star closure and reflexive-hull equalities also do not establish the general norm-closed radical identity.

**Remaining target:** Resolve the full Problem statement with its stated quantifiers and hypotheses; the restricted advances discussed here do not settle that target.

### Online recheck, 2026-10-30

The 2001 Yang-Gao article explicitly concerns width-two CSLs, not all CSLs. Weak-star closure and reflexive-hull equalities also do not establish the general norm-closed radical identity.

The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

Checked 2026-10-30. The general equality is explicitly conjectured in Hopenwasser's primary paper. Known nest, finite-lattice and width-two cases do not settle arbitrary commuting lattices. Bounded current searches found no matching full resolution or announcement. The 1994 publisher body was inaccessible; its available author abstract supplies the stated partial scope.

Full nearby statements were compared against all statuses in AIM, the developing collection and the current public OpenAI announcement index; no equivalent target was located. This is a current literature assessment, not proof that no solution exists.

Review evidence: [owner model and current search](../FURTHER_problems/_tracking/D008-C346-NestAlgebras-ch6-visual-C-20261030/OWNER-EXACT-GENERAL-CSL-JACOBSON-RADICAL-INTERVAL-IDEAL-PRIMARY-PARTIAL-CURRENT-PROPOSAL.json), [independent model check](../FURTHER_problems/_tracking/D008-C346-NestAlgebras-ch6-visual-C-20261030/B-INDEPENDENT-CSL-RADICAL-HOM-INTERVAL-SEMINORM-DIRECTION-MODEL-PEER-PASS.json), and [coordinating review](../FURTHER_problems/_tracking/ROOT-FINAL-general-CSL-Jacobson-radical-interval-ideal-current-semantic-admission-20261030.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-dc1e46acbade0502**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
