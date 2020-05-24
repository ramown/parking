class Area:
	def __init__(self, nome, vagas_max, vagas_livres, vagas_bloqueadas):
		self.nome = nome
		self.vagas_max = vagas_max
		self.vagas_livres = vagas_livres
		self.vagas_bloqueadas = vagas_bloqueadas

	def tupla(self):
		try:
			return (
				self.id, self.nome, self.vagas_max, 
				self.vagas_livres, self.vagas_bloqueadas
			)
		except Exception:
			return (
				self.nome, self.vagas_max, 
				self.vagas_livres, self.vagas_bloqueadas
			)

