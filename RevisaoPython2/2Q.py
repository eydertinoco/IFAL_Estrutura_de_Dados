# Create, Read, Update, Delete

# Exemplar Livro: Livro, Data Aquisição, Custo Compra

# Autor: Nome, Endereço, CPF, Numero de Obras, Descrição
def cadastrarAutor(idUnicoAutor):
    listaAddAutores.insert(0, idUnicoAutor)
    nomeAutor = str(input("Adicione nome do autor: "))
    listaAddAutores.insert(1, nomeAutor)
    enderecoAutor = str(input("Adicione endereço do autor: "))
    listaAddAutores.insert(2, enderecoAutor)

    cadastrarAutorCPF()

    numeroObrasAutor = int(input("Adicione numero de obras do autor: "))
    listaAddAutores.insert(4, numeroObrasAutor)
    descricaoAutor = str(input("Adicione descricao do Autor: "))
    listaAddAutores.insert(5, descricaoAutor)
    listaAutores.insert((idUnicoAutor-1), listaAddAutores)
    print(listaAutores)

def cadastrarAutorCPF():
    if (len(listaAutores)) <= 0:
        cpfAutor = int(input("Adicione cpf do autor: "))
        listaAddAutores.insert(3, cpfAutor)
    else:
        x = 0
        cpfAutor = int(input("Adicione cpf do autor: "))
        while x < (len(listaAutores)):
            if cpfAutor == listaAutores[x][3]:
                print("ERRO 404: CPF já cadastrado! ")
                cadastrarAutor(idUnicoAutor)
            x += 1
        listaAddAutores.insert(3, cpfAutor)

def listarNomesAutores():
    if len(listaAutores) > 0:
        quantidade = 0
        while quantidade < len(listaAutores):
            print(listaAutores[quantidade])
            quantidade += 1
    else:
        print("Não há Autores cadastrado.")

def recuperarAutorCPF():
    procurarCPF = int(input("Adicione o CPF do autor que deseja recuperar: "))
    quantidade = 0
    while quantidade < len(listaAutores):
        if procurarCPF == listaAutores[quantidade][3]:
            print("ID: ", listaAutores[quantidade][0])
            print("Nome: ", listaAutores[quantidade][1])
            print("Endereço: ", listaAutores[quantidade][2])
            print("CPF: ", listaAutores[quantidade][3])
            print("Número de obras publicadas: ", listaAutores[quantidade][4])
            print("Descrição pessoal: ", listaAutores[quantidade][5])
            break
        else:
            quantidade += 1
    print("Nenhum autor possui o CPF informado.")

def deletarAutor():
    procurarCPF = int(input("Adicione o CPF do autor que deseja deletar: "))
    quantidade = 0
    while quantidade < len(listaAutores):
        if procurarCPF == listaAutores[quantidade][3]:
            listaAutores.remove(listaAutores[quantidade])
            break
        else:
            quantidade += 1
    print("Nenhum autor possui o CPF informado.")

# Livro: ISBN, Título, Ano, Lista de Autores
def cadastrarLivros(idUnicoLivro):
    listaAddLivro.insert(0, idUnicoLivro)
    isbnLivro = int(input("Adicione ISBN do livro: "))
    listaAddLivro.insert(1, isbnLivro)
    tituloLivro = str(input("Adicione título do livro: "))
    listaAddLivro.insert(2, tituloLivro)
    anoLivro = int(input("Adicione ano do livro: "))
    listaAddLivro.insert(3, anoLivro)

    listaAddLivroAutor = []
    print("Adicione autores do livro escolhendo o ID: ")
    x = 0
    while x < len(listaAutores):
        print(listaAutores[x])
        x += 1
    x = 0
    while x < len(listaAutores):
        autoreslivro = int(input("Adicione ID autor desejado, adicine 0 ou numero negativo para cancelar: "))
        if autoreslivro <= 0:
            break;
        y = 0
        while y < len(listaAutores):
            if autoreslivro == listaAutores[y][0]:
                listaAddLivroAutor.insert(x, listaAutores[y])
            y += 1
        x += 1
    listaAddLivro.insert(4, listaAddLivroAutor)

    quantidadeLivros = int(input("Adicione quantidade de exemplares do livro: "))
    listaAddLivro.insert(5, quantidadeLivros)
    precoLivro = float(input("Adicione preço unitário do livro: "))
    listaAddLivro.insert(6, precoLivro)

    listaLivros.insert(idUnicoLivro-1, listaAddLivro)

