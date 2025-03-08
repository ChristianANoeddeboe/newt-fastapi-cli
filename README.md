# `vapor`

Want to extend it? Check out the [Development Guide](DEVELOPMENT.md).

**Usage**:

```console
$ vapor [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `version`
- `users`
- `make`

## `vapor version`

**Usage**:

```console
$ vapor version [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `vapor users`

**Usage**:

```console
$ vapor users [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `add`
- `delete`

### `vapor users add`

**Usage**:

```console
$ vapor users add [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]

**Options**:

- `--help`: Show this message and exit.

### `vapor users delete`

**Usage**:

```console
$ vapor users delete [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]

**Options**:

- `--help`: Show this message and exit.

## `vapor make`

**Usage**:

```console
$ vapor make [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `route`: Generate a new route file with boilerplate...

### `vapor make route`

Generate a new route file with boilerplate code.

**Usage**:

```console
$ vapor make route [OPTIONS] NAME
```

**Arguments**:

- `NAME`: [required]
- `version`: [default: v1]
- `path`: [default: /routes/{version}/{name}]

**Options**:

- `--version TEXT`: [default: v1]
- `--help`: Show this message and exit.
