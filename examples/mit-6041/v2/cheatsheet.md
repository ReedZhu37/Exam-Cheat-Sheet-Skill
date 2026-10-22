# MIT 6.041 Quiz 1: probability and discrete random variables (v2; study reference)

Plain Unicode formulas; citations use 1-based source pages.
[A] Historical exam evidence; [B] teaching/emphasis; [C] scope-only/limited evidence; [out] out of scope.

## [A] [binomial] Binomial count
Counts successes in a fixed number of independent trials with identical success probability.
Recognize: Exactly k successes among n trials.
Formula: P(X=k)=C(n,k)p^k(1-p)^(n-k); E[X]=np; Var(X)=np(1-p)
Variables: X: success count; n: trial count; k: successes; p: success probability; C(n,k): binomial coefficient
Conditions: Independent identical Bernoulli trials; integer n>=0, 0<=k<=n; 0<=p<=1; zero elsewhere, endpoints by continuity.
Formula source: [review, p. 26, Binomial row]
Procedure:
1. Count placements and multiply by one sequence's probability.
2. Train Q1(j): given exactly two successes among four identical trials, each indicator's conditional mean is 2/4=1/2.
Pitfalls: Sampling without replacement is generally not binomial. Conditioning on a total makes trials dependent.
Prerequisites: [counting], [bernoulli-indicators]
Sources: [review, p. 26] [train-solution, p. 4, Q1(j)]

## [A] [conditional-expectation] Conditional expectation
Average using the law after conditioning, not the original PMF.
Recognize: Expected cost or count given partial information.
Formula: E[X|A]=sum_x x p_X|A(x); E[X|Y=y]=sum_x x p_X|Y(x|y)
Variables: X,Y: random variables; x,y: values; A: event; p: conditional PMF
Conditions: Positive conditioning mass; conditional absolute integrability.
Formula source: [review, p. 23]
Procedure:
1. Build the conditional PMF, then weight values.
2. Train Q2(e): given Bob green, Alice's prices 300,200,100 have probabilities 3/8,3/8,2/8, giving $212.50.
Pitfalls: Original probabilities are wrong after the observation changes the available outcomes.
Prerequisites: [conditional-laws], [expectation]
Sources: [review, p. 23] [train-solution, p. 6, Q2(e)]

## [A] [conditional-independence] Conditional independence
Independence inside a restricted universe can differ from independence before conditioning.
Recognize: Independence after receiving shared information.
Formula: P(A intersect B|C) = P(A|C)P(B|C)
Variables: A,B: events tested; C: conditioning event
Conditions: P(C)>0; equality defines independence given C.
Formula source: [review, p. 11]
Procedure:
1. Recompute all probabilities under the condition.
2. Train Q1(c): given two fair coins match, only HH and TT remain. Both-heads probability is 1/2, versus product 1/4, so the heads events become dependent.
Pitfalls: Neither unconditional nor conditional independence implies the other.
Prerequisites: [event-independence]
Sources: [review, p. 11] [train-exam, p. 1, Q1(c)]

## [A] [conditional-laws] Conditional PMFs and mixture laws
Restrict a joint law to the observed event and renormalize.
Recognize: Distribution after observing another variable or an event.
Formula: p_X|Y(x|y)=p_XY(x,y)/p_Y(y); p_X|A(x)=P(X=x,A)/P(A)
Variables: X,Y: random variables; x,y: values; A: event; p: indicated PMF
Conditions: Denominator positive.
Formula source: [review, p. 21]
Formula: p_XY(x,y)=p_X|Y(x|y)p_Y(y); p_X(x)=sum_y p_X|Y(x|y)p_Y(y)
Variables: x,y: values; p: indicated joint, conditional, or marginal PMF
Conditions: Sum over positive-mass values of Y.
Formula source: [review, p. 22]
Procedure:
1. Keep compatible cells, divide by retained mass, verify sum one.
2. Train Q3(g): given the second head occurs on toss 7, the first head is uniform on positions 1 through 6.
Pitfalls: Conditioning can change support and destroy independence.
Prerequisites: [joint-marginal], [conditioning]
Sources: [review, p. 21] [review, p. 22] [train-solution, p. 10, Q3(g)]

## [A] [conditioning] Conditional probability
Knowing B occurred restricts the universe to B and renormalizes probabilities.
Recognize: Given, knowing, among, or conditional on.
Formula: P(A|B) = P(A intersect B)/P(B)
Variables: A: target event; B: observed event
Conditions: P(B) > 0.
Formula source: [review, p. 7]
Procedure:
1. Write the conditioning event explicitly; compute its mass and the intersection.
2. Train Q2(a): with four green bikes among nine, P(Alice green)=4/9; given Bob green, it becomes 3/8.
Pitfalls: Conditioning can increase or decrease probability; it does not reverse the conditional automatically.
Prerequisites: [probability-model]
Sources: [review, p. 7] [train-solution, p. 5, Q2(a)]

