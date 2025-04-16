import re
import uuid

class Usuario:
    def __init__(self, 
                 nome: str, 
                 email: str,
                 id: str = None):
        
        self.__nome = nome
        self.__email = email
        self.__id = id or str(uuid.uuid4())

    @property
    def id(self):
        return self.__id

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
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("'email' deve ser uma string.")
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", email):
                raise ValueError("Formato de email inválido.")
        self.__email = email

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "id": self.id
        }
            