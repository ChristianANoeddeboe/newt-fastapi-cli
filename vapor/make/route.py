import typer
from pathlib import Path
from vapor.config import config_values

app = typer.Typer(no_args_is_help=True)

@app.command()
def route(
    name: str = typer.Option(None, help="Name of the route to create"),
    version: str = typer.Option("v1", help="API version"),
    path: str = typer.Option(None, help="Custom path for the route")
):
    """
    Generate a new route file with boilerplate code.
    """
    if name is None:
        name = typer.prompt("Enter the name of the route")
        if not name:
            typer.echo("Name is required.")
            raise typer.Exit(code=1)
        
    default_path = f"routes/{version}"
    if path is None:
        path = typer.prompt(
            "Where should the route be created?", 
            default=default_path
        )
    config_base_path = config_values["MAKE_ROUTE_BASE_PATH"]
    base_path = f"{Path.cwd()}/{config_base_path}/"
    
    project_dir = Path(base_path + path) 
    project_dir.mkdir(parents=True, exist_ok=True)

    route_file = project_dir / f"{name}.py"
    if route_file.exists():
        typer.echo(f"Route {name} already exists.")
        raise typer.Exit(code=1)

    boilerplate = f"""from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_{name.lower()}():
    return {{"message": "Hello from {name}"}}
"""
    route_file.write_text(boilerplate)
    typer.echo(f"Route {name} created successfully at {route_file}"
               f"\n\nAdd the following line to routes/api.py:"
               f"\n\nfrom routes.subroutes.{version} import {name}"
               f"\n\napi_router.include_router({name}.router, prefix='/{version}')")