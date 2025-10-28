import typer
from typing import Optional
from importlib.metadata import version, PackageNotFoundError

from newt.commands.users import app as users_app
from newt.commands.make import app as make_app
from newt.commands.config import app as config_app
from newt.commands.migrate import app as migrate_app

def version_callback(value: bool):
    if value:
        try:
            pkg_version = version("newt-cli")
        except PackageNotFoundError:
            pkg_version = "development"
        typer.echo(f"newt-cli {pkg_version}")
        raise typer.Exit()

app = typer.Typer(
    no_args_is_help=True,
    callback=lambda version: version_callback(version) if version else None
)

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", 
        callback=version_callback, 
        is_eager=True,
        help="Show version and exit"
    )
):
    """
    Newt CLI - FastAPI development toolkit
    """
    pass

app.add_typer(users_app, name="users")
app.add_typer(make_app, name="make")
app.add_typer(config_app, name="config")
app.add_typer(migrate_app, name="migrate")

if __name__ == "__main__":
    app()
