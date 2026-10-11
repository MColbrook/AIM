.PHONY: paper

paper:
	TEXINPUTS="$(CURDIR)/paper//:" SOURCE_DATE_EPOCH=1791756000 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper/build paper/main.tex
