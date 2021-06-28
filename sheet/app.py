import os
from flask import render_template, Flask

app = Flask(__name__)

with app.app_context():
    from sheet import commands, db
    db.init()


@app.route('/')
def index():
    return render_template('index.html', users=db.users())


@app.route('/u/<user>')
def sheet(user):
    return render_template('sheet.html', user=db.user(user))


def run():
    os.environ['FLASK_ENV'] = 'development'
    app.run('0.0.0.0', debug=True)
