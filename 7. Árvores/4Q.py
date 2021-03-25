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
    def contarFolhas(self, atual):
        if atual == None:
            return 0
        if atual.esquerda == None and atual.direita == None:
            return 1
        return self.contarFolhas(atual.esquerda) + self.contarFolhas(atual.direita)


arvore = arvoreBinaria()
i = 0
tamanho = int(0)
# Adicionar Árvore
print("Descubra a quantidade de Folhas de sua Árvore!")
print("Adicione os valores de sua Árvore, para concluir digite -999.")
while i < 1:
    valor = int(input("{}° valor: ".format(tamanho)))
    if valor == -999:
        break;
    arvore.inserirValor(valor)
    tamanho += 1
# Contar N° Folhas
numeroFolhas = arvore.contarFolhas(arvore.root)
print("A quantidade de folhas é {}.".format(numeroFolhas))