def listarLivros():
    if len(listaLivros) > 0:
        quantidade = 0
        while quantidade < len(listaLivros):
            print(listaLivros[quantidade])
            exemplares = int(listaLivros[quantidade][5])
            valorUni = float(listaLivros[quantidade][6])
            custoTotal = float(exemplares * valorUni)
            print("Quant. Exemplares: ", listaLivros[quantidade][5])
            print("Custo Total = ", custoTotal)
            quantidade += 1
    else:
        print("Não há Autores cadastrado.")

def recuperarLivroISBN():
    procurarISBN = int(input("Adicione o ISBN do livro que deseja recuperar: "))
    quantidade = 0
    while quantidade < len(listaLivros):
        if procurarISBN == listaLivros[quantidade][1]:
            print("ID: ", listaLivros[quantidade][0])
            print("ISBN: ", listaLivros[quantidade][1])
            print("Título: ", listaLivros[quantidade][2])
            print("Ano: ", listaLivros[quantidade][3])
            print("Autor(es): ", listaLivros[quantidade][4])
            print("Exemplares: ", listaLivros[quantidade][5])
            print("Preço: ", listaLivros[quantidade][6])
            break
        else:
            quantidade += 1
    print("Nenhum livro possui o ISBN informado.")

def adicionarNovosExemplares():
    procurarISBN = int(input("Adicione o ISBN do livro: "))
    quantidade = 0
    while quantidade < len(listaLivros):
        if procurarISBN == listaLivros[quantidade][1]:
            quantidadeLivros = int(input("Adicione quantidade de novos exemplares do livro: "))
            print("De ", listaLivros[quantidade][5], "exemplares foi adicionado ", quantidadeLivros)
            listaLivros[quantidade][5] = listaLivros[quantidade][5] + quantidadeLivros
            print("Agora possui ", listaLivros[quantidade][5], "exemplares.")

        quantidade += 1


listaAutores = [[1, 'Eyder', 'Avenida', 111, 0, ''], [2, 'Lucas', 'Rua', 112, 0, '']]
idUnicoAutor = 0
listaLivros = []
idUnicoLivro = 0
valorWhile = 0
while valorWhile < 1:
    print("Adicione 1 para cadastrar um autor.")
    print("Adicione 2 para listar todos os autores.")
    print("Adicione 3 para recuperar um autor.")
    print("Adicione 4 para deletar um autor.")
    print("Adicione 5 para cadastrar um livro.")
    print("Adicione 6 para listar livros.")
    print("Adicione 7 para recuperar livro pelo ISBN.")
    print("Adicione 8 para adicionar novos exemplares do livro.")
    print("Adicione 9 para Sair.")
    escolha = int(input())
    if escolha == 1:
        idUnicoAutor += 1
        listaAddAutores = []
        cadastrarAutor(idUnicoAutor)
    elif escolha == 2:
        listarNomesAutores()
    elif escolha == 3:
        recuperarAutorCPF()
    elif escolha == 4:
        deletarAutor()
    elif escolha == 5:
        idUnicoLivro += 1
        listaAddLivro = []
        cadastrarLivros(idUnicoLivro)
    elif escolha == 6:
        listarLivros()
    elif escolha == 7:
        recuperarLivroISBN()
    elif escolha == 8:
        adicionarNovosExemplares()
    elif escolha == 9:
        break
    else:
        print("Valor invalido, tente novamente.")