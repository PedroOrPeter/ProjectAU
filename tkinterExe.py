import tkinter
from tkinter import *

root = Tk()

class AppVoiceRecognition():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title('Voice Recognition')
        self.root.configure(background='black')

AppVoiceRecognition()