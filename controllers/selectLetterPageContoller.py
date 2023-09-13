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
        self.frame.btn_select_letter.config(command=self.clicK_letter_selected)
    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()

    def click_on_back(self):
        self.view.switch("menuPage")


    def populate_letter_tree(self):
        print("Entrada populate tree")
        self.frame.tree_letters.delete(*self.frame.tree_letters.get_children())
        data = self.model.handle_letter_request()

        print("Depois de chamada dos dados")

        try:
            for row in data:
                to_insert= [row[0], row[2], row[3]]
                self.frame.tree_letters.insert("", "end", values=to_insert)

        except TypeError:
            print("Erro tipo de dados")
            return

    def clicK_letter_selected(self):
       # print("Click no botão para selecionar")
        curItem = self.frame.tree_letters.focus()
        if curItem == '':
            print("Nenhuma carta selecionada")
            return

       # print(self.frame.tree_letters.item(curItem))

        id_letter = self.frame.tree_letters.item(curItem).get("values")
        id_letter = id_letter[0]

        print("Id carta: " + str(id_letter))
        self.model.selected_letter_id = id_letter
        self.view.switch("letterPage")


