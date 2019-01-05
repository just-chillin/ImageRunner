from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageFilter
import os
import requests
import sys
import io

"""
Takes in the path to a file, and returns the path of a temporary image
"""


def filter_file(file):
    image = Image.open(file)
    #image = image.convert('L')
    #image = image.filter(ImageFilter.EDGE_ENHANCE)
    image.save(".tmp.png")
    return ".tmp.png"


"""
Destroys the temporary filtered image created for the reader
"""
def destroy_filter():
    pass
    #os.remove('.tmp.png')

def ocr_main(file, extension):
    file = filter_file(file)
    if not os.environ["GOOGLE_APPLICATION_CREDENTIALS"]:
        print("Please make sure the environment variable GOOGLE_APPLICATIONS_CREDENTIALS is set to the path of your "
              "credentials file", file=sys.stderr)
        exit(1)
    client = vision.ImageAnnotatorClient()

    with io.open(file, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    destroy_filter()
    f = open('.tmp.' + extension, 'w+')
    print(response.full_text_annotation.text, file=f)
    f.close()


"""
    headers = {
        "Authorization": "Bearer AIzaSyBvmh8i8Xenxa64k-DIo27nF6zykGK1zCU",
        "Content-Type": "application/json; charset=utf-8"
    }
    data = {
        'requests': [
            {
                'image': {
                    'source': {
                        'imageUri': file
                    }
                },
                'features': [
                    {
                        'type': 'TEXT_DETECTION'
                    }
                ]
            }
        ]
    }
    req = requests.post(url='https://vision.googleapis.com/v1/images:annotate', headers=headers, json=data)
    print(req.reason)
"""

if __name__ == "__main__":
    ocr_main('js_code.png', 'js')
