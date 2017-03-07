#!/usr/bin/env python3

def main():
    count = 1
    while True:
        x = int(input())
        if x == 0:
            break
        print('Case %d: %d' % (count, x))
        count += 1


if __name__ == '__main__':
    main()


# NOTE AOJ question URL (Repetitive Processing - Print Test Cases):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_3_B

# NOTE Stack Overflow pages inspired me to sove this question:
# - Emulate a do-while loop in Python?:
#   http://stackoverflow.com/a/743186/1334728
# - String comparison in Python: is vs. == [duplicate]:
#   http://stackoverflow.com/a/2988117/1334728
# - Behaviour of increment and decrement operators in Python:
#   http://stackoverflow.com/q/1485841/1334728
# - Python integer incrementing with ++ [duplicate]:
#   http://stackoverflow.com/q/2632677/1334728
