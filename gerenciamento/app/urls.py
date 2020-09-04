from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_cliente', Cadastrar_cliente, name='cadastrar_cliente'),
    path('listar_cliente', listar_clientes, name='listar_cliente'),
    path('listar_clientes/<int:id>', listar_cliente_id, name='listar_cliente_id'),
    path('editar_cliente/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', remover_cliente, name='remover_cliente'),
    path('listar_funciorarios', listar_funcionarios, name='listar_funcionarios'),
    path('listar_produtos', listar_produtos, name='listar_produtos'),
    path('listar_fornecedores', listar_forncedores, name='listar_forncedores'),
    path('cadastrar_funcionario', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('editar_funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
    path('remover_funcionario/<int:id>', remover_funcionario, name='remover_funcionario')
]