## [A] [counting] Counting selections and partitions
Count outcomes consistently with whether order matters, replacement is allowed, and groups are labeled.
Recognize: Hands, assignments, arrangements, or fixed numbers of successes.
Formula: N = product_i n_i; P(n,k) = n!/(n-k)!; C(n,k) = n!/[k!(n-k)!]
Variables: n_i: choices at stage i; N: total choices; n: distinct objects; k: objects selected; P(n,k): ordered count; C(n,k): unordered count
Conditions: Stage counts fixed across histories; selections without replacement; integers 0<=k<=n.
Formula source: [review, p. 13]
Formula: N = n!/(n_1! ... n_r!)
Variables: N: partitions; n: objects; n_i: size of labeled group i; r: groups
Conditions: Nonnegative integer sizes summing to n.
Formula source: [review, p. 14]
Procedure:
1. Choose ordered sequences or unordered sets for both numerator and denominator.
2. Train Q1(e): all four aces in a 26-card hand has probability C(48,22)/C(52,26).
Pitfalls: Do not multiply by 4! when ace order is irrelevant.
Prerequisites: [probability-model]
Sources: [review, p. 13] [review, p. 14] [train-solution, p. 3, Q1(e)]

## [A] [event-algebra] Unions, complements, and bounds
Translate 'or' into union, 'and' into intersection, and 'none' into a complement.
Recognize: At least one, neither, or overlapping alternatives.
Formula: P(A union B) = P(A) + P(B) - P(A intersect B) <= P(A) + P(B)
Variables: A,B: events
Conditions: Any two events.
Formula source: [review, p. 5]
Formula: P(A^c) = 1 - P(A)
Variables: A^c: complement of event A
Conditions: Derived from disjoint additivity and normalization.
Formula source: [review, p. 4, Axioms; complement corollary]
Procedure:
1. Prefer the simpler event or its complement.
2. Train Q2(c): no green bike has probability (5/9)(4/8), so at least one green has probability 13/18.
Pitfalls: Adding overlapping events double-counts their intersection.
Prerequisites: [probability-model]
Sources: [review, p. 5] [train-solution, p. 5, Q2(c)]

## [A] [event-independence] Pairwise and mutual independence
Independence means learning one event does not change the other's probability. Mutual independence requires every subset, not just pairs.
Recognize: Independent trials or a request to justify independence.
Formula: P(A intersect B) = P(A)P(B)
Variables: A,B: events
Conditions: Necessary and sufficient for independence.
Formula source: [review, p. 11]
Formula: P(intersection_{i in S} A_i) = product_{i in S} P(A_i)
Variables: A_i: events; S: subset of indices
Conditions: Must hold for every subset S for mutual independence.
Formula source: [review, p. 12]
Procedure:
1. Check factorization, or give one counterexample.
2. Train Q1(b): a fixed urn remains empty with probability (1-1/m)^n for n independent throws into m equally likely urns.
Pitfalls: Disjoint positive-probability events are dependent; pairwise independence is weaker than mutual independence.
Prerequisites: [conditioning]
Sources: [review, p. 11] [review, p. 12] [train-exam, p. 1, Q1(b)]

## [A] [expectation] Expectation and linearity
Expectation is a probability-weighted average. Functions can be averaged directly using the original law.
Recognize: Average cost, gain, or total count.
Formula: E[X]=sum_x x p_X(x); E[g(X)]=sum_x g(x)p_X(x)
Variables: X: random variable; x: value; p_X: PMF; g: function
Conditions: Absolute integrability for finite expectations.
Formula source: [review, p. 17]
Formula: E[aX+bY+c]=aE[X]+bE[Y]+c
Variables: X,Y: random variables; a,b,c: constants
Conditions: Finite means; independence unnecessary.
Formula source: [review, p. 20]
Formula: E[g(X,Y)]=sum_x sum_y g(x,y)p_XY(x,y)
Variables: X,Y: random variables; x,y: values; g: payoff function; p_XY: joint PMF
Conditions: Absolute integrability; independence unnecessary.
Formula source: [review, p. 20]
Procedure:
1. Write the payoff as a function or sum, then average.
2. Generated example: equiprobable X=0,2 gives E[X^2]=2, while (E[X])^2=1.
Pitfalls: Generally E[g(X)] differs from g(E[X]).
Prerequisites: [pmf-cdf]
Sources: [review, p. 17] [review, p. 20]

