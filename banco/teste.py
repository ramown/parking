from connect import Conexao
import os

schemas = [os.path.join('schemas_sql', nome) for nome in os.listdir('schemas_sql')]

for schema in schemas:
	Conexao.criar_schema(schema)
