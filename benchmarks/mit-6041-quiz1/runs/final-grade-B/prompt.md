Independently grade the anonymous exam response against the supplied official solutions. Strict all-or-nothing scoring per distinct subpart: every requested result and proof must be correct for full points, otherwise 0. Accept equivalent mathematics and allowed unsimplified forms. Repeated answer pages do not create extra questions. No partial credit. Carefully check proofs, quantifiers, and multiple requests within a subpart. Do not search or use tools. Classify each error as content_missing, misleading_sheet, solving_error, extraction_damage, or none (do not infer sheet deficiencies when sheet is not supplied). Keep original question IDs. Give your result as exactly one JSON object, without Markdown fencing, with keys items (array), total_points, max_points, correct_subparts, total_subparts, notes. Each item must have item_id, max_points, correct (boolean), rationale (including all required results checked), official_anchor (PDF page and part), sheet_references (array; empty if unavailable), error_type. Limit response to 8000 words.

Fixed final rubric: P1(a-h) max 10,10,10,10,5,10,10,10 and P2(a-c) max 10,10,10. Exactly 11 subparts, total 105.

# Exam
## Original PDF page 1

Massachusetts                Institute                of     Technology
Department   of    Electrical                Engineering           &    Computer                 Science
     6.041/6.431:                     Probabilistic                      Systems              Analysis
                      (Quiz 1 | Fall 2010)

## Original PDF page 2

                             Massachusetts                Institute                of     Technology
                            Department   of    Electrical                Engineering           &    Computer                 Science
                                   6.041/6.431:                     Probabilistic                      Systems              Analysis
                                                         (Quiz 1 | Fall 2010)

Problem               1:    (75      points)

     Note:          All      parts         can       be   done         independently, with the      exception                of    the      last       part.          Just        in    case        you
made          a   mistake   in     the   previous               part,         you     can       use       a   symbol    for      the       expression                  you     found          there,           and
use      that        symbol    in    the      formulas        for      the      last       part.

     Note:         Algebraic                or     numerical               expressions                   do     not      need         to    be simpliﬁed                in    your       answers.

     Jon       and       Stephen              cannot            help        but       think          about       their   commutes        using          probabilistic                     modeling.            Both
of    the      them         start         promptly                at     8am.
     Stephen              drives     and       thus     is    at     the       mercy           of    traﬃc           lights.      When           all     traﬃc           lights    on     his      route          are
green,           the      entire       trip       takes    18     minutes.          Stephen’s                route          includes              5   traﬃc           lights,     each   of    which   is    red
with        probability   1/3,      independent   of    every      other          light.    Each   red      traﬃc           light   that        he     encounters       adds
1   minute    to     his      commute      (for       slowing,          stopping,                and       returning                to     speed).

    1.	   (10       points)      Find         the      PMF,           expectation,               and       variance             of the length           (in      minutes)         of    Stephen’s
        commute.

    2.	   (10      points)      Given     that        Stephen’s                commute      took     him at most         19     minutes,         what         is    the      expected
        number    of    red      lights    that     he     encountered?

    3.	   (10      points)      Given     that        the      last       red      light   encountered by   Stephen              was     the      fourth           light,    what         is
        the      conditional                   variance             of    the   total         number    of    red      lights    he     encountered?

    4.	   (10      points)      Given     that        Stephen              encountered         a   total         of three red      lights,     what         is    the      probability
        that        exactly             two   out       of    the      ﬁrst        three   lights    were      red?

     Jon’s          commuting          behavior        is    rather          simple            to     model.   Jon       walks     a   total         of     20     minutes        from         his
home          to     a   station          and       from         a   station            to     his      oﬃce.           He      also        waits       for     X     minutes        for      a   subway   train,
where         X     has       the      discrete             uniform              distribution            on  {0,      1,    2,    3}.       (All       four        values are      equally             likely,  and
independent   of    the      traﬃc           lights    encountered         by   Stephen.)

    5.	   (5     points)      What          is    the      PMF         of    the      length           of    Jon’s commute      in    minutes?

    6.	   (10       points)      Given     that        there         was     exactly             one       person arriving              at    exactly              8:20am,              what         is    the
        probability   that        this    person          was     Jon?

    7.	   (10       points)      What           is    the       probability    that        Stephen’s                 commute  takes     at     most         as     long        as     Jon’s
        commute?
    8.	   (10      points)      Given     that        Stephen’s                commute      took     at most as    long        as    Jon’s,          what    is   the      conditional
        probability   that        Jon       waited         3   minutes        for      his    train?


