# 671. Are all isometries of the Mabuchi completion induced by smooth Kähler-potential isometries?

**Area:** Complex geometry and pluripotential theory
**Status:** 🔵 OPEN
**Last checked:** 2026-10-30

## Problem statement

Let $`(X,\omega)`$ be a compact connected Kähler manifold of positive complex dimension $`n`$. Put
```math
\mathcal H_\omega=\{u\in C^\infty(X;\mathbb R):\ \omega_u:=\omega+i\partial\bar\partial u>0\},
\qquad
V=\int_X\omega^n.
```

The Mabuchi norm of a tangent vector $`\xi\in T_u\mathcal H_\omega=C^\infty(X;\mathbb R)`$ is
```math
\|\xi\|_u^2=\frac1V\int_X \xi^2\,\omega_u^n.
```

Define the path-length distance
```math
d_2(u,v)=\inf_\gamma\int_0^1\|\dot\gamma(t)\|_{\gamma(t)}\,dt,
```

where the infimum runs over smooth paths $`\gamma:[0,1]\to\mathcal H_\omega`$ from $`u`$ to $`v`$. Let $`(\mathcal E_\omega^2,d_2)`$ denote its metric completion.

Suppose $`F:\mathcal E_\omega^2\to\mathcal E_\omega^2`$ is a surjective isometry:
```math
d_2(F(u),F(v))=d_2(u,v)\qquad(u,v\in\mathcal E_\omega^2).
```

Must $`F(\mathcal H_\omega)=\mathcal H_\omega`$, with $`G=F|_{\mathcal H_\omega}`$ a global differentiable $`L^2`$ isometry in the following sense: $`G`$ is a bijection, it is $`C^1`$ in the Fréchet topology of smooth functions, and
```math
\|D_uG(\xi)\|_{G(u)}=\|\xi\|_u
\qquad(u\in\mathcal H_\omega,\ \xi\in C^\infty(X;\mathbb R))?
```

Here $`C^1`$ includes continuity of $`G`$ and of $`(u,\xi)\mapsto D_uG(\xi)`$ in the indicated Fréchet topologies.

Equivalently, is every surjective isometry of the completion the unique continuous extension of a global differentiable $`L^2`$ isometry of $`\mathcal H_\omega`$? No preservation of smooth potentials or differentiability is assumed for $`F`$. The spaces contain potentials differing by additive constants; they have not been quotiented by constants.

This is the completion-isometry question stated by Darvas immediately after Theorem 1.4 in [1, p. 4094]. The extension formulation makes the desired automatic regularity explicit.

## Application

Mabuchi geometry places Kähler metrics in an infinite-dimensional metric space used to study canonical metrics, energy functionals and stability. Classifying the isometries of its completion asks whether passage to finite-energy, possibly singular potentials creates additional global symmetries invisible in the smooth geometry. This relates the metric structure of the completion to the underlying complex manifold [1, introduction and §2].

## Known results and scope

Darvas's Theorem 1.1 classifies global differentiable $`L^2`$ isometries of the smooth space. The classification uses biholomorphic and anti-biholomorphic pullbacks, the freedom in additive constants, and composition with the Monge–Ampère energy flip. It does not assume every metric isometry of the completion already preserves the smooth space. Each classified smooth isometry does have a unique continuous extension, since $`\mathcal H_\omega`$ is dense in its completion.

The same paper proves that the completion has no local metric symmetries reversing every geodesic at a smooth point (Theorem 1.4). That nonexistence statement leaves the full global isometry group unclassified.

Lempert's local differential classification [2, Theorem 1.1] concerns $`C^1`$ isometries on open subsets of smooth-potential spaces. It does not supply automatic differentiability for arbitrary isometries of the completions; the distinction is explicit in the introduction.

## References

1. T. Darvas, [*The isometries of the space of Kähler metrics*](https://doi.org/10.4171/JEMS/1104), *Journal of the European Mathematical Society* **23** (2021), no. 12, 4091–4108, published 16 June 2021. [Published PDF](https://ems.press/content/serial-article-files/32607), pp. 4091–4094 and §2: definitions, Theorem 1.1, and the explicit completion question. The [arXiv listing](https://arxiv.org/abs/1902.06124) has version 1 dated 16 February 2019.
2. L. Lempert, [*Isometries in spaces of Kähler potentials*](https://doi.org/10.4064/ap180523-6-7), *Annales Polonici Mathematici* **123** (2019), 423–458. [Revised preprint v3, 14 August 2019](https://arxiv.org/pdf/1702.05937v3), pp. 1–3: local $`C^1`$ classification and the separate question about metric completions.
3. T. Darvas and N. McCleerey, [*Lines in the space of Kähler metrics*](https://doi.org/10.1007/s00208-026-03573-8), *Mathematische Annalen* **396** (2026), article 36, published 15 September 2026. Theorems 1.1, 1.2 and 1.6 concern geodesic lines and test lines, rather than classification of global surjective isometries.

## Status review


### Online recheck, 2026-10-30

The original completion-isometry question was reopened in the primary text. Darvas classifies differentiable smooth-space isometries, not arbitrary surjective completion isometries. The current author list includes 2026 entropy and geodesic-line papers without a matching classification announcement. Indexed public-venue and later-result searches found no complete resolution.

Additional comparison sources: [comparison source 1](https://arxiv.org/html/1902.06124); [comparison source 2](https://math.umd.edu/~tdarvas/research.html); [comparison source 3](https://doi.org/10.4171/JEMS/1104). The primary-source formulation and earlier dated status review are retained below. Fresh query results and hypothesis comparisons are recorded in the [integration register](../research/further-integration-2026-10-30/README.md). This is a bounded literature and announcement search, not a guarantee of continued openness or certification of every cited proof.

The eligible 2021 published body explicitly states the question. Current primary records, the author's research list, selected statements in the 2026 geodesic-line paper, exact-title searches, completion-isometry searches, and possible proofs or counterexamples were checked. No matching complete resolution or announcement was located.

The developing list's Kähler-potential questions concern Monge–Ampère masses, singularities, envelopes, extension, or positivity. Nearby metric-isometry announcements concern Banach unit spheres, finite-dimensional immersions, or group actions. They have different domains and conclusions. The comparison included all-status AIM records, current findings and the changed statements in the current public AIM snapshot. The inspected OpenAI catalogue descriptions and indexed Prove2Me search yielded no matching completion-isometry target.

These are bounded literature and duplicate checks. They do not certify every cited proof or establish that an unlocated solution cannot exist. The accompanying audit records exact source passages, version checks, semantic comparisons, and access limits.

Independent admission evidence: [source and scope](../FURTHER_problems/_tracking/mabuchi-completion-independent-peer-2026-10-23.json), [semantic duplicates](../FURTHER_problems/_tracking/mabuchi-completion-coordinator-duplicate-review-2026-10-23.json), [current searches](../FURTHER_problems/_tracking/mabuchi-completion-current-resolution-search-2026-10-23.json), [announcements](../FURTHER_problems/_tracking/mabuchi-completion-announcements-and-catalogues-2026-10-23.json) and [source versions and references](../FURTHER_problems/_tracking/mabuchi-completion-source-versions-and-references-2026-10-23.json).

## Collection provenance

Promoted on 2026-10-30 from retained further problem **FURTHER-0748c27bcb1ed1ac**, with its scores unchanged. The [integration register](../research/further-integration-2026-10-30/README.md) preserves its original path, source bytes, review evidence and current identity. Earlier AIM-number comparisons describe the collection at their original review dates.
