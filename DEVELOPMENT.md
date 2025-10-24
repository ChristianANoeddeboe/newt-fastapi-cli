# Development Guide

This document describes how to set up your development environment to work on the `newt-cli` project.

## Prerequisites

- Python 3.9 or higher
- [UV](https://docs.astral.sh/uv/getting-started/installation/) (for dependency management and building)

## Setting Up Development Environment

1. **Clone the repository**

   ```bash
   git clone https://github.com/ChristianANoeddeboe/newt-fastapi-cli.git
   cd newt-fastapi-cli
   ```

2. **Install dependencies and the package in development mode**

   ```bash
   uv install
   ```

   This will:

   - Create a virtual environment automatically
   - Install all dependencies from `pyproject.toml`

   Now install the package in editable mode:

   ```bash
   uv pip install -e .
   ```

1. **Verify installation**
   ```bash
   newt --help
   ```

## Project Structure

```bash
newt-fastapi-cli/
├── newt/
│   ├── __init__.py
│   ├── main.py                    # Main CLI app with version handling
│   ├── constants.py
│   ├── config
│   │   └── __init__.py            # Configuration management
│   └── commands/                  # Commands folder
│       ├── users/
│       ├── make/
│       ├── config/
│       ├── ...                    # Other commands
│       └── migrate/
├── tests/
├── pyproject.toml                 # Project configuration and dependencies
├── uv.lock                        # Locked dependency versions
├── README.md
└── DEVELOPMENT.md
```

## Development Workflow


1. **Make your changes** in the `newt/` directory

- Changes are reflected immediately since the package is installed in editable mode

2. **Test your changes**

   ```bash
   newt <command>
   newt --help
   ```

3. **Add dependencies** (if needed)
   ```bash
   uv add <package-name>        # Runtime dependency
   uv add --dev <package>       # Development dependency
   ```

## Version Management

The version is managed in `pyproject.toml` and automatically used by the CLI:

**Update version**

   ```bash
   uv version --bump <level>    # [possible values: major, minor, patch, stable, alpha, beta, rc, post, dev]
   # or manually edit pyproject.toml
   ```

## Adding New Commands

1. **Create a new command module** in `newt/commands/`

   ```bash
   mkdir newt/commands/mynewcommand
   touch newt/commands/mynewcommand/__init__.py
   touch newt/commands/mynewcommand/main.py
   ```

2. **Define your Typer app** in the new module

   ```python
   # newt/commands/mynewcommand/main.py
   import typer

   app = typer.Typer()

   @app.command()
   def mycommand():
       """My new command description"""
       typer.echo("Hello from my new command!")
   ```

3. **Import and add to main CLI** in `newt/main.py`

   ```python
   from newt.commands.mynewcommand import app as mynewcommand_app

   # Add to the main app
   app.add_typer(mynewcommand_app, name="mynewcommand")
   ```

## Running Tests

```bash
# Run tests (when implemented)
uv run pytest

# Run tests with coverage
uv run pytest --cov=newt
```

## Building for Distribution

```bash
uv build
```

This creates both wheel and source distributions in the `dist/` directory.

## Publishing (when ready)

1. **Build the package**

   ```bash
   uv build
   ```

2. **Publish to PyPI**
   ```bash
   uv publish
   # or for test PyPI:
   uv publish -r testpypi
   ```