Problem              2.    (30      points)      For    each   one of the      statements    below,     give   either          a   proof    or    a   counterexample
showing         that     the      statement   is    not       always     true.
    1.	   (10      points)      If    events   A    and      B    are      independent,    then        the      events   A    and      Bc   are      also       independent.

    2.	   (10       points)  Let      A,     B,   and      C    be   events    associated           with         a   common               probabilistic              model,       and
        assume             that        0   <    P(C     )   <     1.      Suppose       that       A    and      B     are       conditionally                      independent   given    C.
        Then,         A    and      B    are      conditionally                      independent   given    Cc  .

## Original PDF page 3

                       Massachusetts                Institute                of     Technology
                       Department   of    Electrical                Engineering           &    Computer                 Science
                            6.041/6.431:                     Probabilistic                      Systems              Analysis
                                              (Quiz 1 | Fall 2010)

  3.    (10      points)      Let     X     and      Y    be   independent   random variables.               Then,           var(X    +   Y   ) ≥    var(X     ).


Each   question              is    repeated          in    the      following         pages.           Please           write         your      answer    on
                                             the      appropriate                   page.

## Original PDF page 4

                            Massachusetts                Institute                of     Technology
                            Department   of    Electrical                Engineering           &    Computer                 Science
                                  6.041/6.431:                     Probabilistic                      Systems              Analysis
                                                        (Quiz 1 | Fall 2010)

Problem               1:    (75      points)

     Note:          All      parts         can       be   done         independently, with the      exception                of    the      last       part.          Just        in    case        you
made          a   mistake   in     the   previous               part,         you     can       use       a   symbol    for      the       expression                  you     found          there,           and
use      that        symbol    in    the      formulas        for      the      last       part.

     Note:         Algebraic                or     numerical               expressions                   do     not      need         to    be simpliﬁed                in    your       answers.

     Jon       and       Stephen              cannot            help        but       think          about       their   commutes        using          probabilistic                     modeling.            Both
of    the      them         start         promptly                at     8am.
     Stephen              drives     and       thus     is    at     the       mercy           of    traﬃc           lights.      When           all     traﬃc           lights    on     his      route          are
green,           the      entire       trip       takes    18     minutes.          Stephen’s                route          includes              5   traﬃc           lights,     each   of    which   is    red
with        probability   1/3,      independent   of    every      other          light.    Each   red      traﬃc           light   that        he     encounters       adds
1   minute    to     his      commute      (for       slowing,          stopping,                and       returning                to     speed).

    1.	   (10       points)      Find         the      PMF,           expectation,               and       variance             of the length           (in      minutes)         of    Stephen’s
        commute.

## Original PDF page 5

                       Massachusetts                Institute                of     Technology
                      Department   of    Electrical                Engineering           &    Computer                 Science
                            6.041/6.431:                     Probabilistic                      Systems              Analysis
                                                 (Quiz 1 | Fall 2010)

2.    (10      points)      Given     that        Stephen’s                commute      took     him       at most         19     minutes,         what         is    the      expected
    number    of    red      lights    that     he     encountered?



























3.    (10      points)      Given     that        the      last       red      light   encountered by   Stephen              was     the      fourth           light,    what         is
    the      conditional                   variance             of    the   total         number    of    red      lights    he     encountered?

## Original PDF page 6

                            Massachusetts                Institute                of     Technology
                           Department   of    Electrical                Engineering           &    Computer                 Science
                                  6.041/6.431:                     Probabilistic                      Systems              Analysis
                                                       (Quiz 1 | Fall 2010)

    4.    (10      points)      Given     that        Stephen              encountered         a   total         of    three red      lights,     what         is    the      probability
        that        exactly             two   out       of    the      ﬁrst        three   lights    were      red?






















     Jon’s          commuting          behavior        is    rather           simple            to     model.     Jon       walks     a   total         of     20     minutes        from         his
home          to     a   station          and       from         a   station            to     his      oﬃce.           He      also        waits       for     X     minutes        for      a   subway   train,
where         X     has       the      discrete             uniform              distribution            on  {0,      1,    2,    3}.       (All       four        values are      equally             likely,  and
independent   of    the      traﬃc           lights    encountered         by   Stephen.)

    5.    (5     points)      What          is    the      PMF         of    the      length           of    Jon’s commute      in    minutes?

