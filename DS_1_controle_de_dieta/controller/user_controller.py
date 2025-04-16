from view.user_view import UserView
from model.user_manager import UserManager
from model.user import User

class UserController:

    def __init__(self):
        self.__user_view = UserView()
        self.__user_model = UserManager()

    def register_user(self):
        name, age, gender, weight, height, activity_level, goals = self.__user_view.creat_user()
        new_user = User(name, age, gender, weight, height, activity_level, goals)
        self.__user_model.add_user(new_user)
    
    def register_info(self):
        print("entrou na função de ver registro")
        users = self.__user_model.list_users()
        self.__user_view.show_user(users)

    def daily_consumption(self):
        print("entrou na função de consumo diário")
        pass

    def MB_and_GET(self):
        print("entrou na função de metabolismo basal e consumo diário")
        name = input("Digite o nome do usuário para calcular a TMB e o GET: ")
        user = self.__user_model.get_user_by_name(name)
        
        if user:
            tmb = user.calculate_basal_metabolism()
            get = user.calculate_total_energy_expenditure()
            print(f"TMB de {user.name}: {tmb:.2f} kcal")
            print(f"GET de {user.name}: {get:.2f} kcal")
        else:
            print("Usuário não encontrado.")

    def start_user_menu(self):
        valid_options = {
            "1": self.register_info,
            "2": self.daily_consumption,
            "3": self.MB_and_GET
        }
        while True:
            if self.__user_model.is_user_registered() == True:
                choose_option = self.__user_view.options()
                if choose_option in valid_options:
                    valid_options[choose_option]()
            else:
                self.register_user()
