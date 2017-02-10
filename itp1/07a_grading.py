#!usr/bin/env python3

import sys


def main():
    while True:
        m, f, r = [int(score) for score in sys.stdin.readline().split()]

        if m == f == r == -1:
            break
        if m == -1 or f == -1 or m+f < 30:
            print('F')
        elif m+f >= 80:
            print('A')
        elif 80 > m+f >= 65:
            print('B')
        elif 65 > m+f >= 50:
            print('C')
        elif 50 > m+f >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structured Program II - Grading):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_A

# NOTE: Inspiration resources:
# - How to read a file line-by-line into a list?:
#   http://stackoverflow.com/q/3277503/1334728