## [A] [geometric] Geometric waiting time
Counts trials through the first success, including the successful trial. After failures, the remaining waiting time has the original law.
Recognize: Repeat until success, with a fresh identical chance each time.
Formula: P(T=k)=(1-p)^(k-1)p; E[T]=1/p; Var(T)=(1-p)/p^2
Variables: T: trials through first success; k: positive integer; p: success probability
Conditions: Independent trials, constant 0<p<=1; zero outside positive integers; p=1 gives T=1.
Formula source: [review, p. 26, Geometric row]
Procedure:
1. Name the stopping event first, even if the story calls it a failure. Check endpoints: p=0 has no finite stopping time; p=1 is deterministic. Then distinguish total trials, failures, and remaining trials.
2. Train Q1(g): after one failed driving test with independent pass probability 1/2, expected additional tests remains 2.
Pitfalls: Failures before success starts at zero and has mean 1/p-1.
Prerequisites: [event-independence], [pmf-cdf]
Sources: [review, p. 26] [lecture-6, p. 2, Memoryless property] [train-solution, p. 3, Q1(g)]

## [A] [joint-marginal] Joint and marginal PMFs
A joint law assigns mass to value pairs; marginalization sums away the unwanted variable.
Recognize: A two-dimensional probability table or paired measurements.
Formula: p_XY(x,y)=P(X=x,Y=y); p_X(x)=sum_y p_XY(x,y); p_Y(y)=sum_x p_XY(x,y)
Variables: X,Y: random variables; x,y: values; p_XY: joint PMF; p_X,p_Y: marginals
Conditions: Discrete variables on the same experiment.
Formula source: [review, p. 19]
Procedure:
1. Read axes; sum rows or columns and check total mass.
2. Train Q3(a,b): diagonal entries 1/10 and others 1/20 give each marginal value probability 1/4.
Pitfalls: Uniform marginals do not imply a uniform joint distribution.
Prerequisites: [pmf-cdf]
Sources: [review, p. 19] [train-exam, p. 6, Q3 joint table]

## [A] [probability-trees] Multiplication rule and trees
A tree records successive conditional choices. Multiply along a path; add disjoint terminal paths.
Recognize: Sequential draws or several stages of an experiment.
Formula: P(A intersect B intersect C) = P(A)P(B|A)P(C|A intersect B)
Variables: A,B,C: successive events
Conditions: Conditioning prefixes have positive probability.
Formula source: [review, p. 8]
Procedure:
1. Label branches with probabilities conditional on their entire history.
2. Train Q2(d): same-color probability is (4*3+3*2+2*1)/(9*8)=5/18; different colors gives 13/18.
Pitfalls: Without replacement, update both numerator and denominator after each draw.
Prerequisites: [conditioning]
Sources: [review, p. 8] [train-solution, p. 6, Q2(d)]

## [A] [rv-independence] Independent random variables
The joint law factors into marginals. Separate functions of independent variables remain independent.
Recognize: Test whether one measurement provides information about another.
Formula: p_XY(x,y)=p_X(x)p_Y(y)
Variables: x,y: all possible value pairs; p_XY: joint law; p_X,p_Y: marginals
Conditions: Equality for every pair defines independence.
Formula source: [review, p. 24]
Formula: E[XY]=E[X]E[Y]
Variables: X,Y: random variables
Conditions: Independent, integrable X and Y; converse false.
Formula source: [review, p. 25]
Procedure:
1. Find marginals, then test factorization. A quick disproof is an impossible joint pair whose two marginal probabilities are positive. Check degenerate parameter endpoints separately; a constant variable is independent of any variable.
2. Train Q3(c): p(1,1)=1/10 differs from (1/4)(1/4)=1/16, proving dependence.
Pitfalls: One failed pair disproves independence; one successful pair does not prove it.
Prerequisites: [joint-marginal]
Sources: [review, p. 24] [review, p. 25] [train-exam, p. 6, Q3(c)]

## [A] [stopping-counts] Stopping counts and repeated successes
A stopping rule constrains the final trial and all earlier counts; repeated-success waiting times split into geometric blocks.
Recognize: Until the r-th success or either count reaches a boundary.
Formula: P(U=u)=2*C(u-1,10)*(1/2)^u
Variables: U: tosses until 11 heads or 11 tails; u: stopping time; C: binomial coefficient
Conditions: Independent fair tosses; 11<=u<=21, integer; zero otherwise.
Formula source: [train-solution, p. 10, Q3(h)]
Procedure:
1. Fix the terminal outcome; count valid prefixes and establish support.
2. Train Q3(f), corrected: eleven geometric blocks with p=3/4 give expected tails 11/(3/4)-11=11/3. The source's final 11/12 is an arithmetic error.
Pitfalls: A fixed-length binomial formula can include paths that should have stopped earlier.
Prerequisites: [counting], [geometric], [expectation]
Sources: [train-solution, p. 10, Q3(h)] [train-solution, p. 9, Q3(f); final arithmetic corrected using preceding expression]

