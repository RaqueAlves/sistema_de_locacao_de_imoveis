import json
from model.user import User
from model.daily_consumption import DailyConsumption
from model.food import Food

class UserManager:
    FILE_PATH = "users.json"

    def __init__(self):
        self.users = self.load_users()

    def add_user(self, user):
        """Adiciona um novo usuário e salva no JSON."""
        if not isinstance(user, User):
            raise TypeError("O objeto precisa ser uma instância de User.")
        
        self.users.append(user)
        self.save_users()

    def remove_user(self, name):
        """Remove um usuário pelo nome e salva no JSON."""
        self.users = [user for user in self.users if user.name != name]
        self.save_users()

    def save_users(self):
        """Salva a lista de usuários no arquivo JSON."""
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_users(self):
        """Carrega os usuários do arquivo JSON."""
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                users_data = json.load(file)
                users = []

                for data in users_data:
                    # Remove "daily_consumption" antes de criar o User
                    daily_consumption_data = data.pop("daily_consumption", [])

                    user = User(**data)

                    # Reconstrói a lista de consumo diário
                    user._daily_consumption = [
                        DailyConsumption(
                            food=Food(**consumption["food"]),
                            quantity_grams=consumption["quantity_grams"],
                            date=consumption["date"]
                        )
                        for consumption in daily_consumption_data
                    ]

                    users.append(user)
                return users
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def list_users(self):
        """Lista todos os usuários cadastrados."""
        return self.users

    def is_user_registered(self):
        """Verifica se já há um usuário cadastrado no banco de dados (arquivo JSON)."""
        if len(self.users) > 0:
            return True
        return False
    
    def get_user_by_name(self, name):
        """Retorna um usuário pelo nome, se existir."""
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None