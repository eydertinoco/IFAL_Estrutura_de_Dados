from CadastrarProduto import CadastrarProduto
# from CadastrarUsuarios import CadastrarUsuarios

from datetime import datetime

idProduto = 0
listaProdutos = []
listaClientes = []
listaHistoricoCompra = []
valorWhile = 0
while valorWhile < 1:
    print("\n----------------------------------------")
    print("Adicione 1 para Cadastrar um Produto.")
    print("Adicione 2 para Cadastrar uma Compra.")
    print("Adicione 3 para Cadastrar um Cliente.")
    print("Adicione 4 para Listar as Compra.")
    print("Adicione 5 para Sair.")
    print("----------------------------------------\n")
    escolha = int(input())
    if escolha == 1:
        idProduto += 1
        nomeProduto = str(input("Adicione nome do Produto: "))
        descricaoProduto = str(input("Adicione descrição do Produto: "))
        valorProduto = float(input("Adicione valor do produto: "))
        produtoNovo = CadastrarProduto(idProduto, nomeProduto, descricaoProduto, valorProduto)

    elif escolha == 2:
        listaAddCompra = []
        cadastrarCompra()
    elif escolha == 3:
        listaAddUsuario = []
        nomeCliente = str(input("Adicione nome do Cliente: "))
        cpfCliente = int(input("Adicione CPF do Cliente: "))
        ruaCliente = str(input("Adicione rua do Cliente: "))
        cepCliente = str(input("Adicione CEP do Cliente: "))
        cidadeCliente = str(input("Adicione cidade do Cliente: "))
        usuarioNovo = CadastrarUsuarios(listaAddUsuario, listaClientes, nomeCliente,
                                       cpfCliente, ruaCliente, cepCliente, cidadeCliente)
        print(listaClientes)
    elif escolha == 4:
        listaAddCompra = []
        print("Data: {}".format(listaHistoricoCompra[0][1]))
        print("Nome: {}".format(listaHistoricoCompra[0][2][0]))
        print("CPF: {}".format(listaHistoricoCompra[0][2][1]))
        valor = float(0)
        x = 0
        while x < len(listaHistoricoCompra[0][3]):
            valor += listaHistoricoCompra[0][3][x][3]
            x += 1
        print("Valor: {}".format(valor))
    elif escolha == 5:
        break;
    else:
        print("Valor invalido, tente novamente.")