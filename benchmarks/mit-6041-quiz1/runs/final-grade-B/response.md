{
  "items": [
    {
      "item_id": "P1(a)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correct shifted-binomial PMF, including support and zero elsewhere; all tabulated probabilities agree. Expectation 59/3 and variance 10/9 are correct and justified.",
      "official_anchor": "Official solutions PDF page 1, Problem 1.1",
      "sheet_references": ["Exam PDF page 1: binomial PMF, expectation, and variance"],
      "error_type": "none"
    },
    {
      "item_id": "P1(b)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly identifies the conditioning event as N ≤ 1 and computes the conditional expectation as 80/(32+80) = 5/7.",
      "official_anchor": "Official solutions PDF pages 1–2, Problem 1.2",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P1(c)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly conditions on the fourth light being red and the fifth green. Independence preserves the first three indicators' joint distribution, giving conditional variance 3(1/3)(2/3) = 2/3.",
      "official_anchor": "Official solutions PDF page 2, Problem 1.3",
      "sheet_references": ["Exam PDF page 1: Bernoulli variance"],
      "error_type": "none"
    },
    {
      "item_id": "P1(d)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly justifies equal likelihood of the three-red-light configurations and counts favorable configurations, obtaining C(3,2)C(2,1)/C(5,3) = 3/5.",
      "official_anchor": "Official solutions PDF page 2, Problem 1.4",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P1(e)",
      "max_points": 5,
      "correct": true,
      "rationale": "Correct PMF: probability 1/4 at each of 20, 21, 22, and 23 minutes, and zero elsewhere.",
      "official_anchor": "Official solutions PDF page 2, Problem 1.5",
      "sheet_references": ["Exam PDF page 1: discrete uniform PMF"],
      "error_type": "none"
    },
    {
      "item_id": "P1(f)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly partitions the conditioning event into the two exclusive sole-arrival possibilities and uses independence. The resulting conditional probability 163/403 is correct.",
      "official_anchor": "Official solutions PDF pages 2–3, Problem 1.6",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P1(g)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly conditions on all four equally likely waiting times, using N ≤ 2+X. The cumulative probabilities and their average 909/972 = 101/108 are correct.",
      "official_anchor": "Official solutions PDF page 3, Problem 1.7",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P1(h)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly establishes that X = 3 guarantees S ≤ J, so the joint-event numerator is 1/4. Dividing by 101/108 yields the correct conditional probability 27/101.",
      "official_anchor": "Official solutions PDF pages 3–4, Problem 1.8",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P2(a)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly declares the statement true and proves P(A intersect B-complement) = P(A)P(B-complement) by partitioning A and using independence. The proof also covers events of probability zero or one.",
      "official_anchor": "Official solutions PDF page 4, Problem 2.1",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P2(b)",
      "max_points": 10,
      "correct": true,
      "rationale": "Valid counterexample on six equally likely outcomes. P(C) = 2/3 satisfies the hypothesis; given C, the joint probability 1/4 equals the product of marginals. Given its complement, the joint probability is 1/2 while the product is 1/4, disproving the conclusion.",
      "official_anchor": "Official solutions PDF pages 4–5, Problem 2.2",
      "sheet_references": [],
      "error_type": "none"
    },
    {
      "item_id": "P2(c)",
      "max_points": 10,
      "correct": true,
      "rationale": "Correctly proves variance additivity using independence and then the inequality using nonnegativity of variance. The finite-variance qualification matches the usual setting implicit in the official solution. The additional equality characterization is also correct in that setting.",
      "official_anchor": "Official solutions PDF page 5, Problem 2.3",
      "sheet_references": [],
      "error_type": "none"
    }
  ],
  "total_points": 105,
  "max_points": 105,
  "correct_subparts": 11,
  "total_subparts": 11,
  "notes": "All distinct subparts receive full credit under all-or-nothing scoring. Rubric labels P1(a–h) correspond to printed parts 1.1–1.8, and P2(a–c) to 2.1–2.3. Repeated question pages were counted only once. Sheet references identify the supplied exam's formula-summary page."
}