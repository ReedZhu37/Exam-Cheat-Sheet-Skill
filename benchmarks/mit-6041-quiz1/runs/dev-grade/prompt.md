Independently grade the anonymous exam response against the supplied official solutions. Strict all-or-nothing scoring per distinct subpart: every requested result and proof must be correct for full points, otherwise 0. Accept equivalent mathematics and allowed unsimplified forms. Repeated answer pages do not create extra questions. No partial credit. Carefully check proofs, quantifiers, and multiple requests within a subpart. Do not search or use tools. Classify each error as content_missing, misleading_sheet, solving_error, extraction_damage, or none (do not infer sheet deficiencies when sheet is not supplied). Keep original question IDs. Give your result as exactly one JSON object, without Markdown fencing, with keys items (array), total_points, max_points, correct_subparts, total_subparts, notes. Each item must have item_id, max_points, correct (boolean), rationale (including all required results checked), official_anchor (PDF page and part), sheet_references (array; empty if unavailable), error_type. Limit response to 8000 words.

# Exam
## Original PDF page 1

Massachusetts                Institute                of     Technology
Department   of    Electrical                Engineering           &    Computer                 Science
     6.041/6.431:                     Probabilistic                     Systems              Analysis
                      (Quiz 1 | Fall 2009)

## Original PDF page 2

                            Massachusetts                Institute                of     Technology
                            Department   of    Electrical                Engineering           &    Computer                 Science
                                   6.041/6.431:                     Probabilistic                     Systems              Analysis
                                                        (Quiz 1 | Fall 2009)

Problem               B:      (98       points)      As      a   way    to     practice              his    probability    skills,           Bob        goes     apple          picking.           The
orchard         he     goes    to     grows   two   varieties             of    apples:             gala        and       honey           crisp.
     The       proportion           of     the       gala        apples             in     the       orchard         is p   (0    < p <    1),      the      proportion           of     the
honey           crisp         apples             is    1  −   p.     The        number    of    apples           in    the      orchard         is    so large         that        you     can       assume
that        picking        a   few       apples           does    not       change           the      proportion           of    the      two   varieties.
     Independent   of    all  other          apples,            the      probability that a   randomly                picked     gala        apple          is    ripe   is    g
and       the      probability   that        a   randomly                picked    honey           crisp         apple          is    ripe   is   h.

    1.	   (10       points)       Suppose       that        Bob        picks     an      apple  at  random              (uniformly)                    and        eats        it.      Find         the
        probability   that        it    was     a   ripe   gala         apple.

        Note:            Parts       2   and       3   below    can       be done         independently.

    2.     Suppose      that        Bob        picks    n   apples           at     random (independently      and       uniformly).

         (a)	     (10       points)      Find         the      probability   that        exactly           k of those          are      gala        apples.
         (b)       Suppose      that        there          are      exactly             k    gala        apples             among  the  n    apples            Bob        picked.       Caleb
               comes           by   and       gives    Bob        a   ripe   gala         apple          to     add       to     his      bounty.   Bob        then        picks     an     apple
               at     random             from      the      n   +    1   apples   and       eats        it.
                (i)	    (12       points) What          is    the      probability   that        it    was a   ripe   apple?
                (ii)       (12       points) What          is    the      probability   that        it    was a   gala        apple          if    it    was     ripe?
          (c)	     (10      points) Let      n   =    20,      and       suppose      that Bob picked     exactly             10     gala        apples.             What          is    the
               probability   that        the   ﬁrst        10     apples       that        Bob        picked     were      all     gala?

    3.     Next,          Bob        tries        a   diﬀerent   strategy.	  He      starts          with a   tree       of    the      gala        variety   and       picks     apples           at
        random             from         that        tree.   Once         Bob        picks     an     apple          oﬀ     the      tree,        he     carefully               examines                it    to     make
        sure        it    is    ripe.    Once         he     comes           across           an     apple          that        is    not      ripe,    he     moves    to    another              gala        tree.
        He      does    this       until     he     encounters       an     unripe   apple          on     that        second            tree.         Assume             that        each   tree       has
        a   very      large,          essentially         inﬁnite,             number    of    apples.

         (a)	     (10      points)      Let      Xi   be   the      number     of    apples             Bob        picks     oﬀ     the      ith     tree,        (i    = 1,  2).      Write
               down      the      PMF,          expectation,               and       variance             of    Xi.
         (b)	     (12       points)      For    i  = 1,    2,    let Yi   be   the      total          number    of    ripe   apples             Bob        picked     from         the
               ﬁrst       i   trees.           Find         the       expectation              and       the       variance             of    Y2.    (Note           that       Y1   =    X1   −    1   and
               Y2   = (X1  −    1)    +    (X  2  −    1).)
          (c)	     (12       points)      Find         the      joint   PMF         of    Y1   and      Y2.
         (d)       In     the      following,          answer    just       “yes”      or     “no.”  (Explanations will       not       be   taken     into     account
               in    grading.)
                (i)	    (5     points) Are      X1   and      Y2   independent?
                (ii)	     (5     points) Are      X2   and      Y1   independent?

