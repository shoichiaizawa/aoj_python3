#!/usr/bin/env python3

import sys


def generate_buidlings_with_residents(building, floor, room):
    buildings = {
        key: [[0 for col in range(room)] for row in range(floor)]
        for key in range(1, building+1)
    }

    n = int(sys.stdin.readline())
    for i in range(n):
        lst = [int(num) for num in sys.stdin.readline().split()]
        buildings[lst[0]][lst[1]-1][lst[2]-1] += lst[3]

    return buildings


def print_buildings_with_residents():
    separator = '####################'
    buildings_with_residents = generate_buidlings_with_residents(4, 3, 10)

    for idx, (key, value) in enumerate(buildings_with_residents.items()):
        for floor in value:
            print(' %s %s %s %s %s %s %s %s %s %s' % tuple(floor))
        if key < len(buildings_with_residents):
            print(separator)


def main():
    print_buildings_with_residents()


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Array - Official House):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C

# NOTE: Inspiration resources:
# - How to define two-dimensional array in python:
#   http://stackoverflow.com/q/6667201/1334728
# - How to clone or copy a list?:
#   http://stackoverflow.com/q/2612802/1334728
# - Replacements for switch statement in Python?:
#   http://stackoverflow.com/q/60208/1334728
# - What is the Python equivalent for a case/switch statement? [duplicate]:
#   http://stackoverflow.com/q/11479816/1334728
# - Iterating over dictionaries using for loops in Python:
#   http://stackoverflow.com/q/3294889/1334728
# - Python loop index of key, value for-loop when using items():
#   http://stackoverflow.com/q/25150502/1334728
# - Using Python String Formatting with Lists:
#   http://stackoverflow.com/q/7568627/1334728
# - Python Dictionary Comprehension:
#   http://stackoverflow.com/q/14507591/1334728
# - What is PEP8's E128: continuation line under-indented for visual indent?:
#   http://stackoverflow.com/q/15435811/1334728
# - Line continuation for list comprehensions or generator expressions in
#   python:
#   http://stackoverflow.com/q/5809059/1334728
