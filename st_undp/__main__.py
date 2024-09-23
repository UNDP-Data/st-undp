"""
A command line interface for setting up an app.
"""

import os

import click
import tomlkit

from .utils import read_file


@click.group()
def cli():
    """A simple CLI for setting up a Streamlit app."""
    pass


@cli.command()
def configure():
    """Configure app theme in Streamlit config file."""
    # load a config file if available
    config_path = ".streamlit/config.toml"
    if os.path.exists(config_path):
        action = "Updated"
        click.echo("Found an existing config, editing...")
        with open(config_path, "rb") as file:
            config = tomlkit.load(file)
    else:
        action = "Created"
        click.echo("No config found, creating...")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        config = {}

    # set theme settings
    config |= tomlkit.loads(read_file("config.toml"))
    click.echo("Set required theme settings...")

    # write the config file
    with open(config_path, "w+") as file:
        tomlkit.dump(config, file)
    click.echo(f"{action} Streamlit config at {config_path}.")


if __name__ == "__main__":
    cli()