Each   question              is    repeated          in    the      following         pages.           Please           write         your      answer    on
                                                      the      appropriate                   page.

## Original PDF page 3

                       Massachusetts                Institute                of     Technology
                      Department   of    Electrical                Engineering           &    Computer                 Science
                             6.041/6.431:                     Probabilistic                     Systems              Analysis
                                                 (Quiz 1 | Fall 2009)

1.    (10       points)       Suppose       that        Bob        picks     an      apple  at     random              (uniformly)                    and        eats        it.      Find         the
    probability   that        it    was     a   ripe   gala         apple.


























    Note:            Parts       2   and       3   can       be   done independently.

2.     Suppose      that        Bob        picks    n   apples           at random      (independently      and       uniformly).

     (a)      (10       points)      Find         the      probability   that        exactly           k of    those          are      gala        apples.

## Original PDF page 4

                 Massachusetts                Institute                of     Technology
                 Department   of    Electrical                Engineering           &    Computer                 Science
                       6.041/6.431:                     Probabilistic                     Systems              Analysis
                                           (Quiz 1 | Fall 2009)

(b)       Suppose      that        there          are      exactly             k    gala        apples             among  the      n    apples            Bob        picked.       Caleb
     comes           by   and       gives    Bob        a   ripe   gala         apple          to     add       to     his      bounty.   Bob        then        picks     an     apple
     at     random             from      the      n   +    1   apples   and       eats        it.
      (i)     (12       points) What          is    the      probability   that        it was     a   ripe   apple?

## Original PDF page 5

           Massachusetts                Institute                of     Technology
          Department   of    Electrical                Engineering           &    Computer                 Science
                6.041/6.431:                     Probabilistic                     Systems              Analysis
                                    (Quiz 1 | Fall 2009)

(ii)       (12       points)      What          is    the      probability   that        it was     a   gala        apple          if    it    was   ripe?

## Original PDF page 6

                 Massachusetts                Institute                of     Technology
                Department   of    Electrical                Engineering           &    Computer                 Science
                      6.041/6.431:                     Probabilistic                     Systems              Analysis
                                          (Quiz 1 | Fall 2009)

(c)      (10      points)      Let      n   =    20,      and       suppose      that Bob        picked     exactly             10     gala        apples.             What          is    the
     probability   that        the   ﬁrst        10     apples           that        Bob        picked     were      all     gala?

## Original PDF page 7

                        Massachusetts                Institute                of     Technology
                        Department   of    Electrical                Engineering           &    Computer                 Science
                               6.041/6.431:                     Probabilistic                     Systems              Analysis
                                                    (Quiz 1 | Fall 2009)

