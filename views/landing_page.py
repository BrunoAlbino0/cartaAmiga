import tkinter
from tkinter import Frame, Label, Button,PhotoImage
#Para fazer a importação https://blog.finxter.com/how-to-install-pillow-on-pycharm/
from PIL import Image, ImageTk
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

class LandingPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color= "#ffffff"
        self.configure(bg=background_color)

        self.grid_columnconfigure(0,weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), fg=main_tittle_color, bg=background_color)
        self.label_secure_communication = Label(self, text="Secure communication", font=("Radley", 30), bg=background_color)

        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.label_secure_communication.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

#Tentativa de adicionar imagem
       # self.img_auxiliar = Image.open("marco_correio.jpg")  # Supported formats: GIF, PGM, PPM, and PNG
        #width = 100
        #height = 120
       # self.img_auxiliar = self.img_auxiliar.resize((width, height), Image.ANTIALIAS)
        #self.img_marco_correio = ImageTk.PhotoImage(self.img_auxiliar)

        self.btn_Advance = Button(self, text="Entrar")
        self.btn_Advance.grid(row=0, column=1, padx=10, pady=10)

        #Carregar logo
       # img_auxiliar = Image.open(r"..\Imagens\idoso_ao_computador2.jpg")
        rel_path =r"../Imagens/idoso_ao_computador2.jpg"
        abs_file_path = os.path.join(script_dir, rel_path)

        self.img_auxiliar = Image.open(abs_file_path)
        new_size = (550, 400)
        self.img_auxiliar = self.img_auxiliar.resize(new_size)

        self.img_logo = ImageTk.PhotoImage(self.img_auxiliar)

        self.Label_Img_Logo = Label(self, image=self.img_logo)
        self.Label_Img_Logo.grid(row=2, column=0)

        #self.Label_Teste = Label(self, text="Teste")
        #self.Label_Img_Logo.grid(row=2, column=0)
