from Models.Model import Model
from views.main import View
class WelcomePageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["welcomePage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Welcome.config(command=self.click_on_welcome)
        self.frame.btn_Exit.config(command=self.click_on_exit)
    def click_on_welcome(self):
        print("Welcome")
        self.view.switch("menuPage")

    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()