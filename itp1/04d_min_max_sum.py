#!/usr/bin/env python3

import sys


def string_to_list_spliter():
    lst = [int(i) for i in sys.stdin.readline().split()]
    return lst


def main():
    # XXX: N個の整数がどこにも使われず、AOJジャッジを通過
    n = sys.stdin.readline()
    lst = string_to_list_spliter()
    print(min(lst), max(lst), sum(lst))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Computation - Min, Max and Sum):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_4_D
