class Turma:

    def __init__(self, nome, professor, alunos):
        self.nome = nome
        self.professor = professor
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def listar_alunos(self):
        return [aluno.nome for aluno in self.alunos]

class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        