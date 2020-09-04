from ..models import *


#---------------------Crud Clientes ---------------------------------------

def cadastrar_cliente(cliente):
    Cliente.objects.create(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco, cpf=cliente.cpf,
                           data_nascimento=cliente.data_nascimento, profissao=cliente.profissao)

def editar_cliente(cliente, novo_cliente):
    cliente.nome = novo_cliente.nome
    cliente.email = novo_cliente.email
    cliente.endereco = novo_cliente.endereco
    cliente.cpf = novo_cliente.cpf
    cliente.data_nascimento = novo_cliente.data_nascimento
    cliente.profissao = novo_cliente.profissao
    cliente.save(force_update=True)

def listar_cliente():
    return Cliente.objects.all()

def listar_cliente_id(id):
    return Cliente.objects.get(id=id)


def remover_cliente(cliente):
    cliente.delete()


#---------------------Crud Endereco ---------------------------------------

def listar_endereco_id(id):
    return EnderecoCliente.objects.get(id=id)

def cadastrar_endereco(endereco):
    return EnderecoCliente.objects.create(rua=endereco.rua, cidade=endereco.cidade, estado=endereco.estado)

def editar_endereco(endereco, novo_endereco):
    endereco.rua = novo_endereco.rua
    endereco.cidade = novo_endereco.cidade
    endereco.estado = novo_endereco.estado
    endereco.save(force_update=True)
    return endereco

def remover_endereco(endereco):
    endereco.delete()


#---------------------Crud funcionarios ---------------------------------------

def listar_funcionarios():
    return Funcionario.objects.all()

def listar_funcionario_id(id):
    return Funcionario.objects.get(id=id)

def cadastrar_funcionario(funcionario):
    Funcionario.objects.create(nome=funcionario.nome, email=funcionario.email, endereco=funcionario.endereco,
                               data_nascimento=funcionario.data_nascimento, cpf=funcionario.cpf,
                               profissao=funcionario.profissao, telefone=funcionario.telefone)

def editar_funcionario(funcionario, novo_funcionario):
    funcionario.nome = novo_funcionario.nome
    funcionario.email = novo_funcionario.email
    funcionario.endereco = novo_funcionario.endereco
    funcionario.data_nascimento = novo_funcionario.data_nascimento
    funcionario.cpf = novo_funcionario.cpf
    funcionario.profissao = novo_funcionario.profissao
    funcionario.telefone = novo_funcionario.telefone
    funcionario.save(force_save=True)

def remover_funcionario(funcionario):
    funcionario.delete()


#---------------------Crud Produtos---------------------------------------

def listar_produtos():
    return Produto.objects.all()

def listar_protudo_id(id):
    return Produto.objects.get(id=id)

def cadastar_produto(produto):
    Produto.objects.create(nome=produto.nome, descricao=produto.descricao, preco=produto.preco,
                           fornecedor=produto.fornecedor, codigo_fabricante=produto.codigo_fabricante,
                           categoria=produto.categoria, peso=produto.peso)

def editar_produto(produto, novo_produto):
    produto.nome = novo_produto.nome
    produto.descricao = novo_produto.descricao
    produto.preco = novo_produto.preco
    produto.fornecedor = novo_produto.fornecedor
    produto.codigo_fabricante = novo_produto.codigo_fabricante
    produto.categoria = novo_produto.categoria
    produto.peso = novo_produto.peso
    produto.save(force_update=True)

def remover_produto(produto):
    produto.delete()


#---------------------Crud Fornecedor ---------------------------------------

def listar_fornecedores():
    return Fornecedor.objects.all()

def listar_fornecedor_id(id):
    return Fornecedor.objects.get(id=id)

def cadastar_fornecedor(fornecedor):
    Fornecedor.objects.create(nome_fantasia=fornecedor.nome_fantasia, telefone=fornecedor.telefone, 
                              email=fornecedor.email, endereco=fornecedor.endereco, 
                              cnpj=fornecedor.cnpj)

def editar_fornecedor(fornecedor, novo_fornecedor):
    fornecedor.nome_fantasia = novo_fornecedor.nome_fantasia
    fornecedor.telefone = novo_fornecedor.telefone
    fornecedor.email = novo_fornecedor.email
    fornecedor.endereco = novo_fornecedor.endereco
    fornecedor.cnpj = novo_fornecedor.cnpj
    fornecedor.save(force_update=True)

def remover_fornecedor(fornecedor):
    fornecedor.delete()