import sqlite3
from settings import DATABASE_NAME
from banco.sql_commands import sql_inserir

class Conexao:
	conn = sqlite3.connect(DATABASE_NAME)
	cursor = conn.cursor()

	def __init__(self, tb_name, field_names):
		self.tb_name = tb_name
		self.field_names = field_names

	@classmethod
	def criar_schema(cls, nome_do_schema):
		try:
			with open(nome_do_schema, 'rt') as f:
				schema = f.read()
				cls.cursor.executescript(schema)
				print("Tabela criada com sucesso")
		except sqlite3.Error:
			return False

	def novo(self, tupla):
		comando = sql_inserir(self.tb_name, self.field_names, tupla)
		self.cursor.execute(comando)
		self.conn.commit()
		print("Sucesso na inserção")




		
		


