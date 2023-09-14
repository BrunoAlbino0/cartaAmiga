from tkinter import Frame, Label, Button,PhotoImage,Entry

class MenuPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        background_color = "#f6a2a6"
        main_tittle_color = "#ffffff"
        self.configure(bg=background_color)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41, "bold"), bg=background_color, fg=main_tittle_color)
        self.label_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.btn_Write_Letter = Button(self, text="Write Letter")
        self.btn_Write_Letter.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        

        self.btn_Read_Letter = Button(self, text="Read Letter")
        self.btn_Read_Letter.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
