from typing import Annotated
import typer
from pathlib import Path
from newt.config import config_values

app = typer.Typer(no_args_is_help=True)

@app.command()
def init(
    path: Annotated[str, typer.Argument(help="Relative path to the alembic directory")] = "alembic",
    template: Annotated[str, typer.Option("--template", "-t", help="Custom template for the alembic directory")] = None,
):
    """
    Checks if alembic is already initialized in the current directory.
    If not then it checks if alembic is installed. If not then it will prompt the user to install it.
    After installing alembic it will create a new alembic directory in the current or given path.
    If alembic is already initialized in the current directory then it will ask if the user wants to reinitialize it.
    If the user chooses to reinitialize it, it will remove the existing alembic directory and create a new one.
    If the user chooses not to reinitialize it, it will exit the program.
    """
    # Check if alembic is already initialized via pip
    is_installed = True
    try:
        import alembic
    except ImportError:
        is_installed = False

    if not is_installed:
        # Install alembic
        install = typer.confirm("Alembic is not installed. Do you want to install it?")
        if not install:
            raise typer.Abort()
        else:
            import subprocess
            subprocess.run(["pip", "install", "alembic"])

    # Check if alembic is already initialized in the current directory
    project_dir = Path(f"{Path.cwd()}/{path}")

    #alembic_dir = project_dir / "alembic"
    if project_dir.exists():
        reinitialize = typer.confirm("Alembic is already initialized. Do you want to reinitialize it?")
        if not reinitialize:
            raise typer.Abort()
        else:
            import shutil
            shutil.rmtree(project_dir)
    project_dir.mkdir(parents=True, exist_ok=True)

    # Create command
    command = ["alembic", "init", str(project_dir)]
    if template:
        command.extend(["--template", template])

    # Run alembic init command from a subfolder
    import subprocess
    subprocess.run(command)

