# Problem B

Let \(G\) denote the event that the selected apple is gala, and \(R\) the event that it is ripe.

## 1.

By the multiplication rule,
\[
P(G\cap R)=P(G)P(R\mid G)=\boxed{pg}.
\]

## 2.

Let \(K\) be the number of gala apples among Bob’s original \(n\) apples.

### (a)

Each pick independently yields a gala apple with probability \(p\), so \(K\) is binomial:
\[
\boxed{
P(K=k)=
\begin{cases}
\displaystyle\binom nk p^k(1-p)^{n-k},&k=0,1,\ldots,n,\\
0,&\text{otherwise}.
\end{cases}}
\]
There are \(\binom nk\) possible placements of the \(k\) gala apples, each with probability \(p^k(1-p)^{n-k}\).

### (b)(i)

Condition throughout on \(K=k\). The selected apple can be:
- Caleb’s apple, with probability \(1/(n+1)\), which is certainly ripe;
- an original gala apple, with probability \(k/(n+1)\), ripe with probability \(g\);
- an original honey crisp apple, with probability \((n-k)/(n+1)\), ripe with probability \(h\).

Thus
\[
\boxed{P(R\mid K=k)=\frac{1+kg+(n-k)h}{n+1}}.
\]

### (b)(ii)

The probability of selecting an apple that is both gala and ripe is
\[
P(G\cap R\mid K=k)=\frac{1+kg}{n+1}.
\]
Consequently,
\[
P(G\mid R,K=k)
=\frac{P(G\cap R\mid K=k)}{P(R\mid K=k)}
=\boxed{\frac{1+kg}{1+kg+(n-k)h}}.
\]

### (c)

Given exactly ten gala apples, every set of ten gala positions among the twenty picks is equally likely. Only one such set consists of the first ten positions. Therefore,
\[
\boxed{
P(\text{first ten all gala}\mid K=10)
=\frac{1}{\binom{20}{10}}
=\frac{1}{184756}.
}
\]
Equivalently, the conditional-probability calculation is
\[
\frac{p^{10}(1-p)^{10}}
{\binom{20}{10}p^{10}(1-p)^{10}}.
\]

## 3.

The answers below use the nondegenerate case \(0<g<1\). The endpoint cases, which the statement does not explicitly exclude, are addressed before part (d).

### (a)

For \(X_i=x\), the first \(x-1\) apples on tree \(i\) must be ripe and the next apple unripe. Independence gives
\[
\boxed{
p_{X_i}(x)=
\begin{cases}
g^{x-1}(1-g),&x=1,2,\ldots,\\
0,&\text{otherwise}.
\end{cases}}
\]

Thus \(X_i\) is geometric with stopping probability \(1-g\). Using the geometric mean and variance,
\[
\boxed{\mathbb E[X_i]=\frac{1}{1-g}},
\qquad
\boxed{\operatorname{Var}(X_i)=\frac{g}{(1-g)^2}},
\quad i=1,2.
\]

### (b)

Since
\[
Y_2=X_1+X_2-2,
\]
linearity of expectation gives
\[
\mathbb E[Y_2]
=\frac{2}{1-g}-2
=\boxed{\frac{2g}{1-g}}.
\]

The apple outcomes on the two trees are independent, so \(X_1\) and \(X_2\) are independent. Subtracting a constant does not change variance, hence
\[
\operatorname{Var}(Y_2)
=\operatorname{Var}(X_1)+\operatorname{Var}(X_2)
=\boxed{\frac{2g}{(1-g)^2}}.
\]

### (c)

For integers \(0\le y_1\le y_2\),
\[
\{Y_1=y_1,Y_2=y_2\}
=\{X_1=y_1+1,\ X_2=y_2-y_1+1\}.
\]
Using independence,
\[
\begin{aligned}
P(Y_1=y_1,Y_2=y_2)
&=\bigl[g^{y_1}(1-g)\bigr]
  \bigl[g^{y_2-y_1}(1-g)\bigr]\\
&=(1-g)^2g^{y_2}.
\end{aligned}
\]
Therefore,
\[
\boxed{
p_{Y_1,Y_2}(y_1,y_2)=
\begin{cases}
(1-g)^2g^{y_2},&y_1,y_2\in\mathbb Z,\quad 0\le y_1\le y_2,\\
0,&\text{otherwise}.
\end{cases}}
\]

**Endpoint clarification for part 3:** If \(g=0\), then \(X_1=X_2=1\) and \(Y_1=Y_2=0\) almost surely. The means and variances above remain valid, and the joint PMF has all its mass at \((0,0)\); both independence answers are then “yes.” If \(g=1\), Bob never encounters an unripe apple and never reaches the second tree, so the stated finite stopping-count model does not apply.

### (d)

For \(0<g<1\):

**(i)** No.

**(ii)** Yes.

---

**Uncertain answers:** None. The unspecified endpoint values of \(g\) are addressed above.