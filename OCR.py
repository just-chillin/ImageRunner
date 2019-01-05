from google.cloud import vision
import os
import requests
import sys
import io


def ocr_main(file, lang):
    if not os.environ["GOOGLE_APPLICATION_CREDENTIALS"]:
        print("Please make sure the environment variable GOOGLE_APPLICATIONS_CREDENTIALS is set to the path of your "
              "credentials file", file=sys.stderr)
        exit(1)
    client = vision.ImageAnnotatorClient()

    with io.open(file, 'rb') as image_file:
        image = client.image(content=image_file.read())

    labels = image.detect_labels()
    for label in labels:
        print(label.description)


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
    ocr_main('text.pdf', 'python')
