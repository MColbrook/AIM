# 083. The bulk ground-state energy of the planar Lennard–Jones system

**Area:** Atomistic materials

**Status:** ✅ SOLVED

**Last checked:** 2026-11-03

## Problem statement

For distinct points $`x_1,\ldots,x_N\in\mathbb R^2`$, define

```math
E_N(x_1,\ldots,x_N)=\sum_{1\le i<j\le N}
\left(|x_i-x_j|^{-12}-2|x_i-x_j|^{-6}\right),\qquad
e_\infty=\liminf_{N\to\infty}\frac1N\inf E_N.
```

Let $`\Lambda_\triangle=\mathbb Z(1,0)+\mathbb Z(1/2,\sqrt3/2)`$ and

```math
e_\triangle=\inf_{a>0}\frac12\sum_{p\in\Lambda_\triangle\setminus\{0\}}
\left(|ap|^{-12}-2|ap|^{-6}\right).
```

Prove or disprove $`e_\infty=e_\triangle`$. The finite configurations are unrestricted; they are not assumed to be lattices. This asks for the energy form of bulk crystallization, not the stronger geometric convergence of every minimizing configuration.

## Application

The equality would derive the energetic preference for a triangular crystal directly from a widely used atomic pair potential.

## References

- [Xavier Blanc and Mathieu Lewin, *The crystallization conjecture: a review* (EMS Surveys in Mathematical Sciences, 2015), §2](https://doi.org/10.4171/EMSS/13).
- [Andrea Braides and Maria Stella Gelli, *Analytical treatment for the asymptotic analysis of microscopic impenetrability constraints for atomistic systems* (ESAIM: M2AN, 2017), introduction](https://arpi.unipi.it/retrieve/e0d6c929-b5b5-fcf8-e053-d805fe0aa794/m2an160137.pdf).

- Matthew J. Colbrook, *The bulk energy of the planar Lennard–Jones potential*, 31 October 2026, Theorem 1.1. [Zenodo preprint, version 1](https://doi.org/10.5281/zenodo.23835694); [manuscript PDF](https://zenodo.org/api/records/23835694/files/lennard_jones.pdf/content); [public certificate and mathematical scope](https://github.com/MColbrook/Bulk-energy-of-the-planar-Lennard-Jones-potential).

## Status review

**Resolution update (3 November 2026):** Solved on the basis of an **unverified announcement**. Colbrook’s Theorem 1.1 states the lower bound for every unrestricted finite configuration for the same planar 12–6 potential, and proves that finite triangular patches attain the matching bulk limit. This is the energy equality asked here; it does not assert geometric convergence of every minimizing configuration.

[Claimed solution](https://zenodo.org/api/records/23835694/files/lennard_jones.pdf/content) · [Dated statement comparison](../research/solution-status-audit-2026-11-03/lane-a/083.json). The manuscript checksum and theorem scope were checked. The external proof, its analytic dependencies and its numerical certificates have not been independently verified here; no Lean verification or human peer review is asserted.

### Earlier status record


**Literature check:** Open in cited literature; no later resolution located.

These sources separate unrestricted Lennard–Jones crystallization from results for modified potentials and restricted lattice classes. The status search found recent exact Lennard–Jones lattice optimization work; optimizing over lattices alone does not provide the lower bound over all N-point configurations above.

Status-search topics (2026-09-08): `Lennard-Jones crystallization open problem mathematics`; `crystallization Lennard-Jones 2025 open`; `On minima of differences of Epstein zeta functions and exact solutions to Lennard–Jones lattice energy`. This is a literature search, not a proof that no solution exists.
