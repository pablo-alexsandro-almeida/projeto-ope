class Veiculo():
    def __init__(self, nome, descricao, fabricante, cor, ano):
        self.__nome = nome 
        self.__descricao = descricao
        self.__fabricante = fabricante
        self.__cor = cor
        self.__ano = ano
 
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome= nome


    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao


    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano