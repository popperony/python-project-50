import json
import yaml


def parse_file(path):
    with open(path) as file:
        content = file.read()
    if not content:
        raise ValueError('Empty file')
    last_dot_index = path.rfind('.')
    file_extension = path[last_dot_index + 1:]
    if file_extension == 'yml':
        file_extension = 'yaml'
    match file_extension:
        case 'json':
            return json.loads(content)
        case 'yaml':
            return yaml.safe_load(content)
        case _:
            raise NameError(f'file extension {file_extension} not supported')
