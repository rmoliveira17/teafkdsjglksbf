def media_simples(valores):
	"""Calcula a média aritmética simples dos valores fornecidos."""
	if not valores:
		raise ValueError("A lista de valores não pode estar vazia.")
	return sum(valores) / len(valores)


def media_ponderada(valores, pesos):
	"""Calcula a média ponderada dos valores usando os pesos fornecidos."""
	if not valores or not pesos:
		raise ValueError("Valores e pesos não podem estar vazios.")
	if len(valores) != len(pesos):
		raise ValueError("Valores e pesos devem ter o mesmo tamanho.")

	soma_pesos = sum(pesos)
	if soma_pesos == 0:
		raise ValueError("A soma dos pesos não pode ser zero.")

	return sum(valor * peso for valor, peso in zip(valores, pesos)) / soma_pesos
