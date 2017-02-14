#!usr/bin/env python3

import sys


def main():
    while True:
        # 標準入力のライン末の改行コードを取り除く
        cards = sys.stdin.readline().strip('\n')
        if cards == '-':
            break
        for shuffle in range(int(sys.stdin.readline().strip('\n'))):
            h = int(sys.stdin.readline().strip('\n'))
            cards = cards[h:] + cards[:h]
        print(cards)


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (String - Shuffle):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_B
