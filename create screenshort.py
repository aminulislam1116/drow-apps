import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root=tk.Tk()
canvas1=tk.Canvas(root,width=180,height=150)
canvas1.pack()

def take():
    myscreenshote=pyautogui.screenshot()
    save=asksaveasfilename()
    myscreenshote.save(save+"_screenshote.png")

mybutton=tk.Button(text='Take Screenshot',command=take,font=10)
canvas1.create_window(100,100,window=mybutton)

root.mainloop()