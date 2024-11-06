import click

# @click.command()
# @click.option('--count',default=1,help='count of greetings')
# @click.option('--name',prompt='Enter your name please',help='The person to greet')
# def hello(count,name):
#     for x in range(count):
#         click.echo(f"Welcome {name}!")
# def name():
#     click.echo("Hai, This is saran")


# if __name__ == "__main__":
#     hello()
#     name()

@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)
cli()