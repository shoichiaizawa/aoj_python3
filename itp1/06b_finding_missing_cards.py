#!/usr/bin/env python3

import sys


def init_card_deck():
    """カードデッキを生成
    S: spades
    H: hearts
    C: clubs
    D: diamonds

    Returns:
        辞書型の値
            カードの絵柄を表すstring型のS,H,C,Dの4つのキーを持ち、
            それぞれのキーがカードランクを表すリスト型のデータの値を持つ。
            リスト型のカードデータはstringとしてもつ。
    """
    card_deck = {'S': [], 'H': [], 'C': [], 'D': []}
    n = int(sys.stdin.readline())

    for i in range(n):
        lst = [card for card in sys.stdin.readline().split()]
        card_deck[lst[0]].append(lst[1])

    return card_deck


def print_missing_cards(card_deck):
    """カードデッキに存在しないカードを表示

    カードデッキに存在しないカードをスペード、ハート、クラブ、ダイヤの順番で
    数字を昇順に表示する。
    例：
        S 1
        H 3
        H 7
        C 12
        D 8
    """
    card_symbols = ['S', 'H', 'C', 'D']

    for i in card_symbols:
        for card in range(1, 14):
            if not str(card) in card_deck[i]:
                print(i, card)


def main():
    print_missing_cards(init_card_deck())


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Array - Finding Missing Cards):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_B

# NOTE: Inspiration resources:
# - Python dictionary: Get list of values for list of keys:
#   http://stackoverflow.com/q/18453566/1334728
# - Fastest way to check if a value exist in a list:
#   http://stackoverflow.com/q/7571635/1334728
