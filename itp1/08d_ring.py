#!usr/bin/env python3

import sys
import re


def main():
    s = sys.stdin.readline()  # haystack
    p = sys.stdin.readline()  # needle

    s = s.strip('\n') * 2
    p = p.strip('\n')

    if len(re.findall((p), s)) > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()


# NOTE: AOJ question URL (Character - Ring):
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_D

# NOTE: Inspiration resources:
# - string count with overlapping occurrences:
#   http://stackoverflow.com/q/2970520/1334728
