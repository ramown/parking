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
area = Area("Area B", 100, 100, 0)
controle = AreaControle()
controle.salvar(area)
