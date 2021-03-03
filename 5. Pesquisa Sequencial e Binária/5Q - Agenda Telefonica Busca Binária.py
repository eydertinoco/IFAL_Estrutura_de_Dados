def comparar_id(lista, posicao, novoId, salvarPosicao, addlista):
    if posicao != len(lista):
        if lista[posicao][0] == novoId:
            print("O ID {} já existe na lista".format(novoId))
            return registro_lista_telefonica()
        elif novoId < lista[posicao][0]:
            salvarPosicao = posicao
        return comparar_id(lista, posicao+1, novoId, salvarPosicao, addlista)
    else:
        arrumar_lista(lista, salvarPosicao, novoId, addlista)

def arrumar_lista(lista, posicao, novoId, addlista):
    if lista[posicao][0] < novoId:
        posicao += 1
    elif lista[posicao][0] > novoId:
        listaArrumacao = []
        while (posicao < len(lista)):
            x = lista.pop()
            listaArrumacao.append(x)
        lista.append(addlista)
        while (0 != len(listaArrumacao)):
            x = listaArrumacao.pop()
            lista.append(x)


def registro_lista_telefonica():
    print_lista_telefonica()
    addlista = []
    id = int(input("Adicione o ID: "))
    if id < 0:
        return print("Agenda Encerrada")
    addlista.append(id)
    nome = str(input("Adicione o nome: "))
    addlista.append(nome)
    numero = int(input("Adicione o telefone: "))
    addlista.append(numero)
    print(listaTelefonica)
    comparar_id(listaTelefonica, 0, id, 0, addlista)

def print_lista_telefonica():
    x = 0;
    print("==================")
    print("Lista Telefonica:")
    if len(listaTelefonica) == 0:
        print("Lista Vazia")
    else:
        while x < len(listaTelefonica):
            print(listaTelefonica[x])
            x += 1
    print("==================")

listaTelefonica = []
registro_lista_telefonica()