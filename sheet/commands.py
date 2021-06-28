import click

from flask import current_app as app

from sheet import db, populate

@app.cli.command("create-user")
@click.argument('name')
def create_user(name):
    print(f"Created user: {name}")
    db.user_create(name)


@app.cli.command("populate-users")
@click.option('-num', default=10)
def populate_users(num):
    populate.users(num)
