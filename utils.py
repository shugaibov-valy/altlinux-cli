import json

from msgspec import to_builtins
from msgspec.json import decode

import consts
from essence import StructJsonFile

"""Reading json from downloaded files and conversion in set"""


def read_json_packages():
    with open(consts.P10_FILE_PATH, "rb") as f:
        p10_packages = decode(f.read(), type=StructJsonFile).packages

    with open(consts.SISYPHUS_FILE_PATH, "rb") as f:
        sisyphus_packages = decode(f.read(), type=StructJsonFile).packages

    return set(p10_packages), set(sisyphus_packages)


def save_json_packages_in_file(packages: set):
    with open(consts.OUTPUT_FILE_PATH, "w") as f:
        json_objects = json.loads(json.dumps(to_builtins(packages)))
        json.dump(json_objects, f, indent=4)
