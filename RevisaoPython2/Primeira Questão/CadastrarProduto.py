class CadastrarProduto:
    listaAddProdutos = []

    def __init__(self, idProduto, nomeProduto, descricaoProduto, valorProduto):
        self.idProduto = idProduto
        self.nomeProduto = nomeProduto
        self.descricaoProduto = descricaoProduto
        self.valorProduto = valorProduto
        CadastrarProduto.listaAddProdutos.extend(idProduto, nomeProduto, descricaoProduto, valorProduto)

