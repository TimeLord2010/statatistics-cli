from average import average
from frequency import frequency_distribuition

operations = {
    '1': frequency_distribuition,
    '2': average
}

while True:
    choice = input('''
    Operação:
    1 - Distribuição de frequências;
    2 - Média;
    ''')
    op = operations[choice]
    op()