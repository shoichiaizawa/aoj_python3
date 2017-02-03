#!usr/bin/env python3

def string_two_numbers_spliter():
    x, y = [int(i) for i in input('Enter two numbers concatenated ' +
    'by a single space between them, e.g. \'1 2\': ').split()]
    return x, y


def swap_two_numbers_asc(x, y):
    x, y = y, x
    return x, y


def main():
    while True:
        x, y = string_two_numbers_spliter()
        if x == 0 and y == 0:
            break
        if x > y:
            x, y = swap_two_numbers_asc(x, y)
        print('%d %d' % (x, y))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Repetitive Processing - Swapping Two Numbers?):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_C

# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.

# NOTE Web pages inspired me to sove this question:
# Is there a standardized method to swap two variables in Python?:
# http://stackoverflow.com/q/14836228/1334728
