from .forms import *
from .entidades import cliente, endereco, estoque, fornecedor, funcionario, produto, veiculo, metodopagamento, venda, envolve
from .services import bases
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
import tempfile
from django.contrib.auth.decorators import login_required
import json
from django.forms.models import model_to_dict


@login_required()
def dashboard(request):
    produtos = bases.produtos_vendidos()
    estoque = bases.estoque()
    cliente = bases.clientes() 
    novos_clientes = bases.novos_clientes()
    top_5 = bases.top_5()
    pessoas = bases.listar_funcionarios()
    dados = {'produtos_vendidos': len(produtos), 
             'estoque':estoque,
             'clientes': cliente,
             'novos': len(novos_clientes),
              'top': top_5,
               'pessoas': pessoas}

    return render(request, 'dashboard/dashboard.html', dados)


@login_required()
def listar_venda(request):
    vendas = bases.listar_vendas()
    return render(request, 'venda/lista_venda.html', {'vendas': vendas})


@login_required()
def listar_funcionarios(request):
    funcionarios = bases.listar_funcionarios()
    return render(request, 'funcionario/lista_funcionarios.html', {'funcionarios': funcionarios})

@login_required()
def listar_produtos(request):
    produtos = bases.listar_produtos()
    return render(request, 'produto/lista_produtos.html', {'produtos':produtos})


@login_required()
def listar_fornecedores(request):
    fornecedores = bases.listar_fornecedores()
    return render(request, 'fornecedor/listar_fornecedores.html', {'fornecedores':fornecedores})


@login_required()
def listar_clientes(request):
    clientes = bases.listar_cliente()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


@login_required()
def lista_fornecedor_id(request, id):
    entrada = bases.historico_entrada(id)
    fornecedor = bases.listar_fornecedor_id(id)
    return render(request, 'fornecedor/lista_fornecedor.html', {'fornecedor': fornecedor, 'historico': entrada})


@login_required()
def listar_cliente_id(request, id):
    cliente = bases.listar_cliente_id(id)
    compras = bases.historio_vendas(id) 
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente, 'historico': compras})


@login_required()
def listar_estoque(request):
    estoque = bases.listar_estoque()
    return render(request, 'estoque/listar_estoque.html', {'estoques': estoque})


@login_required()
def listar_veiculos(request):
    veiculos = bases.listar_veiculos()
    return render(request, 'veiculos/listar_veiculos.html', {'veiculos': veiculos})


@login_required()
def listar_metododepagamento(request):
    metododepagamento = bases.listar_metogodepagamento()
    return render(request, 'metododepagamento/listar_metododepagamento.html', {'metododepagamentos': metododepagamento})


@login_required()
def cadastrar_metododepagamento(request):
    if request.method == 'POST':
        form_metododepagamento = MetododepagamentoForm(request.POST)
        if form_metododepagamento.is_valid():
            nome = form_metododepagamento.cleaned_data['nome']
            descricao = form_metododepagamento.cleaned_data['descricao']
            parcelamento = form_metododepagamento.cleaned_data['parcelamento']
            bandeira = form_metododepagamento.cleaned_data['bandeira']
            metodo_novo = metodopagamento.Metodopagamento(nome=nome, descricao=descricao,
                                                          parcelamento=parcelamento, bandeira=bandeira)
            metodo_bd = bases.cadastrar_metododepagamento(metodo_novo)
            return redirect('listar_metododepagamento')
    else:
        form_metododepagamento = MetododepagamentoForm()
        return render(request, 'metododepagamento/forms_metododepagamento.html', {'form_metodo': form_metododepagamento})


@login_required()
def cadastrar_veiculo(request):
    if request.method == 'POST':
        form_veiculo = VeiculosForm(request.POST)
        if form_veiculo.is_valid():
            nome = form_veiculo.cleaned_data['nome']
            descricao = form_veiculo.cleaned_data['descricao']
            fabricante = form_veiculo.cleaned_data['fabricante']
            cor = form_veiculo.cleaned_data['cor']
            ano = form_veiculo.cleaned_data['ano']
            veiculo_novo = veiculo.Veiculo(nome=nome, descricao=descricao, fabricante=fabricante,
                                           cor=cor, ano=ano)
            veiculo_bd = bases.cadastrar_veiculo(veiculo_novo)
            return redirect('listar_veiculos')
    else:
        form_veiculo = VeiculosForm()
        return render(request, 'veiculos/forms_veiculo.html', {'form_veiculo': form_veiculo})


