Solve the attached probability exam. Give a complete answer to every distinct subpart, including requested proofs and intermediate reasoning. Repeated question/answer pages count once. Preserve original part labels. You may use your mathematical prior knowledge and the exam's own formula summary equally in every condition. You have no tools, outside sources, web search, previous sessions or official solutions. Page images are authoritative if extracted text is damaged. If information is unreadable, say so rather than invent it. Limit your response to 8000 words. At the end list any uncertain answers. Do not infer a grading key from source filenames.

# Exam text (all pages; images also attached)
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