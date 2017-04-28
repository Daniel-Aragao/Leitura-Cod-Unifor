class Sala:
    def __init__(self, sala):
        self.Turmas = []
        self.numero = sala

    def add_turma(self, turma):
        # do things
        self.Turmas.append(turma)

    def __str__(self):
        return str(self.numero)
