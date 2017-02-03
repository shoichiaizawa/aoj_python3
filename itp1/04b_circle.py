#!usr/bin/env python3

import sys
from math import pi


def area_of_circle(radius):
    return pi * radius**2


def circumference_of_circle(radius):
    return 2*pi*radius


def main():
    # NOTE
    r = float(sys.stdin.readline())
    print('%f %f' % (area_of_circle(r), circumference_of_circle(r)))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Computation - Circle):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_B

# NOTE Web pages inspired me to sove this question:
# - Python 3 documentation:
#   https://docs.python.org/3/library/math.html#math.pi
# - How do you read from stdin in Python?:
#   http://stackoverflow.com/q/1450393/1334728
