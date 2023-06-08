#!/usr/bin/python3
#2-args.py

if __name__ == "__main__":
    from sys import argv
    res = ""
    total = len(argv) - 1
    delim = 's:' if total > 1 else '.' if total == 0 else ':'
    for count, arg in enumerate(argv[1:]):
        res += '{:d}: {}\n'.format(count+1, arg)
        print('{:d} argument{}\n{}'.format(total, delim, res), end="")
