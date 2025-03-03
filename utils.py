from msgspec.json import decode

import consts
from essence import StructJsonFile


def read_json_packages():
    with open(consts.P10_FILE_PATH, "rb") as f:
        p10_packages = decode(f.read(), type=StructJsonFile).packages

    with open(consts.SISYPHUS_FILE_PATH, "rb") as f:
        sisyphus_packages = decode(f.read(), type=StructJsonFile).packages

    return set(p10_packages), set(sisyphus_packages)
