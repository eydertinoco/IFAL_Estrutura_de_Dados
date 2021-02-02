def depositar(idDeposito, listaDeposito, informacaoConta):
    idConta = int(input("ID da conta a ser depositada: "))
    valor = float(input("Valor do Deposito: "))
    saldoAtual = float(informacaoConta[3] - valor)
    if saldoAtual < 0:
        print(" Erro: Saldo insuficiente!")
    else:
        saldo = saldoAtual
        listaDeposito.insert(0, idDeposito)
        listaDeposito.insert(1, idConta)
        listaDeposito.insert(2, valor)
        informacaoConta[3] = saldoAtual
        listaTabelaDeposito.insert(len(listaTabelaDeposito), listaDeposito)

def sacar(idSacar, listarSacar, informacaoConta):
    idConta = int(input("ID da conta a ser depositada: "))
    valor = float(input("Valor do Deposito: "))
    saldoAtual = float(informacaoConta[3] - valor)
    if saldoAtual < 0:
        print(" Erro: Saldo insuficiente!")
    else:
        informacaoConta[3] = saldoAtual
        listarSacar.insert(0, idSacar)
        listarSacar.insert(1, idConta)
        listarSacar.insert(2, valor)
        listaTabelaSacar.insert(len(listaTabelaSacar), listarSacar)

def transferencia(idTransferencia, listarTransferencia, informacaoConta):
    idConta = int(input("ID da conta a ser depositada: "))
    valor = float(input("Valor do Deposito: "))
    saldoAtual = float(informacaoConta[3] - valor)
    if saldoAtual < 0:
        print(" Erro: Saldo insuficiente!")
    else:
        informacaoConta[3] = saldoAtual
        listarTransferencia.insert(0, idTransferencia)
        listarTransferencia.insert(1, idConta)
        listarTransferencia.insert(2, valor)
        listaTabelaTransferencia.insert(len(listaTabelaTransferencia), listarTransferencia)

def criarconta(idConta, idUsuario, idBanco):
    idConta += 1
    listaAddConta.insert(0, idConta)

    print("1 - Criar dados de um novo usuário.")
    print("2 - Utilizar dados de usuário cadastrado.")
    escolha = int(input())
    listaUsuario = []
    if escolha == 1:
        idUsuario += 1
        nomeUsuario = str(input("Adicione o nome do usuário: "))
        listaUsuario.insert(0, idUsuario)
        listaUsuario.insert(1, nomeUsuario)
        listaAddConta.insert(1, listaUsuario)
        listaCompletaUsuario.insert(len(listaCompletaUsuario), listaUsuario)
    elif escolha == 2:
        if len(listaCompletaUsuario) <= 0:
            print("ERRO: Não há usuários cadastrados.")
        else:
            x = 0
            while x < len(listaCompletaUsuario):
                print(listaCompletaUsuario[x])
                x += 1
            usuarioEscolhido = int(input("Escolha o usuário pela ID informada na lista a cima: "))
            x = 0
            while x < len(listaCompletaUsuario):
                if usuarioEscolhido == listaCompletaUsuario[x][0]:
                    listaAddConta.insert(1, listaCompletaUsuario[x])
                x += 1
    else:
        print("ERRO: Escolha invalida.")

    print("1 - Criar dados de um novo banco.")
    print("2 - Utilizar dados de banco cadastrado.")
    escolha = int(input())
    listaBanco = []
    if escolha == 1:
        idBanco += 1
        nomeBanco = str(input("Adicione o nome do banco: "))
        listaBanco.insert(0, idBanco)
        listaBanco.insert(1, nomeBanco)
        listaAddConta.insert(1, listaBanco)
        listaCompletaBanco.insert(len(listaCompletaBanco), listaBanco)
    elif escolha == 2:
        if len(listaCompletaBanco) <= 0:
            print("ERRO: Não há usuários cadastrados.")
        else:
            x = 0
            while x < len(listaCompletaBanco):
                print(listaCompletaBanco[x])
                x += 1
            bancoEscolhido = int(input("Escolha o banco pela ID informada na lista a cima: "))
            x = 0
            while x < len(listaCompletaBanco):
                if bancoEscolhido == listaCompletaBanco[x][0]:
                    listaAddConta.insert(2, listaCompletaBanco[x])
                x += 1
    else:
        print("ERRO: Escolha invalida.")

    saldo = float(input("Adicione o seu saldo: "))
    listaAddConta.insert(3, saldo)
    listaCompletaConta.insert(len(listaCompletaConta), listaAddConta)

def menuConta(informacaoConta, idDeposito, idSacar, idTransferencia):
    x = 0
    while x < 1:
        print("-------------------------------")
        print("Informações atuais da Conta:")
        print(informacaoConta)
        print("-------------------------------")
        print("1 - Depositar.")
        print("2 - Sacar.")
        print("3 - Transferencia.")
        print("4 - Recuperar Patrimônio de um usuário.")
        print("5 - Recuperar o volume de transações realizadas entre dois bancos.")
        print("6 - Sair.")
        print("-------------------------------")
        escolha = int(input("Qual ação deseja fazer? "))
        if escolha == 1:  # Depositar
            listaDeposito = []
            idDeposito += 1
            depositar(idDeposito, listaDeposito, informacaoConta)
        elif escolha == 2:  # Sacar
            listarSacar = []
            idSacar += 1
            sacar(idSacar, listarSacar, informacaoConta)
        elif escolha == 3:  # Transferencia
            listarTransferencia = []
            idTransferencia += 1
            transferencia(idTransferencia, listarTransferencia, informacaoConta)
        # elif escolha == 4:  # Recuperar Patrimônio de um usuário
        #
        # elif escolha == 5:  # Recuperar o volume de transações realizadas entre dois bancos.

        elif escolha == 6:  # Sair
            print("Saindo da conta...")
            print("")
            print("")
            break;
        else:
            print("ERRO: Numero invalido, tente novamente.")


listaTabelaDeposito = []
idDeposito = int(0)
listaTabelaSacar = []
idSacar = int(0)
listaTabelaTransferencia = []
idTransferencia = int(0)
listaCompletaUsuario = []
idUsuario = int(0)
listaCompletaBanco = []
idBanco = int(0)
listaCompletaConta = []
idConta = int(0)
x = 0;
while x < 1:
    print("-------------------------------")
    print("1 - Entrar em uma conta.")
    print("2 - Criar uma conta.")
    print("3 - Adicionar um Usuário.")
    print("4 - Adicionar um Banco.")
    print("5 - Sair.")
    print("-------------------------------")
    escolha = int(input("Adicione a numero da ação desejada: "))
    if escolha == 1:
        entrandoNaSuaConta = int(input("Adicione o ID da sua conta: "))
        x = 0
        while x < len(listaCompletaConta):
            if entrandoNaSuaConta == listaCompletaConta[x][0]:
                informacaoConta = listaCompletaConta[x]
                menuConta(informacaoConta, idDeposito, idSacar, idTransferencia)
    elif escolha == 2:
        listaAddConta = []
        criarconta(idConta, idUsuario, idBanco)
    elif escolha == 5:
        print("Fim da Operação.")
        break