# `newt`

Want to extend it? Check out the [Development Guide](DEVELOPMENT.md).

**Usage**:

```console
$ newt [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `version`
- `users`
- `make`

## `newt version`

**Usage**:

```console
$ newt version [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `newt users`

**Usage**:

```console
$ newt users [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `add`
- `delete`

### `newt users add`

**Usage**:

```console
$ newt users add [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]

**Options**:

- `--help`: Show this message and exit.

### `newt users delete`

**Usage**:

```console
$ newt users delete [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]

**Options**:

- `--help`: Show this message and exit.

## `newt make`

**Usage**:

```console
$ newt make [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `route`: Generate a new route file with boilerplate...

### `newt make route`

Generate a new route file with boilerplate code.

**Usage**:

```console
$ newt make route [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]
- `version`: [default: v1]
- `path`: [default: /routes/{version}/{name}]

**Options**:

- `--version TEXT`: [default: v1]
- `--help`: Show this message and exit.
