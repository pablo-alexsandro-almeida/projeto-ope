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
    path('listar_fornecedores', listar_fornecedores, name='listar_fornecedores'),
    path('cadastrar_funcionario', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('editar_funcionario/<int:id>', editar_funcionario, name='editar_funcionario'),
    path('remover_funcionario/<int:id>', remover_funcionario, name='remover_funcionario'),
    path('cadastrar_fornecedor', cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('remover_fornecedor/<int:id>', remover_fornecedor, name='remover_fornecedor'),
    path('editar_fornecedor/<int:id>', editar_fornecedor, name='editar_fornecedor'),
    path('remover_produto<int:id>', remover_produto, name='remover_produto'),
    path('cadastrar_priduto', cadastrar_produto, name='cadastrar_produto'),
    path('editar_produto/<int:id>', editar_produto, name='editar_produto'),
    path('', login_usuario, name='login'),
    path('logout', deslogar_usuario, name='logout')
]
