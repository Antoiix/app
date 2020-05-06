from tkinter import *
import webbrowser


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("RandomsApp")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("favicon.ico")
        self.window.config(background='#cff4e5')

        self.frame = Frame(self.window, bg='#cff4e5')

        self.create_widgets()

        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_quit_button()
        self.create_file_menu()
        self.create_youtube_button()

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur RandomsApp", font=("Arial", 40), bg='#cff4e5',
                            fg='#7a807d')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Cliquez sur le bandeau au dessus pour choisir votre Random", font=("Arial", 25), bg='#cff4e5',
                               fg='#7a807d')

    def create_quit_button(self):
        quit_button = Button(self.frame, text="Quitter", font=("Arial", 25), bg='white', fg='#7a807d',
                             command=self.window.quit)
        quit_button.pack(pady=25, fill=X)

    def create_file_menu(self):
        menu_bar = Menu(self.window)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Quitter", command=self.window.quit)
        self.window.config(menu=menu_bar)

    def create_youtube_button(self):
        yt_button = Button(self.frame, text="Ouvrir Youtube", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.open_yt)
        yt_button.pack(pady=25, fill=X)

    def open_yt(self):
        webbrowser.open_new("http://youtube.com/")


app = MyApp()
app.window.mainloop()