## Original PDF page 7

                      Massachusetts                Institute                of     Technology
                      Department   of    Electrical                Engineering           &    Computer                 Science
                            6.041/6.431:                     Probabilistic                      Systems              Analysis
                                               (Quiz 1 | Fall 2010)

6.    (10       points)      Given     that        there         was     exactly             one       person arriving              at    exactly              8:20am,              what         is    the
   probability   that        this    person          was     Jon?

## Original PDF page 8

                     Massachusetts                Institute                of     Technology
                     Department   of    Electrical                Engineering           &    Computer                 Science
                           6.041/6.431:                     Probabilistic                      Systems              Analysis
                                              (Quiz 1 | Fall 2010)

7.    (10       points)      What           is    the       probability    that        Stephen’s                 commute       takes     at     most         as     long        as     Jon’s
   commute?

## Original PDF page 9

                      Massachusetts                Institute                of     Technology
                     Department   of    Electrical                Engineering           &    Computer                 Science
                           6.041/6.431:                     Probabilistic                      Systems              Analysis
                                               (Quiz 1 | Fall 2010)

8.    (10      points)      Given     that        Stephen’s                commute      took     at    most as    long   as    Jon’s,          what         is   the      conditional
   probability   that        Jon       waited         3   minutes        for      his    train?

## Original PDF page 10

                           Massachusetts                Institute                of     Technology
                          Department   of    Electrical                Engineering           &    Computer                 Science
                                 6.041/6.431:                     Probabilistic                      Systems              Analysis
                                                     (Quiz 1 | Fall 2010)

Problem              2.    (30      points)      For    each   one      of    the      statements    below,     give   either          a   proof    or    a   counterexample
showing         that       the      statement   is    not       always     true.
   1.	   (10      points)      If    events   A    and      B    are      independent,    then        the      events   A    and      Bc   are      also       independent.




























   2.	   (10       points)  Let      A,     B,   and      C    be   events    associated           with         a   common               probabilistic   model,       and
       assume             that        0   <    P(C     )   <     1.      Suppose       that       A    and      B     are       conditionally                      independent   given    C.
       Then,         A    and      B    are      conditionally                      independent   given    Cc  .

## Original PDF page 11

                     Massachusetts                Institute                of     Technology
                     Department   of    Electrical                Engineering           &    Computer                 Science
                           6.041/6.431:                     Probabilistic                      Systems              Analysis
                                              (Quiz 1 | Fall 2010)

   (Additional                   space          for     Problem               2.2)



























3.    (10      points)      Let     X     and      Y    be   independent random variables.               Then,           var(X    +   Y   ) ≥    var(X     ).

## Original PDF page 12

MIT OpenCourseWare
http://ocw.mit.edu



6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013




For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms                                                                                                                .
# Official solutions (grader-only)
## Original PDF page 1

                               Massachusetts  Institute  of        Technology
                               Department  of   Electrical  Engineering  &      Computer  Science
                                      6.041/6.431:             Probabilistic    Systems    Analysis
                                                          (Quiz 1 Solutions | Fall 2010)

                                                                  Quiz      1     Solutions:
                                                                  October    12,   2010

Problem       1.

1.	     (10     points)    Let  Ri    be   the   amount   of   time   Stephen   spends   at   the ith   red   light. Ri    is   a   Bernoulli
    random   variable   with p    =  1/3.    The   PMF   for Ri    is:
                                                                                           if  r    =  0,
                                                                                   2/3,
                                                            PRi  (r)  =           1  0,/3,       if  r    =  1,
                                                                                               otherwise.

    The   expectation   and   variance   for Ri    are:

                                                            E[Ri]     =      p    =  3 ,1


                                                         var(Ri)     =      p(1 − p)  =             =     .1 2          2
                                                                                                 3 3          9

    Let  TS     be   the   total   length   of   time   of   Stephen’s   commute   in   minutes.    Then,
                                                                                       ∑5
                                                                      TS     =  18 +           Ri.
                                                                                        i=1

    TS	    is   a   shifted   binomial   with n     =  5   trials   and p    =  1/3.   The   PMF   for TS     is   then:
                                          (     )( )k−18  ( )23−k
                                                           5                 1                       2        if  k   ∈ {18,  19, 20,  21,  22,  23},
                        PTS   (k)  =              k  0,   − 18            3                       3               ,
                                               	                                                                                otherwise.

    The   expectation   and   variance   for TS     are:
                                                                                   [        ]∑5
                                                             E[TS   ]     =     E         18 +           Ri
                                                                                              i=1
                                                                          =             .59
                                                                                 3
                                                                                      (        )∑  5
                                                          var(TS   )      =       var       18 +        Ri
                                                                                                 i=1
                                                                          =             .10
                                                                                 9

