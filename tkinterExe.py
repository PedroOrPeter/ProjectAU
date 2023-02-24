import tkinter
from tkinter import *

root = Tk()


class AppVoiceRecognition:
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        self.button()
       #self.labels_entrys_first()
       # self.labels_entrys_second()
        root.mainloop()

    def screen(self):
        # Title
        self.root.title('Voice Recognition')
        # Configure
        self.root.configure(background='#7D776B')
        # Screen size when it starts
        self.root.geometry('1080x720')
        # Not able to screen resize
        self.root.resizable(False, False)

    def frames_screen(self):
        self.frame_first = Frame(self.root, highlightbackground='black', bg='#DDDDDD')
        self.frame_first.place(relx=0.35, rely=0.06, relheight=0.8, relwidth=0.3)

    def button(self):
        self.button_enter_first = Button(self.frame_first, bg='green', text='Enter', font=('Arial', 15))
        self.button_enter_first.place(relx=0.62, rely=0.83, relheight=0.1, relwidth=0.3)

AppVoiceRecognition()
