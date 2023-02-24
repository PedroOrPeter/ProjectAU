import tkinter
from tkinter import *

root = Tk()


class AppVoiceRecognition:
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        # Title
        self.root.title('Voice Recognition')
        # Configure
        self.root.configure(background='black')
        # Screen size when it starts
        self.root.geometry('1080x720')
        # Not able to screen resize
        self.root.resizable(False, False)


AppVoiceRecognition()
