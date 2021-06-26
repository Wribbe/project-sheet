import os

from sheet.config import get_db, app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
