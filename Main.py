import json
import os
from Webserver import app

config = json.load(open('config.json'))


def prompt_user():
    """
    Prompts the user for a language and an image file
    :return: The path to the image file, and the language
    """
    # Prompt the user for a language
    print("Welcome to ImageRunner")
    path = 'js_code.png'
    language = 'js'
    # path = input("Please enter the path to the image: ")
    # language = input("Please enter the programming language: ")
    return path, language


def cli_main():
    """
    The entry point if you decide to run this on the command line. Currently not used
    :return: None
    """
    image, language = prompt_user()
    settings = config[language]
    extension = settings["extension"]
    run_image(image, language)
    os.system(settings["interpreter"] + " .tmp." + extension)


if __name__ == '__main__':
    from OCR import run_image
    app.run(debug=True)
