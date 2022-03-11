import os
from glob import glob

import click
import pkg_resources
from tutor.commands.context import Context

from .__about__ import __version__
from .commands import export_data, import_data

templates = pkg_resources.resource_filename(
    "tutor_import_export_data", "templates"
)

config = {}

hooks = {}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "tutor_import_export_data", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches


@click.group(help="Manage commands")
@click.pass_obj
def command(context: Context) -> None:
    pass

command.add_command(import_data)
command.add_command(export_data)
