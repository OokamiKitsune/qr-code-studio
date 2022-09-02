import save
from pathlib import Path, PosixPath


def create_qr(storage_path, storage_path_str, user_input_formatted, user_input):
    '''Create a QR code from the users inputed data and then store it in the storage path'''
    # Check if a file with name already exsists. If True ask user if they want to overwrite it. 
    
    direct_path_to_image = (storage_path_str + '/' + user_input_formatted + '.png')
    if Path(direct_path_to_image).exists:
        print('⚠️  File with name: ' + '\"'+ user_input_formatted +'\"' + ' exsists already')
        overwrite_file = input('Do you want to overwrite this file? (Y/N): ').strip().lower()
        while overwrite_file == ' ':
            if overwrite_file == 'y' or overwrite_file == 'yes':
                save.save_file(user_input, user_input_formatted, storage_path, storage_path_str)
                print(user_input_formatted + ' was overwritten.')
        
            else: 
                if overwrite_file == 'n' or overwrite_file == 'no':
                    pass
    else:
        if not Path.exists(storage_path_str + user_input_formatted + '.png'):
            save.save_file(user_input, user_input_formatted, storage_path, storage_path_str)
                
    
        
