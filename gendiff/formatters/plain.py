from gendiff.formatters.make_str import make_str


def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    new_value = f"'{value}'" if isinstance(value, str) else value
    return make_str(new_value)


def format_plain(diffs):
    def iter_(tree, path):
        result = []
        for node in tree:
            key, action_type = node.get('key'), node.get('action_type')
            value, new_value = node.get('value'), node.get('new_value')
            value_str = stringify(value)
            new_value_str = stringify(new_value)
            new_path = key if path == '' else f'{path}.{key}'
            added = f"Property '{new_path}' was added with value: {value_str}"
            removed = f"Property '{new_path}' was removed"
            changed = f"Property '{new_path}' was updated. "\
                + f"From {value_str} to {new_value_str}"
            match action_type:
                case 'added':
                    result.append(added)
                case 'removed':
                    result.append(removed)
                case 'changed':
                    result.append(changed)
                case 'children':
                    result.append(iter_(value, new_path))
        return '\n'.join(result)
    return iter_(diffs, '')
