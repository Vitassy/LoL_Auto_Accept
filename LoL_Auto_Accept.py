import os

#Lib used to search img and move mouse
import pyautogui

#Lib used to make the window and interact with it
from tkinter import *


#Main function
def img():
    if toggle_button.config('text')[-1] == 'ON' :
        print ("Recherche en cours")
        imglocation = pyautogui.locateCenterOnScreen('accept.png', confidence=0.7)
        if imglocation != None:
            toggle_button.config(text='OFF')
            pyautogui.moveTo(imglocation,duration=0.2)
            pyautogui.click()
            print ("gl")
    imglocation2 = pyautogui.locateCenterOnScreen('notaccept.png', confidence=0.7)
    if imglocation2 != None :
        toggle_button.config(text='ON')
        print("Someone didn't accept!")
    root.after(2000,img)


#Get Language
def Lang():
    path = os.getcwd()
    os.chdir(os.path.join(path,"Languages"))
    path = os.getcwd()

    f_in = open("Options.txt","r",encoding="utf-8")
    text= f_in.readline()
    f_in.close()
    text=text[10:]
    text=text.strip()

    os.chdir(os.path.join(path,text))
    
#Button on/off
def Simpletoggle():
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        print("OFF")
    else:
        toggle_button.config(text='ON')
        print("ON")

#Window
root = Tk()
root.title("Skillz")
root.iconbitmap("icon.ico")
Hauteur = 0
Largeur = 200
(H,L,c) = (Hauteur,Largeur,"white")
Dessin = Canvas(root,height=H,width=L,bg=c)
Dessin.pack()

#Button
toggle_button = Button(text='OFF', width=10, command=Simpletoggle)
do = toggle_button['text']
toggle_button.pack(pady=10)


Lang()
#Loop
root.after(2000,img)
root.mainloop()


