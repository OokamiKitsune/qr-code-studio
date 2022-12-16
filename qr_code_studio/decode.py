from time import sleep
from pyzbar.pyzbar import decode
from PIL import Image
import os
from pathlib import Path


def decode_qr(image_file, storage_path):
    '''Decode a qr code image file'''
    image_path = Path.cwd() / storage_path / image_file
    
    try:
        if Path(image_path).exists():
            open_img = Image.open(str(image_path))
            loaded_image = Image.Image.load(str(image_path))
            result = decode(loaded_image)
            if len(result) == 0:
                print('The QR code could not be decoded. ' + image_file)
            else:
                print(result)
            
    except:
        print('There was an error decoding the file. ' + image_file)
        sleep(3)
