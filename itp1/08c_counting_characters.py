#!/usr/bin/env python3

import sys


def main():
    text = str()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for line in sys.stdin:
        text += line.lower()

    for alphabet in alphabets:
        print('%s : %d' % (alphabet, text.count(alphabet)))


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Character - Counting Characters):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_C
