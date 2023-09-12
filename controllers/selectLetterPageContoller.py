from Models.Model import Model
from views.main import View
class SelectLetterPageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["selectLetterPage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Exit.config(command=self.click_on_exit)
        self.frame.btn_Refresh.config(command=self.populate_letter_tree)
        self.frame.btn_return.config(command=self.click_on_back)
    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()

    def click_on_back(self):
        self.view.switch("menuPage")


    def populate_letter_tree(self):
        print("Entrada populate tree")
        data = self.model.handle_letter_request()

        try:
            for row in data:
                values = (data[0], data[2], data[3], data[4])
                self.frame.tree_letters.isert('', values=values)
        except TypeError:
            return