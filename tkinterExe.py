import tkinter
from tkinter import *

root = Tk()


class AppVoiceRecognition:
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        root.mainloop()

    def screen(self):
        # Title
        self.root.title('Voice Recognition')
        # Configure
        self.root.configure(background=""'black')
        # Screen size when it starts
        self.root.geometry('1080x720')
        # Not able to screen resize
        self.root.resizable(False, False)

    def frames_screen(self):
        self.frame_first = Frame(self.root)
        self.frame_second = Frame(self.root)
        self.frame_first.place(relx=0.1, rely=0.06, relheight=0.4, relwidth=0.8)
        self.frame_second.place(relx=0.1, rely=0.5, relheight=0.4, relwidth=0.8)


AppVoiceRecognition()
