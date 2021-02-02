class CadastrarCliente:

    def __init__(self, listaClientes, listaAddClientes, nomeCliente,
                 cpfCliente, ruaCliente, cepCliente, cidadeCliente):
        self.listaAddClientes.insert(0, self.nomeCliente)
        self.listaAddClientes.insert(1, self.cpfCliente)
        self.listaAddClientes.insert(2, self.ruaCliente)
        self.listaAddClientes.insert(3, self.cepCliente)
        self.listaAddClientes.insert(4, self.cidadeCliente)
        quant = len(listaClientes)
        self.listaClientes.insert(quant, self.listaAddClientes)