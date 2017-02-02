#!usr/bin/env python3

def seconds_to_hms_format(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return "%d:%d:%d" % (h, m, s)


def main():
    seconds = input('Enter a large number (assume it\'s the second) to be ' +
    'convered into time in "h:m:s" format: ')
    print(seconds_to_hms_format(seconds))


if __name__ == '__main__':
    main()


# NOTE input() needs to be without a string parameter for the AOJ judge;
# see the NOTE_section in 0101b_x_cubic.py for a detailed explanation.
