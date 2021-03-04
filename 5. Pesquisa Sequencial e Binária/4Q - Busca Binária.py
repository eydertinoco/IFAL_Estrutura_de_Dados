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

def addValorLista():
    adicionarValorLista = int(input("Adicione o {}° valor inteiro: ".format(len(lista))))
    if (adicionarValorLista == -999):
        print(lista)
    else:
        if len(lista) != 0:
            if lista[(len(lista)-1)] != (adicionarValorLista-1):
                print("Para realizar uma busca binária é necessário que os valores sejam sequencial.\nEx: 10, 11, 12, 13, 14\nTente novamente.")
                return addValorLista()
            else:
                lista.append(adicionarValorLista)
                return addValorLista()
        else:
            lista.append(adicionarValorLista)
            return addValorLista()

lista = []
print("Adicione valores inteiros na lista, digite -999 para finalizar a adição de valores.")
addValorLista()
valorDesejado = int(input("Adicione o valor que deseja obter na lista: "))
posicaoValor = pesquisa_binaria_valor(lista, 0, len(lista)-1, valorDesejado)
if posicaoValor < 0:
    print("O valor {} não existe na lista.".format(valorDesejado))
else:
    print("O valor {} existe, está na posição {}.".format(valorDesejado, posicaoValor))