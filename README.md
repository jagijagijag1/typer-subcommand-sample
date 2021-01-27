# Typer Subcommand Sample

### Main command `foo`
```bash
# install
$ pipenv install

# usage
$ pipenv run foo.py --help
Usage: foo.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  bar
  baz
```

### Subcommand `bar`
```bash
$ pipenv run foo.py bar --help
Usage: foo.py bar [OPTIONS] ARG

Arguments:
  ARG  [required]

Options:
  --help  Show this message and exit.

$ python foo.py bar hoge
This is bar command: hoge
```

### Subcommand `baz`
```bash
$ pipenv run foo.py baz --help
Usage: foo.py baz [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  corge
  qux

$ pipenv run python foo.py baz qux fuga
This is baz qux command: fuga

$ pipenv run python foo.py baz corge piyo
This is baz corge command: piyo
```