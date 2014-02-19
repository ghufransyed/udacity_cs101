# Spreading Udaciousness

# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to
# the model) of their friends to take the course next offering. This will
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, hexes_to_udaciousness(n, spread,
# target), that takes three inputs: the starting number of Udacians, the spread
# rate (how many new friends each Udacian convinces to join each hexamester),
# and the target number, and outputs the number of hexamesters needed to reach
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math.


def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return (1 +
                (hexes_to_udaciousness
                 (n * (spread + 1), spread, target)))
