import os
import sqlite3
from flask import g, current_app as app
from pathlib import Path


ROOT = Path(__file__).parent.parent
PATH_DATA = os.environ.get('SHEET_DATA_PATH', ROOT)
PATH_DB = ROOT / 'sheet.db'


def get():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(PATH_DB)
    db.row_factory = sqlite3.Row
    return db


def execute(sql, vals=None, single=False):
    query = cursor().execute(sql, vals or ())
    return query.fetchall() if not single else query.fetchone()


def commit():
    get().commit()


def cursor():
    return get().cursor()


def init():
    if PATH_DB.is_file():
        return
    with app.app_context():
        db = get()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def user_create(name):
    execute('INSERT INTO user(name) VALUES(?);', (name,))
    commit()


def users():
    return execute('SELECT * FROM user ORDER BY name ASC;')


def user(name):
    return execute('SELECT * FROM user WHERE name = (?)', (name,), single=True)
