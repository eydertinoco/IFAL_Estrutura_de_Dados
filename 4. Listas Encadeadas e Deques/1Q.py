from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self.size = self.size + 1

    def __len__(self):
        return self.size
    def get(self, index):

def criar_novo_processo (id_processo, tamanho, estrategia_alocacao):
    print(listaMemoria)
    print("criar_novo_processo")
def deletar_processo (id_processo):
    print("deletar_processo")
def imprimir_dump_memoria():
    print("imprimir_dump_memoria")

#--------------Criação da Memoria Ficticia-----------------------
#----------------------------------------------------------------
print("Criando uma memória em bloco do zero.")
listaMemoria = LinkedList()
tamanhoTotal = int(input("Adicione o tamanho total da memória em bloco:"))
x = int(0)
while x < tamanhoTotal:
    listaMemoria.append("")
    x += 1
#----------------------------------------------------------------

id = int(0)
lista_id = []
i = int(0)
while i < 1:
    print("-------------------------")
    print("-----------Menu----------")
    print("1. Criar Novo Processo\n2. Deletar Processo\n3. Imprimir Dump Memoria\n4. Sair")
    print("-------------------------")
    menuEscolha = int(input("Opção Escolhida: "))
    print("-------------------------")
    if menuEscolha == 1:
        id += 1
        lista_id.append(id)
        id_processo = id
        tamanho = int(input("Adicione o tamanho do Processo:"))
        print("Escolha qual tipo de estrategia de alocação deseja.")
        print("1. First_fit\n2. Best_fit\n3. Worst_fit")
        estrategia_alocacao = int(input("Opção desejada: "))
        if estrategia_alocacao == 1:
            estrategia_alocacao = str("first_fit") #Primeiro bloco que atende ao tamanho
        elif estrategia_alocacao == 2:
            estrategia_alocacao = str("best_fit") #Melhor bloco que atende ao tamanho
        elif estrategia_alocacao == 3:
            estrategia_alocacao = str("worst_fit") #Pior bloco que atende ao tamanho
        else:
            print("Erro: Valor não existente. Recomeçe a operação.")
            break;
        criar_novo_processo(id_processo, tamanho, estrategia_alocacao)

    elif menuEscolha == 2:
        id_processo = int(input("Adicione o id do processo para deletar:"))
        x = int(0)
        while x <= len(lista_id):
            if id_processo == lista_id[x]:
                print("ID encontrado.\nComeçando a operação de deletar o processo.\n")
                deletar_processo(id_processo)
                break;
            if x == len(lista_id):
                print("ID não encontrado.\n")
                break;
            x += 1
    elif menuEscolha == 3:
        imprimir_dump_memoria()
    else:
        print("\nAtenção! Saindo da Operação.\n\n\n\nOperação Finalizada.")
        break;