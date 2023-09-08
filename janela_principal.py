import tkinter as tk
from tkinter import PhotoImage
#Para fazer a importação https://blog.finxter.com/how-to-install-pillow-on-pycharm/
from PIL import Image, ImageTk

# Janela Principal
def mostra_janela_principal():
    janela_principal = tk.Tk()
    janela_principal.title("Carta Amiga")

    #Atribuir dimenões jnalea
    largura_janela = 800
    altura_janela =  900

    window_geometry = f"{largura_janela}x{altura_janela}"

    janela_principal.geometry(window_geometry)

    frame_titulo_cor = "#f6a2a6"

    #Percentagem cada frame
    frame_titulo_percentagem =70
    frame_img_carta_percentagem = 30
    frame_titulo_altura_percentagem = 30
    frame_logo_altura_percentagem = 70

    #Determinar as larguras
    largura_frame_titulo = (largura_janela * frame_titulo_percentagem) // 100
    largura_frame_img_carta = (largura_janela * frame_img_carta_percentagem) // 100

    altura_frame_titulo = (altura_janela * frame_titulo_altura_percentagem) // 100
    altura_frame_logo = (largura_janela * frame_logo_altura_percentagem) // 100

    frame_titulo = tk.Frame(janela_principal, bg=frame_titulo_cor, width=largura_frame_titulo, height=altura_janela)
    frame_img_carta = tk.Frame(janela_principal, bg="blue", width=largura_frame_img_carta, height=altura_janela)

    frame_titulo_interior = tk.Frame(frame_titulo, bg=frame_titulo_cor, width=largura_frame_titulo, height=altura_frame_titulo)
    frame_logo = tk.Frame(frame_titulo, bg="red", width=largura_frame_titulo, height=altura_frame_logo)

    # Place the frames side by side
    frame_titulo.grid(row=0, column=0)
    frame_img_carta.grid(row=0, column=1)

    frame_titulo_interior.grid(row=0, column=0)
    frame_logo.grid(row=1, column=0)


    # Create and place labels, text, and buttons for your landing page
    label_titulo = tk.Label(frame_titulo_interior, text="Carta Amiga", font=("Radley", 41))
    label_titulo.pack()

     # Supported formats: GIF, PGM, PPM, and PNG
    #img_porta = ImageTk.PhotoImage("Imagens\\porta.gif")

    #label_img_porta= tk.Label(frame_titulo_interior, image=img_porta)
    #label_img_porta.pack()

    bLogin = tk.Button(frame_titulo_interior, text="Entrar", command=funcaoEntrar)
    bLogin.pack()

    # A biblioteca tkinter não reconhece diretamente imagens do tipo .jpg, por isso usado a seguinte trexo de código para a conversao
    img_auxiliar = Image.open("Imagens\\cartas.jpg")  # Supported formats: GIF, PGM, PPM, and PNG
    img_carta = ImageTk.PhotoImage(img_auxiliar)

    # Create a label to display the image
    label_img_carta = tk.Label(frame_img_carta, image=img_carta)
    label_img_carta.pack()

    #Carregar logo
    img_auxiliar = Image.open("Imagens\\idoso_ao_computador2.jpg")
    img_logo= ImageTk.PhotoImage(img_auxiliar)

    label_img_logo = tk.Label(frame_logo, image=img_logo)
    label_img_logo.pack()

    return janela_principal # tipo de retorno é do tipo tk.TK

    # Run the main loop
    #janela_principal.mainloop()


def funcaoEntrar():
    print("Entrou")
#
#frame_logo = tk.Frame(janela_principal, bg=red, width="60%",height="100%")
#frame_imagem_cartas = tk.Frame(janela_principal, bg="blue", width="40%", height="100%")
#
#
#label = tk.Label(janela_principal, text="Uma comunicação segura", font=("Ovo", 35))
#label.pack(pady=20)
