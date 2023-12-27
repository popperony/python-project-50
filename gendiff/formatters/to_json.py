import json


def format_json(diffs):
    return json.dumps(diffs, indent=4)
