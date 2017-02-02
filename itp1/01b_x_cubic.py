#!usr/bin/env python3

def cubic(x):
    return x ** 3


def main():
    x = int(input('Enter a number to be cubed: '))
    print(cubic(x))


if __name__ == '__main__':
    main()


# NOTE input() needs to be without a string parameter for the AOJ judge
#
# The solution above works fine in the local development environment but
# not in the AOJ judge, as the question itself only limit the output string to
# the cubted input number.
# In order to make the above code work,
# the built-in input() function must be without a string parameter;
# i.e. Replace Line 7 by `x = int(input())` for a successful submission.