3.     Next,          Bob        tries        a   diﬀerent   strategy.	  He      starts with        a   tree       of    the      gala        variety   and       picks     apples           at
    random             from         that        tree.   Once         Bob        picks     an     apple          oﬀ     the      tree,        he     carefully               examines                it    to     make
    sure        it    is    ripe.    Once         he     comes           across           an     apple          that        is    not      ripe,    he     moves    to    another              gala        tree.
    He      does    this       until     he     encounters       an     unripe   apple          on     that        second            tree.         Assume             that        each   tree       has
    a   very      large,          essentially         inﬁnite,             number    of    apples.

     (a)	     (10      points)      Let      Xi   be   the      number     of    apples             Bob        picks     oﬀ     the      ith      tree,        (i    = 1,    2).      Write
           down      the      PMF,          expectation,               and       variance             of    Xi.





















     (b)	     (12       points)      For    i  = 1,    2, let Yi   be   the      total          number    of    ripe   apples             Bob        picked     from         the
           ﬁrst       i   trees.           Find         the       expectation              and       the       variance             of    Y2.    (Note           that       Y1   =    X1   −    1   and
           Y2   = (X1  −    1)    +    (X  2  −    1).)

## Original PDF page 8

               Massachusetts                Institute                of     Technology
               Department   of    Electrical                Engineering           &    Computer                 Science
                     6.041/6.431:                     Probabilistic                     Systems              Analysis
                                       (Quiz 1 | Fall 2009)

(c)      (12       points)      Find         the      joint   PMF         of    Y1   and      Y2.

## Original PDF page 9

                 Massachusetts                Institute                of     Technology
                Department   of    Electrical                Engineering           &    Computer                 Science
                      6.041/6.431:                     Probabilistic                     Systems              Analysis
                                          (Quiz 1 | Fall 2009)

(d)       In     the      following,          answer    just       “yes”      or     “no.”  (Explanations                       will       not       be   taken     into     account
     in    grading.)
      (i)     (5     points) Are      X1   and      Y2   independent?


























     (ii)      (5     points) Are      X2   and      Y1   independent?

## Original PDF page 10

MIT OpenCourseWare
http://ocw.mit.edu



6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013




For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms                                                                                                                .
# Official solutions (grader-only)
## Original PDF page 1

                        Massachusetts    Institute     of        Technology
                       Department    of   Electrical   Engineering     &      Computer    Science
                               6.041/6.431:             Probabilistic    Systems    Analysis
                                                                 (Fall   2009)

                                                          Quiz      1     Solutions:
                                                          October    13,   2009

1.   (10     points)    We   start   ﬁrst   by   listing   the   following   probabilities:

                                                                          P(gala)       =    p
                                                               P(honey   crisp)       =      1 − p
                                                                 P(ripe | gala)       =    g
                                                     P(ripe | honey   crisp)       =   h.

    The   probability   that   Bob   ate   a   ripe   gala   is:

                                               P(ripe   gala)       =   P(gala)P(ripe | gala)
                                                                      =     pg.

2.      (a)   (10     points)    If  K       is   the   number   of   gala   apples   selected   from   the n     apples,   then K       is   a
            binomial   random   variable.    The   probability   that K       =  k     is:

                                                                 ˆ               n�        pk(1 − p)n−k   ,       0   k     n
                                              pK    (k)     =               0,k
                                                                                                                      otherwise.


      (b)        i.   (12     points)    Among   the n    +  1   apples,   his   bounty   includes:    1   ripe   gala   from   Caleb,
                   k     gala,  n   − k     honey   crisp.     We   can   compute   the   probability   of   eating   a   ripe   apple
                   conditioned   on   Bob   selecting   an   apple   from   each   of   the   three   disjoint   cases   listed
                   above.    The   total   probability   theorem   allows   us   to   then   ﬁnd   the   probability   of   Bob
                   eating   a   ripe   apple.


                         P(ripe   apple)       =   P(ripe   apple | Caleb’s   ripe   gala)P(Caleb’s   ripe   gala)
                                                        +  P(ripe   apple | k     gala)P(k     gala)
                                                        +  P(ripe   apple | n   − k     honey   crisp)P(n   − k     honey   crisp)
                                                  =      1 ·                 + g1                           k                      n   ·                 + h   ·    − k
                                                             n    + 1                n    + 1                 n    + 1
                                                  =                                                     .1 + gk    + h(n   − k)
                                                                   n    + 1
              ii.   (12     points)    Using   Bayes’   Rule:

                                                        P(gala | ripe   apple)   =                                       .P(ripe  \ gala)
                                                                                             P(ripe   apple)

                   We   can   compute   the P(ripe  \ gala)   as   such:





                                                                                                                                        Page   1   of   3

