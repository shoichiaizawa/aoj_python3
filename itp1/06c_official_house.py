#!usr/bin/env python3

import sys
import copy


def main():
    n = int(sys.stdin.readline())
    separator = '####################'

    room, floor = 10, 3;
    building1 = [[0 for col in range(room)] for row in range(floor)]
    building2 = copy.deepcopy(building1)
    building3 = copy.deepcopy(building1)
    building4 = copy.deepcopy(building1)

    buildings = {1 : building1,
                 2 : building2,
                 3 : building3,
                 4 : building4
    }

    for i in range(n):
        lst = [int(num) for num in sys.stdin.readline().split()]
        buildings[lst[0]][lst[1]-1][lst[2]-1] += lst[3]

    for idx, (key, value) in enumerate(buildings.items()):
        for floor in value:
            print(' %s %s %s %s %s %s %s %s %s %s' % tuple(floor))
        if idx < 3:
            print(separator)


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Array - Official House):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C
