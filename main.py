# Tkinter Components
from tkinter import *
import tkinter as tk
import pyautogui as pag, datetime

print("""
Name :: Digital Clock
Version :: 1.0
Note* :: On click ☀ icon to change the background
""")

class digiClock:

    def __init__(self):

        self.ClickColor = False

        self.defaultBg = "#000"
        self.defaultFg = "skyblue"

        self.customBg = "#fff"
        self.customFg = "#000"
        
        self.ClockWind = Tk()
        self.ClockWind.title("Digital Clock")
        self.ClockWind.geometry("400x50+1000+100")
        self.ClockWind.resizable(0,0)
        self.ClockWind.iconbitmap("assets/logoIco.ico")
        self.ClockWind.configure(bg=self.defaultBg)
        self.ctime = Label(self.ClockWind, text="", font=("calibri bold",15, "bold"), foreground=self.defaultFg, background=self.defaultBg)
        self._clock()

        self.changeBtn = Button(self.ClockWind, text="☀", width=4, bg=self.defaultBg, fg=self.defaultFg, bd=0, command=self._changeBgFg)
        self.changeBtn.pack(side="left", ipadx=5)

    def _changeBgFg(self):
        if not self.ClickColor:
            self.ClockWind.configure(bg=self.customBg)
            self.ctime.config(background=self.customBg)
            self.ctime.config(foreground=self.customFg)
            self.changeBtn.config(bg=self.customBg)
            self.changeBtn.config(fg=self.customFg)
            self.ClickColor = True
        else:
            self.ClockWind.configure(bg=self.defaultBg)
            self.ctime.config(background=self.defaultBg)
            self.ctime.config(foreground=self.defaultFg)
            self.changeBtn.config(bg=self.defaultBg)
            self.changeBtn.config(fg=self.defaultFg)
            self.ClickColor = False
            
        return True

    def _clock(self):
        now = datetime.datetime.now().strftime("%I:%M:%S %p - %d.%m.%Y")
        self.ctime.pack(side="left", ipadx=5)#place(x = 5,y = 5)
        self.ctime.config(text=now)
        self.ctime.after(1000, self._clock)

    def runModule(self):
        self.ClockWind.mainloop()

mod = digiClock()
mod.runModule()
