from tkinter import Frame, Label, Button,PhotoImage
#Para fazer a importação https://blog.finxter.com/how-to-install-pillow-on-pycharm/
from PIL import Image, ImageTk

class LandingPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.grid_columnconfigure(0,weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

#Tentativa de adicionar imagem
       # self.img_auxiliar = Image.open("marco_correio.jpg")  # Supported formats: GIF, PGM, PPM, and PNG
        #width = 100
        #height = 120
       # self.img_auxiliar = self.img_auxiliar.resize((width, height), Image.ANTIALIAS)
        #self.img_marco_correio = ImageTk.PhotoImage(self.img_auxiliar)

        self.btn_Advance = Button(self, text="Entrar")
        self.btn_Advance.grid(row=0, column=1, padx=10, pady=10)

        #Carregar logo
        #img_auxiliar = Image.open("..\\Imagens\\idoso_ao_computador2.jpg")
         #img_logo= ImageTk.PhotoImage(img_auxiliar)
        self.Label_Img_Logo = Label(self, text="Suposto Logo")
        self.Label_Img_Logo.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
