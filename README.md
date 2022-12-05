# qr-code-studio
This python3 CLI app generates qr codes and stores them in your home directory.  

# How to use
This python app uses poetry for managing dependencies.

# Install poetry: 
curl -sSL https://install.python-poetry.org | python3 -
# cd to app directory
cd to application directory where the poetrytoml file resides.

# Install dependancies using poetry:
poetry install

# cd to qr_code_studio to run main.py
cd qr_code_studio
python3 main.py


Everytime you create a qr code, the name of the file is whatever you enetered in as your QR code data. This ensures easy identification of the QR Code .PNG in your folder. 
