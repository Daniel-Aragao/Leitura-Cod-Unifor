import xlrd
from Entidades.Sala import Sala
from Entidades.Turma import Turma
from Entidades.Horario import Horario


def main():

    wb = xlrd.open_workbook(r'C:\Users\danie\Documents\Git\Turmas unifor\Turmas.xls')
    wb.sheet_names()
    sh = wb.sheet_by_index(0)
    i = 1
    salas = []

    while i < sh.nrows - 1:
        turma_string = str(sh.cell(i, 12).value)  # Turma
        sala_string = str(sh.cell(i, 13).value)  # Sala
        disciplina_string = str(sh.cell(i, 2).value)  # Disciplina
        cod_disciplina_string = str(sh.cell(i, 0).value)  # Código da disciplina
        d_b1 = turma_string + "  " + sala_string + "  " + disciplina_string

        sala = None
        in_list = False

        for e in salas:
            if e.numero == sala_string:
                sala = e
                in_list = True
                break

        turma = Turma(cod_disciplina_string, disciplina_string)
        turma.add_horario(turma_string)

        if not in_list:
            sala = Sala(sala_string)

        sala.add_turma(turma)

        if not in_list:
            salas.append(sala)

        print(d_b1)

        i += 1
    salas.sort(key=lambda x: x.numero)
    return salas

if __name__ == '__main__':
    lista_salas = main()
    print('fim')
