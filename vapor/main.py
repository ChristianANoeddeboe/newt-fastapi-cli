import typer

from .version import app as version_app
from vapor.commands.users import app as users_app
from vapor.commands.make import app as make_app
from vapor.commands.config import app as config_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(version_app)
app.add_typer(users_app, name="users")
app.add_typer(make_app, name="make")
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()
