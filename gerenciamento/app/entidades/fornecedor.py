class Fornecedor():
    def __init__(self, nome_fantasia, telefone, cnpj, email, endereco):
        self.__nome_fantasia = nome_fantasia
        self.__telefone = telefone
        self.__cnpj = cnpj
        self.__email = email 
        self.__endereco = endereco
    

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco


    @property
    def nome_fantasia(self):
        return self.__nome_fantasia

    @nome_fantasia.setter
    def nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    