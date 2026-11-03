# 213. A spectral gap for almost every pair of quantum gates

**Area:** Spectral theory / quantum dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-11-03

## Problem statement

Let $`G=\mathrm{SU}(2)=\{U\in\mathbb C^{2\times2}:U^*U=I,\det U=1\}`$, with Haar probability measure $`\mu`$. For $`a,b\in G`$, define the lazy averaging operator on $`L^2(G,\mu)`$ by

```math
P_{a,b}f(g)=\frac12 f(g)+\frac18\bigl(f(ag)+f(a^{-1}g)+f(bg)+f(b^{-1}g)\bigr).
```

Is it true that for $`(\mu\otimes\mu)`$-almost every pair $`(a,b)`$ there exists $`\delta(a,b)>0`$ such that

```math
\|P_{a,b}f\|_2\le(1-\delta(a,b))\|f\|_2
\quad\text{whenever }f\in L^2(G,\mu),\quad\int_G f\,d\mu=0?
```

The gap may depend on the chosen pair; no positive bound uniform over all pairs is requested.

## Application

Two single-qubit gates and their inverses generate a random quantum circuit. The conjecture asks whether almost every fixed gate pair makes square-integrable deviations from the uniform distribution decay exponentially with circuit length.

## References

1. Alex Gamburd, Dmitry Jakobson, and Peter Sarnak, [*Spectra of elements in the group ring of SU(2)*](https://ems.press/journals/jems/articles/99), *Journal of the European Mathematical Society* 1 (1999), 51–85. Original spectral-gap conjecture; examples with a gap and spectral statistics.
2. Oleg Pikhurko and Kohki Sakamoto, [*A zero-one law for the spectral gap property of pairs in SU(2)*](https://arxiv.org/html/2603.17869v2), preprint, version 2, 19 October 2026, §1, Theorem 1.1, and Definition 2.1. Explicit current formulation and a zero–one law for pairs.

## Status review

**Literature check:** Open in cited literature; no later resolution located.

The October 2026 revision proves that the set of pairs with a gap has either zero or full Haar measure. It does not determine which alternative holds. Results for algebraic generators establish many examples but do not give positive Haar measure. The lazy averaging formulation above is equivalent to the spectral-gap property defined in that paper.

**Search audit:** Searched “spectral gap SU(2) almost every pair proof 2026”, “Pikhurko Sakamoto spectral gap conjecture”, and subsequent work citing the zero–one law. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
