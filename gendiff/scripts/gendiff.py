#!/usr/bin/env python3
from gendiff.utils.argparser import parse_args
from gendiff import generate_diff


def main():
    path1, path2, format = parse_args()
    print(generate_diff(path1, path2, format))


if __name__ == '__main__':
    main()
