#!usr/bin/env python3

def string_three_numbers_spliter():
    a, b, c = [int(i) for i in input('Enter three numbers concatenated ' +
    'by a single space between them, e.g. \'3 8 1\': ').split()]
    return a, b, c


def main():
    a, b, c = string_three_numbers_spliter()
    lst = [a, b, c]
    lst.sort()
    print(' '.join(str(i) for i in lst))


if __name__ == '__main__':
    main()


# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.

# NOTE Stack Overflow pages inspired me to sove this question:
# - http://stackoverflow.com/questions/3426108/numeric-sort-in-python
# - How to convert list to string [duplicate]:
#   http://stackoverflow.com/a/5618893/1334728
