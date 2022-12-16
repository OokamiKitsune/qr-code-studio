# qr-code-studio
This python3 CLI app generates qr codes and stores them in your home directory.  

## How to use
Run python program in a venv. This python app uses poetry for managing dependencies.

## Installing poetry 
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## cd to app directory
cd to application directory where the poetrytoml file resides.

## Install dependancies using poetry:
```bash
poetry install
```

## run app main.py
```bash
cd qr_code_studio
```

```bash
python3 main.py
```

## If you are having an issue with pyzbar you may need to install the libzbar library 

- On Unix/Linux:

```bash
sudo apt-get install libzbar0
```

- On Mac OS you can use brew:

```bash
brew install zbar
```


Everytime you create a qr code, the name of the file is whatever you enetered in as your QR code data. This ensures easy identification of the QR Code .PNG in your folder. 

