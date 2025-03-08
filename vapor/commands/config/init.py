import typer
from pathlib import Path
from vapor.config import config_values

app = typer.Typer()

@app.command()
def init():
    """Create a default vapor-cli.conf file if none exists."""
    config_file = Path(Path.cwd() / "vapor-cli.conf")
    
    if config_file.exists():
        typer.echo("Config file already exists")
        raise typer.Exit(1)
        
    content = "\n".join(f"{k}={v}" for k, v in config_values.items())
    config_file.write_text(content)
    typer.echo("Created vapor-cli.conf with default settings")
