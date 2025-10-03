import typer

from newt.commands.config.init import app as init_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(init_app)
