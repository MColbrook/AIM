# AIM 651: target comparison

Target revision: `c4036871b0bf15cbc83e79c780b7191bcbb2cfed`. See [statement.md](statement.md).

The target fixes the prescribed boundary subdivision, constrained Delaunay triangulation, vector iteration and initial vector for an arbitrary simple polygon.

The theorem proves 0<g'(s)<1 for every scalar parameter and every simple quadrilateral, including concave and straight-angle cases. Hence the four-prevertex iteration converges from every finite initial parameter. This covers the catalogue algorithm when subdivision leaves four vertices; explicit nonempty families and a concave example are supplied. An originally four-sided polygon with more subdivision vertices is outside this result. General polygons and the higher-dimensional Jacobian are not covered. The entry is Partially resolved.
