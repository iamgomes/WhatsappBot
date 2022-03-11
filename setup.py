import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
files = ['src/']

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == 'win32':
    base = 'Console'  # para execuções em terminal

setup(
    name='WhatsappBot',
    version='0.1',
    description='Bot que baixa arquivos de um contato ou grupo do WhatsApp.',
    options={'build_exe': {'include_files':files}},
    executables=[Executable('main.py', base=base)]
)