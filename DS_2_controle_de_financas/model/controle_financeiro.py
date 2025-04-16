from model.usuario import Usuario
from model.categoria import Categoria
from model.categoria_storage import CategoriaStorage
from model.despesa_storage import DespesaStorage
from fpdf import FPDF

class ControleFinanceiro:
    def __init__(self,
                 usuario: Usuario):
        
        '''Um dicionário onde a chave 
        é o nome da categoria e o valor 
        é uma instância da classe Categoria.'''
        self.__categorias = {}
        self.__usuario = usuario

    @property
    def usuario(self):
        return self.__usuario
    
    @usuario.setter
    def usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("'usuario' deve ser uma instância da classe 'Usuario'.")
        self.__usuario = usuario
    

    def adicionar_categorias(self):

        categorias_salvas = CategoriaStorage()
        lista_objetos = categorias_salvas.list_objects_categories()

        for obj in lista_objetos:
            self.__categorias[obj.nome] = obj

    '''gera relatórios mensais
    com as despesas categoriadas'''
    def emitir_relatorio(self):
        storage = DespesaStorage()
        despesas = storage.load_expenses()
        x = 0

        for despesa in despesas:
            if despesa.usuario_nome == self.__usuario.nome:
                print(despesa.categoria_nome)
                print(despesa.valor)
                print(despesa.descricao)
                print(despesa.data)
                print("-" * 40)
                x = 1
        if x == 0:
            print(f"Usuário {self.__usuario.nome} não encontrado.")
            return None

        self.exportar_dados()

    '''exporta o relatório de
    despesas para um arquivo
    formato pdf'''
    def exportar_dados(self):
        storage = DespesaStorage()
        despesas = storage.load_expenses()
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)

        pdf.cell(200, 10, txt="Relatório de Despesas", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, txt=f"Usuário: {self.__usuario.nome}", ln=True)

        pdf.ln(5)  # Espaço antes da tabela

        encontrou_despesas = False

        for despesa in despesas:
            if despesa.usuario_nome == self.__usuario.nome:
                encontrou_despesas = True

                pdf.set_font("Arial", "B", 12)
                pdf.cell(200, 10, txt=f"Categoria: {despesa.categoria_nome}", ln=True)
                pdf.set_font("Arial", "", 12)
                pdf.cell(200, 8, txt=f"Valor: R$ {despesa.valor:.2f}", ln=True)
                pdf.cell(200, 8, txt=f"Descrição: {despesa.descricao}", ln=True)
                pdf.cell(200, 8, txt=f"Data: {despesa.data}", ln=True)
                pdf.cell(200, 5, txt="-" * 60, ln=True)

        if not encontrou_despesas:
            print(f"Usuário {self.__usuario.nome} não encontrado.")
            return

        nome_arquivo = f"relatorio_{self.__usuario.nome.lower().replace(' ', '_')}.pdf"
        pdf.output(nome_arquivo)
        print(f"Relatório exportado com sucesso para o arquivo: {nome_arquivo}")
