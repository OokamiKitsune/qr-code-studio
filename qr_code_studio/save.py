from time import sleep
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os


def save_file(user_input, user_input_formatted, storage_path, storage_path_str):
        qr = qrcode.QRCode(version=1, box_size=5, border=3)
        qr.add_data(user_input)

        qr.make(fit=True)
        img = qr.make_image(fill_color='white', back_color='black')
        print(user_input_formatted)
        img.save(storage_path_str + '/' + user_input_formatted + '.png')

        
        print('💾 QR Code saved to path: ', storage_path)
        sleep(3)