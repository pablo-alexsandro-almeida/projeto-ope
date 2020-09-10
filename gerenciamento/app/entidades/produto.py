class Produto():
    def __init__(self, nome, descricao, preco, codigo_fabricante, veiculo, peso, fornecedor):
        self.__nome = nome 
        self.__descricao = descricao
        self.__preco = preco
        self.__codigo_fabricante = codigo_fabricante
        self.__veiculo = veiculo
        self.__peso = peso
        self.__fornecedor = fornecedor

    @property
    def fornecedor(self):
        return self.__fornecedor

    @fornecedor.setter
    def fornecedor(self, fornecedor):
        self.__fornecedor = fornecedor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao= descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    
    @property
    def codigo_fabricante(self):
        return self.__codigo_fabricante

    @codigo_fabricante.setter
    def codigo_fabricante(self, codigo_fabricante):
        self.__codigo_fabricante = codigo_fabricante

    
    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        self.__veiculo = veiculo

    
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

