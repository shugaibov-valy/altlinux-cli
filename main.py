import asyncio
from parser import create_tasks_parse

import click

import consts
from enums import Arch, Branch
from utils import find_newer_packages, read_json_packages, save_json_packages_in_file


@click.group()
def cli():
    print("It is AltLinux CLI for https://packages.altlinux.org/ru/")


@cli.command()
@click.argument("arch", type=str)
def parsing(arch: str):
    """Parsing json relative to the selected architecture"""
    if arch not in [arch.value for arch in Arch]:
        raise click.BadParameter(
            "The architecture must be one of: "
            + ", ".join([arch.value for arch in Arch])
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
    if branch not in [branch.value for branch in Branch]:
        raise click.BadParameter(
            "The branch must be one of: " + ", ".join([arch.value for arch in Branch])
        )
    try:
        p10_packages, sisyphus_packages = read_json_packages()
    except FileNotFoundError:
        raise click.BadParameter(
            'You must first parse json data using the "parsing <arch>" command.'
        )

    if branch == Branch.p10:
        only_p10_packages = p10_packages - sisyphus_packages  # 1 task
        click.echo(
            f"Number packages that are in p10 but not in sisyphus - {len(only_p10_packages)}"
        )
        save_json_packages_in_file(only_p10_packages)
        click.echo(f"Path on output file of packages - {consts.OUTPUT_FILE_PATH}")

    elif branch == Branch.sisyphus:
        only_sisyphus_packages = sisyphus_packages - p10_packages  # 2 task
        click.echo(
            f"Number packages that are in sisyphus but not in p10 - {len(only_sisyphus_packages)}"
        )
        save_json_packages_in_file(only_sisyphus_packages)
        click.echo(f"Path on output file of packages - {consts.OUTPUT_FILE_PATH}")

    elif branch == Branch.compare:  # 3 task
        new_packages = find_newer_packages(sisyphus_packages, p10_packages)
        click.echo(
            f"Number packages with version-release greater in sisyphus than in p10 - {len(new_packages)}"
        )
        save_json_packages_in_file(new_packages)
        click.echo(f"Path on output file of packages - {consts.OUTPUT_FILE_PATH}")


if __name__ == "__main__":
    cli()
