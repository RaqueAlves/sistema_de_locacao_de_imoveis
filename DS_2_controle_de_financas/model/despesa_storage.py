import json
from model.despesa import Despesa

class DespesaStorage:
    FILE_PATH = "despesas.json"

    def __init__(self):
        self.__expenses = self.load_expenses()
    
    '''Recebe um usuário, 
    adiciona-o à lista de usuários
    e chama a função save_users'''
    def add_expense(self, expense):
        if not isinstance(expense, Despesa):
            raise TypeError("'user' deve ser um objeto da classe 'Usuario'.")
        self.__expenses.append(expense)
        self.save_expenses(self.__expenses)

    '''tenta ler o arquivo json,
    converte os dados para um objeto
    da classe User e retorna 
    uma lista de objetos'''
    def load_expenses(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                expenses_data = json.load(file)

                expenses_object = []
                for ex in expenses_data:
                    expense = Despesa(**ex)
                    expenses_object.append(expense)

                return expenses_object
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do aruivo'''
    def save_expenses(self, expenses):
        expenses_data = []
        for ex in expenses:
            expenses_data.append(ex.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(expenses_data, file, ensure_ascii=False, indent=4)
        
        self.__expenses = expenses

    '''retorna a lista 'users' 
    de objetos 'Usuario' 
    convertida em dicionário'''
    def list_expenses(self):
        return [expense.to_dict() for expense in self.__expenses]