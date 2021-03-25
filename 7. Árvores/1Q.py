class arvore:
    def __init__(self, valor):
        self.atual = valor
        self.filhos = []

    def adicionarFilhos(self, atual):
        filho = arvore(atual)
        self.filhos.append(filho)
        return filho

    def maiorElemento(self):
        lista.append(raiz.filhos.atual)
        i = int(0)
        while i < 10:
            lista.append(raiz.filhos[i].atual)
            i += 1



lista = []
raiz = arvore(5)
lista.append(raiz.atual)
raiz.adicionarFilhos(9)
raiz.adicionarFilhos(2)
raiz.filhos[0].adicionarFilhos(10)
print(raiz.maiorElemento())