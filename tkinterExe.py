import tkinter
from tkinter import *

root = Tk()


class AppVoiceRecognition:
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        self.button()
        self.labels()
        self.entrys()
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

    def labels(self):
        self.lb_nome = Label(self.frame_first, text="Nome:", font=('Arial', 11), bg="#DDDDDD")
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.lb_sobrenome = Label(self.frame_first, text="Sobrenome:", font=('Arial', 11), bg="#DDDDDD")
        self.lb_sobrenome.place(relx=0.6, rely=0.05)

        self.lb_idade = Label(self.frame_first, text="Idade:", font=('Arial', 11), bg="#DDDDDD")
        self.lb_idade.place(relx=0.05, rely=0.2)

        self.lb_email = Label(self.frame_first, text="Email:", font=('Arial', 11), bg="#DDDDDD")
        self.lb_email.place(relx=0.6, rely=0.2)

        self.lb_motivo = Label(self.frame_first, text="Motivo pelo uso do robô:", font=('Arial', 11), bg="#DDDDDD")
        self.lb_motivo.place(relx=0.05, rely=0.4)

    def entrys(self):
        self.nome_entry = Entry(self.frame_first)
        self.nome_entry.place(relx=0.05, rely=0.1, relwidth=0.37)

        self.idade_entry = Entry(self.frame_first)
        self.idade_entry.place(relx=0.05, rely=0.25, relwidth=0.241)

        self.sobrenome_entry = Entry(self.frame_first)
        self.sobrenome_entry.place(relx=0.6, rely=0.1, relwidth=0.37)

        self.email_entry = Entry(self.frame_first)
        self.email_entry.place(relx=0.6, rely=0.25, relwidth=0.37)

        self.motivo_entry = Text(self.frame_first)
        self.motivo_entry.place(relx=0.05, rely=0.45, relwidth=0.7, relheight=0.3)


AppVoiceRecognition()
