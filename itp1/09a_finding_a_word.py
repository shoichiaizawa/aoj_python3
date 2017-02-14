#!usr/bin/env python3

import sys


def main():
    w = sys.stdin.readline().lower().strip('\n')
    s = 0

    for line in sys.stdin:
        if line == 'END_OF_TEXT':
            break
        s += line.lower().split().count(w)

    print(s)


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (String - Finding a Word):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_A
