class SQLCommands:
	def __init__(self, modelo):
		self.fields = modelo.fields 
		self.tb_name = modelo.tb_name

	def todos(self):
		return f"SELECT * FROM {self.tb_name}"
		#return f"SELECT * FROM {self.tb_name} ORDER BY vagas_livres"

	def get(self, id):
		return f"SELECT * FROM {self.tb_name} WHERE id = {id}"

	def inserir(self, tupla):
		campos = ', '.join(self.fields)
		valores = ', '.join([f"'{valor}'" if type(valor) == str else str(valor) for valor in tupla])
		sql_command = f"INSERT INTO {self.tb_name} ({campos}) VALUES ({valores})"
		return sql_command

	def excluir(self, id):
		return f"DELETE FROM {self.tb_name} WHERE id = {id}"

	def atualizar(self, valores):
		comando = f"UPDATE {self.tb_name} SET "
		alteracoes = []
		for i, valor in enumerate(valores[1::]):
			if type(valor) == str:
				valor = f"'{valor}'"
			alteracoes.append(f'{self.fields[i]} = {valor}')
		condicao = f' WHERE id = {valores[0]}'
		return comando + ', '.join(alteracoes) + condicao
		

