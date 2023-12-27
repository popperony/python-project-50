from gendiff.parser import parse_file
from gendiff.build_diff import make_diff
from gendiff.formatters.format_router import formatter


def generate_diff(path1, path2, format_='stylish'):
    data1 = parse_file(path1)
    data2 = parse_file(path2)
    diffs = make_diff(data1, data2)
    return formatter(diffs, format_)
