"#Lol_Auto_Accept" 

Already compiled file (the .exe) download link : 
- https://mega.nz/file/S8xmFY4I#VMKhsp5-y0uB6uTK-Fa73VjeT30FdiFSDZDCW-TW9_c


Features:
- Click on the on/off button to start the search of a staring game
- The programm will automatically set to off once it found the game so no risk of clicking somewhere once you've started the game
- If someone didn't accept the game the program will switch to "on" mode to search again
- That's it !

How to add your own language :
- Take a screenshot of the "accept" button of your game and cut it to only have the button using any image edit software (from paint to photoshop the choice is yours) and rename it "accept.png"
- Do the same when someone doesn't accept the game (just take a part of the sentence like "declined ready check") and rename it "notaccept.png"
- The images don't have to be precise just be carefull you don't have any background showing and save them to .png
- Create a new folder inside the "Languages" one (call it wathever you want but i reccomand using the language you're aiming to add) and put the two images you just cropped inside it.
- Open the "Option.txt" file located in the "Languages" folder. Change the first line to "Language = [The name of the folder you just created]"
- This should work !


How to compile the code into an .exe using cx_Freeze (https://cx-freeze.readthedocs.io/en/latest/index.html): 
- Install cx_Freeze (by using pip : most likely by typing "python -m pip install --upgrade cx_Freeze" or "python3 -m pip install --upgrade cx_Freeze" on your command prompt) 
- Open your command prompt and move to the directory where the script are
- Type "python setup.py build" or "python3 setup.py build" depending on your version of python
- The .exe should appear in "\build\exe.win-amd64-3.9\\" ("exe.win-amd64-3.9" will change according to your os and python version)
- Copy the "Language" folder and "icon.ico" in the same folder as your .exe
- Enjoy !
