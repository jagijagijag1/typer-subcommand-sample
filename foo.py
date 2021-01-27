import typer

from commands import bar, baz

fooapp = typer.Typer(add_completion=False)
# fooapp.add_typer(bar.barapp, name="bar")
fooapp.command(name='bar')(bar.main)
fooapp.add_typer(baz.bazapp, name="baz")


if __name__ == "__main__":
    fooapp()