@login_required()
def cadastrar_estoque(request):
    if request.method == 'POST':
        form_estoque = EstoqueForm(request.POST)
        if form_estoque.is_valid():
            quantidade = form_estoque.cleaned_data['quantidade']
            produto = form_estoque.cleaned_data['produto']
            data_entrada  = form_estoque.cleaned_data['data_entrada']
            estoque_novo = estoque.Estoque(produto=produto, quantidade=quantidade, 
                                           data_entrada=data_entrada)
            estoque_bd = bases.cadastrar_produto_estoque(estoque_novo)

            return redirect('listar_estoque')
    else:
        form_estoque = EstoqueForm()
        return render(request, 'estoque/forms_estoque.html', {'form_estoque': form_estoque})


@login_required()
def cadastrar_venda(request):
    form_produto = ProdutoVendaForm(request.POST or None)
    form_venda = VendaForm(request.POST or None)
    items = []
    if request.method == "POST" and 'submit-general-add' in request.POST:
        if form_venda.is_valid() and form_produto.is_valid():
            if 'items' in request.session:
                items = request.session['items']
            produto = form_produto.cleaned_data['produto']
            quantidade = form_produto.cleaned_data['quantidade']

            item = {'produto': model_to_dict(produto),
                    'quantidade': quantidade}
            try:
                items.index(item)
            except:
                items.append(item)
                request.session['cliente'] = str(form_venda.cleaned_data['cliente'])
                request.session['desconto'] =  str(form_venda.cleaned_data['desconto'])
                request.session['total'] =  str(form_venda.cleaned_data['total'])
                request.session['metodo_pagamento'] =  str(form_venda.cleaned_data['metodo_pagamento'])
                request.session['vendedor'] =  str(form_venda.cleaned_data['vendedor'])
                request.session['data_venda'] =  str(form_venda.cleaned_data['data_venda'])
                request.session['items'] = items

            return render(request, 'venda/forms_vendas.html', {
                'form_venda': form_venda, 
                'form_produto':form_produto,
                'items': items} )

    elif request.method == "POST" and 'submit-general-geral' in request.POST:
        if form_venda.is_valid():
            cliente = form_venda.cleaned_data['cliente']
            desconto = form_venda.cleaned_data['desconto']
            total = form_venda.cleaned_data['total']
            metodo_pagamento = form_venda.cleaned_data['metodo_pagamento']
            vendedor = form_venda.cleaned_data['vendedor']
            data_venda = form_venda.cleaned_data['data_venda']
            nova_venda = venda.Venda(cliente=cliente,
                                     desconto=desconto, total=total,
                                     metodo_pagamento=metodo_pagamento,
                                     vendedor=vendedor, data_venda=data_venda)
            n_venda = bases.cadastrar_venda(nova_venda)
            for item in request.session['items']:
                produto = bases.get_product(item['produto'])
                quantidade = item['quantidade']
                envolvimento = envolve.Envolve(produto=produto, quantidade=quantidade, venda=n_venda)
                saida_produto = bases.saida_produto(envolvimento)
            return redirect('listar_venda')  

    if request.method == "POST":
        if 'items' in request.session:
            items = request.session['items']            
        return render(request, 'venda/forms_vendas.html', {
                'form_venda': form_venda, 
                'form_produto':form_produto,
                'items': items} )

    request.session['items'] = items
    return render(request, 'venda/forms_vendas.html', {
        'form_venda': form_venda, 
        'form_produto':form_produto,
        'items': items})

  

@login_required()
def cadastro_produto(request, id):
    form_produto = ProdutoVendaForm(request.POST)
    if request.method == "POST" and 'submit-general-add' in request.POST:
        pass
    else: 
        form_produto = ProdutoVendaForm()
        return render(request, 'venda/forms_produtos.html', {'form_produto': form_produto})


@login_required()
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


