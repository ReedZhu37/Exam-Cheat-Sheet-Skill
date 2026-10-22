# Sheet-only coverage audit

**Full coverage: 11 / 11 distinct subparts.** Repeated questions on later pages are counted once; Problem 1.1 includes all three requested quantities.

Coverage below relies on explicit sheet formulas and procedures—not merely topic headings. The exam’s formula summary on **original PDF p. 1** independently supplies the binomial and discrete-uniform formulas.

Let \(R\) be Stephen’s red-light count, \(S=18+R\), and \(J=20+X\), as specified by the exam. Write \(q_r=P(R=r)\).

## Problem 1

### 1.1 — Stephen’s PMF, expectation, and variance  
**FULL** — Exam pp. 2, 4.

Required steps:
1. Identify \(R\) as a binomial count with \(n=5,\ p=1/3\), and obtain
   \[
   q_r=\binom5r(1/3)^r(2/3)^{5-r},\qquad r=0,\ldots,5.
   \]
   **[binomial]**; also exam formula summary, p. 1.
2. Translate the support and masses through \(S=18+R\): \(p_S(s)=q_{s-18}\) for integer \(18\le s\le23\), zero otherwise. **[transformed-variables]**, **[pmf-cdf]**.
3. Use \(E[S]=18+E[R]\), with the binomial mean. **[expectation]**, **[binomial]**.
4. Use \(\operatorname{Var}(18+R)=\operatorname{Var}(R)\), with the binomial variance. **[variance]**, **[binomial]**.

### 1.2 — Expected red-light count given a commute of at most 19 minutes  
**FULL** — Exam pp. 2, 5.

Required steps:
1. Translate the observation to \(R\le1\). This is algebra using the exam’s commute definition.
2. Retain masses \(q_0,q_1\) and renormalize:
   \[
   P(R=r\mid R\le1)=\frac{q_r}{q_0+q_1},\qquad r=0,1.
   \]
   **[binomial]**, **[conditional-laws]**, **[pmf-cdf]**.
3. Average \(0\) and \(1\) under that conditional PMF. **[conditional-expectation]**.

The sheet explicitly supplies the required “restrict, renormalize, then average” procedure.

### 1.3 — Conditional variance when the last red light was the fourth  
**FULL** — Exam pp. 2, 5.

Required steps:
1. Express the observation as
   \[
   L=\{\text{light 4 red, light 5 green}\}.
   \]
   The first three lights are unrestricted. Event translation is supported by **[event-algebra]**.
2. Establish the conditional distribution rather than simply asserting that independence survives conditioning. For a particular first-three-light pattern with \(k\) reds,
   \[
   P(\text{pattern}\mid L)
   =\frac{(1/3)^k(2/3)^{3-k}(1/3)(2/3)}
          {(1/3)(2/3)}.
   \]
   Product probabilities and cancellation use **[event-independence]**, **[conditioning]**, and **[event-algebra]** for green probabilities.
3. Count the \(\binom3k\) such patterns. Thus, under the conditional law, \(R\) has the distribution of \(1+B\), where \(B\) is binomial with parameters \(3,1/3\). **[counting]**, **[binomial]**, **[conditional-laws]**.
4. Apply the variance rule to this conditional distribution; the added constant contributes no variance. **[variance]**, **[binomial]**.

No additional theorem about preservation of conditional independence is needed.

### 1.4 — Exactly two of the first three lights red, given three reds overall  
**FULL** — Exam pp. 2, 6.

Required steps:
1. Write the requested probability as an intersection probability divided by \(P(R=3)\). **[conditioning]**.
2. For the numerator, choose two red positions among the first three and one among the last two:
   \[
   \binom32\binom21.
   \]
   **[counting]**.
3. Each qualifying complete pattern has probability \((1/3)^3(2/3)^2\); add these disjoint pattern probabilities. **[event-independence]**, **[event-algebra]**, **[probability-model]**.
4. Obtain the denominator from **[binomial]** and cancel the common pattern probability:
   \[
   \frac{\binom32\binom21}{\binom53}.
   \]

A separate hypergeometric-distribution rule is unnecessary.

### 1.5 — Jon’s commute PMF  
**FULL** — Exam pp. 2, 6.

Required steps:
1. Use the stated uniform waiting-time PMF on \(0,1,2,3\). **[discrete-uniform]**; also exam formula summary, p. 1.
2. Apply the one-to-one shift \(J=20+X\), translating both support and masses. **[transformed-variables]**.
3. Include zero mass outside \(20,21,22,23\). **[pmf-cdf]**.

### 1.6 — Jon was the sole person arriving exactly at 8:20  
**FULL** — Exam pp. 2, 7.

Required steps:
1. Define \(A=\{J=20\}\) and \(B=\{S=20\}\). “Exactly one” means the disjoint union
   \[
   D=(A\cap B^c)\cup(A^c\cap B).
   \]
   **[event-algebra]**.
