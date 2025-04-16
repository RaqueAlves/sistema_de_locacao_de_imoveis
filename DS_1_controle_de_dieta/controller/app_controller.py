from controller.user_controller import UserController
from controller.food_controller import FoodController
from view.app_view import AppView

class AppController:

    def __init__(self):
        self.__user_controller = UserController()
        self.__food_controller = FoodController()
        self.__app_view = AppView()

    def open_user(self):
        self.__user_controller.start_user_menu()

    def open_food(self):
        self.__food_controller.start_food_controler()

    def options_menu(self):
        app_options_list = {
            "1": self.open_user,
            "2": self.open_food
        }

        while True:
            select_option = self.__app_view.options()
            if select_option in app_options_list:
                app_options_list[select_option]()
            else:
                self.__app_view.popup("Opção inválida!")