# Correspondence with AIM 325

Target: [A constant bound for fixed-order prefix discrepancy](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/325-strong-komlos-prefix-discrepancy.md),
revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The requested assertion is an absolute upper bound for one signing of every
ordered Euclidean-unit family. The submitted exposition gives its full
negation through **Kintali's existing counterfamily**, not a new construction.
The direct primary proof is [ECCC TR26-242](https://eccc.weizmann.ac.il/report/2026/242/),
Lemma 2.2 and Theorem 3.1, Sections 2--3.1, pages 2--5.

| Original clause | Result and location in the exposition | Coverage |
| --- | --- | --- |
| One C independent of dimension, length and input | Theorem 1 and the last paragraph of Section 3 give, for each C>0, a level k with lower bound greater than C. | Full negation |
| Positive finite d,T | Section 3 gives d_k=2^(2^k-1) and the finite positive length recurrence n_0=1, n_(k+1)=(1+n_k d_k^(d_k))(n_k+1)^(d_k)-1. | Exact |
| Real input vectors with Euclidean norm at most one | Section 2 counts exactly 2^k nonzero entries in each integer column at level k; Section 3 divides by sqrt(2^k), giving norm exactly one. | Exact |
| Fixed given order | Equations (3)--(5) define every original, detector and nested word before signs are fixed. Witness selection only finds an interval of this word. | Exact |
| Same arbitrary offline signs for all coordinates and prefixes | Lemma 2 fixes arbitrary independent coefficients on all physical occurrences, with magnitude at least one; this includes every full offline signing. | Exact |
| Prefixes 1 through T, not separate signings or only the terminal sum | Theorem 1 uses all nonempty prefixes. Section 3 removes prefix zero because its norm is zero and the lower bound is positive. | Exact |
| Maximum over physical coordinates | Lemma 2 combines a frozen mean and a difference in the same pair at the same global time, using max(abs(h+z),abs(h-z))=abs(h)+abs(z). | Exact |
| All items retained, no coordinate-size or input-distribution restriction | Every column occurrence remains in the fixed word. The final family uses real unit vectors and ordinary signs, with no deletion, reordering, noise or online constraint. | Exact |

The conclusion is qualitative: the number of columns grows rapidly and no
efficient construction or optimal dimension/length dependence is claimed.
The note reproduces the complete mathematical argument and credits Kintali
throughout. Its AI-assisted checking supplies no independent human or formal
certification; maintainer assessment and catalogue disposition are pending.
