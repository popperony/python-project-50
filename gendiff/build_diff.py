def make_diff(data1, data2):
    keys = sorted(set(data1.keys() | data2.keys()))
    diffs = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1.keys():
            diffs.append({
                'key': key,
                'action_type': 'added',
                'value': value2
            })
        elif key not in data2.keys():
            diffs.append({
                'key': key,
                'action_type': 'removed',
                'value': value1
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diffs.append({
                'key': key,
                'action_type': 'children',
                'value': make_diff(value1, value2)
            })
        elif value1 == value2:
            diffs.append({
                'key': key,
                'action_type': 'not_changed',
                'value': value1
            })
        else:
            diffs.append({
                'key': key,
                'action_type': 'changed',
                'value': value1,
                'new_value': value2
            })
    return diffs
