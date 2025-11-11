import shutil
import subprocess
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def init(
    path: Annotated[str, typer.Argument(help="Relative path to the alembic directory")] = "alembic",
    template: Annotated[str, typer.Option("--template", "-t", help="Custom template for the alembic directory")] = None,
):
    """
    Creates a new alembic directory in the current or given path.
    If alembic is already initialized in the specified directory, it will ask if the user wants to reinitialize it.
    If the user chooses to reinitialize, it will remove the existing alembic directory and create a new one.
    If the user chooses not to reinitialize, it will exit the program.
    """
    # Check if alembic is already initialized in the current directory
    project_dir = Path(f"{Path.cwd()}/{path}")

    #alembic_dir = project_dir / "alembic"
    if project_dir.exists():
        reinitialize = typer.confirm("Alembic is already initialized. Do you want to reinitialize it?")
        if not reinitialize:
            raise typer.Abort()
        else:
            shutil.rmtree(project_dir)
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create command
    command = ["alembic", "init", path]
    if template:
        command.extend(["--template", template])

    # Run alembic init command from a subfolder
    subprocess.run(command)

