import typer
from pathlib import Path
try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python < 3.11

app = typer.Typer()


@app.command()
def version():
    project_root = Path(__file__).parent.parent
    toml_path = project_root / "pyproject.toml"
    
    with open(toml_path, "rb") as f:
        data = tomllib.load(f)
    
    version = data["project"]["version"]
    print(f"Vapor Version {version}")
