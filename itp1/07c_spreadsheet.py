#!usr/bin/env python3

import sys


def generate_default_spreadsheet():
    r, c = [int(row_col) for row_col in sys.stdin.readline().split()]
    sheet = [
                [int(row_num) for row_num in sys.stdin.readline().split()]
                for row in range(r)
            ]
    return c, sheet


def generate_spreadsheet_with_sums():
    orig_total_col, sheet_with_sums = generate_default_spreadsheet()

    sheet_with_sums.append([0 for col in range(orig_total_col)])

    for row in range(len(sheet_with_sums)-1):
        for col in range(len(sheet_with_sums[0])):
            sheet_with_sums[-1][col] += sheet_with_sums[row][col]

    for row in sheet_with_sums:
        row.append(sum(row))

    return sheet_with_sums


def print_summed_spreadsheet():
    sheet_with_sums = generate_spreadsheet_with_sums()
    [print(*row) for row in sheet_with_sums]


def main():
    print_summed_spreadsheet()


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Structured Program II - Spreadsheet):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_C
