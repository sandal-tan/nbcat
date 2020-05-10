"""The CLI for nbcat."""

import json

from rich.console import Console, ConsoleOptions
import click

from .notebook import Notebook

@click.command()
@click.argument('file')
def nbcat(file):
    console = Console()
    with open(file) as fp:
        nb_obj = json.load(fp)
    nb = Notebook(**nb_obj)
    nb.render(console)