@login_required()
def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form_fornecedor = FornecedorForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_fornecedor.is_valid():
            nome_fantasia = form_fornecedor.cleaned_data['nome_fantasia']
            telefone = form_fornecedor.cleaned_data['telefone'] 
            cnpj = form_fornecedor.cleaned_data['cnpj'] 
            email = form_fornecedor.cleaned_data['email']
            if form_endereco.is_valid(): 
                rua = form_endereco.cleaned_data["rua"]
                cidade = form_endereco.cleaned_data["cidade"]
                estado = form_endereco.cleaned_data["estado"]
                endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
                endereco_bd = bases.cadastrar_endereco(endereco_novo)
                fornecedor_novo = fornecedor.Fornecedor(nome_fantasia=nome_fantasia, telefone=telefone,
                                                        cnpj=cnpj, email=email, endereco=endereco_bd)
                fornecedor_bd = bases.cadastar_fornecedor(fornecedor_novo)
                return redirect('listar_fornecedores')
    else:
        form_fornecedor = FornecedorForm()
        form_endereco = EnderecoForm()
    
    return render(request, 'fornecedor/forms_fornecedor.html', {'form_fornecedor': form_fornecedor, 'form_endereco': form_endereco})


@login_required()
def cadastrar_produto(request):
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)        
        if form_produto.is_valid():
            nome = form_produto.cleaned_data['nome']
            descricao = form_produto.cleaned_data['descricao']
            preco = form_produto.cleaned_data['preco']
            codigo_fabricante = form_produto.cleaned_data['codigo_fabricante']
            veiculo = form_produto.cleaned_data['veiculo']
            peso = form_produto.cleaned_data['peso']
            fornecedor = form_produto.cleaned_data['fornecedor']
            produto_novo = produto.Produto(nome=nome, descricao=descricao, preco=preco, 
                                           codigo_fabricante=codigo_fabricante, veiculo=veiculo,
                                           peso=peso, fornecedor=fornecedor,)
            produto_bd = bases.cadastar_produto(produto_novo)
            return redirect('listar_produtos')
    else:
        form_produto = ProdutoForm()
    return render(request, 'produto/forms_produtos.html', {'form_produto': form_produto})


@login_required()
def cadastrar_funcionario(request):
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST)
        if form_funcionario.is_valid():
            nome = form_funcionario.cleaned_data['nome']
            cpf = form_funcionario.cleaned_data['cpf']
            data_nascimento = form_funcionario.cleaned_data['data_nascimento']
            profissao = form_funcionario.cleaned_data['profissao']
            telefone = form_funcionario.cleaned_data['telefone']
            username = form_funcionario.cleaned_data['username']
            password = make_password(form_funcionario.cleaned_data['password1'])
            email = form_funcionario.cleaned_data['email']
            
            funcionario_novo = funcionario.Funcionario(nome=nome, cpf=cpf, email=email, 
                                                        data_nascimento=data_nascimento, profissao=profissao, 
                                                        telefone=telefone,
                                                        username=username, password=password)
            funcionario_bd = bases.cadastrar_funcionario(funcionario_novo)

            return redirect('listar_funcionarios')
    else:
        form_funcionario = FuncionarioForm()
        form_endereco = EnderecoForm()
    return render(request, 'funcionario/forms_funcionarios.html', {'form_funcionario': form_funcionario})


@login_required()
def editar_veiculo(request, id):
    veiculo_editar = bases.listar_veiculo_id(id)
    form_veiculo = VeiculosForm(request.POST or None, instance = veiculo_editar)
    if request.method == "POST":
        if form_veiculo.is_valid():
            nome = form_veiculo.cleaned_data['nome']
            descricao = form_veiculo.cleaned_data['descricao']
            fabricante = form_veiculo.cleaned_data['fabricante']
            cor = form_veiculo.cleaned_data['cor']
            ano = form_veiculo.cleaned_data['ano']
            veiculo_novo = veiculo.Veiculo(nome=nome, descricao=descricao, fabricante=fabricante,
                                           cor=cor, ano=ano)
            veiculo_bd = bases.editar_veiculo(veiculo_editar, veiculo_novo)
            return redirect('listar_veiculos')

    return render(request, 'veiculos/forms_veiculo.html', {'form_veiculo': form_veiculo})


