import sys
import argparse
import json


def process_stdin():
   return sys.stdin.read()

def do_something(data):
    data["update"]["event"]
    transient = data["state"]["transient"]
    persistent = data["state"]["persistent"]
    transient.update({"script2": {"cityofsanamteo/law": "this is transient"}})
    persistent.update({"script2": {"cityofsanamteo/law": "this is persistent"}})
    return {
        "transient": transient,
        "persistent": persistent
    }


if __name__ == '__main__':
    data = process_stdin()
    data = json.loads(data)
    print(json.dumps(do_something(data)))