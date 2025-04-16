import json
from model.usuario import Usuario

class UsuarioStorage:
    FILE_PATH = "usuarios.json"

    def __init__(self):
        self.__users = self.load_users()
    
    '''Recebe um usuário, 
    adiciona-o à lista de usuários
    e chama a função save_users'''
    def add_user(self, user):
        if not isinstance(user, Usuario):
            raise TypeError("'user' deve ser um objeto da classe 'Usuario'.")
        self.__users.append(user)
        self.save_users(self.__users)

    '''tenta ler o arquivo json,
    converte os dados para um objeto
    da classe User e retorna 
    uma lista de objetos'''
    def load_users(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                users_data = json.load(file)

                users_object = []
                for user_data in users_data:
                    user = Usuario(**user_data)
                    users_object.append(user)

                return users_object
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do aruivo'''
    def save_users(self, users):
        users_data = []
        for user in users:
            users_data.append(user.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(users_data, file, ensure_ascii=False, indent=4)
        
        self.__users = users

    '''retorna a lista 'users' 
    de objetos 'Usuario' 
    convertida em dicionário'''
    def list_users(self):
        return [user.to_dict() for user in self.__users]
    
    '''retorna a lista 'users'
    de objetos 'Usuario' '''
    def list_objects_users(self):
        return [user for user in self.__users]