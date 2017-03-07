#!/usr/bin/env python3

import sys


def string_to_list_spliter():
    h, w = [int(i) for i in sys.stdin.readline().split()]
    return h, w


def generate_ractangle(h, w):
    rect = ''
    for i in range(h):
        for j in range(w):
            rect += '#'
        rect += '\n'
    return rect


def main():
    while True:
        h, w = string_to_list_spliter()
        if h == 0 and w == 0:
            break
        print(generate_ractangle(h, w))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Structured Program I - Print a Rectangle):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_A
