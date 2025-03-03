import msgspec

"""msgspec library class for parsing json objects"""


class Package(msgspec.Struct):
    arch: str
    buildtime: int
    disttag: str
    epoch: int
    name: str
    release: str
    source: str
    version: str

    def __hash__(self):
        return hash(
            (
                self.arch,
                self.buildtime,
                self.disttag,
                self.epoch,
                self.name,
                self.release,
                self.source,
                self.version,
            )
        )

    def __eq__(self, other):
        if isinstance(other, Package):
            return (self.name) == (other.name)
        return False


class RequestArgs(msgspec.Struct):
    arch: str


class StructJsonFile(msgspec.Struct):
    request_args: RequestArgs
    length: int
    packages: list[Package]
