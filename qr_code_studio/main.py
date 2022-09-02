import os
import generate
import decode
from pathlib import Path, PosixPath
from time import sleep

# This program generates a QR code using the inputs from the command line.

# Initialize app and storage directory

try:
    
    # storage_path = ('qr-code-studio/qr-codes/')
    storage_path = Path.home() / 'qr-code-studio/qr-codes'
    storage_path_str = str(storage_path)
    # storage_path = Path.expanduser('~/qr-code-studio/qr-codes')
    if not Path.exists(storage_path):
    # if not os.path.exists(storage_path):
        Path.mkdir(Path.mkdir(storage_path, mode=0o777, parents=True, exist_ok=False))
        # os.mkdir(storage_path)
        print('Storage path created: ' + storage_path_str)
except OSError as error :
    print(error)
    print('There was an error creating the storage directory ' + storage_path_str + '\nAppliction will still run but you may be unable to save QR codes.')



while True:

    print('⚡  Welcome to QR Generator! \nQR Codes are stored in: ' + '\n' + storage_path_str + '\nSelect an option:')

    print('➡️  Enter \'1\' to create a new QR Code.')
    print('➡️  Enter \'2\' to decode a QR Code from an image file.')
    user_option = input ('Enter option: ').strip()
    if user_option == 'q':
        print('Bye!')
        break

    if user_option == '1':
        print('Create a new QR Code!')
        user_input_formatted = ''
        user_input = input('⌨️  Enter data to store inside your new QR Code: ')

        # User input checked for non alpha numeric characters.
        for character in user_input:
            if character.isalnum():
                user_input_formatted += character
        print('File name will be: ' + user_input_formatted)
        sleep(3)
                
        # Function call to create QR
        generate.create_qr(storage_path, storage_path_str, user_input_formatted, user_input)
        print('🎉')
    
    if user_option == '2':

        print('Decode a QR Code.')
        # // TODO Implement the decode function
        
        image_file = input('Enter the location of the QR Code: ')
        
        # Fucntion call to decode a qr code
        decode.decode_qr(image_file)


