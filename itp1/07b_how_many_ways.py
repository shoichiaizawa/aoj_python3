#!/usr/local/env python3

import sys


def main():
    while True:
        count = 0
        n, r = map(int, sys.stdin.readline().split())
        if n == r == 0:
            break
        for n1 in range(1, n-1):
            for n2 in range(n1+1, n):
                for n3 in range(n2+1, n+1):
                    if n1 + n2 + n3 == r:
                        count += 1
        print(count)


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structured Program II - How many ways?):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B

# NOTE: Inspiration resources:
# - Finding all possible combinations of numbers to reach a given sum
#   http://stackoverflow.com/q/4632322/1334728
# - Subset sum problem -- Wikipedia:
#   https://en.wikipedia.org/wiki/Subset_sum_problem
