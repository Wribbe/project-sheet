import os
import sqlite3
from flask import g, current_app as app
from pathlib import Path


ROOT = Path(__file__).parent.parent
PATH_DATA = os.environ.get('SHEET_DATA_PATH', ROOT)
PATH_DB = ROOT / 'sheet.db'


def db_get():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(PATH_DB)
    return db


def cursor():
    return db_get().cursor()


def db_init():
    if PATH_DB.is_file():
        return
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def user_create(name):
    db = db_get()
    cur = db.cursor()
    cur.execute('INSERT INTO user(name) VALUES(?);', (name,))
    db.commit()


def users():
    cur = cursor()
    return cur.execute('SELECT * FROM user;')
