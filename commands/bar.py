import typer

barapp = typer.Typer(add_completion=False)


@barapp.command()
def main(arg: str):
    typer.echo(f"This is bar command: {arg}")


if __name__ == "__main__":
    barapp()
