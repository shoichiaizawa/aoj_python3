#!usr/bin/env python3

import sys


def string_to_list_spliter():
    h, w = [int(i) for i in sys.stdin.readline().split()]
    return h, w


def generate_crossboard(h, w):
    crossboard = ''
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                if j % 2 == 0:
                    crossboard += '#'
                else:
                    crossboard += '.'
            else:
                if j % 2 == 0:
                    crossboard += '.'
                else:
                    crossboard += '#'
        crossboard += '\n'
    return crossboard


def print_crossboard():
    while True:
        h, w = string_to_list_spliter()
        if h == 0 and w == 0:
            break
        print(generate_crossboard(h, w))


def main():
    print_crossboard()


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Structured Program I - Print a Crossboard):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_C
