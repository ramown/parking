from banco.connect import Conexao
from controles.areas_controle import AreaControle
from modelos.area import Area
import os

# schemas = [os.path.join('schemas_sql', nome) for nome in os.listdir('schemas_sql')]

# for schema in schemas:
# 	Conexao.criar_schema(schema)
# campos = ['nome', 'idade', 'qualquer']
# tupla = (1,2,3)
# Conexao('tb_name', campos).novo(tupla)
controle = AreaControle()
modelo = Area("Area ZF", 100, 100, 0)

modelo_find = controle.get_id(4)
# print(modelo_find.tupla())
print(controle.get_id(4).tupla())
modelo_find.nome = 'Zona BB'
# modelo_find.vagas_livres = 50
controle.salvar(modelo)

for i in controle.todos():
	print(i)
