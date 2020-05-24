from banco.connect import Conexao
from settings import *

def criar_schemas():
	for schema in SCHEMAS:
		Conexao.criar_schema(schema)

commands = {
            'gerar_tabelas': criar_schemas()
            }
