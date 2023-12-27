from gendiff.formatters.make_str import make_str


REPLACER = ' '
SPACES_COUNT = 4


def stringify(value, depth):
    if not isinstance(value, dict):
        return make_str(value)
    lines = ['{']
    for key in value.keys():
        current = value[key]
        format_key = f'{REPLACER * (depth + SPACES_COUNT * 2)}{key}: '
        if isinstance(current, dict):
            lines.append(format_key
                         + stringify(current, depth + SPACES_COUNT))
        else:
            lines.append(format_key + make_str(current))
    lines.append(f'{REPLACER * (depth + SPACES_COUNT) + "}"}')
    return '\n'.join(lines)


def format_stylish(diffs):
    def iter_(tree, depth):
        result = ['{']
        offset = depth + SPACES_COUNT
        for node in tree:
            key, action_type = node.get('key'), node.get('action_type')
            value, new_value = node.get('value'), node.get('new_value')
            value_str = stringify(value, depth)
            new_value_str = stringify(new_value, depth)
            spaces = REPLACER * (offset - 2)
            added = f'{spaces}+ {key}: {value_str}'
            removed = f'{spaces}- {key}: {value_str}'
            not_changed = f'{spaces}  {key}: {value_str}'
            changed = f'{spaces}+ {key}: {new_value_str}'
            match action_type:
                case 'added':
                    result.append(added)
                case 'removed':
                    result.append(removed)
                case 'not_changed':
                    result.append(not_changed)
                case 'changed':
                    result.append(removed)
                    result.append(changed)
                case 'children':
                    result.append(f'{REPLACER * offset}{key}: '
                                  + iter_(value, offset))
        result.append(f'{REPLACER * depth + "}"}')
        return '\n'.join(result)
    return iter_(diffs, 0)
