#!usr/bin/env python3

def string_three_numbers_spliter():
    a, b, c = [int(i) for i in input('Enter three numbers concatenated ' +
    'by a single space between them, e.g. \'1 3 8\': ').split()]
    return a, b, c


def main():
    a, b, c = string_three_numbers_spliter()

    if a < b and a < c:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()


# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.
