from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image
from pathlib import Path


def decode_qr(image_file):
    '''Decode a qr code image file'''
    try:
        if Path(image_file).exists():
            image_file = Image.open(image_file)
            result = decode(image_file)
            print(result)
    except:
        print('There was an error decoding the file. ' + image_file)
        sleep(3)
