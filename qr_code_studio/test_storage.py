from pathlib import Path, PosixPath

# storage_path = ('qr-code-studio/qr-codes/')
storage_path = Path.home() / 'qr-code-studio/qr-codes'
storage_path_str = str(storage_path)
# storage_path = Path.expanduser('~/qr-code-studio/qr-codes')
if not Path.exists(storage_path):
    # if not os.path.exists(storage_path):
    Path.mkdir(storage_path, mode=0o777, parents=True, exist_ok=False)
    # os.mkdir(storage_path)
    print('Storage path created: ' + storage_path_str)