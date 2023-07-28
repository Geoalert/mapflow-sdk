import json


def save_result(filename, result):
    with open(filename, "w") as dst:
        dst.write(json.dumps(result))