import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def init(
    path: Annotated[
        str, typer.Argument(help="Relative path to the alembic directory")
    ] = "alembic",
    template: Annotated[
        str,
        typer.Option(
            "--template", "-t", help="Custom template for the alembic directory"
        ),
    ] = None,
):
    """
    Creates a new alembic directory structure with alembic.ini at the top level
    and migration files in an 'alembic' subdirectory.
    """
    project_dir = Path.cwd() / path

    # Check if directory exists and handle reinitialize
    if project_dir.exists():
        if not typer.confirm(
            "Alembic is already initialized. Do you want to reinitialize it?"
        ):
            raise typer.Abort()
        shutil.rmtree(project_dir)

    project_dir.mkdir(parents=True, exist_ok=True)

    # Create alembic structure in temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Build and run alembic init command
        command = ["alembic", "init", str(temp_path / "alembic")]
        if template:
            command.extend(["--template", template])

        try:
            subprocess.run(command, cwd=temp_dir, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            typer.echo(f"Error: {e}", err=True)
            typer.echo(
                "Please ensure alembic is installed: pip install alembic", err=True
            )
            raise typer.Abort()

        # Move alembic directory to target location
        shutil.move(str(temp_path / "alembic"), str(project_dir / "alembic"))

        # Move and update alembic.ini
        with open(temp_path / "alembic.ini", "r") as f:
            ini_content = f.read()

        # Update script_location to point to alembic subdirectory
        ini_content = re.sub(
            r"script_location = .*",
            "script_location = %(here)s/alembic",
            ini_content,
        )

        with open(project_dir / "alembic.ini", "w") as f:
            f.write(ini_content)
