import os
import generate
import decode
from pathlib import Path, PosixPath
from time import sleep
from qrcode_term import qrcode_string as qr_terminal

# This program generates a QR code using the inputs from the command line.

# Initialize app and storage directory

try:
    # Try to create a storage directory in home path.
    storage_path = Path.home() / 'qr-code-studio/qr-codes'
    storage_path_str = str(storage_path)

    # Check for the exsistance of the path. If path does not exsist, create it. 
    if not Path.exists(storage_path):
        # Create direcotry and set read/write permissions for directory.
        Path.mkdir(Path.mkdir(storage_path, mode=0o777, parents=True, exist_ok=False))
        print('Storage path created here: ' + storage_path_str)
    else:
        # If path already exsists, tell user. 
        print('Storage path already created!')
        sleep(3)
except OSError as error :
    print(error)
    print('There was an error creating the storage directory ' + storage_path_str + '\nApplication needs permission to create a directory in order to save QR codes' '\nAppliction will still run but may be unable to save QR codes.')



while True:
    print('\n')
    print('⚡⚡⚡ >> Welcome to QR Generator << ⚡⚡⚡\n \nYour QR codes are stored in: ' + '\n' + storage_path_str + '\n \nEnter an option:')

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
        

        # Print QR code preview to terminal
        if user_input == "":
            pass

        else:
            print (f'🎉 Here is a preview of your {user_input} QR Code!')
            qr_code_to_terminal = qr_terminal(user_input)
            print(qr_code_to_terminal)

    
    if user_option == '2':
            
        print('Decode a QR Code.\n' + 'Path to look for images is: ' + storage_path_str)
        # // TODO Implement the decode function
        
        image_file = input('Enter the location of the QR Code: ')
        full_image_path = storage_path_str + image_file
        
        # Fucntion call to decode a qr code
        decode.decode_qr(image_file)


