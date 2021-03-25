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
        # Primeiro precisa criar um novo Nó
        novo = No(valor, None, None)
        # Vai reconhecer se é o primeiro Nó criado ou não.
        # Se for o primeiro será a Raiz.
        if self.root == None:
            self.root = novo
        # Sub-Arvore
        else:
            atual = self.root
            while True:
                anterior = atual
                # Esquerda
                if valor <= atual.item:
                    atual = atual.esquerda
                    if atual == None:
                        anterior.esquerda = novo
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        anterior.direita = novo
                        return

    def imprimirValores(self, atual, n, repeticao):
        if atual != None:
            if atual.item <= n:
                self.imprimirValores(atual.esquerda, n, repeticao)
                print(atual.item, end=" ")
                self.imprimirValores(atual.direita, n, repeticao)
            else:
                self.imprimirValores(atual.esquerda, n, repeticao)
                self.imprimirValores(atual.direita, n, repeticao)


arvore = arvoreBinaria()
tamanho = int(0)
i = 0
# Adicionar Árvore
print("Adicione os valores de sua Árvore, para concluir digite -999.")
while i < 1:
    valor = int(input("{}° valor: ".format(tamanho)))
    if valor == -999:
        break
    arvore.inserirValor(valor)
    tamanho += 1
# Ordenar Árvore
n = int(input("Adicione o valor N que deseja: "))
arvore.imprimirValores(arvore.root, n, 0)