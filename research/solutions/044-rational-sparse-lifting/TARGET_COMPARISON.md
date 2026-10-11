# Comparison with the pinned AIM 044 target

Target: [044. Quadratic-scale bit complexity for well-conditioned sparse systems](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/044-sparse-linear-solve-bit-complexity.md)
at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Manuscript: [A rational-input specialization of Kelner's sparse linear solver](paper/aim044.pdf),
Theorem 1 and Sections 2-3.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Every fixed positive integer c; n at least 1 | Theorem 1 states these quantifiers; Section 3 checks K at least 1, including n=1 | Full |
| Nonsingular rational n-by-n A given by its sparse nonzero list; m=nnz(A) | Theorem 1 uses this input; Section 3 observes m at least n and rounding preserves sparsity | Full; no symmetry or definiteness requirement |
| Condition number kappa_2(A) at most n^c | Theorem 1 uses the same induced Euclidean condition number; Section 3 puts K=n^c and propagates it in the forward error | Full promised-input class |
| Nonzero rational b | Theorem 1; Eq. (4) gives the nonzero input scale and x=A^-1 b not zero | Full |
| All input numerators and denominators have at most c ceil(log_2(2n)) bits | Theorem 1 fixes B exactly; Eqs. (5)-(6) round each rational individually with short integer operands | Full; no common input denominator |
| Rational output vector | Section 2 reconstructs exact reduced rational coordinates of the working system; Eq. (7) returns their radix scaling | Full |
| Relative Euclidean solution error at most n^-c | Theorem 1/Eq. (1) and the proof's Eq. (8) give the stronger n^-c/10 bound | Full |
| Success probability at least 0.99 | All steps in Theorem 1 are deterministic | Probability one |
| Tilde O(nm) bit operations, including arithmetic and input/output | Lemma 1 bounds short sparse lifting and one digit assembly; Lemma 2 gives fast recovery and output cost; Section 3 absorbs n^2 using m at least n | Full; constants depend on fixed c and suppressed factors are logarithmic in 2n |

The original question allows a randomized algorithm; a deterministic one is
an admissible special case. Nonsingularity and conditioning remain input
promises and are not separately certified by the software. The proof is
all-input; the 14 tests and 16 reproduction cases are finite implementation
evidence and do not restrict the theorem's scope.

Kelner's identity-modulus mechanism and Theorem 2.3 on fast bounded rational
reconstruction are the imported results. The manuscript states the exact
reconstruction hypotheses (including composite modulus, coprime denominator
and strict height-product bound), and supplies the rational rounding, short
residual and direct forward-error specialization. The contribution is an
explicit resolution report based on that primary source, not a claim to have
invented the central solver. Independent mathematical review remains pending.