## Original PDF page 2

                         Massachusetts    Institute     of        Technology
                         Department    of   Electrical   Engineering     &      Computer    Science
                                6.041/6.431:             Probabilistic    Systems    Analysis
                                                                     (Fall   2009)



                         P(ripe  \ gala)       =    P(ripe  \ gala | Caleb’s   ripe   gala)P(Caleb’s   ripe   gala)
                                                            +  P(ripe  \ gala | k     gala)P(k     gala)
                                                            +  P(ripe  \ gala | n   − k     honey   crisp)P(n   − k     honey   crisp)
                                                     =      1 ·                 + g1                           k                      n   ·                 + 0 ·    − k
                                                                 n    + 1                n    + 1                n     + 1
                                                     =                        .1 + gk
                                                             n    + 1
                     Combining   this   result   with   that   of   (i),
                                                                                         1+gk                                     1 + gk
                                           P(gala | ripe   apple)   =               n+1                =                                                  .
                                                                                   1+gk+h(n−k)            1 + gk    + h(n   − k)
                                                                                          n+1
      (c)   (10     points)    Let  A      be   the   event   that   the   ﬁrst   10   apples   picked   were   all   gala   and   let B
             be   the   event   that   exactly   10   gala   apples   were   picked   out   of   the   20   apples.

                                                                     P(A    | B)  =                             .P(A    \ B)
                                                                                             P(B)
             The   probability   of   the   event �          B      can   be   computed   by   using   the   result   in   (a),   where n     =   20
             and  k     =   10.   P(B)  =            p10(1 − p)1020              .   P(A    \ B)   can   be   computed   by   seperating   the
                                                      10
             event   of   A   and   B   into   disjoint   events.    The   event {A    \ B} =  {1st   10   apples   picked   are
             gala   and   the   last   10   apples   are   honey   crisp}.  P(A    \ B)  =  p10(1 − p)10   .   Therefore,
                                                                                  p10(1 − p)10                     1
                                                         P(A    | B)  =  �     20                                                              20                                    =  �      .p10(1 − p)10
                                                                                10                                                              10
3.      (a)   (10    points)    Bob   picks   apples   from   each   tree   until   he   ﬁnds   one   that   is   not   ripe,   and   so   if
             we   think   of   the   event   “picking   an   unripe   apple”   as   a   “success”,   then Xi   is   the   number   of
             apples   picked   (i.e.    trials)   until   we   get   our   ﬁrst   success.    Therefore Xi    is   a   geometrically
             distributed   random   variable   with   probability   of   success   1 − g.
             Since   each   tree   has   a   random   collection    of   apples,    the   apples   Bob   picks   from   the   ﬁrst
             tree   are   independent   of   the   apples   he   picks   from   the   second   tree,   and   therefore X1     and
             X2     are   independent   and   identically   distributed   random   variables.
             The   PMF   of Xi    is
                                     pX1   (k)  =  pX2   (k)       =       (1 ˆ       gk−1(1 − g),                  k− (1 − g))k−1(1 − g)
                                                                     =             0,                                =  1,  2,  3, . . . ,
                                                                                                                                otherwise,
             the   expectation   of Xi    is                                                                          1
                                                                   E[X1]  =  E[X2]  =                ,1 − g

             and   the   variance   of Xi    is
                                                         var(X1)   =   var(X2)     =          (1 − g)21 − (1 − g)

                                                                                             =                            .g
                                                                                                    (1 − g)2


                                                                                                                                                Page   2   of   3

