from Models.Model import Model
from views.main import View

class LoginPageController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["loginPage"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.btn_Exit.config(command=self.click_on_exit)
        self.frame.btn_Login.config(command=self.click_login)
        self.frame.btn_Regist_New_User.config(command=self.click_regist)

    def click_regist(self):
        new_nickname = self.frame.Input_nickname_unregisted.get()
        new_password = self.frame.Input_password_unregisted.get()
        print("Clicou para registar com nickname: " + new_nickname + " e password: " +  new_password )

        self.model.user_info_search_by_name(self.model, new_nickname)

    def click_login(self):
        login_nickname = self.frame.Input_nickname_registed.get()
        login_password = self.frame.Input_password_registed.get()
        print("Clicou em login com nickname: " + login_nickname + " e password: " + login_password)

        self.model.user_info_search_by_name(self.model, login_nickname)

    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()