## [A] [total-expectation] Total expectation
Compute a difficult mean by conditioning on simpler cases.
Recognize: A hidden type is chosen once and controls later behavior.
Formula: E[X]=sum_i P(A_i)E[X|A_i]
Variables: X: integrable random variable; A_i: partition events; i: case index
Conditions: Disjoint exhaustive positive-probability cases.
Formula source: [review, p. 23]
Procedure:
1. Find the mean within each type, then weight by type probability.
2. Train Q3(e): choose one dice pair permanently; mean rolls is (3/4)/(2/5)+(1/4)/(1/4)=23/8.
Pitfalls: A mixture of geometric waiting times has mean averaged reciprocals, not reciprocal average success probability.
Prerequisites: [conditional-expectation], [total-probability]
Sources: [review, p. 23] [train-solution, p. 9, Q3(e)]

## [A] [total-probability] Total probability
Average conditional probabilities over mutually exclusive, exhaustive cases.
Recognize: Choose a device/type first, then observe an outcome.
Formula: P(B) = sum_i P(A_i)P(B|A_i)
Variables: B: target event; A_i: partition cases; i: case index
Conditions: Cases partition Omega; use positive-probability cases.
Formula source: [review, p. 9]
Procedure:
1. Choose a useful partition and weight each conditional result.
2. Train Q3(d): dice-pair weights 3/4, 1/4 and double probabilities 2/5, 1/4 give (3/4)(2/5)+(1/4)(1/4)=29/80.
Pitfalls: An unweighted average is valid only for equally probable cases.
Prerequisites: [probability-trees]
Sources: [review, p. 9] [train-exam, p. 6] [train-exam, p. 7, Q3(d) and second joint table]

## [B] [bernoulli-indicators] Bernoulli variables and indicators
An indicator is one when an event occurs and zero otherwise; a count is a sum of indicators.
Recognize: Expected number of matches, occupied bins, or successes.
Formula: P(I=1)=p; P(I=0)=1-p; E[I]=p; Var(I)=p(1-p)
Variables: I: Bernoulli indicator; p: success probability
Conditions: 0<=p<=1.
Formula source: [review, p. 26, Bernoulli row]
Formula: E[sum_i I_i]=sum_i P(A_i)
Variables: I_i: indicator of event A_i; i: finite index
Conditions: No independence required; derived using Bernoulli means and linearity.
Formula source: [review, p. 20, Linearity, applied to indicators (Bernoulli row on p26)]
Procedure:
1. Assign one indicator per object and sum its success probability.
2. Generated solution to lecture 7's hat exercise: each of n people gets their own hat with probability 1/n, so expected matches is 1 despite dependence.
Pitfalls: Linearity needs no independence; variance additivity does.
Prerequisites: [expectation]
Sources: [review, p. 26] [review, p. 20] [lecture-7, p. 2, Hat problem; extracted text reviewed]

## [C] [bayes] Bayes' rule
Update a prior case probability using the likelihood of observed evidence.
Recognize: Infer which hidden cause produced an observed outcome.
Formula: P(A_i|B) = P(B|A_i)P(A_i) / sum_j P(B|A_j)P(A_j)
Variables: A_i,A_j: partition cases; B: evidence; i,j: case indices
Conditions: P(B)>0; partition cases have positive prior mass.
Formula source: [review, p. 10]
Procedure:
1. Draw cause-to-evidence branches; divide the desired path mass by all evidence paths.
2. Generated from train Q3's dice setup: after observing a double, the first pair's posterior is (3/10)/(29/80)=24/29.
Pitfalls: Likelihood P(B|A) is not posterior P(A|B).
Prerequisites: [total-probability]
Sources: [review, p. 10] [train-exam, p. 7, Q3(d), setup for generated reverse question]

