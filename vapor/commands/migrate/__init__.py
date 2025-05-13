import typer

from .init import app as init
from .up import app as up
from .down import app as down
from .make import app as make

app = typer.Typer(no_args_is_help=True)

app.add_typer(init)
app.add_typer(up)
app.add_typer(down)
app.add_typer(make)
