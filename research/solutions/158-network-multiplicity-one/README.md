# Multiplicity two in a tangent flow of an embedded planar network

Kaiwen Jin

The paper proposes a counterexample to AIM problem 158. It constructs a planar network with six triple junctions and four fixed boundary endpoints. At its first singular time, the tangent flow at the origin has two exterior rays of weight two.

- [Paper (PDF)](paper/article.pdf)
- [Comparison with the AIM statement and review disclosure](TARGET_COMPARISON.md)
- [Original AIM problem at the cited revision](https://github.com/MColbrook/AIM/blob/b2ec0fac559f532fc0ed04fce81deea0ce07c68b/problems/158-network-multiplicity-one.md)
- [File checksums](SHA256SUMS)

To compile the editable source, run the following command in the `paper` directory with a TeX distribution that provides AMS-LaTeX, Latin Modern, TikZ and latexmk. The TikZ source of Figure 1 is included in `main.tex`.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

This submission is a **Solution claimed**. Independent mathematical review is requested.
