import tkinter
from tkinter import *

root = Tk()


class AppVoiceRecognition:
    def __init__(self):
        self.root = root
        self.screen()
        self.frames_screen()
        self.button()
        self.labels_entrys_first()
        self.labels_entrys_second()
        root.mainloop()

    def screen(self):
        # Title
        self.root.title('Voice Recognition')
        # Configure
        self.root.configure(background='#34495E')
        # Screen size when it starts
        self.root.geometry('1080x720')
        # Not able to screen resize
        self.root.resizable(False, False)

    def frames_screen(self):
        self.frame_first = Frame(self.root, bd=6, highlightbackground='black', highlightthickness=2)
        self.frame_second = Frame(self.root, bd=6, highlightbackground='black', highlightthickness=2)
        self.frame_first.place(relx=0.1, rely=0.06, relheight=0.4, relwidth=0.8)
        self.frame_second.place(relx=0.1, rely=0.5, relheight=0.4, relwidth=0.8)

    def button(self):
        self.button_enter_first = Button(self.frame_first, bg='green', text='Enter', font=('Arial', 15))
        self.button_enter_second = Button(self.frame_second, bg='green', text='Enter', font=('Arial', 15))
        self.button_enter_first.place(relx=0.78, rely=0.78, relheight=0.2, relwidth=0.2)
        self.button_enter_second.place(relx=0.78, rely=0.78, relheight=0.2, relwidth=0.2)

    def labels_entrys_first(self):
        self.lb_nome = Label(self.frame_first, text= "Nome:")
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.nome_entry = Entry(self.frame_first)
        self.nome_entry.place(relx=0.1, rely=0.05, relwidth=0.15)

        self.lb_sobrenome = Label(self.frame_first, text="Sobrenome:")
        self.lb_sobrenome.place(relx=0.05, rely=0.2)

        self.sobrenome_entry = Entry(self.frame_first)
        self.sobrenome_entry.place(relx=0.134, rely=0.2, relwidth=0.15)

        self.lb_idade = Label(self.frame_first, text="Idade:")
        self.lb_idade.place(relx=0.35, rely=0.05)

        self.idade_entry = Entry(self.frame_first)
        self.idade_entry.place(relx=0.4, rely=0.05, relwidth=0.15)

        self.lb_email = Label(self.frame_first, text="Email:")
        self.lb_email.place(relx=0.35, rely=0.2)

        self.email_entry = Entry(self.frame_first)
        self.email_entry.place(relx=0.4, rely=0.2, relwidth=0.15)

        self.lb_motivo = Label(self.frame_first, text="Motivo:")
        self.lb_motivo.place(relx=0.05, rely=0.4)

        self.motivo_entry = Entry(self.frame_first)
        self.motivo_entry.place(relx=0.11, rely=0.4, relwidth=0.7, relheight=0.3)

    def labels_entrys_second(self):
        self.lb_nome = Label(self.frame_second, text="Nome:")
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.nome_entry = Entry(self.frame_second)
        self.nome_entry.place(relx=0.1, rely=0.05, relwidth=0.15)

        self.lb_sobrenome = Label(self.frame_second, text="Sobrenome:")
        self.lb_sobrenome.place(relx=0.05, rely=0.2)

        self.sobrenome_entry = Entry(self.frame_second)
        self.sobrenome_entry.place(relx=0.134, rely=0.2, relwidth=0.15)

        self.lb_idade = Label(self.frame_second, text="Idade:")
        self.lb_idade.place(relx=0.35, rely=0.05)

        self.idade_entry = Entry(self.frame_second)
        self.idade_entry.place(relx=0.4, rely=0.05, relwidth=0.15)

        self.lb_email = Label(self.frame_second, text="Email:")
        self.lb_email.place(relx=0.35, rely=0.2)

        self.email_entry = Entry(self.frame_second)
        self.email_entry.place(relx=0.4, rely=0.2, relwidth=0.15)

        self.lb_motivo = Label(self.frame_second, text="Motivo:")
        self.lb_motivo.place(relx=0.05, rely=0.4)

        self.motivo_entry = Entry(self.frame_second)
        self.motivo_entry.place(relx=0.11, rely=0.4, relwidth=0.7, relheight=0.3)


AppVoiceRecognition()
