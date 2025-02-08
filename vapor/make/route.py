import typer
from pathlib import Path

app = typer.Typer()

command_name = "make:route"


@app.command()
def route(name: str, version: str = "v1"):
    """
    Generate a new route file with boilerplate code.
    """
    project_dir = Path.cwd() / "routes" / "subroutes" / version
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
