#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    len_argv = len(argv) - 1

    if len_argv > 1:
        print(len_argv, 'arguments:')
        for i in range(1, len_argv + 1):
            print('{:d}: {}'.format(i, argv[i]))
    elif len_argv == 1:
        print(len_argv, 'argument:')
        for i in range(1, len_argv + 1):
            print('{:d}: {}'.format(i, argv[i]))
    elif len_argv == 0:
        print(len_argv, 'arguments.')
