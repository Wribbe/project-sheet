import os
import sqlite3

from flask import g, Flask
from pathlib import Path

app = Flask(__name__)

ROOT = Path(__file__).parent.parent
PATH_DATA = os.environ.get('SHEET_DATA_PATH', ROOT)
PATH_DB = ROOT / 'sheet.db'

def get_db():
    db = getattr(g, '_database', None)
    if not db:
        db = g._database = sqlite3.connect(PATH_DB)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if not PATH_DB.is_file():
    init_db()