## [C] [discrete-uniform] Discrete uniform distribution
Every integer in a consecutive finite interval has equal mass.
Recognize: Symmetry gives equal probability to each possible integer value.
Formula: P(X=k)=1/(b-a+1); E[X]=(a+b)/2; Var(X)=(b-a)(b-a+2)/12
Variables: X: uniform integer; a,b: integer endpoints; k: integer value
Conditions: a<=k<=b, a<=b; PMF zero otherwise.
Formula source: [review, p. 26, Uniform row]
Procedure:
1. Count endpoints inclusively.
2. Generated example: uniform X on 1,...,6 has mean 7/2 and variance 35/12.
Pitfalls: Equal elementary outcomes do not make every derived variable uniform.
Prerequisites: [pmf-cdf]
Sources: [review, p. 26]

## [C] [pmf-cdf] Discrete random variables and cumulative probabilities
A random variable assigns a number to each outcome. Its PMF assigns mass to each attainable value; cumulative notation below is a derived convenience.
Recognize: Find a distribution or a threshold probability.
Formula: p_X(x) = P(X=x)
Variables: X: random variable; x: value; p_X: PMF
Conditions: Discrete X.
Formula source: [review, p. 15]
Formula: p_X(x)>=0; sum_x p_X(x)=1; F_X(t)=P(X<=t)=sum_{x<=t} p_X(x)
Variables: p_X: PMF; F_X: cumulative probability; x: support value; t: threshold
Conditions: Discrete support; cumulative identity derived by summing the threshold event.
Formula source: [review, p. 16, PMF properties; derived choice S={x:x<=t}, not an explicit CDF slide]
Procedure:
1. List support, collect outcome masses, normalize; sum through the requested threshold.
Pitfalls: A PMF value is a point mass, not a cumulative probability. Include zero outside support.
Prerequisites: [probability-model]
Sources: [review, p. 15] [review, p. 16]

## [C] [probability-model] Sample space and probability law
Omega lists possible outcomes; an event is a subset. A probability law assigns nonnegative mass totaling one.
Recognize: Start here when translating a story into outcomes.
Formula: P(A) >= 0; P(Omega) = 1; P(union_i A_i) = sum_i P(A_i)
Variables: Omega: sample space; A: any event; A_i: events; i: index
Conditions: Finite or countable disjoint events for additivity.
Formula source: [review, p. 4]
Formula: P(A) = |A|/|Omega|
Variables: A: event; |.|: number of outcomes; Omega: sample space
Conditions: Finite, equally likely elementary outcomes.
Formula source: [review, p. 6]
Procedure:
1. Specify one elementary outcome and its probability; then identify favorable outcomes.
Pitfalls: Unordered occupancy patterns need not be equally likely even when individual throws are uniform.
Sources: [review, p. 3] [review, p. 4] [review, p. 6]

## [C] [transformed-variables] Functions of random variables
Different input outcomes producing the same output contribute to the same output mass.
Recognize: Sum, minimum, square, or joint measurements defined from the same inputs.
Formula: p_Z(z)=sum_{(x,y):g(x,y)=z} p_XY(x,y)
Variables: Z: g(X,Y); g: function; x,y: input values; z: output value; p_XY: joint PMF
Conditions: Discrete inputs; include every preimage.
Formula source: [review, p. 20]
Formula: p_Y(y)=sum_{x:g(x)=y} p_X(x)
Variables: Y: g(X); g: function; x,y: values; p_X: input PMF
Conditions: Discrete X.
Formula source: [review, p. 16]
Procedure:
1. Write the requested output event; solve its inverse constraints. Translate the original integer support before evaluating probabilities. For joint outputs apply the same event-preimage rule to both equations; sum every compatible input pair, or evaluate the unique pair when the map is one-to-one.
2. Generated example: equally likely X=-1,0,1 gives P(X^2=1)=2/3 and P(X^2=0)=1/3.
Pitfalls: A many-to-one map cannot be handled using only one inverse value.
Prerequisites: [pmf-cdf]
Sources: [review, p. 16] [review, p. 20]

## [C] [variance] Variance and scaling
Variance measures mean squared distance from the mean.
Recognize: Spread, uncertainty, or variance of a total.
Formula: Var(X)=E[(X-E[X])^2]=E[X^2]-(E[X])^2; Var(aX+b)=a^2 Var(X)
Variables: X: random variable; a,b: constants
Conditions: Finite second moment.
Formula source: [review, p. 18]
Formula: Var(sum_i X_i)=sum_i Var(X_i)
Variables: X_i: random variables; i: finite index
Conditions: Independent variables with finite variances.
Formula source: [review, p. 25]
Procedure:
1. Compute first and second moments; subtract the squared mean.
2. Generated example: X=0 or 2 equally likely has variance 1; 3X+7 has variance 9.
Pitfalls: Constants shift means, not variance. Dependent summands need cross terms.
Prerequisites: [expectation]
Sources: [review, p. 18] [review, p. 25]
