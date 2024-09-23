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


def __modify_config():
    """
    Modify `config.toml` to include the required theming for a Streamlit project.

    If the file does not exist, it will be created.
    """
    config_path = ".streamlit/config.toml"

    # load a config file if available
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


@cli.command()
def configure():
    """Configure the project settings."""
    __modify_config()

if __name__ == "__main__":
    cli()
