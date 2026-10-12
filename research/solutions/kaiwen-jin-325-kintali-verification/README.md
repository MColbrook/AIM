# Kintali's counterexample to fixed-order prefix balancing

This is an attributed verification and literature-update package for
[AIM problem 325 at revision c9929805](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/325-strong-komlos-prefix-discrepancy.md).

The construction and amplification proof are due to **Shiva Kintali**,
[*On the Fixed-Order Strong Komlós Conjecture*, ECCC TR26-242](https://eccc.weizmann.ac.il/report/2026/242/),
Sections 2--3.1, Lemma 2.2 and Theorem 3.1, pages 2--5.
The PDF title page says September 15, 2026; the ECCC report record says
September 26; the publication field gives October 9. These are distinct
source dates. No new construction or mathematical priority is claimed.

The [four-page exposition](paper/komlos_verification.pdf), by Kaiwen Jin,
includes a complete finite-induction proof. Its fixed ordered unit-column
family has dimension `d_k=2^(2^k-1)` and, for every offline signing, a
nonempty prefix of maximum norm at least `2^(k/2-1)`. This bound tends to
infinity and gives the negative answer to the full constant-bound question.
The [target comparison](TARGET_COMPARISON.md) explains every relevant clause.

OpenAI Codex assisted with retrieval, reconstruction, checking and exposition.
The checking was AI-assisted. No independent human review, peer-reviewed
acceptance or proof-assistant verification is claimed. Independent assessment
of the source and this exposition is requested. Catalogue status remains
for maintainer review.

## Reproduction

The proof is analytic and uses no numerical experiment or computed certificate.
Its [editable source](paper/komlos_verification.tex) contains its bibliography
and requires ordinary LaTeX packages `geometry`, `amsmath`, `amssymb`,
`amsthm`, and `hyperref`.

From this package directory, compile with TeX Live and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/komlos_verification.tex
```

The distributed PDF compiled successfully. Every page was read and visually
checked; its equation and theorem references were checked against the source.
These checks verify this exposition's preparation, not independent acceptance
of the mathematical claim.

`PUBLIC_MANIFEST.json` records the four content files and their hashes.
`SHA256SUMS` additionally checks that manifest; the checksum file does not
hash itself. Run `shasum -a 256 -c SHA256SUMS` to verify the package bytes.
