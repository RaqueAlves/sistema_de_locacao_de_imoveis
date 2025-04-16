from datetime import date
import uuid

class Despesa():
    def __init__(self,
                 valor: float,   
                 descricao: str,
                 categoria_nome: str,
                 usuario_nome: str,
                 categoria_id: str = None,
                 usuario_id: str = None,
                 data: date = None,
                 id: str = None):
        
        self.__valor = valor
        self.__descricao = descricao
        self.__categoria_nome = categoria_nome
        self.__usuario_nome = usuario_nome
        self.__categoria_id = categoria_id or None
        self.__usuario_id = usuario_id or None
        self.__data = data or date.today().strftime("%d/%m/%Y")
        self.__id = id or str(uuid.uuid4())

    '''O valor da despesa.'''
    @property
    def valor(self):
        return self.__valor

    '''A data em que a despesa foi registrada
    (formato: "DD/MM/AAAA").'''
    @property
    def data(self):
        return self.__data

    '''Uma descrição breve da despesa.'''
    @property
    def descricao(self):
        return self.__descricao

    '''O nome da categoria da despesa
    (Educação, Energia, etc.).'''
    @property
    def categoria_nome(self):
        return self.__categoria_nome

    '''O id da categoria da despesa
    (Educação, Energia, etc.).'''
    @property
    def categoria_id(self):
        return self.__categoria_id
    
    '''Id da despesa'''
    @property
    def id(self):
        return self.__id
    
    '''nome do usuario que 
    possui aquela despesa'''
    @property
    def usuario_nome(self):
        return self.__usuario_nome
    
    '''Id do usuario que
    possui aquela despesa'''
    @property
    def usuario_id(self):
        return self.__usuario_id
    
    def choose_category(self, categoria_storage):
        for categoria in categoria_storage.list_objects_categories():
            if categoria.nome == self.__categoria_nome:
                self.__categoria_id = categoria.id
                return
            
        raise ValueError(f"Categoria '{self.__categoria_nome}' não encontrada.")
    
    def choose_user(self, usuario_storage):
        for user in usuario_storage.list_objects_users():
            if user.nome == self.__usuario_nome:
                self.__usuario_id = user.id
                return
            
        raise ValueError(f"Usuário '{self.__usuario_nome}' não encontrado.")

    '''retorna uma string que representa
    o objeto de maneira detalhada'''
    def __repr__(self):
        return (f"Despesa(valor={self.valor}, "
            f"descricao='{self.descricao}', "
            f"categoria_nome='{self.categoria_nome}', "
            f"usuario_nome='{self.usuario_nome}', "
            f"categoria_id='{self.categoria_id}', "
            f"usuario_id='{self.usuario_id}', "
            f"data={self.data}, "
            f"id='{self.id}')")
    
    def to_dict(self):
        return {
            "valor": self.valor,
            "descricao": self.descricao,
            "categoria_nome": self.categoria_nome,
            "usuario_nome": self.usuario_nome,
            "categoria_id": self.categoria_id,
            "usuario_id": self.usuario_id,
            "data": self.data,
            "id": self.id
        }