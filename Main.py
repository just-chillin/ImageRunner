import json
import os
from OCR import ocr_main
from Webserver import app


def prompt_user():
    # Prompt the user for a language
    print("Welcome to ImageRunner")
    path = 'js_code.png'
    language = 'js'
    # path = input("Please enter the path to the image: ")
    # language = input("Please enter the programming language: ")
    return path, language


def main():
    image, language = prompt_user()
    settings = json.load(open('config.json'))[language]
    extension = settings["extension"]
    ocr_main(image, extension)
    os.system(settings["interpreter"] + " .tmp." + extension)


if __name__ == '__main__':
    app.run(debug=True)