@login_required()
def editar_metododepagamento(request, id):
    metodopagamento_editar = bases.listar_metododepagamento_id(id)
    form_metododepagamento = MetododepagamentoForm(request.POST or None, instance=metodopagamento_editar)
    if form_metododepagamento.is_valid():
            nome = form_metododepagamento.cleaned_data['nome']
            descricao = form_metododepagamento.cleaned_data['descricao']
            parcelamento = form_metododepagamento.cleaned_data['parcelamento']
            bandeira = form_metododepagamento.cleaned_data['bandeira']
            metodo_novo = metodopagamento.Metodopagamento(nome=nome, descricao=descricao,
                                                          parcelamento=parcelamento, bandeira=bandeira)
            
            metodo_bd = bases.editar_metododepagamento(metodopagamento_editar, metodo_novo)
            return redirect('listar_metododepagamento')
    
    return render(request, 'metododepagamento/forms_metododepagamento.html', {'form_metodo': form_metododepagamento})


@login_required()
def editar_estoque(request, id):
    estoque_editar = bases.listar_estoque_id(id)
    form_estoque = EstoqueForm(request.POST or None, instance=estoque_editar)
    if request.method == 'POST':
        if form_estoque.is_valid():
            quantidade = form_estoque.cleaned_data['quantidade']
            produto = form_estoque.cleaned_data['produto']
            data_entrada  = form_estoque.cleaned_data['data_entrada']
            estoque_novo = estoque.Estoque(produto=produto, quantidade=quantidade, 
                                           data_entrada=data_entrada)
            estoque_bd = bases.editar_produto_estoque(estoque_editar, estoque_novo)

            return redirect('listar_estoque')

    return render(request, 'estoque/forms_estoque.html', {'form_estoque': form_estoque})


@login_required()
def editar_produto(request, id):
    produto_editar = bases.listar_protudo_id(id)
    form_produto = ProdutoForm(request.POST or None, instance=produto_editar)
    if request.method == 'POST':
        form_produto = ProdutoForm(request.POST)        
        if form_produto.is_valid():
            nome = form_produto.cleaned_data['nome']
            descricao = form_produto.cleaned_data['descricao']
            preco = form_produto.cleaned_data['preco']
            codigo_fabricante = form_produto.cleaned_data['codigo_fabricante']
            veiculo = form_produto.cleaned_data['veiculo']
            peso = form_produto.cleaned_data['peso']
            fornecedor = form_produto.cleaned_data['fornecedor']
            produto_novo = produto.Produto(nome=nome, descricao=descricao, preco=preco, 
                                           codigo_fabricante=codigo_fabricante, veiculo=veiculo,
                                           peso=peso, fornecedor=fornecedor)
            produto_bd = bases.editar_produto(produto_editar, produto_novo)
            return redirect('listar_produtos')
    
    return render(request, 'produto/forms_produtos.html', {'form_produto': form_produto})


@login_required()
def editar_funcionario(request, id):
    funcionario_editar = bases.listar_funcionario_id(id)
    funcionario_editar.data_nascimento = funcionario_editar.data_nascimento.strftime('%Y-%m-%d') #Conversão da data
    form_funcionario = FuncionarioForm(request.POST or None, instance=funcionario_editar)
    if form_funcionario.is_valid():
        nome = form_funcionario.cleaned_data['nome']
        cpf = form_funcionario.cleaned_data['cpf']
        data_nascimento = form_funcionario.cleaned_data['data_nascimento']
        email = form_funcionario.cleaned_data['email']
        profissao = form_funcionario.cleaned_data['profissao']
        telefone = form_funcionario.cleaned_data['telefone']
        username = form_funcionario.cleaned_data['username']
        password = make_password(form_funcionario.cleaned_data['password1'])
        funcionario_novo = funcionario.Funcionario(nome=nome, cpf=cpf, username=username, password=password, 
                                            data_nascimento=data_nascimento, profissao=profissao, 
                                            telefone=telefone, email=email)
        bases.editar_cliente(funcionario_editar, funcionario_novo)
        return redirect('listar_funcionarios')

    return render(request, 'funcionario/forms_funcionarios.html', {'form_funcionario': form_funcionario})


