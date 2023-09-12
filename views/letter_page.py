from tkinter import Frame, Label, Button,PhotoImage,Entry

class LetterPage(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.label_titulo = Label(self, text="Friendly Letter", font=("Radley", 41))
        self.label_titulo.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_Exit = Button(self, text="Exit")
        self.btn_Exit.grid(row=0, column=1, padx=10, pady=10)

        self.label_letter_tittle = Label(self, text="Tittle:")
        self.Input_letter_tittle = Entry(self)
        self.label_letter_tittle.grid(row=1, column=0, padx=10, sticky="w")
        self.Input_letter_tittle.grid(row=2, column=0, padx=(0, 20), sticky="ew")

        self.label_letter_tittle = Label(self, text="Content")
        self.label_letter_tittle.grid(row=3, column=0, padx=10, sticky="w")
        self.Input_letter_content = Entry(self)
        self.Input_letter_content.grid(row=4, padx=(0, 20), sticky="ew")

        self.btn_go_back = Button(self, text="Return")
        self.btn_go_back.grid(row=5, column=0, padx=10, pady=10)

        self.btn_save_letter = Button(self, text="Save")
        self.btn_save_letter.grid(row=5, column=1, padx=10, pady=10)