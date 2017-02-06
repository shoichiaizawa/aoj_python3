#!usr/bin/env python3

import sys


def string_to_list_spliter():
    h, w = [int(i) for i in sys.stdin.readline().split()]
    return h, w


def generate_frame(h, w):
    frame = ''
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1:
                frame += '#'
            else:
                if j == 0 or j == w-1:
                    frame += '#'
                else:
                    frame += '.'
        frame += '\n'
    return frame


def print_frame():
    while True:
        h, w = string_to_list_spliter()
        if h == 0 and w == 0:
            break
        print(generate_frame(h, w))


def main():
    print_frame()


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Structured Program I - Print a Frame):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_5_B