2. Obtain \(a=P(A)\) from Jon’s uniform law and \(b=P(B)=q_2\) from Stephen’s binomial law. **[discrete-uniform]**, **[binomial]**, **[transformed-variables]**.
3. Use the stated independence of the underlying inputs and the sheet’s separate-functions independence property to factor the two exclusive-arrival probabilities. Complements supply \(1-a\) and \(1-b\). **[rv-independence]**, **[event-independence]**, **[event-algebra]**.
4. Add the disjoint alternatives and condition:
   \[
   P(A\mid D)=
   \frac{a(1-b)}{a(1-b)+(1-a)b}.
   \]
   **[probability-model]**, **[conditioning]**.

### 1.7 — Stephen’s commute is at most as long as Jon’s  
**FULL** — Exam pp. 2, 8.

Required steps:
1. Translate \(S\le J\) into \(R\le2+X\).
2. Partition by \(X=0,1,2,3\). **[total-probability]**.
3. Under each case, use independence to retain the original red-count distribution, then sum its PMF through the appropriate threshold. **[rv-independence]**, **[conditional-laws]**, **[binomial]**, **[pmf-cdf]**.
4. Weight the four cases using the uniform waiting-time probabilities:
   \[
   Q=P(S\le J)=
   \sum_{x=0}^{3}\frac14\sum_{r=0}^{2+x}q_r.
   \]
   **[discrete-uniform]**, **[total-probability]**.

### 1.8 — Jon waited three minutes, given Stephen arrived no later  
**FULL** — Exam pp. 2, 9.

Required steps:
1. Set \(E=\{S\le J\}\), and use
   \[
   P(X=3\mid E)=\frac{P(\{X=3\}\cap E)}{P(E)}.
   \]
   **[conditioning]**.
2. When \(X=3\), Jon takes 23 minutes, while Stephen’s support ends at 23. Therefore \(\{X=3\}\subseteq E\); the intersection is just \(\{X=3\}\). Support identification uses **[binomial]**, **[transformed-variables]**.
3. Obtain the numerator from **[discrete-uniform]** and use \(Q\) from 1.7 as the denominator.

The denominator’s complete sheet-supported route is supplied in 1.7.

## Problem 2

### 2.1 — Independence of \(A\) and \(B^c\)  
**FULL** — Exam pp. 2, 10.

Required proof steps:
1. Decompose \(A\) into the disjoint events \(A\cap B\) and \(A\cap B^c\). **[event-algebra]**, **[probability-model]**.
2. Subtract and substitute the given independence:
   \[
   P(A\cap B^c)=P(A)-P(A\cap B)
   =P(A)-P(A)P(B).
   \]
   **[event-independence]**.
3. Factor and apply the complement formula to obtain \(P(A)P(B^c)\). **[event-algebra]**.
4. Recognize the resulting factorization as the definition of independence. **[event-independence]**.

The proof follows from supplied rules; no separate complement-independence theorem is required.

### 2.2 — Conditional independence given \(C\) implies it given \(C^c\)  
**FULL** — Exam pp. 2, 10–11.

Required counterexample strategy:
1. Specify a finite probability model, then recompute and test factorization separately under \(C\) and \(C^c\). This is the sheet’s explicit restricted-universe testing procedure. **[probability-model]**, **[conditioning]**, **[conditional-independence]**.
2. A minimal witness is three equally likely outcomes:
   \[
   \Omega=\{u,v,w\},\qquad C=\{u\},\qquad A=B=\{v\}.
   \]
   Equal-outcome probabilities are supported by **[probability-model]**.
3. Verify \(P(C)=1/3\). Given \(C\), both marginal probabilities and the intersection probability are zero, so factorization holds. Given \(C^c\), both marginals are \(1/2\), but the intersection probability is \(1/2\), not \(1/4\). **[conditioning]**, **[conditional-independence]**.

This construction applies the supplied rules directly; it does not rely merely on the sheet’s general warning that conditioning can change independence.

### 2.3 — \(\operatorname{Var}(X+Y)\ge\operatorname{Var}(X)\) for independent variables  
**FULL** — Exam pp. 3, 11, under the usual finite-variance interpretation.

Required proof steps:
1. Apply the explicitly supplied independent-sum rule:
   \[
   \operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).
   \]
   **[variance]**.
2. Use the squared-deviation definition to establish nonnegativity of \(\operatorname{Var}(Y)\). **[variance]**, with nonnegative PMF-weighted averaging from **[expectation]**, **[pmf-cdf]**.
3. Conclude the inequality by algebra.

The sheet requires finite variances for this rule; the exam does not explicitly state that regularity assumption. No claim about undefined variances is needed.

## Totals

| Label | Distinct subparts |
|---|---:|
| FULL | **11** |
| PARTIAL | 0 |
| ABSENT | 0 |

**NOT COVERED steps:** None in the routes above, subject to the stated finite-variance qualification for 2.3.