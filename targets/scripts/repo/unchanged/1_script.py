import argparse
import json


def do_something(data):
    print(data["changed"])
    print(data["event"])
    return {
        "transient": "hello from transient",
        "persistent": "hello from persistent"
    }


parser = argparse.ArgumentParser()
parser.add_argument('--data')
if __name__ == '__main__':
    args = parser.parse_args()
    data = json.loads(args.data)
    data = json.loads(data)
    print(json.dumps(do_something(data)))