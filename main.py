from average import average
from frequency import frequency_distribuition
from median import median
from mode import mode

operations = {
    '1': frequency_distribuition,
    '2': average,
    '3': median,
    '4': mode
}

while True:
    choice = input('''
    Operação:
    1 - Distribuição de frequências;
    2 - Média;
    3 - Mediana;
    4 - Moda;
    ''')
    op = operations[choice]
    op()