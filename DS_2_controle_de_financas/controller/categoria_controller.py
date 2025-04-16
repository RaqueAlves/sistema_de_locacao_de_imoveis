from model.categoria_storage import CategoriaStorage
from model.categoria import Categoria

class CategoriaController:

    def __init__(self):
        self.storage = CategoriaStorage()

    '''
    verifica se uma dada categoria existe,
    se sim, apenas modifica o valor limite,
    caso contrário,   
    cria uma nova Categoria com 
    os parametros recebidos,
    adiciona a nova categoria à
    lista recebida, salva a lista
    completa e por fim retorna 
    a nova categoria'''
    def cadastrar_categoria(self, nome, limite):

        #carrega uma lista de categorias
        categorias = self.storage.load_categories() 
        check_category = self.finds_category_by_name(nome, categorias)
        if check_category == None:
            nova_categoria = Categoria(nome, limite)
            categorias.append(nova_categoria)
            self.storage.save_categories(categorias)
            return nova_categoria
        
        check_category.limite = limite
        self.storage.save_categories(categorias)
        return check_category
    
    def finds_category_by_name(self, nome, categorias):
        for categoria in categorias:
            if categoria.nome == nome:
                return categoria
        return None