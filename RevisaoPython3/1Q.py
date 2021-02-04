from typing import List
from copy import deepcopy

import none as none


def adquirirValor(x, stack):
    valor1 = int(stack.pop(x-1))
    valor2 = int(stack.pop(x-2))
    return valor1, valor2

print("Primeira Questão:\nAdicione uma Notação Polonesa Inversa(RPN) para ser calculada.")
equacao = str(input("Adicione a equação: "))

stack: List[str] = []

x = 0
valorStack = none
tamanho = len(equacao)
while x < tamanho:
    if equacao[x] == " ":
        valorStack = none
    elif x == "+":
        adquirirValor(x, stack)
    elif x == "-":
    elif x == "/":
    elif x == "*":

    elif equacao[x] != " " and equacao[x + 1] == " ":
        valorStack += equacao[x]
        stack.append(valorStack)
        valorStack = none
    else:

    x += 1
stack.append('A')
stack.append('B')
stack.append('C')

x = 0
while x < len(equacao):
    stack.append(equacao[x])
    if x == "+":
        adquirirValor(stack)
        stack.append(( valor1 + valor2 ))
    elif x == "-":
        valor1 = int(stack.pop(x - 1))
        valor2 = int(stack.pop(x - 2))
        stack.append((valor1 - valor2))
    elif x == "/":
        valor1 = int(stack.pop(x - 1))
        valor2 = int(stack.pop(x - 2))
        stack.append((valor1 / valor2))
    elif x == "*":
        valor1 = int(stack.pop(x - 1))
        valor2 = int(stack.pop(x - 2))
        stack.append((valor1 * valor2))
    else:
        stack.append(equacao[x])

top_item = stack.pop() #Retorna o valor do topo de pilha.

print(stack, top_item)