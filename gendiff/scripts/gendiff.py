#!/usr/bin/env python3
from gendiff.cli import parse_args
from gendiff import generate_diff


def main():
    path1, path2, format_ = parse_args()
    print(generate_diff(path1, path2, format_))


if __name__ == '__main__':
    main()
