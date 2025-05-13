from typing import Annotated
import typer
app = typer.Typer(no_args_is_help=True)

@app.command()
def make(
    message: Annotated[str, typer.Argument(help="Message for the migration file")],
    manual: Annotated[bool, typer.Option("--manual", "-m", help="Disable auto generation of migration files")] = False,
):
    """
    Creates a new migration file.
    If manual is set to True, it will create an empty migration file.
    If manual is set to False, it will create a migration file with the changes detected in the database.
    """
    try:
        import alembic
    except ImportError:
        typer.echo("Alembic is not installed. Please install it first.")
        raise typer.Abort()

    # Create command
    command = ["alembic", "revision", "-m", message]
    if not manual:
        command.append("--autogenerate")

    # Run alembic upgrade command from a subfolder
    import subprocess
    subprocess.run(command)
    
    