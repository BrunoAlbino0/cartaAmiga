from Models.Model import Model
from views.main import View
class MenuPageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["menuPage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Exit.config(command=self.click_on_exit)
        self.frame.btn_Read_Letter.config(command=self.click_on_read)
        self.frame.btn_Write_Letter.config(command=self.click_on_write)


    def click_on_write(self):
        print("Click on write")
        self.model.selected_letter_id = 0
        self.view.switch("letterPage")
    def click_on_read(self):
        print("Click on read")
        self.view.switch("selectLetterPage")
        #self.model.handle_letter_request()

    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()
