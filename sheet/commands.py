import click

from flask import current_app as app

from sheet import db

@app.cli.command("create-user")
@click.argument('name')
def create_user(name):
    print(f"Created user: {name}")
    db.user_create(name)
