import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os


def decode_qr(image_file):
    '''Decode a qr code image file'''
    try:
        if os.path.exists(image_file + '.png'):

            image_file = Image.open(image_file + '.png')
            result = decode(image_file)
            print(result)
    except:
        print('There was an error decoding the file.')
