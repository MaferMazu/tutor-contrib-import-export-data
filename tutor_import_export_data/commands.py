import click


@click.command(name='import')
@click.argument('from_path')
def import_data(from_path: str):
    click.echo(f"Import from: {from_path}")


@click.command(name='export')
@click.argument('from_path')
def export_data(from_path: str):
    click.echo(f"Export from: {from_path}")
