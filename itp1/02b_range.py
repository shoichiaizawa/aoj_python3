#!/usr/bin/env python3

def string_three_numbers_spliter():
    a, b, c = [int(i) for i in input().split()]
    return a, b, c


def main():
    a, b, c = string_three_numbers_spliter()

    if a < b and a < c:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

