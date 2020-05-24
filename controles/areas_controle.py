from banco.connect import Conexao
from modelos.area import Area


class AreaControle(Conexao):
	def __init__(self):
		self.fields = ['nome', 'vagas_max','vagas_livres', 'vagas_bloqueadas']
		self.tb_name = 'areas'
		super(AreaControle, self).__init__(self)


	def get_id(self, id):
		try:
			id, nome, vagas_max, vagas_livres, vagas_bloqueadas = self.get(id)
			modelo = Area(nome, vagas_max, vagas_livres, vagas_bloqueadas)
			modelo.id = id
			return modelo
		except Exception as e:
			print('Dado não cadastrado')
			return None
		
		
	def salvar(self, modelo):
		tupla = modelo.tupla()
		if len(tupla) == len(self.fields)+1:
			self.atualizar(tupla)
		else:
			self.novo(tupla)
