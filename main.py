from Servicos.ExportarSalas import *
from Servicos.ImportSalas import get_salas

if __name__ == '__main__':
    path = r'C:\Users\danie\Documents\Git\Turmas unifor'
    lista_salas = get_salas(path + r'\Turmas.xls')

    # seguir modelo de objeto de exportação

    # write_salas(path + r'\Dia.xls')
    # write_salas(lista_salas, path + r'\Sala.xls')

    # write_salas_por_dia(lista_salas, path + r'\BookDia.xls')
    write_sala_por_sala(lista_salas, path + r'\BookSala.xls')
    print('fim')
