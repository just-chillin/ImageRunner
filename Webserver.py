from flask import Flask, request, render_template_string
from OCR import run_image
import json

app = Flask(__name__)


def get_webpage():
    res = ''
    for line in open('html/index.html'):
        res += line
    return res


@app.route('/languages')
def languages():
    config = json.load(open('config.json'))
    return ','.join(config.keys())


@app.route('/', methods=["GET", "POST"])
def index():
    config = json.load(open('config.json'))
    if request.method == 'GET':
        return render_template_string(get_webpage(), langs=config.keys())
    else:
        return run_image(request.files['img'], request.form['lang'])
