def pesquisa_binaria_valor(lista, i, r, valorDesejado):
    if r >= i:
        posicao = (i+r) // 2
        if lista[posicao] == valorDesejado:
            return valorDesejado
        elif lista[posicao] > valorDesejado:
            return pesquisa_binaria_valor(lista, i, posicao-1, valorDesejado)
        else:
            return pesquisa_binaria_valor(lista, posicao+1, r, valorDesejado)
    return -1

addValorLista = int(input("Adicione uma quantidade da lista com um valor inteiro e positivo na lista: "))
lista = list(range(0,addValorLista))
valorDesejado = int(input("Adicione o valor que deseja obter na lista: "))
posicaoValor = pesquisa_binaria_valor(lista, 0, len(lista)-1, valorDesejado)
if posicaoValor < 0:
    print("O valor não existe na lista.")
else:
    print("O valor existe, está na posição {}.".format(posicaoValor))