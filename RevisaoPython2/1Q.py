from datetime import datetime

def cadastrarCliente():
    nomeCliente = str(input("Adicione nome do Cliente: "))
    listaClientes.insert(0, nomeCliente)
    cpfCliente = int(input("Adicione CPF do Cliente: "))
    listaClientes.insert(1, cpfCliente)
    ruaCliente = str(input("Adicione rua do Cliente: "))
    listaClientes.insert(2, ruaCliente)
    cepCliente = str(input("Adicione CEP do Cliente: "))
    listaClientes.insert(3, cepCliente)
    cidadeCliente = str(input("Adicione cidade do Cliente: "))
    listaClientes.insert(4, cidadeCliente)

def cadastrarProduto():
    # ID do Produto
    listaAddProdutos.insert(0, int((len(listaProdutos) + 1)))
    nomeProduto = str(input("Adicione nome do Produto: "))
    listaAddProdutos.insert(1, nomeProduto)
    descricaoProduto = str(input("Adicione descrição do Produto: "))
    listaAddProdutos.insert(2, descricaoProduto)
    valorProduto = float(input("Adicione valor do produto: "))
    listaAddProdutos.insert(3, valorProduto)
    validar = input("Você realmente quer salvar esse produto? s/n")
    if validar == "s":
        quant = len(listaProdutos)
        listaProdutos.insert(quant, listaAddProdutos)

def cadastrarCompra():
    # ID do Produto
    listaAddCompra.insert(0, (len(listaHistoricoCompra) + 1))

    dataCompra = datetime.now()
    listaAddCompra.insert(1, dataCompra)

    cadastrarCliente()
    listaAddCompra.insert(2, listaClientes)

    x = 0;
    listaProdutosComprados = []
    while x < 1:
        idProduto = int(input("ID do Produto:"))
        if (idProduto < 1) and (len(listaAddCompra[2]) > 0):
            break;
        elif (idProduto < 1) and (produtoComprado.isEmpty()):
            error()
        y = 0
        x = int(len(listaProdutos))
        while y < x:
            if listaProdutos[y][0] == idProduto:
                produtoComprado = listaProdutos[y]
                quantidade = int(input("Qual a quantidade que você deseja adicionar desse Produto?"))
                z = 0
                while z < quantidade:
                    listaProdutosComprados.insert((len(listaProdutosComprados)), produtoComprado)
                    z += 1
            y += 1
    listaAddCompra.insert(3, listaProdutosComprados)
    listaHistoricoCompra.insert((len(listaHistoricoCompra)), listaAddCompra)



def error():
    print("ERRO: Não há nenhum produto com essa ID.")


listaProdutos = []
listaClientes = []
listaHistoricoCompra = []
valorWhile = 0;
while valorWhile < 1:
    print("Adicione 1 para Cadastrar um Produto.")
    listaAddProdutos = []
    print("Adicione 2 para Cadastrar uma Compra.")
    listaAddCompra = []
    print("Adicione 3 para Listar as Compra.")
    print("Adicione 4 para Sair.")
    escolha = int(input())
    if escolha == 1:
        cadastrarProduto()
        print(listaProdutos)
        print(listaProdutos[0])
        print(listaProdutos[0][0])
    elif escolha == 2:
        cadastrarCompra()
        print(listaHistoricoCompra)
    elif escolha == 3:
        print("Data: {}".format(listaHistoricoCompra[0][1]))
        print("Nome: {}".format(listaHistoricoCompra[0][2][0]))
        print("CPF: {}".format(listaHistoricoCompra[0][2][1]))
        valor = float(0)
        x = 0
        while x < len(listaHistoricoCompra[0][3]):
            valor += listaHistoricoCompra[0][3][x][3]
            x += 1
        print("Valor: {}".format(valor))
    elif escolha == 4:
        break;
    else:
        print("Valor invalido, tente novamente.")