2.	     (10     points)    Let  N  be   the   number   of   red   lights   Stephen   encountered   on   his   commute.    Given   that
    TS   ≤ 19,   then N       =  0   or N       =   1.  The   unconditional   probability   of   ( 3            N       =   0   is  P(N       =  0)  =  ( 32   )5   .    The
    unconditional   probability   of N       =  1   is P(N       =  1)  = (5)                2   )4( 31   )1  .
                                                                                        1

## Original PDF page 2

                                  Massachusetts  Institute  of        Technology
                                 Department  of   Electrical  Engineering  &      Computer  Science
                                         6.041/6.431:             Probabilistic  Systems    Analysis
                                                          (Quiz 1 Solutions | Fall 2010)

     To   ﬁnd   the   conditional   expectation,   the   following   conditional   PDF   is   calculated:
                                                                                        ( 2   )5
                                                                                                   3
                                                              
                                                                   ()                         ,       if  n     =  0,    
                                                                       )5    +     5     ( 2   )4( 1   )1
                                                             	       ( 2                                                                           if  n     =  0,
                                                                           3                       1       3           3  ( 2                    2/7,
                 PN|TS                |  TS   ≤ 19)   =     (5)                    )4( 1   )1                                                   =          5/7,       if  n     =  1,
                           ≤19(n                                                       1  (3 )         3                  ,       if  n     =  1,    
                                                             	       ( 2                    5           )4( 1   )1
                                                                                               ( 2    +                                                         0,             otherwise.
                                                                           )5
                                                             	             3                       1       3           3
                                                                     0,	                                                    otherwise,

     Therefore,
                                                                                                                            5
                                                                         E[N    |  TS   ≤ 19]   =     .7

3.	     (10     points)     Given  that   the   last   red   light   encountered   by   Stephen   was   the   fourth   light, R4     =  1
     and  R5    =  0.
     We   are   asked   to   compute   var(N    | {R4    =  1} ∩ {R5    =  0}).    Therefore,

              var(N    | {R4    =  1} ∩ {R5    =  0})       =       var(R1    + R2    + R3    + R4    + R5   | {R4    =  1} ∩ {R5    =  0})
                                                                      =	      var(R1    + R2    + R3    + 1 + 0 | {R4    =  1} ∩ {R5    =  0})
                                                                      =	      var(R1    + R2    + R3    + 1)
                                                                      =	      var(R1    + R2    + R3)
                                                                      =	      3var(R1)
                                                                      =          .6
                                                                             9

4.	     (10     points)     Under   the    given    condition,    the    discrete    uniform    law    can    be    used    to    compute    the )    ways   that   Stephen   can   encounter   a   total   of   three   red   lights.
     probability   of   i()    nterest.    There   are (53
     There   are     23       ways   that   two   out   of   the   ﬁrst   three   lights   were   red.    This   leaves   one   additional   red
     light   out   of   the   last   two   lights   and   there   are (2)    possible   ways   that   this   event   can   occur.    Putting   it
                                                                                    1
     all   together,
                                                                                                                                         (3)(2)            3
                         P(two   of   ﬁrst   three   lights   were   red|  total   of   three   red   lights)   = 2 (5) 1       =      .
                                                                                                                                              3           5

5.	     (5     points)  Let  TJ     be   the   total   length   of   time   of   Jon’s   commute   in   minutes.    The   PMF   of   Jon’s
     commute   is:                {        1
                                                         PTJ                             if  ℓ   ∈ {20,  21,  22,  23},
                                                                 (ℓ)  =          4 ,
                                                                               0,        otherwise.

6.	     (10     points)     Let  A  be  the   event   that   Jon   arrives   at   work   in   20   minutes   and   let B  be   the   event
     that   exactly   one   person   arrives   in   20   minutes.
                             P(A    |  B)     =          P(B) P(A    ∩ B)

                                                =     P({TJ                      P({TJ     =  20} ∩ {TS   ⁄      20})=
                                                                     =  20} ∩ {TS   ⁄      20}) + P({TJ=                       ⁄     =  20} ∩ {TS     =  20})
                                                =	                                                                                                                                       .P(TJ     =  20)P(TS   ⁄      20) =
                                                       P(TJ     =  20)P(TS   ⁄      20) + P(TJ=                   ⁄     =  20)P(TS     =  20)

## Original PDF page 3

                                 Massachusetts  Institute  of        Technology
                                 Department  of   Electrical  Engineering  &      Computer  Science
                                         6.041/6.431:             Probabilistic  Systems    Analysis
                                                         (Quiz 1 Solutions | Fall 2010)

     Jon   arrives    at    work    in   20    minutes    (or TJ      =   20)    if   he   does    not   have    to    wait    for    the   train    at    the
     station  (or  X       =  0).    The   probability   of   this   event   occurring   is:
                                                                 P(TJ                                 =  0)   =     .1
                                                                             =  20)   = P(X                      4

     Stephen   arrives   at   work  in  20   minutes  if  he   encounters  2   red  lights.    The  probability   of   this   event  is
     a   binomial   probability:              (	 )(   )2
                                                                                          5           1               2 )3  (
                                                              P(TS     =  20)   =	                                               .2           3               3

     Thus,
                                                                                        (	          )() (      ( 2
                                                                                     1                          5         11 − )2 )3
                                         P(A    |  B)     =         1 (	          )4                          2         3             3    (        ) .
                                                                         (5)( 11 −                                       + )2  ( 2 )3               3  (5)( 1 )2  ( 2 )3
                                                                    4                          2         3             3                         4          2         3              3

7.	     (10     points)     The   probability   of    interest   is P(TS    ≤  TJ   ).     This   can   be   calculated    using   the   total
     probability   theorem   by   conditioning   on   the   length   of   Jon’s   commute   or   Jon’s   wait   at   the   station.    If
     Jon’s   commute  is  20   minutes  (or X       =   0),   then   Stephen   can   encounter   up   to   2   red   lights   to   satisfy
     TS   ≤ TJ   .    Similarly   if  Jon’s   commute  is  21   minutes  (or X       =  1),   Stephen   can   encounter   up   to   3   red
     lights   and   so   on.
                                                                             ∑3
                                              P(TS   ≤ TJ   )      =             P(TS   ≤ TJ   |  X       =  x)   P(X       =  x)
                                                                             x=0
                                                                             1   ∑∑ 3        2+x ( )(              5           1               2    )k  ( )5−k
                                                                      =      4                         k             3              3
                                                                                x=0    k=0
                                                                      =      0.9352.

     An  alternative  approach  follows.    We   ﬁrst  compute  the  joint  PMF   of   the  commute  times  of  Stephen
     and   Jon PTS    ,TJ   (k,  ℓ).    Because   of   independence, PTS    ,TJ   (k,  ℓ)  =    PTS   (k)PTJ   (ℓ).
     Therefore,

           P(TS   ≤ TJ   )     =     P(TS     =  18) + P(TS     =  19) + P(TS     =  20) + P({TS     =  21} ∩ {TJ   ≥ 21})
                                          (	  )5+ P({TS     =  22} ∩ {TJ   )1      ≥ 22}) + P({TS   )2     =  23} ∩ {TJ     =  23})    )3
                                              2                    5           1              2                    5           1              2                    5           1              2                  3    ( )(  ( )4   ( )(  ( )3   ( )(  ( )2  ( )
                                   =                       +	                                                +                                                +                            · 3                    1           3              3                    2           3              3                    3           3              3              4
                                                (	 )(5           1              2                 2                   1                 1    )4  ( )1  ( )   ( )5  ( )
                                            +	                            ·               +           · 4           3              3                 4                   3                 4

                                   =      0.9352.

8.     (10     points)    We   express   the   conditional   probability   as   such:

                                                P(X       =  3 |  TS                    P({X  =  3} ∩ {TS   ≤ TJ  })
                                                                        ≤ TJ   )  =	                                                                     .P(TS   ≤ TJ   )

## Original PDF page 4

                             Massachusetts  Institute  of        Technology
                            Department  of   Electrical  Engineering  &      Computer  Science
                                   6.041/6.431:             Probabilistic  Systems    Analysis
                                                 (Quiz 1 Solutions | Fall 2010)

    If   Jon   waited   3   minutes   at   the   train,   his   commute   was   23   minutes   and   Stephen’s   commute   takes
    at   most   as   long   as   Jon’s   commute   since   the   longest   possible   commute   for   Stephen   is   23   minutes.
    Therefore,   the   numerator   in   the   previous   expression   is   equal   to P(X       =  3)   =  14   .   The   denominator
    was   computed   in   the   previous   part.
                                     P(X       =  3 |  TS                                       1
                                                           ≤ TJ   )     =            3∑∑        2+x (	             5           1               2 	 )(   )k  ( )5−k


                                                                            x=0    k=0    k             3              3
                                                                      =      0.2673.

Problem       2.
1.     (10     points)    Always  True.  We   need   to   show   that

                                                          P(A ∩ Bc)  =  P(A)P(Bc).

    We   start   with   expressing P(A)  as  P(A    ∩ B) + P(A    ∩ Bc).    Therefore,

                                                   P(A    ∩ Bc)      =     P(A) − P(A    ∩ B)
                                                                      =     P(A) − P(A)P(B)
                                                                      =     P(A)(1 − P(B))
                                                                      =     P(A)P(Bc),
    which   shows   that A      and  Bc    are   independent.

2.	     (10     points)    Not    Always    True.  Using   the   diagram   below,   let C      =  A   ∩ B      and   let P(A)  >     P(C)
    and   let  P(B)  >     P(C).    The   conditional   probability P(A    ∩ B    |  C)  =  1.    Furthermore,  P(A    |  C)  =  1
    and   P(B     |  C)    =    1.      Since   P(A    ∩ B     |  C)   =   P(A     |  C)P(B     |  C),   A       and   B       are    conditionally
    independent  given   a  third   event C.    Given C c  ,  A      and  B      are   disjoint   which   means   that A and  B  are
    not   independent.













    The  following  is  an  alternative   counterexample.    Imagine  having  3   coins  with   the  following  probabil­
    ity   of   heads: p    =  1/5,  p    =  1/3   and p    =  2/3,   respectively.    Each   coin   has   equal   probability   of   being
    selected.    Let C      be   the   event   that   you   select   the   coin   with p    =  1/5.    Let C c    be   the   event   that   you
    choose   one   of   the   other   two   coins.    Let A      be  the   event  that  the   ﬁrst  coin  toss   results  in  heads.    Let B
    be  the   event  that  the   second   coin  toss   results  in  heads.    For   a  given   coin,  the  tosses   are  independent
    such   that:
                                                          P(B    |  A    ∩ C)  =  P(B    |  C).

## Original PDF page 5

                           Massachusetts  Institute  of        Technology
                           Department  of   Electrical  Engineering  &      Computer  Science
                                 6.041/6.431:             Probabilistic    Systems    Analysis
                                               (Quiz 1 Solutions | Fall 2010)

    Given  C c  ,  A      and  B       are   not   independent   since   we   can   have   either   the p =  1/3   coin   or   the p    =  2/3
    coin.    Knowing  A  changes   our   beliefs   of   the   result   of   the   second   coin   toss.
                                               P(B    |  A    ∩ C c)     =            AB    ∩ A    ∩ C c
                                                                               (        )   ∩ C c(
    ()2
                                                                             1     1      )2+ 2
                                                                             3     3(        3 )
                                                                       =
                    11+   2
                                                                                  3   3     3
                                                                       =          .5
                                                                             9
    However,

                                                      P(B    |  C c)     =      P(B    ∩ C c)
                                                                                (
   )P(C c)
                                                                              1   1 +
  2
                                                                        =     3   3     3
                                                                                    2
                                                                                    3
                                                                        =          .1
                                                                              2
    As   shown, P(B    |  A   ∩ C c) ⁄      P(B=     |  C c).

3.   (10     points)    Always  True.   Using   independence   of X  and  Y ,   var(X  +  Y )   =   var(X)  +  var(Y    ).
    Since   variance   is   always   non-negative,   var(X) + var(Y    ) ≥ var(X).

## Original PDF page 6

MIT OpenCourseWare
http://ocw.mit.edu



6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013




For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms                                                                                                                .
# Anonymous response
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
Image attachment order: first 12 exam pages in order, then 6 official-solution pages in order. The two documents have independent page numbering.
