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
    Funcionario.objects.create(nome=funcionario.nome,
                               data_nascimento=funcionario.data_nascimento, cpf=funcionario.cpf,
                               profissao=funcionario.profissao, telefone=funcionario.telefone,
                               username=funcionario.username, password=funcionario.password,
                               email=funcionario.email)

def editar_funcionario(funcionario, novo_funcionario):
    funcionario.email = novo_funcionario.email
    funcionario.username = novo_funcionario.username
    funcionario.password = novo_funcionario.username
    funcionario.nome = novo_funcionario.nome
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
                           veiculo=produto.veiculo, peso=produto.peso)

def editar_produto(produto, novo_produto):
    produto.nome = novo_produto.nome
    produto.descricao = novo_produto.descricao
    produto.preco = novo_produto.preco
    produto.fornecedor = novo_produto.fornecedor
    produto.codigo_fabricante = novo_produto.codigo_fabricante
    produto.veiculo = novo_produto.veiculo
    produto.peso = novo_produto.peso
    produto.fornecedor = novo_produto.fornecedor
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

#---------------------Crud Estoque ---------------------------------------

def listar_estoque():
    return Estoque.objects.all()

def listar_estoque_id(id):
    return Estoque.objects.get(id=id)

def remover_produto_estoque(produto):
    produto.delete()

def cadastrar_produto_estoque(produto):
    Estoque.objects.create(quantidade=produto.quantidade, produto=produto.produto, 
                           data_entrada=produto.data_entrada)

def editar_produto_estoque(produto, novo_produto):
    produto.quantidade = novo_produto.quantidade
    produto.produto = novo_produto.produto
    produto.data_entrada = novo_produto.data_entrada
    produto.save(force_update=True)

#---------------------Crud Veiculo ---------------------------------------

def listar_veiculos():
    return Veiculo.objects.all()

def listar_veiculo_id(id):
    return Veiculo.objects.get(id=id)

def remover_veiculo(veiculo):
    veiculo.delete()

def cadastrar_veiculo(veiculo):
    Veiculo.objects.create(nome=veiculo.nome, cor=veiculo.cor,
                           descricao=veiculo.descricao, ano=veiculo.ano,
                           fabricante=veiculo.fabricante)

def editar_veiculo(veiculo, novo_veiculo):
    veiculo.nome = novo_veiculo.nome
    veiculo.cor = novo_veiculo.cor 
    veiculo.descricao = novo_veiculo.descricao
    veiculo.ano = novo_veiculo.ano 
    veiculo.fabricante = novo_veiculo.fabricante
    veiculo.save(force_update=True)


#------------------------Crud Metodo de Pagamento -----------------------------

def listar_metogodepagamento():
    return Metodopagamento.objects.all()

def listar_metododepagamento_id(id):
    return Metodopagamento.objects.get(id=id)

def remover_metododepagamento(metododepagamento):
    metododepagamento.delete()

def cadastrar_metododepagamento(metododepagamento):
    Metodopagamento.objects.create(nome=metododepagamento.nome,
                                   descricao=metododepagamento.descricao,
                                   parcelamento=metododepagamento.parcelamento,
                                   bandeira=metododepagamento.bandeira)

def editar_metododepagamento(metododepagamento, novo_metododepagamento):
    metododepagamento.nome = novo_metododepagamento.nome
    metododepagamento.descricao = novo_metododepagamento.descricao
    metododepagamento.parcelamento = novo_metododepagamento.parcelamento
    metododepagamento.bandeira = metododepagamento.bandeira
    metododepagamento.save(force_update=True)