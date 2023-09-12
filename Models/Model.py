from Models.Session import DbSession
from Models.User_Info_Dao import User_Info_Dao
from Models.Letter_Dao import Letter_Dao

class Model:

    def __init__(self):
        self.user_logged = False
        self.user_id = 0
        self.session = DbSession().dbsession
        self.user_info_dao = User_Info_Dao(self.session)
        self.selected_letter_id = 0
        self.letter_dao = Letter_Dao(self.session)

    def user_info_search_by_id(self, user_id):
        print("Recebi no modelo: " + user_id)
        return self.user_info_dao.user_info_search_by_id(user_id)

    def user_info_search_by_name(self, user_name):
        print("Recebi no modelo: " + user_name)
        return self.user_info_dao.user_info_search_by_name(user_name)

    def handle_user_regist(self, user_name, user_password, administrator):
        if self.user_info_dao.check_user_name_availability(user_name):
            self.user_info_dao.add_user_info(user_name, user_password, administrator)
        else:
            print("Nome já em uso!")


    def handle_user_login(self, user_name, user_passord):

        result = self.user_info_dao.check_user_login(user_name, user_passord)
        if result > 0:
            self.user_logged = True
            self.user_id = result
        else:
            self.user_logged = False
            self.user_id = 0


    def handle_letter_submition(self, title, message):
        print("Modelo a gravar carta")
        self.letter_dao.add_letter( self.user_id, 0, title, message)

