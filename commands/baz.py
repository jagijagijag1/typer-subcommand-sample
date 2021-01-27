import typer

bazapp = typer.Typer(add_completion=False)


@bazapp.command()
def qux(arg: str):
    typer.echo(f"This is baz qux command: {arg}")


@bazapp.command()
def corge(arg: str):
    typer.echo(f"This is baz corge command: {arg}")


if __name__ == "__main__":
    bazapp()
