from flask import Flask
import qp
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/timur')
def timur():
    return 'mur-mur-mur'


@app.route('/dasha')
def dasha():
    return 'miau'

@app.route('/synonym/<query>')
def synonym(query):
    s = qp.synonym(query)
    return s
