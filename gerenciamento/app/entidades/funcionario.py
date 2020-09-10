class Funcionario():
    def __init__(self, nome, cpf, data_nascimento, profissao, telefone, username, password, email):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__profissao = profissao
        self.__telefone = telefone
        self.__username = username
        self.__password = password
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nome):
        self.__password = password 

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, nome):
        self.__username = username 

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome   

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def profissao(self):
        return self.__profissao

    @profissao.setter
    def profissao(self, profissao):
        self.__profissao = profissao

    @property
    def telefone(self):
        return self.__telefone
        
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone