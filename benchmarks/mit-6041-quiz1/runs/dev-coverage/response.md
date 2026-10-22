# Sheet-only coverage audit

**Full coverage: 10 / 10 distinct subparts.**  
**PARTIAL: 0. ABSENT: 0.** Repeated questions on later pages are counted only once.

The classifications below rely on explicit sheet formulas and procedures, not merely topic headings. The formula summary in the attached image of **exam page 1** also supplies binomial and geometric formulas.

## 1 — Ripe gala apple
**Exam pages 2–3 · FULL**

Required steps:
1. Identify \(G=\{\text{gala}\}\) and \(R=\{\text{ripe}\}\). The problem supplies \(P(G)=p\) and \(P(R\mid G)=g\).
2. Multiply the conditional probability by the probability of its conditioning event:
   \[
   P(G\cap R)=P(G)P(R\mid G)=pg.
   \]
   **Coverage:** [conditioning], equivalently [probability-trees].

No missing rule or strategy.

## 2(a) — Exactly \(k\) gala apples
**Exam pages 2–3 · FULL**

Required steps:
1. Treat each independent pick’s gala indicator as a Bernoulli variable with parameter \(p\). **Coverage:** [bernoulli-indicators]; independence and identical probabilities are given in the exam.
2. Recognize the total as a fixed-length binomial count and apply
   \[
   P(K=k)=\binom nk p^k(1-p)^{n-k},\qquad k=0,\ldots,n,
   \]
   with zero mass elsewhere. **Coverage:** [binomial]; also **exam page 1, Binomial row**.

No missing rule or strategy.

## 2(b)(i) — Ripe apple after Caleb’s addition
**Exam pages 2 and 4 · FULL**

Required steps:
1. Work within the stated condition that the original collection contains exactly \(k\) gala apples. Partition the final choice into:
   - Caleb’s apple;
   - an original gala apple;
   - an original honey crisp apple.
   
   Uniform selection gives respective probabilities
   \[
   \frac1{n+1},\quad \frac{k}{n+1},\quad \frac{n-k}{n+1}.
   \]
   **Coverage:** [conditioning], [probability-model].
2. Use conditional ripeness probabilities \(1,g,h\), supplied by the story, and average over that partition:
   \[
   P(R\mid K=k)=\frac{1+kg+(n-k)h}{n+1}.
   \]
   **Coverage:** [total-probability].

Zero-size categories are omitted, consistently with the positive-mass condition in [total-probability]. Crucially, Caleb’s apple is not assigned ripeness probability \(g\).

No missing rule or strategy.

## 2(b)(ii) — Gala given that the eaten apple was ripe
**Exam pages 2 and 5 · FULL**

Required steps:
1. In the same conditioned collection, combine the two disjoint ripe-gala routes: Caleb’s apple and an original gala apple. Their total mass is
   \[
   P(G\cap R\mid K=k)=\frac{1+kg}{n+1}.
   \]
   **Coverage:** [probability-trees] for path multiplication and disjoint-path addition; [probability-model] for uniform selection.
2. Divide this intersection probability by the ripe probability from 2(b)(i):
   \[
   P(G\mid R,K=k)=\frac{1+kg}{1+kg+(n-k)h}.
   \]
   **Coverage:** [conditioning], [total-probability]. Alternatively, [bayes] supplies the reverse-conditioning strategy.

The denominator is positive because Caleb contributes a guaranteed ripe apple.

No missing rule or strategy.

## 2(c) — First ten gala, given exactly ten gala among twenty
**Exam pages 2 and 6 · FULL**

Required steps:
1. Let \(A\) mean that the first ten picks are gala and \(B=\{K=10\}\). Set up \(P(A\mid B)=P(A\cap B)/P(B)\). **Coverage:** [conditioning].
2. Recognize that \(A\cap B\) specifies exactly one type sequence: ten gala followed by ten honey crisp. Its probability is
   \[
   p^{10}(1-p)^{10}.
   \]
   **Coverage:** [event-independence] for multiplying independent trial probabilities; [event-algebra] for complementary type probabilities.
3. Evaluate \(P(B)\) using [binomial], then cancel:
   \[
   P(A\mid B)
   =\frac{p^{10}(1-p)^{10}}
   {\binom{20}{10}p^{10}(1-p)^{10}}
   =\binom{20}{10}^{-1}.
   \]

This route does not assume independence after conditioning or require an unstated exchangeability theorem. **Coverage:** [binomial] explicitly warns that conditioning on the total creates dependence.

No missing rule or strategy.

## 3(a) — PMF, expectation, and variance of \(X_i\)
**Exam pages 2 and 7 · FULL**

