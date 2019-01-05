from flask import Flask, request, render_template_string
from OCR import ocr_main
import json
import os
import subprocess

app = Flask(__name__)


def get_webpage():
    res = ''
    for line in open('html/index.html'):
        res += line
    return res


@app.route('/', methods=["GET", "POST"])
def index():
    config = json.load(open('config.json'))
    if request.method == 'GET':
        return render_template_string(get_webpage(), langs=config.keys())
    lang, img = request.form['lang'], request.files['img']
    settings = config[lang]
    img.save('.tmp.png')

    file_extension = settings["extension"]
    ocr_main('.tmp.png', file_extension)
    try:
        return subprocess.check_output([settings['interpreter'], '.tmp.' + file_extension], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return e.output
