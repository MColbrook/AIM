# Authoritative local publication — 3 November 2026

The local catalogue, problem identities, status decisions and editorial cuts are authoritative. The fourteen upstream commits through `8729eab98bafe409b66c5e39253bf56569a62327` had already been reviewed and incorporated by the earlier integration; publication retains that history without replacing the local tree with upstream content.

The public checkout omits `FURTHER_problems/`, `PROBLEM_SCORING/` and `cut_problems/`. All three stay intact locally. Downloaded primary-source caches also remain local; published scope reviews retain source URLs and locators. The public catalogue preserves the historical selection registry and current ID replacements, and validates it without unpublished archives. When a local archive is present, its records remain subject to the strict local checks.

Publishing compatibility changes preserve mathematical problem statements and manuscripts. Four documentation fixes remove links to missing draft receipts and a superseded manuscript; details are in [manifest.json](manifest.json).

Validation: local catalogue and frozen-selection checks pass; 36 focused tests pass. The public-checkout baseline now passes its full write/check and problem-preservation test, addressing the omitted-local-archive fixture issue recorded by the earlier status audit.