@login_required()
def editar_fornecedor(request, id):
    fornecedor_editar = bases.listar_fornecedor_id(id)
    form_fornecedor = FornecedorForm(request.POST or None, instance=fornecedor_editar)
    endereco_editar = bases.listar_endereco_id(fornecedor_editar.endereco.id)
    form_endereco = EnderecoForm(request.POST or None, instance=endereco_editar)
    if form_fornecedor.is_valid():
        nome_fantasia = form_fornecedor.cleaned_data['nome_fantasia']
        telefone = form_fornecedor.cleaned_data['telefone'] 
        cnpj = form_fornecedor.cleaned_data['cnpj'] 
        email = form_fornecedor.cleaned_data['email']
        if form_endereco.is_valid(): 
            rua = form_endereco.cleaned_data["rua"]
            cidade = form_endereco.cleaned_data["cidade"]
            estado = form_endereco.cleaned_data["estado"]
            endereco_novo = endereco.Endereco(rua=rua, cidade=cidade, estado=estado)
            endereco_bd = bases.editar_endereco(endereco_editar, endereco_novo)
            fornecedor_novo = fornecedor.Fornecedor(nome_fantasia=nome_fantasia, telefone=telefone,
                                                    cnpj=cnpj, email=email, endereco=endereco_bd)
            fornecedor_bd = bases.editar_fornecedor(fornecedor_editar, fornecedor_novo)
            return redirect('listar_fornecedores')
    return render(request, 'fornecedor/forms_fornecedor.html', {'form_fornecedor': form_fornecedor, 'form_endereco': form_endereco})



@login_required()
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


@login_required()
def remover_fornecedor(request, id):
    fornecedor = bases.listar_fornecedor_id(id)
    endereco = bases.listar_endereco_id(fornecedor.endereco.id)
    if request.method == 'POST':
        bases.remover_fornecedor(fornecedor)
        bases.remover_endereco(endereco)
        return redirect('listar_fornecedores')
    return render(request, 'fornecedor/confirmar_exclusao.html', {'fornecedor': fornecedor})



@login_required()
def remover_funcionario(request, id):
    funcionario = bases.listar_funcionario_id(id)
    if request.method == 'POST':
        bases.remover_funcionario(funcionario)
        return redirect('listar_funcionarios')
    return render(request, 'funcionario/confirmar_exclusao.html', {'funcionario': funcionario})


@login_required()
def remover_produto(request, id):
    produto = bases.listar_protudo_id(id)
    if request.method == "POST":
        bases.remover_produto(produto)
        return redirect('listar_produtos')
    return render(request, 'produto/confirmar_exclusao.html', {'produto':produto})


@login_required()
def remover_estoque(request, id):
    estoque = bases.listar_estoque_id(id)
    if request.method == "POST":
        bases.remover_produto_estoque(estoque)
        return redirect('listar_estoque')
    return render(request, 'estoque/confirmar_exclusao.html', {'estoque':estoque})


@login_required()
def remover_veiculo(request, id):
    veiculo = bases.listar_veiculo_id(id)
    if request.method == "POST":
        bases.remover_veiculo(veiculo)
        return redirect('listar_veiculos')
    return render(request, 'veiculos/confirmar_exclusao.html', {'veiculo': veiculo})


@login_required()
def remover_cliente(request, id):
    cliente = bases.listar_cliente_id(id)
    endereco = bases.listar_endereco_id(cliente.endereco.id)
    if request.method == 'POST':
        bases.remover_endereco(endereco)
        bases.remover_cliente(cliente)
        return redirect('listar_cliente')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente':cliente})


@login_required()
def remover_metododepagamento(request, id):
    metodo = bases.listar_metododepagamento_id(id)
    if request.method == 'POST':
        bases.remover_metododepagamento(metodo)
        return redirect('listar_metododepagamento')
    return render(request, 'metododepagamento/confirma_exclusao.html', {'metodo': metodo})



def login_usuario(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('dashboard')
            else:
                messages.error(request, "Credencias informadas estão erradas")
                return redirect('login')
    else:
        form_login = AuthenticationForm()
        return render(request, 'autenticacao/login.html', {'form_login':form_login})


@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('login')


@login_required()
def gerar_pdf_Venda(request, id):
    venda = bases.listar_venda_id(id)
    produtos = bases.listar_envolve(venda.id)
    total = 0 
    for x in produtos:
        total += x.quantidade
    html_string = render_to_string('dashboard/pdf.html', {'venda': venda, 'produtos':produtos, 'total':total})
    html = HTML(string=html_string)
    resultado_pdf = html.write_pdf()

    resposta = HttpResponse(content_type='application/pdf;')
    resposta['Content-Disposition'] = 'inline; filename=lista_pedidos.pdf'
    resposta['Content-Transfer-Enconding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(resultado_pdf)
        output.flush()
        output = open(output.name, 'rb')
        resposta.write(output.read())

    return resposta