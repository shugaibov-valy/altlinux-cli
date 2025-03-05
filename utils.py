import json

from msgspec import to_builtins
from msgspec.json import decode

import consts
from essence import Package, StructJsonFile

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


def compare_version_release(pkg1: Package, pkg2: Package) -> int:
    """
    Сравнивает version-release двух пакетов.
    Возвращает:
    - 1, если pkg1 > pkg2
    - -1, если pkg1 < pkg2
    - 0, если pkg1 == pkg2
    """
    if pkg1.version > pkg2.version:
        return 1
    elif pkg1.version < pkg2.version:
        return -1
    else:
        if pkg1.release > pkg2.release:
            return 1
        elif pkg1.release < pkg2.release:
            return -1
        else:
            return 0


def find_newer_packages(sisyphus: set[Package], p10: set[Package]) -> set[Package]:
    p10_by_name = {pkg.name: pkg for pkg in p10}

    def is_newer(sisyphus_pkg):
        if sisyphus_pkg.name in p10_by_name:
            p10_pkg = p10_by_name[sisyphus_pkg.name]
            return compare_version_release(sisyphus_pkg, p10_pkg) > 0
        return False

    newer_packages = set(filter(is_newer, sisyphus))
    return newer_packages
