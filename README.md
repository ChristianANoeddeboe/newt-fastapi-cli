# `newt`

Newt CLI - FastAPI development toolkit

Want to extend it? Check out the [Development Guide](DEVELOPMENT.md).

**Usage**:

```console
$ newt [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Show version and exit
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `users`
* `make`
* `config`
* `migrate`

## `newt users`

**Usage**:

```console
$ newt users [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`
* `delete`

### `newt users add`

**Usage**:

```console
$ newt users add [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

### `newt users delete`

**Usage**:

```console
$ newt users delete [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `--help`: Show this message and exit.

## `newt make`

**Usage**:

```console
$ newt make [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `route`: Generate a new route file with boilerplate...

### `newt make route`

Generate a new route file with boilerplate code.

**Usage**:

```console
$ newt make route [OPTIONS]
```

**Options**:

* `--name TEXT`: Name of the route to create
* `--version TEXT`: API version  [default: v1]
* `--path TEXT`: Custom path for the route
* `--help`: Show this message and exit.

## `newt config`

**Usage**:

```console
$ newt config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `init`: Create a default newt-cli.conf file if...

### `newt config init`

Create a default newt-cli.conf file if none exists.

**Usage**:

```console
$ newt config init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `newt migrate`

**Usage**:

```console
$ newt migrate [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `init`: Checks if alembic is already initialized...
* `up`: Upgrades the database to the specified...
* `down`: Downgrades the database to the specified...
* `make`: Creates a new migration file.

### `newt migrate init`

Checks if alembic is already initialized in the current directory.
If not then it checks if alembic is installed. If not then it will prompt the user to install it.
After installing alembic it will create a new alembic directory in the current or given path.
If alembic is already initialized in the current directory then it will ask if the user wants to reinitialize it.
If the user chooses to reinitialize it, it will remove the existing alembic directory and create a new one.
If the user chooses not to reinitialize it, it will exit the program.

**Usage**:

```console
$ newt migrate init [OPTIONS] [PATH]
```

**Arguments**:

* `[PATH]`: Relative path to the alembic directory  [default: alembic]

**Options**:

* `-t, --template TEXT`: Custom template for the alembic directory
* `--help`: Show this message and exit.

### `newt migrate up`

Upgrades the database to the specified revision.
If no revision is specified, it will upgrade to the next revision.
If the revision is not found, it will prompt the user to choose a revision from the list of available revisions.
If the user chooses to upgrade to a revision that is not the latest revision, it will prompt the user to confirm the upgrade.

**Usage**:

```console
$ newt migrate up [OPTIONS] [REVISION]
```

**Arguments**:

* `[REVISION]`: Revision to upgrade to

**Options**:

* `--help`: Show this message and exit.

### `newt migrate down`

Downgrades the database to the specified revision.
If no revision is specified, it will downgrade to the previous revision.
If the revision is not found, it will prompt the user to choose a revision from the list of available revisions.
If the user chooses to downgrade to a revision that is not the latest revision, it will prompt the user to confirm the downgrade.

**Usage**:

```console
$ newt migrate down [OPTIONS] [REVISION]
```

**Arguments**:

* `[REVISION]`: Revision to downgrade to

**Options**:

* `--help`: Show this message and exit.

### `newt migrate make`

Creates a new migration file.
If manual is set to True, it will create an empty migration file.
If manual is set to False, it will create a migration file with the changes detected in the database.

**Usage**:

```console
$ newt migrate make [OPTIONS] MESSAGE
```

**Arguments**:

* `MESSAGE`: Message for the migration file  [required]

**Options**:

* `-m, --manual`: Disable auto generation of migration files
* `--help`: Show this message and exit.
