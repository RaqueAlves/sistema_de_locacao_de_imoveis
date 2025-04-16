import uuid

class Categoria:
    def __init__(self,
                 nome: str, 
                 limite: float,
                 id: str = None):
                                            
        self.__nome = nome
        self.__limite = limite
        self.__id = id or str(uuid.uuid4()) 

    '''O nome da categoria da despesa
    (ex: "Educação", "Energia")'''
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("'nome' deve ser uma string.")    
        if not len(nome) >= 3:
            raise ValueError("'nome' deve ter no mínimo 3 caracteres.")
        self.__nome = nome

    '''Um valor que define um limite
    para gastos nesta categoria.'''
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        if limite is not None and not isinstance(limite, (float, int)):
            raise TypeError("'limite' deve ser um Float, Integer ou None.")
        if limite < 0:
            raise ValueError("'limite' não pode ser um valor negativo.")
        self.__limite = limite

    @property
    def id(self):
        return self.__id

    def to_dict(self):
        return {
            "nome": self.__nome,
            "limite": self.__limite,
            "id" : self.__id
        }