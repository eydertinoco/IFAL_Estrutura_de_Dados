class No:
    def __init__(self, valor, direita, esquerda):
        self.item = valor
        self.direita = direita
        self.esquerda = esquerda

class arvoreBinaria:
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserirValor(self, valor):
        novo = No(valor, None, None)
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                # Esquerda ========================
                if valor <= atual.item:
                    atual = atual.esquerda
                    if atual == None:
                        anterior.esquerda = novo
                        return
                # Direita ========================
                else:
                    atual = atual.direita
                    if atual == None:
                        anterior.direita = novo
                        return
    def imprimir(self, atual):
        if atual != None:
            print(atual.item, end=" ")
            self.imprimir(atual.esquerda)
            self.imprimir(atual.direita)

    def inverterArvore(self, atual):
        if atual == None:
            return
        trocarPosicao = atual.esquerda
        atual.esquerda = atual.direita
        atual.direita = trocarPosicao
        self.inverterArvore(atual.esquerda)
        self.inverterArvore(atual.direita)

arvore = arvoreBinaria()
# Adicionar Árvore
arvore.inserirValor(4)
arvore.inserirValor(2)
arvore.inserirValor(1)
arvore.inserirValor(3)
arvore.inserirValor(6)
arvore.inserirValor(5)
arvore.inserirValor(10)
arvore.inserirValor(8)
print("Utilizando a Árvore presente na questão, o código é uma inversão, invertendo as sub-àrvores e suas folhas.:")
print("Árvore Original:")
arvore.imprimir(arvore.root)
print("\n")
print("Árvore Invertida:")
arvore.inverterArvore(arvore.root)
arvore.imprimir(arvore.root)

