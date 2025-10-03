import typer

from .route import app as route_app

app = typer.Typer(no_args_is_help=True)

app.add_typer(route_app)
