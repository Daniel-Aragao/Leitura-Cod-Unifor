import xlrd
from Servicos.ExcelTools import Excel

from Entidades.Sala import Sala
from Entidades.Turma import Turma


def get_salas(path):
    """
    
    :param path: path 
    :return: list
    """
    #                        sheet_index
    #                           row_start
    #                               cod_disp, disp, turma, sala
    sheet = Excel.read_sheet(0, 1, [0, 2, 12, 13], path)

    salas = []

    for row in sheet:
        cod_disciplina_string = row[0]  # Código da disciplina
        disciplina_string = row[1]  # Disciplina
        turma_string = row[2]  # Turma
        sala_string = row[3]  # Sala
        d_b1 = cod_disciplina_string + " " + sala_string + "  " + turma_string + "  " + disciplina_string

        if disciplina_string == 'A FIXAR' or sala_string == 'EAD' or sala_string == '999':
            continue
        turma = Turma(cod_disciplina_string, disciplina_string)
        turma.add_horario(turma_string)

        if turma.Horarios:
            sala = None
            in_list = False

            for e in salas:
                if e.numero == sala_string:
                    sala = e
                    in_list = True
                    break

            if not in_list:
                sala = Sala(sala_string)

            sala.add_turma(turma)

            if not in_list:
                salas.append(sala)

            # print(d_b1)

    salas.sort(key=lambda x: x.numero)
    return salas
