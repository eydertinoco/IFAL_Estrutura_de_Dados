def addValorLista():
    adicionarValorLista = int(input("Adicione o {}° valor inteiro: ".format(len(lista))))
    if (adicionarValorLista == -999):
        print(lista)
    else:
        lista.append(adicionarValorLista)
        addValorLista()

def pesquisa_valor_sequencialmente(valorDesejado, lista, posicao):
    while posicao < len(lista):
        if lista[posicao] == valorDesejado:
            return print("O valor {} existe, está na posição {}.".format(valorDesejado, posicao))
        posicao += 1
    return print("O valor {} não existe na lista.".format(valorDesejado))

posicao = 0
lista = []
print("Adicione valores inteiros na lista, digite -999 para finalizar a adição de valores.")
addValorLista()
valorDesejado = int(input("Adicione o valor que deseja encontrar: "))
pesquisa_valor_sequencialmente(valorDesejado, lista, posicao)