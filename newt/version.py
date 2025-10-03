import typer
from .__version__ import __version__

app = typer.Typer()

@app.command()
def version():
    print(f"newt Version {__version__}")
