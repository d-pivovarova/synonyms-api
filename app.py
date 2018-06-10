from flask import Flask
import json
import qp

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/synonym/<query>')
def synonym(query):
    s = qp.synonym(query)
    return json.dumps(s, ensure_ascii=False)

