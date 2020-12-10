from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import DateInput
from django.core.validators import RegexValidator
 

class SaidaProdutoForm(forms.ModelForm):
    class Meta:
        model = Envolve
        fields = "__all__"

class ProdutoVendaForm(forms.ModelForm):
    quantidade = forms.IntegerField()
    produto = forms.ModelChoiceField(queryset=Produto.objects.all())
    class Meta:
        model = Produto
        fields = ['produto', 'quantidade']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'desconto', 'total', 'metodo_pagamento', 'vendedor', 'data_venda']
        widgets = {
            'data_venda': DateInput(
                attrs={'type':"date"}
            )
        }

class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['nome', 'cor', 'fabricante', 'ano', 'descricao']


class FuncionarioForm(UserCreationForm):
    telefone = forms.CharField(min_length=7, validators=[RegexValidator('^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$', message="Telefone invalido")])
    class Meta:
        model = Funcionario
        fields = UserCreationForm.Meta.fields + ('nome', 'cpf', 'data_nascimento', 'profissao', 'telefone', 'email')
        
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type':"date"}
            )
        }


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_fantasia', 'telefone', 'cnpj', 'email']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'codigo_fabricante', 'veiculo', 'peso', 'fornecedor'] 


class EstoqueForm(forms.ModelForm): 
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade', 'data_entrada']
        widgets = {
            'data_entrada': DateInput(
                attrs={'type':"date"}
            )
        }


class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'data_nascimento', 'profissao']

        widgets = {
            'data_nascimento': DateInput(
                attrs={'type':"date"}
            )
        }


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = EnderecoCliente
        fields = ['rua', 'cidade', 'estado']


class MetododepagamentoForm(forms.ModelForm):
    class Meta:
        model = Metodopagamento
        fields = ['nome', 'descricao', 'parcelamento', 'bandeira']