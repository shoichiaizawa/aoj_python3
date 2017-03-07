#!/usr/bin/env python3

def string_two_numbers_spliter():
    a, b = [int(i) for i in input().split()]
    return a, b


def main():
    a, b = string_two_numbers_spliter()

    if a < b:
        print('a < b')
    elif a > b:
        print('a > b')
    else:
        print('a == b')


if __name__ == '__main__':
    main()

