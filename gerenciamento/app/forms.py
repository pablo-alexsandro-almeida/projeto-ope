from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import DateInput
 

class FuncionarioForm(UserCreationForm):
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
