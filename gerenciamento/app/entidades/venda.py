class Venda():
    def __init__(self, cliente, desconto, total, metodo_pagamento, vendedor, data_venda):
        self.__cliente = cliente
        self.__desconto = desconto
        self.__total = total
        self.__metodo_pagamento = metodo_pagamento
        self.__vendedor = vendedor
        self.__data_venda = data_venda
    
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, total):
        self.__total = total

    @property
    def metodo_pagamento(self):
        return self.__metodo_pagamento
    
    @metodo_pagamento.setter
    def metodo_pagamento(self, metodo_pagamento):
        self.__metodo_pagamento = metodo_pagamento

    @property
    def vendedor(self):
        return self.__vendedor
    
    @vendedor.setter
    def vendedor(self, vendedor):
        self.__vendedor = vendedor

    @property
    def data_venda(self):
        return self.__data_venda
    
    @data_venda.setter
    def data_venda(self, data_venda):
        self.__data_venda= data_venda