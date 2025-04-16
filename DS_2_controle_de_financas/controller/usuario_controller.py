from model.usuario_storage import UsuarioStorage
from model.usuario import Usuario
from model.controle_financeiro import ControleFinanceiro

class UsuarioController:

    def __init__(self):
        self.storage = UsuarioStorage()

    '''cria um novo Usuario com 
    os parametros recebidos
    carrega a lista de usuarios,
    adiciona o novo usuario à
    lista recebida, salva a lista
    completa e por fim retorna 
    o novo usuario'''
    def cadastrar_usuario(self, nome, email):
        #deveria estar recebendo os argumentos pelo view
        novo_usuario = Usuario(nome, email)
        usuarios = self.storage.load_users()
        usuarios.append(novo_usuario)
        self.storage.save_users(usuarios)
        return novo_usuario