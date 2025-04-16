import json
from model.food import Food

class Menu:
    FILE_PATH = "menu.json"

    def __init__(self):
        self.menu = self.__load_menu()

    def add_food_to_menu(self, food):
        """Adiciona uma nova comida e salva no JSON."""
        if not isinstance(food, Food):
            raise TypeError("O objeto precisa ser uma instância de Food.")
        
        self.menu.append(food)
        self.__save_menu()

    def remove_food_from_menu(self, name):
        """Remove uma comida pelo nome e salva no JSON."""
        self.menu = [food for food in self.menu if food.name != name]
        self.__save_menu()

    def __save_menu(self):
        """Salva a lista de alimentos no arquivo JSON."""
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([food.to_dict() for food in self.menu], file, indent=4)

    def __load_menu(self):
        """Carrega os alimentos do arquivo JSON."""
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                menu_data = json.load(file)
                return [Food(**data) for data in menu_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Arquivo menu.json não encontrado ou corrompido. Criando um novo arquivo.")
            return []

    def list_menu(self):
        """Lista todos os alimentos cadastrados."""
        return self.menu