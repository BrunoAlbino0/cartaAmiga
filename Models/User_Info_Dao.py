from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, declarative_base
from Models.Session import DbSession
from Models.DatabaseModels import UserInfo

class User_Info_Dao():

    def __init__(self, session):
        self.session = session

    def get_user_info_by_id(self, user_id):
        print("A Iniciar pesquisa pelo nome")
        return self.session.execute(select(UserInfo).where(UserInfo.user_info_id == user_id))

    def user_info_search_by_name(self, name):
        print("A iniciar procura pelo nome: " + name)
        return self.session.execute(select(UserInfo).where(UserInfo.name == name))

    def check_user_name_availability(self, name):
        print("A verificar se o nome inserido já foi registado: "+ name)
        search_result = self.user_info_search_by_name(name)
        number_of_records = 0

        for record in search_result:
            number_of_records +=1

        if number_of_records > 0:
            return False
        else:
            return True

    def check_user_login(self, name, password):
        search_result = self.user_info_search_by_name(name).first()

        number_of_records = 0
        id_user = 0
        password_from_DB = ""

        for record in search_result:
            number_of_records += 1
            id_user = record.user_info_id
            password_from_DB = record.password

        if number_of_records == 1:
            if password_from_DB == password:
                return id_user
            else:
                return 0
        else:
            return 0

    def add_user_info(self, user_name, user_password, administrator):
        newUser = UserInfo(user_name, user_password, administrator)
        self.session.add(newUser)
        self.session.commit()

    def list_all_users(self):
        search_result = self.session.query(UserInfo).all()

        print("ID:\t Name:\n")
        for record in search_result:
            print(str(record.user_info_id) +"\t" + record.name);
