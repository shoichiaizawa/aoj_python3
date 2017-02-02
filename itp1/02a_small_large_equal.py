#!usr/bin/env python3

def string_two_numbers_spliter():
    a, b = [int(i) for i in input('Enter two numbers concatenated ' +
    'by a single space between them, e.g. \'1 2\': ').split()]
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


# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.
