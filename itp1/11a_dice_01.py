#!usr/bin/env python3

import sys


class Die:
    def __init__(self, pips):
        self.pips = pips

    def move_die(self, direction):
        tmp = int()
        if direction == 'N':
            tmp = self.pips[0]
            self.pips[0] = self.pips[1]
            self.pips[1] = self.pips[5]
            self.pips[5] = self.pips[4]
            self.pips[4] = tmp
        elif direction == 'S':
            tmp = self.pips[0]
            self.pips[0] = self.pips[4]
            self.pips[4] = self.pips[5]
            self.pips[5] = self.pips[1]
            self.pips[1] = tmp
        elif direction == 'E':
            tmp = self.pips[0]
            self.pips[0] = self.pips[3]
            self.pips[3] = self.pips[5]
            self.pips[5] = self.pips[2]
            self.pips[2] = tmp
        elif direction == 'W':
            tmp = self.pips[0]
            self.pips[0] = self.pips[2]
            self.pips[2] = self.pips[5]
            self.pips[5] = self.pips[3]
            self.pips[3] = tmp

    def get_upside(self):
        return self.pips[0]


def init_die():
    pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]
    die = Die(pips)
    return die


def roll_die(die):
    directions = list(sys.stdin.readline().strip('\n'))

    for direction in directions:
        die.move_die(direction)

    return die


def main():
    die = init_die()
    die = roll_die(die)
    print(die.get_upside())


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structure and Class - Dice I):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A

# NOTE: Inspiration resources:
# - correct way to define class variables in Python [duplicate]:
#   http://stackoverflow.com/q/9056957/1334728
# - How to split a string into array of characters with Python?:
#   http://stackoverflow.com/q/4978787/1334728
