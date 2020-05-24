import sqlite3
from settings import DATABASE_NAME

class Conexao:
	conn = sqlite3.connect(DATABASE_NAME)
	cursor = conn.cursor()

	@classmethod
	def criar_schema(cls, nome_do_schema):
		try:
			with open(nome_do_schema, 'rt') as f:
				schema = f.read()
				cls.cursor.executescript(schema)
				print("Tabela criada com sucesso")
		except sqlite3.Error:
			return False



		
		


