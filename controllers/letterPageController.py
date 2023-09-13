from Models.Model import Model
from views.main import View
class LetterPageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["letterPage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Exit.config(command=self.click_on_exit)
        self.frame.btn_go_back.config(command=self.click_on_back)
        self.frame.btn_save_letter.config(command=self.click_on_save)
        self.frame.btn_show_letter.config(command=self.mostra_carta)
    def click_on_welcome(self):
        print("Welcome")
        self.view.switch("welcomePage")

    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()

    def click_on_back(self):
        if self.model.selected_letter_id == 0:
            self.view.switch("menuPage")
        else:
            self.model.selected_letter_id = 0
            self.view.switch("selectLetterPage")


    def click_on_save(self):
        print("Click on save")

        title = self.frame.Input_letter_tittle.get()
        message = self.frame.Input_letter_content.get()

        if len(title) != 0 or len(message) != 0:
            self.model.handle_letter_submition(title, message)
        else:
            print("Insira um titulo e o conteudo da carta")

    def mostra_carta(self):
        if self.model.selected_letter_id == 0:
            self.frame.Input_letter_tittle.insert(0, "")
            self.frame.Input_letter_content.insert(0, "")
        else:
            letter_data = self.model.get_letter_data()
            if len(letter_data) > 0:
                self.frame.Input_letter_tittle.insert(0, letter_data[0])
                self.frame.Input_letter_content.insert(0, letter_data[1])
