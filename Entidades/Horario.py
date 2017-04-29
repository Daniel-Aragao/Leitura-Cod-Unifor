from Utils import Constantes as c


class Horario:
    def __init__(self, dia, turno, codigo, codigo_completo):
        self.dia = int(dia)
        self.turno = turno
        self.codigo = codigo
        self.codigo_completo = codigo_completo
        self.hora = None

        if dia not in c.dias or turno not in c.turnos or codigo not in c.horas or not codigo_completo:
            raise Exception('Código inválido: ' + codigo_completo)
        # if self.turno == c.Noite:
        #     for i in self.codigo:
        #         if i > 'D':
        #             raise Exception('Noite não possui horário E ou F: ' + codigo_completo)

