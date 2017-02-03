#!usr/bin/env python3

def string_three_numbers_spliter():
    a, b, c = [int(i) for i in input('Enter three numbers concatenated ' +
    'by a single space between them, e.g. \'5 14 80\' etc: ').split()]
    return a, b, c


def count_nums_of_factors_of_c_in_a_and_b(a, b, c):
    count = 0
    # XXX Refactor the algorithm below as it is exhaustive and inefficient.
    for i in range(1, c+1):
        if (c % i == 0):
            if i >= a and i <= b:
                count += 1
    return count


def main():
    a, b, c = string_two_numbers_spliter()
    print(count_nums_of_divisors_of_c_in_a_and_b(a, b, c))


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Repetitive Processing - How Many Divisors?):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_D

# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.

# NOTE The following web sites might be helpful to find factors of a number:
# - What is the most efficient way of finding all the factors of a number in
# Python?:
# http://stackoverflow.com/q/14836228/1334728
# - What is the best way to get all the divisors of a number?:
# http://stackoverflow.com/q/171765/1334728
