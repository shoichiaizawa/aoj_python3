#!usr/bin/env python3

import sys


def reverse_list():
    lst = [int(i) for i in sys.stdin.readline().split()]
    lst.reverse()
    return lst


def main():
    # XXX: 数列の長さNはどこにも使われず、AOJジャッジを通過
    n = sys.stdin.readline()
    print(*reverse_list())


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Array - Reversing Numbers):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_A
