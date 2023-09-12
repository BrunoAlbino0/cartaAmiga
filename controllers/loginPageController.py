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
        self.frame.btn_list_all_users.config(command=self.list_all_Users)

    def click_regist(self):
        new_nickname = self.frame.Input_nickname_unregisted.get()
        new_password = self.frame.Input_password_unregisted.get()

        #Validar Input
        if self.input_validation(new_nickname, new_password) == False: return

        if len(new_nickname) == 0 or len(new_password) == 0 or new_nickname.find(" ") != -1:
            if len(new_nickname) == 0:
                print("Preencha o nome")

            if new_nickname.find(" ") != -1:
                print("O nome não pode conter espaços em branco")

            if len(new_password) == 0:
                print("Preencha a password!")

            return

        print("A entrar na validação de nome")
        self.model.handle_user_regist(new_nickname, new_password, False)

        if self.model.user_logged == True:
            print("Registado com sucesso")
            self.view.switch("welcomePage")
        else:
            print("Erro a registar")

    def click_login(self):
        login_nickname = self.frame.Input_nickname_registed.get()
        login_password = self.frame.Input_password_registed.get()

        if self.input_validation(login_nickname, login_password) == False: return

        self.model.handle_user_login(login_nickname, login_password)
        if self.model.user_logged == True:
            print("Login Efetuado com sucesso")
            self.view.switch("welcomePage")
        else:
            print("Erro a e efutaur login")

    def click_on_exit(self):
        print("Click Exit")
        self.view.stop_mainloop()

    def input_validation(self, username, password):
        # Validar Input
        if len(username) == 0 or len(password) == 0 or username.find(" ") != -1:
            if len(username) == 0:
                print("Preencha o nome")

            if username.find(" ") != -1:
                print("O nome não pode conter espaços em branco")

            if len(password) == 0:
                print("Preencha a password!")

            return False

        return True

    def list_all_Users(self):
        self.model.user_info_dao.list_all_users()