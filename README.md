# AltLinux-CLI

### Requirements
* Python 3.9+
* Poetry 1.8+

### Installation Poetry

```bash
apt-get update
apt install -y python3-poetry
poetry --version
```

### 1. Prepare project virtual environment:
```bash
mkdir altlinux_cli/
git clone https://github.com/shugaibov-valy/altlinux-cli.git altlinux_cli
cd altlinux_cli/
mkdir files/
poetry env use python3
poetry config virtualenvs.create true && poetry install
poetry show
```


### Run CLI
```bash
(altlinux-cli-py3.12) root@important-produce:~/altlinux_cli# python3 main.py  --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get-branch  Getting packages for a specific branch
  parsing     Parsing json relative to the selected architecturex
```

