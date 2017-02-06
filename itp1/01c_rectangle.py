#!usr/bin/env python3

def string_two_numbers_spliter():
    a, b = [int(i) for i in input().split()]
    return a, b


def main():
    a, b = string_two_numbers_spliter()
    print(str(a*b) + ' ' + str((a+b) * 2))


if __name__ == '__main__':
    main()

