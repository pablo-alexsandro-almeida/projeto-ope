class Metodopagamento():
    def __init__(self, nome, descricao, parcelamento, bandeira):
        self.__nome = nome
        self.__descricao= descricao
        self.__parcelamento = parcelamento
        self.__bandeira = bandeira

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
        self.__descricao = descricao

    
    @property
    def parcelamento(self):
        return self.__parcelamento

    @parcelamento.setter
    def parcelamento(self, parcelamento):
        self.__parcelamento = parcelamento

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira


        