#!/usr/bin/env python3

import sys


def int_fetcher():
    num = int(sys.stdin.readline())
    return num


def call(num):
    res = ''
    for i in range(1, num+1):
        x = i
        if x % 3 == 0 or x % 10 == 3:
            res += ' ' + str(i)
            continue
        while x:
            if x % 10 == 3:
                res += ' ' + str(i)
                break
            x //= 10
    return res


def main():
    print(call(int_fetcher()))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Structured Program I - Structured Program I):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_D
