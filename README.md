"#Lol_Auto_Accept" 

How to compile the code into an .exe using cx_Freeze (https://cx-freeze.readthedocs.io/en/latest/index.html): 
- Install cx_Freeze (most likely by typing "python -m pip install --upgrade cx_Freeze" or "python3 -m pip install --upgrade cx_Freeze" on your command prompt) 
*
- Open your command prompt and move to the directory where the script is
- Type "python setup.py build" or "python3 setup.py build" depending on your version of python
- The .exe should appear in "\build\exe.win-amd64-3.9\"
- Copy the "Language" folder and "icon.ico" in the same folder as your .exe
- Enjoy !

