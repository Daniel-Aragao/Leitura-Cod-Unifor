from Utils import Constantes as c


class Horario:
    def __init__(self, dia, turno, codigo, codigo_completo):
        self.dia = dia
        self.turno = turno
        self.codigo = codigo
        self.codigo_completo = codigo_completo
        self.hora = None

        if self.turno == c.Noite:
            for i in self.codigo:
                if i > 'D':
                    raise Exception('Noite não possui horário E ou F: ' + codigo_completo)

