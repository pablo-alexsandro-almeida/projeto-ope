class Envolve():
    def __init__(self, produto, quantidade, venda):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__venda = venda
    
    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade


    @property
    def venda(self):
        return self.__venda

    @venda.setter
    def venda(self, venda):
        self.__venda = venda