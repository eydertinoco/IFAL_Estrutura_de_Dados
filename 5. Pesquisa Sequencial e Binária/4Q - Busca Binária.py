def pesquisa_binaria_valor(tamanhoTotalLista, valorDesejado, procurandoPosicao):
    if procurandoPosicao < tamanhoTotalLista:
        procurandoPosicao = (tamanhoTotalLista+procurandoPosicao) // 2
        if valorDesejado == lista[procurandoPosicao]:
            return procurandoPosicao
        elif valorDesejado > lista[procurandoPosicao]:
            return pesquisa_binaria_valor(tamanhoTotalLista, valorDesejado, procurandoPosicao)
        else:
            return pesquisa_binaria_valor(tamanhoTotalLista-1, valorDesejado, procurandoPosicao)
    return posicaoValor == str("false")

addValorLista = int(input("Adicione uma quantidade da lista com um valor inteiro e positivo na lista: "))
lista = list(range(0,addValorLista))
print(lista)
valorDesejado = int(input("Adicione o valor que deseja obter na lista: "))
posicaoValor = pesquisa_binaria_valor(addValorLista, valorDesejado, 0)
if posicaoValor == "false":
    print("O valor {} não existe na lista.".format(valorDesejado))
else:
    print("O valor {} existe, está na posição {}.".format(valorDesejado, posicaoValor))