class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f"Curso: {self.nome}, Duração: {self.duracao} horas")