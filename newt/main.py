import typer

from .version import app as version_app
from newt.commands.users import app as users_app
from newt.commands.make import app as make_app
from newt.commands.config import app as config_app
from newt.commands.migrate import app as migrate_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(version_app)
app.add_typer(users_app, name="users")
app.add_typer(make_app, name="make")
app.add_typer(config_app, name="config")
app.add_typer(migrate_app, name="migrate")

if __name__ == "__main__":
    app()
