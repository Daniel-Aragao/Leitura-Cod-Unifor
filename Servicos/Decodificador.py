from Servicos.StringTools import cleanString as cs
from Utils import Constantes as c
from Entidades.Horario import Horario


def decodificar(chave):
    chave = cs(chave)
    copia = chave
    horarios = []

    while has_numbers(copia):
        digit = get_digit(copia)
        index = copia.index(digit)

        turn = get_turno(copia[:index:])

        if turn is None:
            raise Exception('Não há turnos para o dia ' + c.diasToLiteral[digit]+"("+chave+")")

        horas = get_horas(copia[index+1::])

        if not len(horas):
            raise Exception("Não há horários para o dia " + c.diasToLiteral[digit]+"("+chave+")")

        for hora in horas:
            for char in hora:
                horarios.append(Horario(digit, turn, char, chave))

        copia = copia[:index:] + copia[index + 1::]

    return horarios


def get_horas(s):
    horas = []

    for i in s:
        if i in c.horas:
            horas.append(i)
        elif len(horas):
            break
    return horas


def get_turno(s):
    for char in s[::-1]:
        if char in c.turnos:
            return char
    return None


def get_digit(copia):
    for i in copia:
        if i.isdigit():
            return i
    return None


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

"""
Look around:
    Buscar ignora os digitos e busca pelas letras ao redor do digito
    selecionado previamente, para esse digito será decidido quem são
    as letras relevantes para ele como turno e codigo da hora
    
"""