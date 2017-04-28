
"""
N46CD
N2CD6AB
M6EF
T3EF-T5EF
N5AB-N3AB

A FIXAR

T3N6AB
T3NAB6

M = Manhã
AB (7h30 - 9h10)
CD (9h30 - 11h10)
EF (11h20 - 13h)

T = Tarde
AB (13h30 - 15h10)
CD (15h30 - 17h10)
EF (17h20 - 19h)*

N = Noite
AB (19h - 20h40)
CD (21h - 22h40)

Dias da semana
2- Segunda-feira
3- Terça-feira
4- Quarta-feira
5- Quinta-feira
6- Sexta-feira
7- Sábado

"""

Noite = 'N'
Tarde = 'T'
Manha = 'M'

Segunda = '2'
Terca = '3'
Quarta = '4'
Quinta = '5'
Sexta = '6'
Sabado = '7'

diasToLiteral = {2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}

turnos = [Manha, Tarde, Noite]
dias = [Segunda, Terca, Quarta, Quinta, Sexta, Sabado]
horas = ['A', 'B', 'C', 'D', 'E', 'F']
