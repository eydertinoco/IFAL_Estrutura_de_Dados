Banco
idBanco = int()
nomeBanco = str()

idConta = int()
idUsuario = int()
idBanco = int()
saldo = float()

idUsuario = int()
nomeUsuario = str()

Transferencia
idTransferencia = int()
idContaOrigem = int()
idContaDestino = int()
valor = float()

saque
idSaque = int()
idConta = int()
valor = float()


def depositar(idDeposito):
    idConta = int(input("ID da conta a ser depositada: "))
    valor = float(input("Valor do Deposito: "))
    listaDeposito.insert(0, idDeposito)
    listaDeposito.insert(1, idConta)
    listaDeposito.insert(2, valor)
    listaTabelaDeposito.insert(len(listaTabelaDeposito), listaDeposito)

def sacar(idSacar):


listaTabelaDeposito = []
idDeposito = 0

escolha = int(input())
if escolha == 1:    #Depositar
    listaDeposito = []
    idDeposito += 1
    depositar(idDeposito)
#  Deve solicitar ao usu ́ario o id da conta a ser depositada e o valor, inserir a transa ̧c ̃ao
# na tabela ’deposito’ e atualizar o saldo na tabela conta;
elif escolha == 2:  #Sacar
#  Deve solicitar ao usu ́ario o id da conta a ser depositada e o valor, inserir a transa ̧c ̃ao
# na tabela ’saque’ e atualizar o saldo na tabela conta;
elif escolha == 3:  #Transferencia
#  Deve solicitar ao usu ́ario o id da conta de origem, o id da conta de destino e o valor
# da transferˆencia. Em seguida deve-se inserir a transa ̧c ̃ao na tabela ’transferencia’ e
# atualizar o saldo na tabela conta para ambos os usu ́arios;
elif escolha == 4:  #Recuperar Patrimônio de um usuário
#  Deve solicitar o id do usu ́ario, recuperar as contas que esse usu ́ario possui e calcular e
# somar o saldo de todas as contas que este usu ́ario possui. Em seguida, deve-se exibir
# os dados do usu ́ario juntamente com o valor do patrimˆonio.
elif escolha == 5:  #Recuperar o volume de transações realizadas entre dois bancos.
#  Deve solicitar o id de dois bancos distintos, recuperar as transa ̧c ̃oes realizadas entre
# contas dos mesmos e somar o valor das transa ̧c ̃oes, exibindo em seguida para na tela.
elif escolha == 6:  #Sair

else:
    print("ERRO: Numero invalido, tente novamente.")