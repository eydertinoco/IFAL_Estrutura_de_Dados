class CadastrarProduto:

    def __init__(self, listaProdutos, listaAddProdutos, idProduto, nomeProduto, descricaoProduto, valorProduto):
        self.listaAddProdutos.insert(0, self.idProduto)
        self.listaAddProdutos.insert(1, self.nomeProduto)
        self.listaAddProdutos.insert(2, self.descricaoProduto)
        self.listaAddProdutos.insert(3, self.valorProduto)
        quant = len(listaProdutos)
        self.listaProdutos.insert(quant, self.listaAddProdutos)