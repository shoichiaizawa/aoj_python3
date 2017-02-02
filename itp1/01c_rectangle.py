#!usr/bin/env python3

def string_two_numbers_spliter():
    a, b = [int(i) for i in input('Enter two numbers concatenated ' +
    'by a single space between them, e.g. \'3 5\': ').split()]
    return a, b


def main():
    a, b = string_two_numbers_spliter()
    print(str(a*b) + ' ' + str((a+b) * 2))


if __name__ == '__main__':
    main()


# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.
