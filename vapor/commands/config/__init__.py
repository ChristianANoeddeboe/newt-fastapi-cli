import typer

from vapor.commands.config.init import app as init_app

app = typer.Typer(invoke_without_command=True)

app.add_typer(init_app)
