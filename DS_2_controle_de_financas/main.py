from controller.usuario_controller import UsuarioController
from controller.categoria_controller import CategoriaController
from controller.despesa_controller import DespesaController
from model.controle_financeiro import ControleFinanceiro
from model.usuario import Usuario

if __name__ == "__main__":
    #cadastrando um novo usuário
    nome_usuario = "Susana"
    # email = "sus_peita@gmail.com"

    # controlador_de_usuario = UsuarioController()
    # controlador_de_usuario.cadastrar_usuario(nome_usuario, email)

    # cadastrando uma nova categoria
    # nome = "Educação"
    # limite = 2800

    # controlador_de_categoria = CategoriaController()
    # controlador_de_categoria.cadastrar_categoria(nome, limite)
    
    # cadatrando uma nova despesa
    # valor = 2000
    # descricao = "preço dos materiais escolares"
    # categoria_nome = "Educação"

    # controlador_de_despesa = DespesaController()
    # controlador_de_despesa.cadastrar_despesa(valor, descricao, categoria_nome, nome_usuario, None, None, None, None)

    # usuario = Usuario("raquel", "raquelavsp7@gmail.com")

    # controleFinanceiro = ControleFinanceiro(usuario)
    # controleFinanceiro.adicionar_categorias()

    
    #cadastrando uma nova categoria
    # nome = "Internet"
    # limite = 150

    # controlador_de_categoria = CategoriaController()
    # controlador_de_categoria.cadastrar_categoria(nome, limite)

    # cadatrando uma nova despesa
    # valor = 150
    # descricao = "valor mensal de internet"
    # categoria_nome = "Internet"

    # controlador_de_despesa = DespesaController()
    # controlador_de_despesa.cadastrar_despesa(valor, descricao, categoria_nome, nome_usuario, None, None, None, None)
    
    #cadastrando uma nova categoria
    nome = "Saídas com Amigos"
    limite = 300

    controlador_de_categoria = CategoriaController()
    controlador_de_categoria.cadastrar_categoria(nome, limite)

    valor = 70
    descricao = "Ingressos do jogo do Figueirense e Ponta Preta"
    categoria_nome = "Saídas com Amigos"

    controlador_de_despesa = DespesaController()
    controlador_de_despesa.cadastrar_despesa(valor, descricao, categoria_nome, nome_usuario, None, None, None, None)

