# Source map: stochastic dynamics, kinetics and optimization (276–300)

Reviewed on **13 September 2026**. The entries concern relaxation, reaction networks, routing, resource allocation, sequence comparison, random media, and spatial population models. The mathematical statements and literature checks are on the linked pages. This map records selected reading and locators, not a claim to have read every cited book or proof in full.

## Books, extended surveys and manuscripts

| Source inspected | Locator and role | Entries |
| --- | --- | --- |
| Levin and Peres, with Wilmer, [*Markov Chains and Mixing Times*, second edition (2017)](https://pages.uoregon.edu/dlevin/MARKOV/mcmt2e.pdf) | Chapter 26, Questions 2, 3(i), 5 and 8; original open questions compared with later scan and cutoff papers | 276–278, 281 |
| Steele, [*Probability and Problems in Euclidean Combinatorial Optimization*, in *Probability and Algorithms* (1992)](https://www.nationalacademies.org/read/2026/chapter/9) | §8.8; geometric optimization fluctuations, supplemented by Aldous–Durrett’s explicit 2002 optimal-tour CLT question | 284 |
| Járai, [*Sandpile models*, Probability Surveys 15 (2018)](https://doi.org/10.1214/14-PS228) | §3.3.2, Conjecture 3.8; separate avalanche observables, with only total topplings selected | 292 |
| Durrett, [*Interacting Particle Systems: Ideas, Techniques, Applications*, current author manuscript](https://sites.math.duke.edu/~rtd/PASTA/PASTAcurrent.pdf) | §3.2, Open Problem 3.2.3, printed p.89; discrete spatial coexistence example | 293 |
| Bernardo et al., [*Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024)](https://liu.diva-portal.org/smash/get/diva2%3A1809739/FULLTEXT01.pdf) | Bounded-confidence clustering; followed by Dey–Etesami–Gopalan’s explicit strong 2R conjecture | 295 |
| Berezansky, Braverman and Idels, [*Nicholson’s blowflies differential equations revisited: Main results and open problems* (2010)](https://doi.org/10.1016/j.apm.2009.08.027) | Global stability questions; the autonomous single-delay equation is retained | 296 |
| Liu, [*Topics on the Longest Common Subsequences: Simulations, Computations, and Variance*, dissertation (2018)](https://repository.gatech.edu/bitstreams/0312a292-44ee-435a-8440-7ce2883e6704/download) | Chapter 1 and §3.1; competing predictions and biased versus fair strings | 297 |

The Durrett text is an evolving manuscript. Entry 285 explicitly normalizes the neighborhood fraction by neighborhood population, resolving an omitted-hat denominator in the manuscript using its stated frequency interpretation. Liu’s thesis dates to 2018 even though search results gave it a recent crawl date.

## Specific papers and exact retained targets

| Entry | Main additional source or status comparison |
| --- | --- |
| [267](../problems/266-ising-gap-monotonicity.md) | Nacu’s cycle theorem; arbitrary graphs remain the question. |
| [268](../problems/267-ising-systematic-scan.md) | Gaitonde–Mossel, arXiv:2410.11136, Theorems 1.1–1.2; general polynomial comparisons do not settle the ferromagnetic constant comparison. |
| [269](../problems/268-transitive-expander-cutoff.md) | Salez’s cutoff work, including arXiv:2508.21055, §2.2; uniform expansion and transitivity are the retained assumptions. |
| [270](../problems/269-coloring-glauber-threshold.md) | Frieze–Vigoda’s coloring survey; Chen–Liu, arXiv:2608.25491, high-degree girth restrictions. |
| [271](../problems/270-exclusion-independent-mixing.md) | Hermon–Pymar, arXiv:1808.10846, Introduction, Oliveira’s conjecture; exclusion and independent-particle total-variation times. |
| [272](../problems/271-transitive-mixing-diameter.md) | Olesker-Taylor–Zanetti (2024), Introduction and geometric bounds; optimizing transition weights changes the problem. |
| [273](../problems/272-reaction-network-positive-recurrence.md) | Anderson–Kim (2018), §6; Xu, arXiv:2601.00176, first-order results. |
| [274](../problems/273-reaction-network-persistence.md) | Gopalkrishnan–Miller–Shiu (2014), Conjecture 4.4; Craciun (2019), §2.2; a 2026 Journal of Mathematical Biology paper, §4.2, still records persistence. |
| [275](../problems/274-euclidean-tsp-clt.md) | Aldous–Durrett’s 2002 probability workshop report, §1.2; spanning-tree CLTs are separate. |
| [276](../problems/275-metric-tsp-four-thirds.md) | Cook–Hougardy–Petrich, arXiv:2603.12995; Jin–Klein–Williamson, arXiv:2607.01536. Bounded-size computations and restricted metrics are not the universal four-thirds inequality. |
| [277](../problems/276-planar-steiner-ratio.md) | Friedel–Widmayer (1989), five points; Ke et al., arXiv:2601.22365v3, 2 September 2026, improved lower bound below the conjectured ratio. |
| [278](../problems/277-binary-lcs-constant.md) | Dixon, arXiv:1307.2796; Li–Ren–Wen, arXiv:2504.10425 (published 2026), multiple-string bounds. |
| [279](../problems/278-unrelated-machine-makespan.md) | Lenstra–Shmoys–Tardos (1990); Bamas et al., arXiv:2307.08453, arbitrary unrelated processing times. |
| [280](../problems/279-general-santa-claus.md) | Bamas et al., arXiv:2307.08453; *Mathematical programming approaches for social welfare maximization*, 4OR (2026), §5.1.3, Open problem 5. |
| [281](../problems/280-planar-lorentz-mirrors.md) | Elboim–Gloria–Hernández, arXiv:2505.01341, planar localization conjecture; Lefevere–Tasaki, arXiv:2602.07988, different hierarchical geometry. |
| [282](../problems/281-planar-sandpile-size-exponent.md) | Bhupatiraju–Hanson–Járai, arXiv:1602.06475; Hutchcroft, arXiv:1804.04120, dimensions at least five. |
| [283](../cut_problems/problems/282-spatial-hawk-dove-coexistence.md) | Durrett–Levin (1994), original spatial model and simulations; the current book explicitly asks for coexistence. |
| [284](../cut_problems/problems/283-axelrod-multifeature-clustering.md) | Lanchier–Schweinsberg, arXiv:1107.4413, Introduction; Lanchier–Scarlatos, arXiv:1301.0130. The two-state clustering theorem is excluded from the target. |
| [285](../cut_problems/problems/284-hegselmann-krause-cluster-lattice.md) | Dey–Etesami–Gopalan, arXiv:2508.08299, §3.3, Conjecture 2. Only the Poisson cluster-location case is selected. |
| [286](../problems/285-nicholson-local-global-stability.md) | Röst–Wu (2007), Introduction and Nicholson example; strict local stability avoids neutral characteristic-root endpoints. |
| [287](../problems/286-binary-lcs-linear-variance.md) | Lember–Matzinger (2009), Introduction and biased binary theorem; the fair binary case is distinct from determining the mean constant in 288. |
| [288](../problems/287-gaussian-polymer-tracy-widom.md) | Krishnan–Quastel, arXiv:1610.06975; Agarwal, arXiv:2509.21453, intermediate disorder; arXiv:2603.14477 is numerical. |
| [289](../problems/288-critical-four-state-potts-mixing.md) | Gheissari–Lubetzky, arXiv:1607.02182, Introduction; polynomial versus quasi-polynomial critical bounds. |
| [290](../problems/289-majority-ising-fixation.md) | Morris, arXiv:0809.0353; BIRS workshop 24w5300 report (2024), critical initial-density question. |

Per-page references contain the full links. The search distinguished theorem hypotheses, numerical evidence, proof claims, and different models. The resulting status remains a dated literature assessment, not a certification that no proof exists.
