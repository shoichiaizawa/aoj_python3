#!usr/bin/env python3


def main():
    while True:
        numbers = input()
        if int(numbers) == 0:
            break
        res = 0
        for i in numbers:
            res += int(i)
        print(res)


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Character - Sum of Numbers):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_B