Required steps:
1. Regard “unripe” as the stopping success, with probability \(q=1-g\). **Coverage:** [event-algebra].
2. Recognize that \(X_i\) counts trials **including** the first unripe apple. Independent apples and constant ripeness probability meet the geometric conditions. **Coverage:** [geometric].
3. Substitute \(q=1-g\) into the geometric PMF and moments:
   \[
   P(X_i=x)=g^{x-1}(1-g),\qquad x=1,2,\ldots,
   \]
   \[
   E[X_i]=\frac1{1-g},\qquad
   \operatorname{Var}(X_i)=\frac{g}{(1-g)^2},
   \]
   with zero PMF outside the positive integers. **Coverage:** [geometric]; also **exam page 1, Geometric row**.

No missing rule or strategy, subject to the parameter qualification below.

## 3(b) — Expectation and variance of \(Y_2\)
**Exam pages 2 and 7 · FULL**

Required steps:
1. Use the exam’s identity \(Y_2=X_1+X_2-2\).
2. Establish independence of the tree counts rather than merely assuming that separate trees suffice. For fixed positive integers \(a,b\), the event \(X_1=a,X_2=b\) specifies \(a-1\) ripe apples and an unripe apple on the first tree, and \(b-1\) ripe apples and an unripe apple on the second. Independence of the apples gives
   \[
   P(X_1=a,X_2=b)
   =g^{a-1}(1-g)\,g^{b-1}(1-g).
   \]
   This factors into the geometric marginals. **Coverage:** [event-independence], [geometric], [rv-independence].
3. Apply linearity of expectation:
   \[
   E[Y_2]=2E[X_1]-2=\frac{2g}{1-g}.
   \]
   **Coverage:** [expectation], [geometric].
4. Remove the constant shift and add the independent variances:
   \[
   \operatorname{Var}(Y_2)=\frac{2g}{(1-g)^2}.
   \]
   **Coverage:** [variance], [geometric].

No missing rule or strategy.

## 3(c) — Joint PMF of \(Y_1,Y_2\)
**Exam pages 2 and 8 · FULL**

Required steps:
1. Invert the identities supplied by the exam:
   \[
   Y_1=u,\ Y_2=v
   \quad\Longleftrightarrow\quad
   X_1=u+1,\ X_2=v-u+1.
   \]
   This is algebraic event identification; the joint-PMF definition is supplied by [joint-marginal].
2. Require positive integer values of both \(X_i\), giving integer support \(0\le u\le v\). **Coverage:** [geometric], [pmf-cdf].
3. Evaluate the corresponding independent geometric masses, using the factorization justified in 3(b):
   \[
   p_{Y_1,Y_2}(u,v)=
   \begin{cases}
   (1-g)^2g^v,&u,v\in\mathbb Z,\ 0\le u\le v,\\
   0,&\text{otherwise}.
   \end{cases}
   \]
   **Coverage:** [rv-independence], [geometric], [joint-marginal]. The preimage strategy is also explicitly supported by [transformed-variables].

No negative-binomial formula or additional transformation theorem is needed.

No missing rule or strategy.

## 3(d)(i) — Independence of \(X_1\) and \(Y_2\)
**Exam pages 2 and 9 · FULL**

Required steps:
1. Use the sheet’s strategy of disproving independence with one failed factorization. **Coverage:** [rv-independence].
2. For \(0<g<1\), choose \(X_1=2\) and \(Y_2=0\). Their intersection is impossible because \(Y_2=X_1+X_2-2\) and \(X_2\ge1\). Thus its mass is zero. **Coverage:** [geometric] for support; [probability-model] for the impossible-event probability.
3. Both marginal masses are positive:
   \[
   P(X_1=2)=g(1-g),\qquad P(Y_2=0)=(1-g)^2.
   \]
   The latter event requires \(X_1=X_2=1\). **Coverage:** [geometric], [event-independence], [joint-marginal].
4. The joint mass therefore differs from the product, establishing **no**. **Coverage:** [rv-independence].

No missing rule or strategy.

## 3(d)(ii) — Independence of \(X_2\) and \(Y_1\)
**Exam pages 2 and 9 · FULL**

Required steps:
1. Establish \(X_1,X_2\) independence through the finite-path factorization given in 3(b). **Coverage:** [event-independence], [geometric], [rv-independence].
2. Use \(Y_1=X_1-1\), supplied by the exam. The sheet explicitly states that separate functions of independent variables remain independent. Consequently \(X_2\) and \(Y_1\) are independent: **yes**. **Coverage:** [rv-independence].

No missing rule or strategy.

## Parameter qualification

The exam does not explicitly restrict \(g\) to \(0<g<1\).

- At \(g=0\), [geometric] explicitly covers the degenerate stopping law: \(X_1=X_2=1\), \(Y_1=Y_2=0\). In particular, 3(d)(i) becomes **yes**, by [rv-independence].
- At \(g=1\), no unripe apple is encountered, so the stopping construction does not produce the finite-valued counts requested in Part 3. This is a **problem-domain issue**, not an absent sheet rule; [geometric] expressly requires positive stopping probability.

**Final audit: FULL 10 / 10; no required step is NOT COVERED in the well-defined stopping regime.**