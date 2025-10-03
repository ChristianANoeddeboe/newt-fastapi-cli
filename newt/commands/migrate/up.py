from typing import Annotated
import typer
app = typer.Typer(no_args_is_help=True)

@app.command()
def up(
    revision: Annotated[str, typer.Argument(help="Revision to upgrade to")] = None,
):
    """
    Upgrades the database to the specified revision.
    If no revision is specified, it will upgrade to the next revision.
    If the revision is not found, it will prompt the user to choose a revision from the list of available revisions.
    If the user chooses to upgrade to a revision that is not the latest revision, it will prompt the user to confirm the upgrade.
    """
    try:
        import alembic
    except ImportError:
        typer.echo("Alembic is not installed. Please install it first.")
        raise typer.Abort()

    # Create command
    command = ["alembic", "upgrade"]
    if revision:
        command.append(revision)
    else:
        command.append("head")

    # Run alembic upgrade command from a subfolder
    import subprocess
    subprocess.run(command)
    
    