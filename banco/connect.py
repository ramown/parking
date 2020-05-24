import sqlite3
from settings import DATABASE_NAME
from banco.sql_commands import SQLCommands 

class Conexao:
	conn = sqlite3.connect(DATABASE_NAME)
	cursor = conn.cursor()

	def __init__(self, controle):
		self.controle = controle
		self.sql_com = SQLCommands(controle)


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
		resultado = self.cursor.execute(self.sql_com.todos())
		return resultado.fetchall()

	def get(self, id):
		resultado = self.cursor.execute(self.sql_com.get(id))
		return resultado.fetchone()


	def novo(self, tupla):
		self.cursor.execute(self.sql_com.inserir(tupla))
		self.conn.commit()


	def apagar(self, id):
		self.cursor.execute(self.sql_com.excluir(id))
		self.conn.commit()	

	
	def atualizar(self, tupla):
		self.cursor.execute(self.sql_com.atualizar(tupla))
		self.conn.commit()	

		
		
