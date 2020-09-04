from .forms import ClientesForm, EnderecoForm, FornecedorForm, FuncionarioForm, ProdutoForm
from .entidades import cliente, endereco, fornecedor, funcionario, produto
from .services import bases
from django.shortcuts import render, redirect


def listar_funcionarios(request):
    funcionarios = bases.listar_funcionarios()
    return render(request, 'funcionario/lista_funcionarios.html', {'funcionarios': funcionarios})


def listar_produtos(request):
    produtos = bases.listar_produtos()
    return render(request, 'produto/lista_produtos.html', {'produtos':produtos})


def listar_forncedores(request):
    fornecedores = bases.listar_fornecedores()
    return render(request, 'fornecedor/listar_fornecedores.html', {'forneccedores':fornecedores})


def listar_clientes(request):
    clientes = bases.listar_cliente()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def listar_cliente_id(request, id):
    cliente = bases.listar_cliente_id(id=id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})


def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            email = form_funcionario.cleaned_data['email']
            cpf = form_funcionario.cleaned_data['cpf']
            data_nascimento = form_funcionario.cleaned_data['data_nascimento']
            profissao = form_funcionario.cleaned_data['profissao']
            telefone = form_funcionario.cleaned_data['telefone']
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = bases.cadastrar_endereco(endereco_novo)
                funcionario_novo = funcionario.Funcionario(nome=nome, email=email, cpf=cpf, 
                                                         data_nascimento=data_nascimento, profissao=profissao, 
                                                         telefone=telefone, endereco=endereco_bd)
                funcionario_bd = bases.cadastrar_funcionario(funcionario_novo)

                return redirect('listar_funcionarios')
    else:
        form_funcionario = FuncionarioForm()
        form_endereco = EnderecoForm()
    return render(request, 'funcionario/forms_funcionarios.html', {'form_funcionario': form_funcionario, 'form_endereco': form_endereco})


def Cadastrar_cliente(request):
    if request.method == 'POST':
        form_cliente = ClientesForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_cliente.is_valid():
            nome = form_cliente.cleaned_data['nome']
            email = form_cliente.cleaned_data['email']
            cpf = form_cliente.cleaned_data['cpf']
            data_nascimento = form_cliente.cleaned_data['data_nascimento']
            profissao = form_cliente.cleaned_data['profissao']
            if form_endereco.is_valid():
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = bases.cadastrar_endereco(endereco_novo)
                Cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, 
                                      data_nascimento=data_nascimento, 
                                      profissao=profissao, endereco=endereco_bd)
                cliente_bd = bases.cadastrar_cliente(Cliente_novo)

                return redirect('listar_cliente')

    else:
        form_cliente = ClientesForm()
        form_endereco = EnderecoForm()

    return render(request, 'clientes/forms_clientes.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})


def editar_funcionario(request, id):
    funcionario_editar = bases.listar_funcionario_id(id)
    funcionario_editar.data_nascimento = funcionario_editar.data_nascimento.strftime('%Y-%m-%d') #Conversão da data
    form_funcionario = FuncionarioForm(request.POST or None, instance=funcionario_editar)
    endereco_editar = bases.listar_endereco_id(funcionario_editar.endereco.id)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco_editar)
    if form_funcionario.is_valid():
        nome = form_funcionario.cleaned_data['nome']
        email = form_funcionario.cleaned_data['email']
        cpf = form_funcionario.cleaned_data['cpf']
        data_nascimento = form_funcionario.cleaned_data['data_nascimento']
        profissao = form_funcionario.cleaned_data['profissao']
        telefone = form_funcionario.cleaned_data['telefone']
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_bd = bases.editar_endereco(endereco_editar, endereco_novo)
            funcionario_novo = funcionario.Funcionario(nome=nome, email=email, cpf=cpf, 
                                                       data_nascimento=data_nascimento, profissao=profissao, 
                                                       telefone=telefone, endereco=endereco_bd)
            bases.editar_cliente(funcionario_editar, funcionario_novo)
            return redirect('listar_funcionarios')

    return render(request, 'funcionario/forms_funcionarios.html', {'form_funcionario': form_funcionario, 'form_endereco': form_endereco})


def editar_cliente(request, id):
    cliente_editar = bases.listar_cliente_id(id)
    cliente_editar.data_nascimento = cliente_editar.data_nascimento.strftime('%Y-%m-%d') #Conversão da data
    form_cliente = ClientesForm(request.POST or None, instance=cliente_editar)
    endereco_editar = bases.listar_endereco_id(cliente_editar.endereco.id)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco_editar)
    if form_cliente.is_valid():
        nome = form_cliente.cleaned_data['nome']
        email = form_cliente.cleaned_data['email']
        cpf = form_cliente.cleaned_data['cpf']
        data_nascimento = form_cliente.cleaned_data['data_nascimento']
        profissao = form_cliente.cleaned_data['profissao']
        if form_endereco.is_valid():
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_bd = bases.editar_endereco(endereco_editar, endereco_novo)
            Cliente_novo = cliente.Cliente(nome=nome, email=email, cpf=cpf, 
                                    data_nascimento=data_nascimento, 
                                    profissao=profissao, endereco=endereco_bd)
            bases.editar_cliente(cliente_editar, Cliente_novo)
            return redirect('listar_cliente')
    return render(request, 'clientes/forms_clientes.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})


def remover_funcionario(request, id):
    funcionario = bases.listar_funcionario_id(id)
    endereco = bases.listar_endereco_id(funcionario.endereco.id)
    if request.method == 'POST':
        bases.remover_funcionario(funcionario)
        bases.remover_endereco(endereco)
        return redirect('listar_funcionarios')
    return render(request, 'funcionario/confirmar_exclusao.html', {'funcionario': funcionario})

    
def remover_cliente(request, id):
    cliente = bases.listar_cliente_id(id)
    endereco = bases.listar_endereco_id(cliente.endereco.id)
    if request.method == 'POST':
        bases.remover_endereco(endereco)
        bases.remover_cliente(cliente)
        return redirect('listar_cliente')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente':cliente})