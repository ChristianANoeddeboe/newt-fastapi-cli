from pathlib import Path

# Values for the configuration file
config_values = {
    "MAKE_ROUTE_BASE_PATH": "routes"
}

# Initialize the configuration file if it exists and load values
file = Path(Path.cwd() / "vapor-cli.conf")

if file.exists():
    with file.open() as f:
        for line in f:
            key, value = line.strip().split("=")
            config_values[key] = value



