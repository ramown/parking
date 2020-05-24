class SQLCommands:
	def __init__(self, modelo):
		self.fields_names = modelo.fields 
		self.tb_name = modelo.tb_name

	def todos(self):
		return f"SELECT * FROM {self.tb_name}"

	def inserir(self, tupla):
		campos = ', '.join(self.fields_names)
		valores = ', '.join([f"'{valor}'" if type(valor) == str else str(valor) for valor in tupla])
		sql_command = f"INSERT INTO {self.tb_name} ({campos}) VALUES ({valores})"
		return sql_command


