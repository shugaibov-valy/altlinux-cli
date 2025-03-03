import asyncio
from parser import create_tasks_parse

import click

import consts
from enums import Arch, Branch
from utils import read_json_packages

# # Пересечение множеств для 3 случая
# pereshenine = p10_packages ^ sisyphus_packages
# for pack1 in sisyphus_packages:
#     data = [x for x in pereshenine if x.name == pack1.name]
#     print(data)
#     pass


@click.group()
def cli():
    pass


@cli.command()
@click.argument("arch", type=str)
def parsing(arch: str):
    """Parsing json relative to the selected architecture"""
    if arch not in Arch.__members__:
        raise click.BadParameter(
            "The architecture must be one of: "
            + ", ".join([arch.value for arch in Arch.__members__.values()])
        )
    asyncio.run(create_tasks_parse(consts.P10_URL + arch, consts.SISYPHUS_URL + arch))
    click.echo(
        "Parsing was successful: "
        + consts.P10_FILE_PATH
        + " "
        + consts.SISYPHUS_FILE_PATH
    )


@cli.command()
@click.argument("branch", type=str)
def get_branch(branch: str):
    """Getting packages for a specific branch"""
    if branch not in Branch.__members__:
        raise click.BadParameter(
            "The branch must be one of: "
            + ", ".join([arch.value for arch in Branch.__members__.values()])
        )
    try:
        p10_packages, sisyphus_packages = read_json_packages()
    except FileNotFoundError:
        raise click.BadParameter(
            'You must first parse json data using the "parsing <arch>" command.'
        )

    if branch == Branch.p10:
        only_p10_packages = (
            p10_packages - sisyphus_packages
        )  # все пакеты, которые есть в p10 но нет в sisyphus
        click.echo(len(only_p10_packages))
    elif branch == Branch.sisyphus:
        only_sisyphus_packages = (
            sisyphus_packages - p10_packages
        )  # все пакеты, которые есть в sisyphus но их нет в p10
        click.echo(len(only_sisyphus_packages))


if __name__ == "__main__":
    cli()
