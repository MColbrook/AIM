# Pre-submission mathematical check: AIM 570

Checked on 2026-10-03 by OpenAI Codex (AI), against the repository statement pinned in [SUBMISSION.json](SUBMISSION.json). This is an AI-assisted pre-submission check, not a documented independent human audit, acceptance decision, or proof-assistant verification. No substantive proof gap was found in this check.

The counterexample matches the complete repository question, which quantifies over arbitrary real Banach spaces. It uses the fixed norm-one inclusion from l1([0,1]) to l2([0,1]). Both spaces are nonseparable; no conclusion is claimed for a restriction to separable spaces.

For threshold 1/(K+1), soft thresholding is 1-Lipschitz in l1 and leaves at most K nonzero coordinates on the closed unit ball. Its squared l2 error is at most 1/(K+1), including equality-threshold cases. Each of the first 2K moments is a continuous functional composed with this threshold map. The difference of two K-sparse vectors has at most 2K distinct support points, so the Vandermonde argument gives uniqueness even for signed coefficients. The arbitrary decoder is defined on all of R^(2K), returning zero for moment vectors with no sparse representative.

For any continuous decoder, the image of the separable space R^n is separable. A countable dense subset of that image has countable union of supports; its closure is contained in the closed coordinate subspace l2(J). A unit vector at any coordinate outside J has distance at least one from every decoded vector, independently of the encoder. The zero decoder proves the matching upper bound. Hence delta_n=1 for every finite n, while e_(2K) <= 1/sqrt(K+1). Choosing K+1>C^2 refutes every finite universal C; K=4 refutes C=2 at n=8.

The root audit checked all continuity domains, the definition of the decoder outside the encoder image, norm topology and the nonadaptive requirement. The manuscript now states both error quantities explicitly and cites the originating survey as well as the exact preprint lemma. The argument is analytic and contains no numerical evidence or computer algebra dependency.

The checked claim is submitted for pull-request review. The catalogue page and status are unchanged. The source snapshot, original notes and reference audit are included so reviewers can assess the argument and its scope.
