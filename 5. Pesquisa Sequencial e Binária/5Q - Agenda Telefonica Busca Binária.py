def pesquisa_binaria_valor(lista, i, r, valorDesejado):
    if r >= i:
        posicao = (i+r) // 2
        if lista[posicao] == valorDesejado:
            return posicao
        elif lista[posicao] > valorDesejado:
            return pesquisa_binaria_valor(lista, i, posicao-1, valorDesejado)
        else:
            return pesquisa_binaria_valor(lista, posicao+1, r, valorDesejado)
    return -1

def add_valor_lista(addlista, listaTelefonica, posicao):
    if posicao == len(listaTelefonica):
        listaTelefonica.insert(posicao, addlista)
        return registro_lista_telefonica()
    if addlista[0] == listaTelefonica[posicao][0]:
        print("O ID {} já existe na lista telefonica".format(addlista[0]))
        return registro_lista_telefonica()
    elif listaTelefonica[posicao-1][0] < addlista[0] < listaTelefonica[posicao][0]:
        listaTelefonica.insert(posicao, addlista)
        return registro_lista_telefonica()
    else:
        return add_valor_lista(addlista, listaTelefonica, posicao+1)

def registro_lista_telefonica():
    addlista = []
    id = int(input("Adicione o ID: "))
    if id < 0:
        return print_lista_telefonica()
    addlista.append(id)
    nome = str(input("Adicione o nome: "))
    addlista.append(nome)
    numero = str(input("Adicione o telefone: "))
    addlista.append(numero)
    if len(listaTelefonica) == 0:
        listaTelefonica.insert(0, addlista)
        return registro_lista_telefonica()
    else:
        add_valor_lista(addlista, listaTelefonica, 0)

def print_lista_telefonica():
    x = 0;
    print("\n==================")
    print("Lista Telefonica:")
    print("==================")
    if len(listaTelefonica) > 0:
        while x < len(listaTelefonica):
            print(listaTelefonica[x])
            x += 1
    else:
        print("Lista Vazia")
    print("==================")

listaTelefonica = []
registro_lista_telefonica()