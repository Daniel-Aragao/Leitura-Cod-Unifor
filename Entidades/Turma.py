from Servicos.Decodificador import decodificar as decode


class Turma:
    def __init__(self, cod, disc):
        self.Horarios = []
        self.codigo_disciplina = cod
        self.disciplina = disc

    def add_horario(self, horario):
        if horario is None:
            raise Exception('Horario inválido')
        
        horarios = decode(horario)

        for e in horarios:
            self.Horarios.append(e)
