class arvore:
    def __init__(self, valor):
        self.atual = valor
        self.filhos = []

    def adicionarFilhos(self, atual, elemento):
        filho = arvore(atual)
        self.filhos.append(filho)
        if elemento[0] < filho.atual:
            elemento.pop()
            elemento.append(filho.atual)
        return filho

elemento = []
elemento.append(0)
raiz = arvore(5)
raiz.adicionarFilhos(9, elemento)
raiz.adicionarFilhos(2, elemento)
raiz.filhos[0].adicionarFilhos(10, elemento)
raiz.filhos[1].adicionarFilhos(11, elemento)
raiz.filhos[0].filhos[0].adicionarFilhos(15, elemento)
maiorElemento = elemento.pop()
print("O maior elemento da Árvore é: {}".format(maiorElemento))