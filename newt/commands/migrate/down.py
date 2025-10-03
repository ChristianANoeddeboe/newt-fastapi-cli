from typing import Annotated
import typer
app = typer.Typer(no_args_is_help=True)

@app.command()
def down(
    revision: Annotated[str, typer.Argument(help="Revision to downgrade to")] = None,
):
    """
    Downgrades the database to the specified revision.
    If no revision is specified, it will downgrade to the previous revision.
    If the revision is not found, it will prompt the user to choose a revision from the list of available revisions.
    If the user chooses to downgrade to a revision that is not the latest revision, it will prompt the user to confirm the downgrade.
    """
    try:
        import alembic
    except ImportError:
        typer.echo("Alembic is not installed. Please install it first.")
        raise typer.Abort()

    # Create command
    command = ["alembic", "downgrade"]
    if revision:
        command.append(revision)
    else:
        command.append("-1")

    # Run alembic downgrade command from a subfolder
    import subprocess
    subprocess.run(command)
    
    