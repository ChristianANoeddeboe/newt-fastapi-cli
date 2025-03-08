import typer

from .route import app as route_app

app = typer.Typer()

app.add_typer(route_app)
