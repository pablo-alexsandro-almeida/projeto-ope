from django.db import models
from django.contrib.auth.models import AbstractUser
from django_localflavor_br.br_states import STATE_CHOICES

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=3, choices=STATE_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.rua


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(blank=False, null=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=10, null=False, blank=False)
    telefone = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=254,blank=False, null=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome_fantasia


class Veiculo(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    ano = models.DateField(null=False, blank=False)
    cor = models.CharField(max_length=10, null=False, blank=False)
    fabricante = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=70, null=False, blank=False)
    descricao = models.CharField(max_length=150, null=False, blank=False)
    preco = models.IntegerField(null=False, blank=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    codigo_fabricante = models.CharField(max_length=100, blank=False, null=False)
    veiculo = models.ManyToManyField(Veiculo)
    peso = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    quantidade = models.IntegerField(blank=False, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_entrada = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.produto


class Metodopagamento(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=150, blank=False, null=False)
    parcelamento = models.IntegerField(blank=False, null=False)
    bandeira = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nome


class Funcionario(AbstractUser):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    profissao = models.CharField(max_length=25, null=True, blank=True)
    telefone = models.CharField(max_length=26, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    produto = models.ManyToManyField(Produto)
    desconto = models.IntegerField()
    total = models.IntegerField(blank=False, null=False)
    metodo_pagamento = models.ManyToManyField(Metodopagamento)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_venda = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.cliente

