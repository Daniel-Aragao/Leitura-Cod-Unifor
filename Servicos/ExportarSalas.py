from Servicos.ExcelTools import *
from Entidades.Sala import Sala


def write_salas(salas: list, path):
    """
    :param book: ExportarSalas.Book 
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
        for turma in sala.Turmas:
            for horario in turma.Horarios:
                sheet = sheets[horario.dia]

                # e as salas q n tão em todos os dias? vão quebrar
                if len(sheet.data) == i + i_offset:
                    row = [None for x in range(0, len(header2))]
                    row[0] = sala.numero
                    sheet.data.append(row)
                    print('___'+str(i)+'___' + str(sheet.titulo))
                else:
                    print(str(i) + '___'+str(sheet.titulo))

                if i == 3 and horario.dia == 6:
                    print('aqui')
                row = sheet.data[i + i_offset]
                index = j_offset + turnos_offset[horario.turno] + horas_offset[horario.codigo]

                # if index >= len(row):
                #     raise Exception('Turma inválida')

                # if row[index]:
                #     raise Exception('Choque de horário')
                row[index] = turma.disciplina

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
