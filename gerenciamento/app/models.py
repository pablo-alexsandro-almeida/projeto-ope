from django.db import models
from django_localflavor_br.br_states import STATE_CHOICES

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=30, null=False, blank=False)
    estado = models.CharField(max_length=3, choices=STATE_CHOICES, null=False, blank=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(blank=False, null=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)

class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=10, null=False, blank=False)
    telefone = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=254,blank=False, null=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=50, null=False, blank=False)


CATEGORIA_CHOICES = (
    ("car", "Carro"),
    ('mot', 'Moto'),
    ('cam', 'Caminhao')
) 

class Produto(models.Model):
    nome = models.CharField(max_length=70, null=False, blank=False)
    descricao = models.CharField(max_length=150, null=False, blank=False)
    preco = models.IntegerField(null=False, blank=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    codigo_fabricante = models.CharField(max_length=100, blank=False, null=False)
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, blank=False, null=False)
    peso = models.IntegerField(blank=False, null=False)

class Estoque(models.Model):
    quantidade = models.IntegerField(blank=False, null=False)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_entrada = models.DateField(blank=False, null=False)

class Item(models.Model):
    produto = models.ManyToManyField(Produto)
    quatidade = models.IntegerField(blank=False, null=False)

class Metodopagamento(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=150, blank=False, null=False)
    parcelamento = models.IntegerField(blank=False, null=False)
    bandeira = models.CharField(max_length=20, blank=False, null=False)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    endereco = models.ForeignKey(EnderecoCliente, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    data_nascimento = models.DateField(blank=False, null=False)
    profissao = models.CharField(max_length=25, null=False, blank=False)
    telefone = models.CharField(max_length=26, null=False, blank=False)

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False, null=False)
    produto = models.ManyToManyField(Item)
    desconto = models.IntegerField()
    total = models.IntegerField(blank=False, null=False)
    metodo_pagamento = models.ManyToManyField(Metodopagamento)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_venda = models.DateField(blank=False, null=False)

