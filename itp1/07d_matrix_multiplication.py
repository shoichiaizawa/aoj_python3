#!/usr/bin/env python3

import sys


def multiply_matrix_a_b():
    n, m, l = [int(i) for i in sys.stdin.readline().split()]
    matrix_a = [[0 for col in range(m)] for row in range(n)]
    matrix_b = [[0 for col in range(l)] for row in range(m)]
    matrix_res = [[0 for col in range(l)] for row in range(n)]

    for row in range(n):
        lst = [int(element) for element in sys.stdin.readline().split()]
        for col in range(m):
            matrix_a[row][col] += lst[col]

    for row in range(m):
        lst = [int(element) for element in sys.stdin.readline().split()]
        for col in range(l):
            matrix_b[row][col] += lst[col]

    for row_a in range(len(matrix_a)):
        for col_a in range(len(matrix_b[0])):
            for row_b in range(len(matrix_b)):
                matrix_res[row_a][col_a] += \
                        matrix_a[row_a][row_b] * matrix_b[row_b][col_a]

    return matrix_res


def main():
    [print(*row) for row in multiply_matrix_a_b()]


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structured Program II - Matrix Multiplication):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_D

# NOTE: Inspiration resources:
# - Python Program to Multiply Two Matrices:
#   https://www.programiz.com/python-programming/examples/multiply-matrix
