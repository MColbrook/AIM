# AIM 446: the sharp Beurling–Ahlfors estimate

This package is an attributed literature update for [AIM 446](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/446-beurling-ahlfors-sharp-norm.md), frozen at repository revision c9929805cece044705abaaebe1cebddac1ba11a6.

Agazzi and collaborators establish the sharp complex operator norm in [Sharp Higher Integrability Theory, Part I: The Lp-norm of the Beurling–Ahlfors transform, arXiv:2609.28311v2](https://arxiv.org/abs/2609.28311v2). Their Theorem 1 gives unrestricted planar quasiconvexity, and Corollary 2, equation (4), states the norm equality for every real $1<p<\infty$. The [complete versioned primary proof](https://arxiv.org/html/2609.28311v2) is publicly accessible. The first version was submitted on September 23, 2026, and version 2 on October 8, 2026; the frozen AIM page was last checked on September 22, 2026.

[A note on the sharp Beurling–Ahlfors bound](paper/beurling_ahlfors_update.pdf), by Kaiwen Jin, gives the passage from that quasiconvexity theorem to the precise disk principal-value operator in the AIM statement. Theorem 1 of the note proves

$$
\|\mathcal Bf\|_{L^p(\mathbb C)}
\le \bigl(\max\{p,p/(p-1)\}-1\bigr)\|f\|_{L^p(\mathbb C)}
$$

for every complex $f\in C_c^\infty(\mathbb C;\mathbb C)$ and every real $1<p<\infty$, using area measure and the kernel $-1/(\pi z^2)$. Its proof includes the absolutely convergent power integral, a scalar majorant, the Cauchy-potential cutoff, the disk normalization, the $p=2$ multiplier identity, and complex duality below 2.

The sharp result and its quasiconvexity proof belong to Agazzi and collaborators. This note explains their implication for the catalogue statement. The submission is a literature update based on a preprint and requests independent mathematical review.

## Files and reproduction

- [Manuscript PDF](paper/beurling_ahlfors_update.pdf) and [editable TeX](paper/beurling_ahlfors_update.tex).
- [Target comparison](TARGET_COMPARISON.md), with equation and section locators.
- [Public manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

From the package directory, a TeX installation with latexmk can rebuild the manuscript:

    mkdir -p build
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/beurling_ahlfors_update.tex

The source uses standard TeX packages and has no additional manuscript assets. The analytic argument uses the cited public theorem and the proof in the manuscript. There are no numerical experiments or computer-assisted certificates in this result.

Check the supplied file hashes with:

    shasum -a 256 -c SHA256SUMS

SHA256SUMS covers the manuscript, public prose, and manifest. The manifest describes the four payload files; neither checksum document includes a self-hash.

## AI use and review

Codex assisted primary-source comparison, the displayed transfer calculations, drafting, and document checks. The manuscript contains an AI-use disclosure. A separate detailed AI review report is not submitted. Independent mathematical review of the note and its cited primary result is requested.
