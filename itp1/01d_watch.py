#!/usr/bin/env python3

def seconds_to_hms_format(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%d:%d:%d" % (h, m, s)


def main():
    seconds = input()
    print(seconds_to_hms_format(seconds))


if __name__ == '__main__':
    main()

