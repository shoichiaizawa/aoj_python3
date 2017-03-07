#!/usr/bin/env python3

import sys
import operator
from math import floor


def string_to_list_spliter():
    lst = [i for i in sys.stdin.readline().split()]
    return lst


def main():
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    # TODO Refactor: include the ugly code below into the function above.
    while True:
        lst = string_to_list_spliter()
        if lst[1] == '?':
            break
        elif lst[1] == '+':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '-':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '*':
            print(ops[lst[1]](int(lst[0]), int(lst[2])))
        elif lst[1] == '/':
            print(floor(ops[lst[1]](int(lst[0]), int(lst[2]))))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Computation - Simple Calculator):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_C

# NOTE Web pages inspired me to sove this question:
# - Python 3 documentation:
#   https://docs.python.org/3.6/library/operator.html
# - Python:: Turn string into operator:
#   http://stackoverflow.com/q/1740726/1334728
# - Math operations from string [duplicate]:
#   http://stackoverflow.com/q/9685946/1334728

# NOTE Web pages below might be helpful to refactor the code:
# - How to compare type of an object in Python?:
#   http://stackoverflow.com/q/707674/1334728
# - if else in a list comprehension:
#   http://stackoverflow.com/q/4406389/1334728
