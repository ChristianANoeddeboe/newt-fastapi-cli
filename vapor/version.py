import typer

app = typer.Typer()


@app.command()
def version():
    print("Vapor Version 1.0")
