from model.despesa_storage import DespesaStorage
from model.despesa import Despesa
from model.categoria_storage import CategoriaStorage
from model.usuario_storage import UsuarioStorage

class DespesaController:

    def __init__(self):
        self.storage =  DespesaStorage()
        self.categoria_storage = CategoriaStorage()
        self.usuario_storage = UsuarioStorage()

    '''cria uma nova Despesa com 
    os parametros recebidos
    carrega a lista de despesass,
    adiciona a nova despesa à
    lista recebida, salva a lista
    completa e por fim retorna 
    a nova despesa'''
    def cadastrar_despesa(self, valor, data, descricao, categoria_nome, usuario_nome, categoria_id, Usuario_id, id):
        #deveria estar recebendo os argumentos pelo view
        nova_despesa =  Despesa(valor, data, descricao, categoria_nome, usuario_nome, categoria_id, Usuario_id, id)
        nova_despesa.choose_category(self.categoria_storage)
        nova_despesa.choose_user(self.usuario_storage)
        despesas = self.storage.load_expenses()
        despesas.append(nova_despesa)
        self.storage.save_expenses(despesas)
        return nova_despesa
    
    def alerta_de_gastos(self, categoria_id):
        pass