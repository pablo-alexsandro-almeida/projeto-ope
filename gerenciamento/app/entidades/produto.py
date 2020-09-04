class Produto():
    def __init__(self, nome, descricao, preco, codigo_fabricante, categoria, peso):
        self.__nome = nome 
        self.__descricacao = descricacao
        self.__preco = preco
        self.__codigo_fabricante = codigo_fabricante
        self.__categoria = categoria
        self.__peso = peso
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricacao(self):
        return self.__descricacao

    @descricacao.setter
    def descricacao(self, descricacao):
        self.__descricacao = descricacao

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
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso