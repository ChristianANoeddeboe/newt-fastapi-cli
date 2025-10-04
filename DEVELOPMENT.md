# Development Guide

This document describes how to set up your development environment to work on the `newt-cli` project.

## Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/) (for dependency management and building)

## Setting Up Development Environment

1. **Clone the repository**

   ```bash
   git clone https://github.com/ChristianANoeddeboe/newt-fastapi-cli.git
   cd newt-fastapi-cli
   ```

2. **Install dependencies and the package in development mode**

   ```bash
   poetry install
   ```

   This will:

   - Create a virtual environment automatically
   - Install all dependencies from `pyproject.toml`
   - Install the `newt` package in editable mode

3. **Verify installation**
   ```bash
   poetry run newt --help
   # or activate the shell and run directly:
   poetry shell
   newt --help
   ```

## Project Structure

```
newt-fastapi-cli/
├── newt/
│   ├── __init__.py
│   ├── main.py                    # Main CLI app with version handling
│   ├── constants.py
│   └── commands/                  # Command modules
│       ├── users/
│       ├── make/
│       ├── config/
│       └── migrate/
├── tests/
├── pyproject.toml                 # Project configuration and dependencies
├── poetry.lock                    # Locked dependency versions
├── README.md
└── DEVELOPMENT.md
```

## Development Workflow

1. **Activate the Poetry environment**

   ```bash
   poetry shell
   # or run commands with: poetry run <command>
   ```

2. **Make your changes** in the `newt/` directory

   - Changes are reflected immediately since the package is installed in editable mode

3. **Test your changes**

   ```bash
   newt <command>
   newt --help
   newt -v  # Check version
   ```

4. **Add dependencies** (if needed)
   ```bash
   poetry add <package-name>        # Runtime dependency
   poetry add --group dev <package> # Development dependency
   ```

## Version Management

The version is managed in `pyproject.toml` and automatically used by the CLI:

1. **Update version**

   ```bash
   poetry version patch    # 0.1.0 -> 0.1.1
   poetry version minor    # 0.1.0 -> 0.2.0
   poetry version major    # 0.1.0 -> 1.0.0
   # or manually edit pyproject.toml
   ```

2. **Reinstall to pick up version changes**

   ```bash
   poetry install
   ```

3. **Verify version**
   ```bash
   newt -v
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
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=newt
```

## Building for Distribution

```bash
poetry build
```

This creates both wheel and source distributions in the `dist/` directory.

## Publishing (when ready)

1. **Build the package**

   ```bash
   poetry build
   ```

2. **Publish to PyPI**
   ```bash
   poetry publish
   # or for test PyPI:
   poetry publish -r testpypi
   ```
