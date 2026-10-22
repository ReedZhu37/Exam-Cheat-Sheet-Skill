"""Reproduce the recorded dev-driven v1 -> v2 clarity revision (no final input)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'examples/mit-6041/concepts-v1.json'
data = json.loads(path.read_text(encoding='utf-8'))
data['title'] = data['title'].replace('(v1)', '(v2; study reference)')
data['scope_notes'] = [
    '23/23 means the authored review-topic inventory, not independently proven coverage of every chapter or exercise in the official scope.',
    'Textbook chapters 1-2, recitations 1-7, problem sets 1-4 and tutorials 1-3 were not ingested; their additional topics remain unaudited.',
    'All downloaded lecture pages were extracted, but lecture 1-3 content was not semantically reviewed. Exact visual-review coverage is in ../source-review.md.',
    'Poisson and total variance were not supported by the reviewed sources and were omitted; this is not a claim that they are outside the complete official scope.',
]
by_id = {c['concept_id']: c for c in data['concepts']}
by_id['geometric']['procedure'][0] = (
    'Name the stopping event first, even if the story calls it a failure. '
    'Check endpoints: p=0 has no finite stopping time; p=1 is deterministic. '
    'Then distinguish total trials, failures, and remaining trials.'
)
by_id['transformed-variables']['recognition'] = 'Sum, minimum, square, or joint measurements defined from the same inputs.'
by_id['transformed-variables']['procedure'][0] = (
    'Write the requested output event; solve its inverse constraints. Translate '
    'the original integer support before evaluating probabilities. For joint '
    'outputs apply the same event-preimage rule to both equations; sum every '
    'compatible input pair, or evaluate the unique pair when the map is one-to-one.'
)
by_id['rv-independence']['procedure'][0] = (
    'Find marginals, then test factorization. A quick disproof is an impossible '
    'joint pair whose two marginal probabilities are positive. Check degenerate '
    'parameter endpoints separately; a constant variable is independent of any variable.'
)
for source in data['sources']:
    source['extraction_status'] = 'needs_review'
(ROOT / 'examples/mit-6041/concepts-v2.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print('Wrote v2; unchanged formulas, source pool, scope, and exam-frequency evidence.')
