def sql_inserir(tb_name, field_names, tupla):
	campos = ', '.join(field_names)
	valores = ', '.join([f"'{valor}'" if type(valor) == str else str(valor) for valor in tupla])
	sql_command = f"INSERT INTO {tb_name} ({campos}) VALUES ({valores})"
	return sql_command


