import os
from flask import render_template, Flask

app = Flask(__name__)

with app.app_context():
    from sheet import commands, db
    db.db_init()

@app.route('/')
def index():
    return render_template('index.html', users=db.users())

def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
