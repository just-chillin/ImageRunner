from flask import Flask, request, render_template_string
from OCR import run_image
import json

app = Flask(__name__)


def get_webpage(name):
    res = ''
    for line in open('html/%s' % name):
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
        return render_template_string(get_webpage('index.html'), langs=config.keys())
    else:
        result = run_image(request.files['img'], request.form['lang'])
        if result == '\0':
            return render_template_string(get_webpage('Error_output.html'), output=result)
        else:
            return render_template_string(get_webpage('Output.html'), output=result)
