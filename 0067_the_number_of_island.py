#!usr/bin/env python3

import sys


def eliminate_ones(grid, row, col):
    if 0 <= row < 12 and 0 <= col < 12 and grid[row][col] == 1:
        grid[row][col] = 0
        eliminate_ones(grid, row+1, col)
        eliminate_ones(grid, row-1, col)
        eliminate_ones(grid, row, col+1)
        eliminate_ones(grid, row, col-1)


def main():
    while True:
        grid = [[int(num) for num in sys.stdin.readline().strip()]
                for _ in range(12)]

        num_of_islands = int()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    num_of_islands += 1
                    eliminate_ones(grid, row, col)

        print(num_of_islands)

        if not sys.stdin.readline():
            break


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (The Number of Island):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0067
