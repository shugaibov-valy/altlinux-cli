from enum import Enum


class Branch(Enum):
    p10 = "p10"
    sisyphus = "sisyphus"


class Arch(Enum):
    aarch64 = "aarch64"
    i586 = "i586"
    x86_64 = "x86_64"
    noarch = "noarch"
    x86_64_i586 = "x86_64-i586"
