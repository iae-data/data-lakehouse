# from src.configuration import Config

# if __name__ == "__main__":
#    config = Config()
#    config.print_config()
import click
from app.src.configuration import Config


@click.group()
def cli():
    pass


@cli.command()
def process():
    config = Config()
    config.print_config()
    # TODO: Add logic to process data


@cli.command()
def train():
    config = Config()
    config.print_config()
    # TODO: Add logic to train models


@cli.command()
def dashboard():
    config = Config()
    config.print_config()
    # TODO: Add logic to launch the dashboard


@cli.command()
def run():
    choice = click.prompt("Choose an option: \n1: Process data\n2: Train models\n3: Launch UI\n", type=int)
    if choice == 1:
        process()
    elif choice == 2:
        train()
    elif choice == 3:
        dashboard()
    else:
        click.echo("Invalid choice, please choose a valid option")


if __name__ == "__main__":
    cli()
