import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
 
executables = [Executable("LoL_Auto_Accept.py", base=base, icon="icon.ico")]
packages = ["idna","tkinter","pyautogui","os"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "LOL_Auto_Accept",
    options = options,
    version = "1.0",
    description = 'skillz',
    executables = executables
)
