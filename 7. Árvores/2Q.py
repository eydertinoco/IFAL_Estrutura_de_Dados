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
    def ordenar(self, atual):
        if atual != None:
            self.ordenar(atual.esquerda)
            print(atual.item, end=" ")
            self.ordenar(atual.direita)

    def removerImpar(self, tamanho):
        # Se a Arvore for vazia
        if self.root == None:
            return
        # Se Não...
        atual = self.root
        pai = self.root
        filho_esq = True
        impar = (atual.item)%2
        if impar != 0:
            # Se nao possui nenhum filho (é uma folha), elimine-o
            if atual.esquerda == None and atual.direita == None:
                if atual == self.root:
                    self.root = None  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = None  # se for filho a esquerda do pai
                    else:
                        pai.direita = None  # se for filho a direita do pai

            # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
            elif atual.direita == None:
                if atual == self.root:
                    self.root = atual.esquerda  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = atual.esquerda  # se for filho a esquerda do pai
                    else:
                        pai.direita = atual.esquerda  # se for filho a direita do pai

            # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
            elif atual.esquerda == None:
                if atual == self.root:
                    self.root = atual.direita  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = atual.direita  # se for filho a esquerda do pai
                    else:
                        pai.direita = atual.direita  # se for  filho a direita do pai

            # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
            else:
                self.ordenar(atual.esquerda)
                self.ordenar(atual.direita)
            return
        else:
            # Se nao possui nenhum filho (é uma folha), elimine-o
            if atual.esquerda == None and atual.direita == None:
                if atual == self.root:
                    self.root = None  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = None  # se for filho a esquerda do pai
                    else:
                        pai.direita = None  # se for filho a direita do pai

            # Se é pai e nao possui um filho a direita, substitui pela subarvore a direita
            elif atual.direita == None:
                if atual == self.root:
                    self.root = atual.esquerda  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = atual.esquerda  # se for filho a esquerda do pai
                    else:
                        pai.direita = atual.esquerda  # se for filho a direita do pai

            # Se é pai e nao possui um filho a esquerda, substitui pela subarvore a esquerda
            elif atual.esquerda == None:
                if atual == self.root:
                    self.root = atual.direita  # se raiz
                else:
                    if filho_esq:
                        pai.esquerda = atual.direita  # se for filho a esquerda do pai
                    else:
                        pai.direita = atual.direita  # se for  filho a direita do pai

            # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
            else:
                self.ordenar(atual.esquerda)
                self.ordenar(atual.direita)
            print(atual.item, end=" ")


arvore = arvoreBinaria()
tamanho = 0
i = 0
# Adicionar Árvore
while i < 1:
    valor = int(input("Adicione o valor: "))
    if valor < 0:
        break;
    arvore.inserirValor(valor)
    tamanho += 1
# Ordenar Árvore
# arvore.ordenar(arvore.root)
# Remover valores Impar da Árvore
print("Árvore sem valores Impar: ")
while tamanho >= 0:
    arvore.removerImpar(tamanho)
    tamanho -= 1