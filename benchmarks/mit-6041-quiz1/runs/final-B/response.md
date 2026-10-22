## Problem 1

Let \(R_i\) indicate that light \(i\) is red, and let
\[
N=\sum_{i=1}^5R_i.
\]
The indicators are independent Bernoulli random variables with parameter \(1/3\), so \(N\sim\operatorname{Binomial}(5,1/3)\). Stephen’s commute time is \(S=18+N\). Jon’s commute time is \(J=20+X\), where \(X\) is uniform on \(\{0,1,2,3\}\) and independent of \(N\).

### 1. PMF, expectation, and variance of Stephen’s commute

Since \(S=18+N\),
\[
\boxed{
p_S(s)=
\begin{cases}
\displaystyle\binom5{s-18}\left(\frac13\right)^{s-18}
\left(\frac23\right)^{23-s},&s\in\{18,19,20,21,22,23\},\\
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

Adding a constant shifts expectation but does not change variance. Thus
\[
\boxed{\mathbb E[S]=18+\frac53=\frac{59}{3}\text{ minutes}},
\qquad
\boxed{\operatorname{Var}(S)=5\left(\frac13\right)\left(\frac23\right)
=\frac{10}{9}\text{ minutes}^2}.
\]

### 2. Expected number of red lights given a commute of at most 19 minutes

The conditioning event is \(N\le1\). Under this condition, \(N\) is either zero or one, so
\[
\mathbb E[N\mid S\le19]
=P(N=1\mid N\le1)
=\frac{80/243}{(32+80)/243}.
\]
Therefore,
\[
\boxed{\mathbb E[N\mid S\le19]=\frac57}.
\]

### 3. Conditional variance given that the last red light was the fourth light

Let \(L\) denote the conditioning event. It specifies that the fourth light is red and the fifth light is green:
\[
L=\{R_4=1,R_5=0\}.
\]
Independence means this does not change the joint distribution of the first three lights. Consequently, conditional on \(L\),
\[
N=1+R_1+R_2+R_3,
\]
where the three remaining random indicators are independent Bernoulli\((1/3)\). Hence
\[
\boxed{\operatorname{Var}(N\mid L)
=3\left(\frac13\right)\left(\frac23\right)=\frac23}.
\]

### 4. Exactly two of the first three lights red, given three red lights total

Given \(N=3\), all \(\binom53\) choices of red-light positions are equally likely: each has unconditional probability \((1/3)^3(2/3)^2\).

For the desired event, choose two red positions among the first three and one among the last two. Thus
\[
\boxed{
P(R_1+R_2+R_3=2\mid N=3)
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

Let \(E\) be the event that exactly one of Jon and Stephen arrives at 8:20am. The two disjoint possibilities are
\[
\{J=20,S\ne20\},\qquad \{S=20,J\ne20\}.
\]
Since \(P(J=20)=1/4\), \(P(S=20)=80/243\), and their commute times are independent,
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

The event \(S\le J\) is equivalent to \(N\le2+X\). Conditioning on \(X\) and using independence,
\[
P(S\le J)=\frac14\bigl[P(N\le2)+P(N\le3)+P(N\le4)+P(N\le5)\bigr].
\]
The binomial PMF gives
\[
P(N\le2)=\frac{192}{243},\quad
P(N\le3)=\frac{232}{243},\quad
P(N\le4)=\frac{242}{243},\quad
P(N\le5)=1.
\]
Thus
\[
\boxed{
P(S\le J)
=\frac{192+232+242+243}{4\cdot243}
=\frac{101}{108}}.
\]

### 8. Probability that Jon waited 3 minutes, given \(S\le J\)

When \(X=3\), Jon’s commute lasts 23 minutes. Stephen’s commute never exceeds 23 minutes, so \(\{X=3\}\subseteq\{S\le J\}\). Therefore,
\[
\boxed{
P(X=3\mid S\le J)
=\frac{P(X=3,S\le J)}{P(S\le J)}
=\frac{1/4}{101/108}
=\frac{27}{101}}.
\]

## Problem 2

### 1. If \(A\) and \(B\) are independent, then \(A\) and \(B^c\) are independent

**True.** The events \(A\cap B\) and \(A\cap B^c\) partition \(A\). Hence, using independence,
\[
\begin{aligned}
P(A\cap B^c)
&=P(A)-P(A\cap B)\\
&=P(A)-P(A)P(B)\\
&=P(A)\bigl(1-P(B)\bigr)\\
&=P(A)P(B^c).
\end{aligned}
\]
This is precisely the required independence.

### 2. Conditional independence given \(C\) implies conditional independence given \(C^c\)

**False.** Consider six equally likely outcomes,
\[
\Omega=\{1,2,3,4,5,6\},
\]
and define
\[
C=\{1,2,3,4\},\qquad
A=\{1,2,5\},\qquad B=\{1,3,5\}.
\]
Here \(P(C)=2/3\), so \(0<P(C)<1\).

Given \(C\), the four outcomes in \(C\) are equally likely, and
\[
P(A\mid C)=P(B\mid C)=\frac12,\qquad
P(A\cap B\mid C)=\frac14.
\]
Thus \(A\) and \(B\) are conditionally independent given \(C\).

However, \(C^c=\{5,6\}\), and
\[
P(A\mid C^c)=P(B\mid C^c)=\frac12,
\qquad
P(A\cap B\mid C^c)=\frac12\ne\frac14.
\]
Therefore, they are not conditionally independent given \(C^c\).

### 3. Independent \(X,Y\) satisfy \(\operatorname{Var}(X+Y)\ge\operatorname{Var}(X)\)

**True, assuming finite variances as usual for the variance identity.** Independence gives
\[
\mathbb E[XY]=\mathbb E[X]\mathbb E[Y].
\]
Expanding the variance,
\[
\begin{aligned}
\operatorname{Var}(X+Y)
&=\mathbb E[X^2]+2\mathbb E[XY]+\mathbb E[Y^2]
-\bigl(\mathbb E[X]+\mathbb E[Y]\bigr)^2\\
&=\operatorname{Var}(X)+\operatorname{Var}(Y)\\
&\ge\operatorname{Var}(X),
\end{aligned}
\]
because variance is nonnegative. Equality holds exactly when \(Y\) is almost surely constant.

**Uncertain answers:** None.