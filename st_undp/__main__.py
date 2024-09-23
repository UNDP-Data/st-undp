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
@click.option(
    "--settings",
    type=click.Choice(["style", "deployment"], case_sensitive=False),
    default="style",
    help="The type of configuration settings for your project. `style` modifies `config.yaml` to style your app"
    " while `deployment` adds a `startup.sh` with commands to style and run your app on Azure App Service."
    " See the package documentation for usage details.",
)
def configure(settings: str):
    """Configure the project settings."""
    if settings == "style":
        __modify_config()
    elif settings == "deployment":
        file_name = "startup.sh"
        script = read_file(file_name)
        with open(file_name, "w") as file:
            file.write(script)
        click.echo(f"Added {file_name} for deployment to Azure Web Apps.")
        message = click.style(
            "Make sure to add 'startup.sh' as a startup command on Azure.",
            bold=True,
        )
        click.echo(message)


if __name__ == "__main__":
    cli()
