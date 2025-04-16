import json
from model.categoria import Categoria

class CategoriaStorage:
    FILE_PATH = "categorias.json"

    PREDEFINED_CATEGORIES = [
        "Educação", 
        "Energia", 
        "Água", 
        "Internet", 
        "Alimentação", 
        "Transporte", 
        "Residência", 
        "Entretenimento"
    ]

    def __init__(self):
        self.__categories = self.load_categories()

        if not self.__categories:
            self.add_default_categories()
    
    '''Recebe uma categoria, 
    adiciona-o à lista de categorias
    e chama a função save_categories'''
    def add_category(self, category):
        if not isinstance(category, Categoria):
            raise TypeError("'category' deve ser um objeto "
            "da classe 'Category'.")
        self.__categories.append(category)
        self.save_categories()

    '''tenta ler o arquivo json,
    converte os dados para um objeto
    da classe Categoria e retorna 
    uma lista de objetos'''
    def load_categories(self):
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                categories_data = json.load(file)

                categories_object = []
                for category_data in categories_data:
                    category = Categoria(**category_data)
                    categories_object.append(category)

                return categories_object
            
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    '''abre ou cria um arquivo json
    caso não exista e salva os dados 
    dentro do arquivo'''
    def save_categories(self, categories):
        categories_data = []
        for c in categories:
            categories_data.append(c.to_dict())

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(categories_data, file, ensure_ascii=False, indent=4)
        
        self.__categories = categories

    '''retorna a lista 'categories' 
    de objetos 'Categoria' 
    convertida em dicionário'''
    def list_categories(self):
        return [category.to_dict() for category in self.__categories]
    
    '''retorna a lista 'categories'
    de objetos 'Categoria' '''
    def list_objects_categories(self):
        return [category for category in self.__categories]
    
    '''cria uma lista de categorias 
    padrão e salva as categorias'''
    def add_default_categories(self):
        add_categories = [Categoria(nome=nome, limite=None) for nome in self.PREDEFINED_CATEGORIES]
        self.__categories.extend(add_categories)
        self.save_categories(self.__categories)