from google.cloud import vision
import requests



def ocr_main(file, lang):
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



if __name__ == "__main__":
    ocr_main('text.pdf', 'python')
