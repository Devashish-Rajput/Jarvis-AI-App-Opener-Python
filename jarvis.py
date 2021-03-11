import numpy as np 
import cv2 
import pyautogui 
import speech_recognition
from fuzzywuzzy import process
import time
import os
import pyttsx3

path='Your Path\\'
#path='apps shortcut\\' with '\\' symbol and it shoudl be apps shortcut 
apps = [x for x in os.listdir(path)]
engine = pyttsx3.init() 
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def function_1(): 
    win.attributes('-alpha', 0)
    time.sleep(0.5)
    image = pyautogui.screenshot() 
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    with open('E:/Library/Python Project/num.txt',encoding='utf8') as f:
        ck = [line.rstrip() for line in f]
    c = int(ck[0])
    x="E:/Library/Pictures/image"+str(c)+".png"
    cv2.imwrite(x, image)
    #print("Screenshot Taken!")
    c=c+1
    with open("E:/Library/Python Project/num.txt", "w") as outfile:
        outfile.write(str(c))
    win.attributes('-alpha', 1.0)    


def function_2():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            
            audio = recognizer.listen(src)
            str2Match = recognizer.recognize_google(audio).lower()

            highest = process.extractOne(str2Match,apps)
            if highest[1]>40:
                appL=path+str(highest[0])
                os.startfile(appL)
                engine.say("Opening"+str(highest[0]))  
                engine.runAndWait()    
        except Exception as ex:
            print("Sorry. Could not understand.")

############################################### Tkinter Window #################################

from tkinter import *
import tkinter as tk
win = Tk()
win.attributes('-topmost', True) # note - before topmost
win.overrideredirect(True)
win.geometry("80x35+750+1010")
win.attributes('-topmost', True) # note - before topmost
win.resizable(0,0)
def close_program():
    win.destroy()

def disable_event():
    pass

btn = tk.Button(win, text = "S", command = function_1)
btn.pack(side=LEFT)
tcn = tk.Button(win, text = "Y", command = quit)
tcn.pack(side=LEFT)
tcn = tk.Button(win, text = "R", command = quit)
tcn.pack(side=LEFT)
tcn = tk.Button(win, text = "L", command = function_2)
tcn.pack(side=LEFT)


win.protocol("WM_DELETE_WINDOW", disable_event)

win.mainloop()

  
