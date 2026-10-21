# Preregistered demonstration protocol

Registered before examination of the final questions or official solutions.

## Splits and scope

MIT OCW 6.041SC Fall 2013, Quiz 1: textbook chapters 1–2, lectures/recitations
1–7, problem sets 1–4, tutorials 1–3. This example uses publicly licensed review
and lecture slides, not the separately copyrighted textbook.

- Train: Quiz 1 review, lectures 1–7, Spring 2009 quiz and official solutions.
- Dev: Fall 2009 quiz and solutions. One initial independent assisted solution,
  feedback-driven sheet revision; any repeats remain development results.
- Final: Fall 2010 quiz. Acquire questions only after freeze; acquire solutions
  separately for grading after both answers have been written.

## Fixed design

One run each of A (exam with its own formula page) and B (identical exam plus
frozen sheet). One independent C coverage audit, not a performance comparator.
A/B use `openai/gpt-6-astra#high`, no tool permissions, new sessions,
identical reasoning/knowledge rules and output request (at most 8,000 words).
No best-of selection. Record actual model/variant from session events rather
than trusting a default. Both groups may use prior mathematical knowledge.

The harness builds the exact prompt from page text plus page-image attachments,
and a permission-denied agent cannot read files, shell, network, MCP or other
sessions. The controller can supply attachments but does not supply solutions.
Record prompts, input/output hashes, configuration and raw events. This is
tool-level context isolation, not an operating-system air gap. Public exams
may have been present in model pretraining.

## Strict grading (fixed before answers)

Final has 105 points and 11 distinct subparts: P1(a–h) =
10,10,10,10,5,10,10,10; P2(a–c) = 10,10,10. Repeated answer pages count once.
Award all subpart points only if every requested result and required proof is
correct; otherwise zero. Accept mathematically equivalent expressions and
unsimplified forms permitted by the question. No partial-credit metric.
Grader receives official solutions and the anonymized response, never another
group's result. Log rationale, official page/part anchor, error category and
sheet references. Review discrepancies without erasing initial judgments.

Report A/B points /105, correct subparts /11, B−A, and C coverage separately.
C may use only named sheet rules plus arithmetic/algebra; it must say
NOT COVERED when a substantive step needs an absent rule. The C denominator
is the 11 subparts; full/partial/absent classifications include step citations.
High scores in both groups indicate a ceiling effect, not demonstrated gain.
These single-model, single-run results establish no generalization guarantee.

## Freeze and revisions

v1/v2 and change rationale are retained. Freeze all v2 products, source concept
records, input manifest, protocol, and code revision before fetching final.
Do not revise the frozen artifact using final feedback. Fixes to evaluator code
after freezing must be separately recorded and must not change sheet hashes.

## Licensing

Course-derived concepts, sheets, exam responses and grading commentary are
CC BY-NC-SA 4.0; attribute MIT OpenCourseWare / John Tsitsiklis, 6.041SC Fall
2013. Code and original generic tooling are MIT. MIT does not endorse this work.
