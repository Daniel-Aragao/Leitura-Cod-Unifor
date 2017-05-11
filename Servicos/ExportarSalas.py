from Servicos.ExcelTools import *
from Entidades.Sala import Sala


def write_salas(salas: list, path):
    """
    :param salas: ExportarSalas.Book 
    :param path: str
    :return: None
    """

    header1 = ['', 'Manhã', '', '', '', '', '', 'Tarde', '', '', '', '', '', 'Noite', '', '', '', '', '']
    header2 = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']
    i_offset = 2

    turnos_offset = {'N': 12, 'T': 6, 'M': 0}
    horas_offset = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    j_offset = 1

    sheets = {
        2: Sheet([header1, header2], 'Segunda'),
        3: Sheet([header1, header2], 'Terça'),
        4: Sheet([header1, header2], 'Quarta'),
        5: Sheet([header1, header2], 'Quinta'),
        6: Sheet([header1, header2], 'Sexta'),
        7: Sheet([header1, header2], 'Sábado')
    }

    book = Book(sheets, path)

    for i, sala in enumerate(salas):
        if sala.numero == 999:  # 999 EAD, A FIXAR no codigo
            continue
        for dia in range(2, 8):
            row = [None for x in range(0, len(header2))]
            row[0] = sala.numero
            sheets[dia].data.append(row)

        for turma in sala.Turmas:
            for horario in turma.Horarios:
                sheet = sheets[horario.dia]

                row = sheet.data[i + i_offset]
                index = j_offset + turnos_offset[horario.turno] + horas_offset[horario.codigo]

                # if index >= len(row):
                #     raise Exception('Turma inválida')

                # if row[index]:
                #     raise Exception('Choque de horário')

                row[index] = turma.codigo_disciplina  # 'X'  # turma.disciplina

    Excel.write_workbook(book)


def write_sala_por_dia(salas: list, path):
    """
        :param salas: ExportarSalas.Book 
        :param path: str
        :return: None
        """

    sheets = []

    book = Book(sheets, path)

    header = ['', '', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    offset_top = 1
    left1 = ['Manhã', '', '', '', '', '', 'Tarde', '', '', '', '', '', 'Noite', '', '', '', '', '']
    left2 = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'E', 'F']
    offset_left = 2
    turnos_offset = {'N': 12, 'T': 6, 'M': 0}
    horas_offset = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    for sala in salas:
        rows = [header]

        for i in range(0, len(left2)):
            v = ['' for x in range(0, len(header))]
            v[0] = left1[i]
            v[1] = left2[i]
            rows.append(v)

        sheet = Sheet(rows, sala.numero)
        sheets.append(sheet)
        for turma in sala.Turmas:
            for horario in turma.Horarios:
                row = rows[offset_top + turnos_offset[horario.turno] + horas_offset[horario.codigo] ]
                row[horario.dia] = turma.codigo_disciplina

    Excel.write_workbook(book)



"""
book = {
    'sheets': [
        {
            'titulo': 'p1',
            'data': [
                ['col1', 'col2'], ['col1', 'col2']
            ]
        },
        {
            'titulo': 'p2',
            'data': [
                ['col1', 'col2'], ['col1', 'col2']
            ]
        }
    ],

    'titulo': 'book'
}
"""
