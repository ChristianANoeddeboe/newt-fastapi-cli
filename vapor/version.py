import typer
from .constants import VERSION

app = typer.Typer()

@app.command()
def version():
    print(f"Vapor Version {VERSION}")
