#!usr/bin/env python3

from math import floor


def string_two_numbers_spliter():
    a, b = [int(i) for i in input('Enter two numbers concatenated ' +
    'by a single space between them, e.g. \'3 2\': ').split()]
    return a, b


def main():
    a, b = string_two_numbers_spliter()
    print('%d %d %f' % (floor(a/b), a%b, a/b))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Computation - A/B Problem):
# http://judge.u-aizu.ac.jp/onlinejudge/topic.jsp?cid=ITP1#problems/ITP1_4

# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.
