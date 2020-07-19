import tkinter as tk
from tkinter import filedialog, Text
import os
import time
import pyautogui

# get all inputs and start program 
def runmacrofb():
    for x in range(1, int(enti.get())):
        pyautogui.click(int(PosX), int(PosY))
        pyautogui.typewrite(ent.get())
        pyautogui.press("enter")
        time.sleep(int(entt.get()))

# only mouse macro
def runmacromouse():
    for x in range(1, int(enti.get())):
        pyautogui.click(int(PosX), int(PosY))
        time.sleep(int(entt.get()))

# Getting MousePosition program
PosX,PosY = 0,0
def MousePosition():
    global PosX, PosY
    time.sleep(5)
    PosX = pyautogui.position()[0]
    PosY = pyautogui.position()[1]

root = tk.Tk() # create window 



#words
tk.Label(root, text="What to type?(not reqUired when running mouse only)").grid(row=0)
tk.Label(root, text="How many times?").grid(row=1)
tk.Label(root, text="delay?").grid(row=2)
tk.Label(root, text="Run program").grid(row=3)
tk.Label(root, text="Run program using only amount and delay").grid(row=4)
tk.Label(root, text="Get mouse location(hover over point for 5 seconds)").grid(row=5)

# make entry places where u can type
ent = tk.Entry(root, width=25)
ent.grid(row=0, column=1)
enti = tk.Entry(root, width=22)
enti.grid(row=1, column=1)
entt = tk.Entry(root, width=20)
entt.grid(row=2, column=1)


# creating pressable buttons that run commands which can be seen above
runmacrobutton = tk.Button(root, text="Run Macro", padx=10, pady=5, fg="white", bg="black", command=runmacrofb)
runmacrobutton.grid(row=3, column=1)

runmacromousebt = tk.Button(root, text="Run Mouse only macro", padx=10, pady=5, fg="white", bg="black", command=runmacromouse)
runmacromousebt.grid(row=4, column=1)

runMousepositionbutton = tk.Button(root, text="Get mouse location", padx=10, pady=5, fg="white", bg="black", command=MousePosition)
runMousepositionbutton.grid(row=5, column=1)

root.mainloop() # ending project




