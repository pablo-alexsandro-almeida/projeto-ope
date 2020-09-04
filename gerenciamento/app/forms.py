from django import forms
from .models import *
from django.forms import DateInput
 
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'cpf', 'data_nascimento', 'profissao', 'telefone']
        
        widgets = {
            'data_nascimento': DateInput(
                attrs={'type':"date"}
            )
        }


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'codigo_fabricante', 'categoria', 'peso'] 


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_fantasia', 'telefone', 'cnpj', 'email']


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
