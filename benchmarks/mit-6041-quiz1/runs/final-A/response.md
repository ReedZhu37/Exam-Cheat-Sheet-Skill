## Problem 1

Let \(R\) be the total number of red lights Stephen encounters, and let \(S\) and \(J\) be Stephen’s and Jon’s commute lengths in minutes. Then
\[
R\sim\operatorname{Binomial}(5,1/3),\qquad S=18+R,\qquad J=20+X,
\]
where \(X\) is uniform on \(\{0,1,2,3\}\) and independent of \(R\).

### 1. PMF, expectation, and variance of Stephen’s commute

The binomial PMF gives
\[
\boxed{
p_S(s)=
\begin{cases}
\displaystyle \binom{5}{s-18}\left(\frac13\right)^{s-18}
\left(\frac23\right)^{23-s},
&s\in\{18,19,20,21,22,23\},\\
0,&\text{otherwise}.
\end{cases}}
\]
Explicitly,
\[
\begin{array}{c|rrrrrr}
s&18&19&20&21&22&23\\ \hline
p_S(s)&32/243&80/243&80/243&40/243&10/243&1/243
\end{array}
\]

Adding a constant shifts the expectation but leaves the variance unchanged. Thus
\[
\boxed{\mathbb E[S]=18+5\left(\frac13\right)=\frac{59}{3}\text{ minutes}},
\]
\[
\boxed{\operatorname{var}(S)=5\left(\frac13\right)\left(\frac23\right)
=\frac{10}{9}\text{ minutes}^2}.
\]

### 2. Expected number of red lights given a commute of at most 19 minutes

The condition \(S\le19\) is equivalent to \(R\le1\). Under this condition, \(R\) takes only the values 0 and 1, so
\[
\mathbb E[R\mid S\le19]
=P(R=1\mid R\le1)
=\frac{P(R=1)}{P(R=0)+P(R=1)}.
\]
Therefore,
\[
\boxed{\mathbb E[R\mid S\le19]=\frac{80}{32+80}=\frac57}.
\]

### 3. Conditional variance given that the last red light was the fourth light

Let \(L\) be the given event. It specifies that the fourth light was red and the fifth light was green; it imposes no restriction on the first three lights.

By independence, conditional on \(L\), the first three lights remain independent with red probability \(1/3\). Consequently,
\[
R\mid L\ \text{has the distribution of }1+\operatorname{Binomial}(3,1/3).
\]
Thus
\[
\boxed{\operatorname{var}(R\mid L)=3\left(\frac13\right)\left(\frac23\right)=\frac23}.
\]

### 4. Exactly two of the first three lights red, given three red lights total

Given \(R=3\), all \(\binom53\) sets of three red-light positions are equally likely. The desired configurations choose two positions among the first three and one position among the last two. Hence
\[
\boxed{
P(\text{exactly two of the first three red}\mid R=3)
=\frac{\binom32\binom21}{\binom53}
=\frac35}.
\]

### 5. PMF of Jon’s commute

Since \(J=20+X\),
\[
\boxed{
p_J(j)=
\begin{cases}
1/4,&j\in\{20,21,22,23\},\\
0,&\text{otherwise}.
\end{cases}}
\]

### 6. Probability that Jon was the sole person arriving at exactly 8:20am

Let \(E\) be the event that exactly one of Jon and Stephen arrives at 8:20am. This is the disjoint union
\[
E=\{J=20,S\ne20\}\ \cup\ \{S=20,J\ne20\}.
\]
Using independence and \(P(S=20)=80/243\),
\[
\begin{aligned}
P(J=20\mid E)
&=\frac{P(J=20,S\ne20)}
{P(J=20,S\ne20)+P(S=20,J\ne20)}\\
&=\frac{\frac14\left(1-\frac{80}{243}\right)}
{\frac14\left(1-\frac{80}{243}\right)+\frac{80}{243}\frac34}.
\end{aligned}
\]
Therefore,
\[
\boxed{P(J=20\mid E)=\frac{163}{403}}.
\]

### 7. Probability that Stephen’s commute takes at most as long as Jon’s

Conditioning on Jon’s waiting time and using independence,
\[
P(S\le J)
=\frac14\sum_{x=0}^3P(R\le2+x).
\]
The needed cumulative probabilities are
\[
P(R\le2)=\frac{192}{243},\quad
P(R\le3)=\frac{232}{243},\quad
P(R\le4)=\frac{242}{243},\quad
P(R\le5)=1.
\]
Thus
\[
\boxed{
P(S\le J)=\frac{192+232+242+243}{4\cdot243}
=\frac{101}{108}}.
\]

### 8. Probability that Jon waited 3 minutes, given \(S\le J\)

When \(X=3\), Jon’s commute takes 23 minutes. Stephen’s commute never exceeds 23 minutes, so \(X=3\) guarantees \(S\le J\). Hence
\[
P(X=3,S\le J)=P(X=3)=\frac14.
\]
Using part 7,
\[
\boxed{
P(X=3\mid S\le J)
=\frac{1/4}{101/108}
=\frac{27}{101}}.
\]

## Problem 2

### 1. If \(A\) and \(B\) are independent, then \(A\) and \(B^c\) are independent

**True.** Because \(A\cap B\) and \(A\cap B^c\) partition \(A\),
\[
\begin{aligned}
P(A\cap B^c)
&=P(A)-P(A\cap B)\\
&=P(A)-P(A)P(B)\\
&=P(A)\bigl(1-P(B)\bigr)\\
&=P(A)P(B^c).
\end{aligned}
\]
This is exactly the independence condition for \(A\) and \(B^c\).

### 2. Conditional independence given \(C\) implies conditional independence given \(C^c\)

**False.** Consider a uniform probability space
\[
\Omega=\{1,2,3,4,5,6\},
\]
and define
\[
C=\{1,2,3,4\},\qquad
A=\{1,2,5\},\qquad
B=\{1,3,5\}.
\]
Here \(P(C)=2/3\), so \(0<P(C)<1\).

Conditional on \(C\),
\[
P(A\mid C)=\frac12,\qquad
P(B\mid C)=\frac12,\qquad
P(A\cap B\mid C)=\frac14.
\]
Thus \(A\) and \(B\) are conditionally independent given \(C\).

However, \(C^c=\{5,6\}\), and
\[
P(A\mid C^c)=P(B\mid C^c)=\frac12,
\]
while
\[
P(A\cap B\mid C^c)=\frac12
\ne\frac14=P(A\mid C^c)P(B\mid C^c).
\]
Therefore, they are not conditionally independent given \(C^c\).

### 3. If \(X\) and \(Y\) are independent, then \(\operatorname{var}(X+Y)\ge\operatorname{var}(X)\)

**True**, under the usual assumption that the variances are finite.

Independence implies
\[
\operatorname{Cov}(X,Y)=\mathbb E[XY]-\mathbb E[X]\mathbb E[Y]=0.
\]
Expanding the variance of the sum gives
\[
\operatorname{var}(X+Y)
=\operatorname{var}(X)+\operatorname{var}(Y)
+2\operatorname{Cov}(X,Y)
=\operatorname{var}(X)+\operatorname{var}(Y).
\]
Since variance is nonnegative,
\[
\boxed{\operatorname{var}(X+Y)\ge\operatorname{var}(X)}.
\]

**Uncertain answers:** None.