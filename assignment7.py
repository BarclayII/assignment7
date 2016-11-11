
import sys
from interval import *


if __name__ == '__main__':
    while True:
        try:
            interval_list = input('List of intervals (comma separated)?')
        except EOFError:
            sys.exit(0)

        try:
            comma_sep = interval_list.split(',')
            if len(comma_sep) % 2 != 0:
                raise ValueError('invalid list')
            iv_list = [','.join(comma_sep[i:i+2])
                    for i in range(0, len(comma_sep), 2)]
            iv_list = [interval.fromString(i) for i in iv_list]
            break
        except ValueError as e:
            print(str(e))

    while True:
        try:
            cmd = input('Interval?')
            if cmd.lower() == 'quit':
                break
            i = interval.fromString(cmd)
            iv_list = insert(iv_list, i)
            print(', '.join([str(i) for i in iv_list]))
        except ValueError as e:
            print(str(e))
        except EOFError:
            break