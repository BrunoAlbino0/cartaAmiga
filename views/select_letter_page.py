from tkinter import Frame, Label, Button,PhotoImage,Entry

class SelectLetterPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.label_New_Letters = Label(self, text="New Letters", font=("Radley", 41))
        self.label_New_Letters.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
