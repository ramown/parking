import sqlite3
from settings import DATABASE_NAME
from banco.sql_commands import sql_inserir

class Conexao:
	conn = sqlite3.connect(DATABASE_NAME)
	cursor = conn.cursor()

	def __init__(self, modelo):
		self.modelo = modelo


	@classmethod
	def criar_schema(cls, nome_do_schema):
		try:
			with open(nome_do_schema, 'rt') as f:
				schema = f.read()
				cls.cursor.executescript(schema)
				print("Tabela criada com sucesso")
		except sqlite3.Error:
			return False

	def todos(self):
		pass


	def novo(self, tupla):
		comando = sql_inserir(self.modelo.tb_name, self.modelo.fields, tupla)
		self.cursor.execute(comando)
		self.conn.commit()
		print("Sucesso na inserção")
