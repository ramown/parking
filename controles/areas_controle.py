from banco.connect import Conexao


class AreaControle(Conexao):
	def __init__(self, tb_name, modelo):
		self.field_names = modelo.fields
		self.modelo = modelo
		super(AreaControle, self).__init__(tb_name, self.field_names)

	def salvar(self):
		self.novo(self.modelo.get())
		print(f"Salvo com sucesso: {self.modelo.get()}")