## Original PDF page 3

                  Massachusetts    Institute     of        Technology
                 Department    of   Electrical   Engineering     &      Computer    Science
                        6.041/6.431:             Probabilistic    Systems    Analysis
                                                           (Fall   2009)

(b)   (12     points)    Given   that Y2    =  (X1   − 1)  + (X2   − 1),   we   can   use   the   linearity   property   of
      expectations   to   ﬁnd   the   expectation   of Y2.

                                                 E[Y2]     =     E[(X1   − 1)  + (X2   − 1)]
                                                             =     E[X1] + E[X2] − 2
                                                             =             − 2 2
                                                                    1 − g
                                                             =                    .2g
                                                                    1 − g

      Since    adding    or    subtracting    a    constant    from    a    random    variable    has    no    e    ect    on    its
      variance,   and   since X1     and  X2     are   independent,   we   have

                                              var(Y2)       =       var((X1   − 1)  + (X2   − 1))
                                                             =       var(X1    + X2)
                                                             =       var(X1)  +  var(X2)
                                                             =                            .2g
                                                                    (1 − g)2

(c)   (12     points)
      Let   k        0    and  ℓ       k.       The    event    “Y1      =   k      and   Y2      =   ℓ”    is    identical    to    the    event
      “X1     =   k     +   1    and X2     =   ℓ   − k     +   1”.      Since X1     and   X2     are    independent,    the    desired
      probability    is    (1 − g)gk+1−1(1 − g)g                          =    (1 − g)2gℓ−k+1−1                                                  ℓ     ,    when    0    k       ℓ,    and    zero
      otherwise.

                                             ˆ       gℓ(1 − g)2   ,                  k    =  0,  1, . . .  ℓ,    and  ℓ    =  k,  k    + 1, . . . ,
                  pY1,Y2   (k,  ℓ)      =               0,                                          otherwise.


      Note   that   we   can   interpret   this   result   as   the   probability   of ℓ    failures   (i.e.    picking ℓ    ripe
      apples)   and   two    successes    (i.e.     the   two    unripe   apples    that   cause   Bob    to   stop   at   each
      tree).     Note   also   that   although   the   expression   for   the   joint   PMF   doesn’t   depend   on k,
      the   sample   space   does   depend   on k     because  ℓ     k:    Bob   cannot   pick   more   ripe   apples   in
      the   ﬁrst   tree   than   he   does   in   the   ﬁrst   two   trees   combined.
(d)     (i)   (5    points)    No.   X1    and  Y2    are   not   independent   because Y2     X1  − 1   and   so   knowing
             X1    gives   us   information   about Y2.    Speciﬁcally,   if   we   know   that   Bob   picked   10   total
             apples   from   the   ﬁrst   tree   (i.e. X1     =   10),    then   we   also   know   that   Bob   must   have
             picked   at   least   9   ripe   apples   from   the   ﬁrst   two   trees   combined   (i.e. Y2     9).
      (ii)   (5     points)    Yes.   X2     relates   only   to   the   second   tree   and Y1     relates   only   to   the   ﬁrst
             tree,    and   since   the   picking   of    apples   is    independent   across    trees,    the   two    random
             variables   are   independent.








                                                                                                                                  Page   3   of   3

## Original PDF page 4

MIT OpenCourseWare
https://ocw.mit.edu



6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013





For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms                                                                                                                .
# Anonymous response
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
Image attachment order: first 10 exam pages in order, then 4 official-solution pages in order. The two documents have independent page numbering.
