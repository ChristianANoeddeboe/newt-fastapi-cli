# Development Guide

This document describes how to set up your development environment to work on the `vapor-cli` project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setting Up Development Environment

1. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**

   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install the package in development mode**

   ```bash
   pip install -e .
   ```

4. **Verify installation**
   ```bash
   vapor --help
   ```

## Project Structure

```
vapor-cli/
├── vapor/
│   ├── __init__.py
│   ├── main.py
│   ├── users.py
│   ├── version.py
│   └── make.py
├── setup.py
├── README.md
└── Development.md
```

## Development Workflow

1. Make your changes in the `vapor/` directory
2. Since the package is installed in development mode (`-e` flag), your changes will be reflected immediately
3. Test your changes by running the CLI:
   ```bash
   vapor <command>
   ```

## Adding New Commands

1. Create a new module in the `vapor/` directory
2. Define your Typer app in the new module
3. Import and add your new app to `main.py` using `app.add_typer()`

## Running Tests

(Add test instructions when tests are implemented)

## Building for Distribution

To build the package for distribution:

```bash
python -m build
```
