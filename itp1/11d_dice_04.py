#!/usr/bin/env python3

import sys


class Die:
    def __init__(self, pips):
        self.pips = pips

    def move_die(self, direction):
        if direction == 'N':
            tmp = self.pips[0]
            self.pips[0] = self.pips[1]
            self.pips[1] = self.pips[5]
            self.pips[5] = self.pips[4]
            self.pips[4] = tmp
            del tmp
        elif direction == 'S':
            tmp = self.pips[0]
            self.pips[0] = self.pips[4]
            self.pips[4] = self.pips[5]
            self.pips[5] = self.pips[1]
            self.pips[1] = tmp
            del tmp
        elif direction == 'E':
            tmp = self.pips[0]
            self.pips[0] = self.pips[3]
            self.pips[3] = self.pips[5]
            self.pips[5] = self.pips[2]
            self.pips[2] = tmp
            del tmp
        elif direction == 'W':
            tmp = self.pips[0]
            self.pips[0] = self.pips[2]
            self.pips[2] = self.pips[5]
            self.pips[5] = self.pips[3]
            self.pips[3] = tmp
            del tmp

    def spin_die_clockwise(self):
        tmp = self.pips[1]
        self.pips[1] = self.pips[2]
        self.pips[2] = self.pips[4]
        self.pips[4] = self.pips[3]
        self.pips[3] = tmp
        del tmp


def init_die():
    pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]
    die = Die(pips)

    return die


def roll_die(die):
    directions = list(sys.stdin.readline().strip('\n'))

    for direction in directions:
        die.move_die(direction)

    return die


def question_rightside(die):
    q = int(sys.stdin.readline().strip('\n'))
    rightsides = []

    for question in range(q):
        q_pips = [int(pip) for pip in sys.stdin.readline().strip('\n').split()]

        if q_pips[0] == die.pips[1]:
            die.move_die('N')
        elif q_pips[0] == die.pips[2]:
            die.move_die('W')
        elif q_pips[0] == die.pips[3]:
            die.move_die('E')
        elif q_pips[0] == die.pips[4]:
            die.move_die('S')
        elif q_pips[0] == die.pips[5]:
            die.move_die('N')
            die.move_die('N')

        while die.pips[1] != q_pips[1]:
            die.spin_die_clockwise()

        rightsides.append(die.pips[2])

    return rightsides


def are_identical(die1, die2):
    if sorted(die1.pips) != sorted(die2.pips):
        return 'No'
    else:
        for idx, pip in enumerate(die2.pips):
            for spin in range(4):
                if die1.pips == die2.pips:
                    return 'Yes'
                else:
                    die1.spin_die_clockwise()
            if idx in {0, 1, 2}:
                die1.move_die('N')
            if idx in {3}:
                die1.move_die('N')
                die1.move_die('E')
            if idx in {4}:
                die1.move_die('E')
                die1.move_die('E')

        return 'No'


def check_all_dice_not_identical():
    n = int(sys.stdin.readline().strip('\n'))
    dice = [init_die() for _ in range(n)]

    not_identical_count = 0

    if len(dice) != 2:
        num_of_all_not_identical = len(dice) * (len(dice)-1)
    else:
        num_of_all_not_identical = 2

    for idx_base, die_base in enumerate(dice):
        for idx_compared, die_compared in enumerate(dice):
            if idx_base != idx_compared:
                if are_identical(die_base, die_compared) == 'No':
                    not_identical_count += 1

    if not_identical_count != num_of_all_not_identical:
        return 'No'
    else:
        return 'Yes'


def main():
    print(check_all_dice_not_identical())


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structure and Class - Dice III):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_C

# NOTE: Inspiration resources:
# - How to create multiple class objects with a loop in python?:
#   http://stackoverflow.com/q/21598872/1334728
