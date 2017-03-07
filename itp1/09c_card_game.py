#!/usr/bin/env python3

import sys


def main():
    n = int(sys.stdin.readline().strip('\n'))
    taro_score = 0
    hanako_score = 0

    for turn in range(n):
        animals = [animal for animal in
                   sys.stdin.readline().strip('\n').split(' ')]
        if animals[0] == animals[1]:
            taro_score += 1
            hanako_score += 1
        elif max(animals[0], animals[1]) == animals[0]:
            taro_score += 3
        elif max(animals[0], animals[1]) == animals[1]:
            hanako_score += 3

    print('%d %d' % (taro_score, hanako_score))


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (String - Card Game):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_C
