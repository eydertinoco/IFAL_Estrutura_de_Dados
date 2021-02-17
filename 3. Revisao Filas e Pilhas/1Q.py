from typing import List

def adquirirValor(stack, tamanhoStack, x, equacao):
    valor1 = float(stack.pop())
    tamanhoStack -= 1
    valor2 = float(stack.pop())
    tamanhoStack -= 1
    if equacao[x] == "+":
        stack.append(float(valor2+valor1))
    elif equacao[x] == "-":
        stack.append(float(valor2-valor1))
    elif equacao[x] == "*":
        stack.append(float(valor2*valor1))
    else:
        stack.append(float(valor2/valor1))
    print(stack)

print("Adicione uma Notação Polonesa Inversa(RPN) para ser calculada.")
equacao = str(input("Adicione a equação: "))
print(equacao)
stack: List[str] = []

x = 0
tamanhoStack = 0
valor1 = float(0)
valor2 = float(0)
InformacaoParaAdicionarPilha = str("")
tamanho = len(equacao)
print("-----------------------------------")
print("-------- Folha de cálculo ---------")
print("-----------------------------------")
while x < tamanho:
    if (equacao[x] == str("+")):
        adquirirValor(stack, tamanhoStack, x, equacao)
        tamanhoStack -= 1
    elif (equacao[x] == str("-")):
        adquirirValor(stack, tamanhoStack, x, equacao)
        tamanhoStack -= 1
    elif (equacao[x] == str("*")):
        adquirirValor(stack, tamanhoStack, x, equacao)
        tamanhoStack -= 1
    elif (equacao[x] == str("/")):
        adquirirValor(stack, tamanhoStack, x, equacao)
        tamanhoStack -= 1
    elif (equacao[x] != str(" ")):
        InformacaoParaAdicionarPilha += equacao[x]
    elif (equacao[x] == str(" ")):
        if InformacaoParaAdicionarPilha != "":
            stack.append(InformacaoParaAdicionarPilha)
            tamanhoStack += 1
            print(stack)
            InformacaoParaAdicionarPilha = str("")
    x += 1
print("-----------------------------------")