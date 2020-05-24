from banco.connect import Conexao


class AreaControle(Conexao):
	def __init__(self):
		self.fields = ['nome', 'vagas_max','vagas_livres', 'vagas_bloqueadas']
		self.tb_name = 'areas'
		super(AreaControle, self).__init__(self)

	def salvar(self, modelo):
		self.novo(modelo.get())
		print(f"Salvo com sucesso: {modelo.get()}")

