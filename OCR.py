from google.cloud import vision
from PIL import Image
import os
import sys
import io
import subprocess
from threading import Lock

run_program_lock = Lock()
image_file_lock = Lock()


def filter_file(file: str):
    """
    A function for adding various filters to the image in case.
    WARNING: THIS FUNCTION IS NOT THREAD SAFE
    :param file: The path to the image file
    """
    image = Image.open(file)
    # image = image.convert('L')
    # image = image.filter(ImageFilter.EDGE_ENHANCE)
    image.save(".tmp.png")


def run_interpreter(language, code):
    """
    Runs code with interpreter and returns the output. Thread safe.
    :param language: The name of the language chosen by the user
    :param code: A string containing the code in memory
    """
    from Main import config
    program_fname = '.tmp.%s' % config[language]["extension"]
    interpreter = config[language]["interpreter"]
    run_program_lock.acquire(blocking=True)
    with open(program_fname, 'w+') as program_file:
        print(code, file=program_file)
    try:
        output = subprocess.check_output([interpreter, program_fname])
    except subprocess.CalledProcessError as e:
        output = "\0"
    run_program_lock.release()
    return output


def fix_common_text_issues(code_str: str) -> str:
    """
    Fixes common, generic OCR issues.
    :param code_str: The string containing the code in memory
    :return: The fixed string
    """
    return code_str.replace('–', '-')


def get_text_from_image(image):
    """
    Sends a image file to google's servers to be OCR'ed. Thread safe.
    :param file: The path to the file to interpret.
    :return: The response from google's servers.
    """
    client = vision.ImageAnnotatorClient()
    image_file_lock.acquire(blocking=True)
    image_path = '.tmp.png'
    image.save(image_path)
    filter_file(image_path)
    with io.open(image_path, 'rb') as image_file:
        image = image_file.read()
        image_file = vision.types.Image(content=image)
        response = client.document_text_detection(image=image_file)
    image_file_lock.release()
    return response


def run_image(file: str, language: str) -> str:
    """
    Runs the image.
    :param file: The path to the image file
    :param language: The language to use settings for
    :return: The output of the interpreter
    """
    if not os.environ["GOOGLE_APPLICATION_CREDENTIALS"]:
        print("Please make sure the environment variable GOOGLE_APPLICATIONS_CREDENTIALS is set to the path of your "
              "credentials file", file=sys.stderr)
        exit(1)
    response = get_text_from_image(file)
    code: str = fix_common_text_issues(response.full_text_annotation.text)
    return run_interpreter(language, code)
