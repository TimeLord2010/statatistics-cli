from standard_deviation import standard_deviation
from variance import variance
from average import average
from frequency import frequency_distribuition
from median import median
from mode import mode

operations = {
    '1': frequency_distribuition,
    '2': average,
    '3': median,
    '4': mode,
    '5': variance,
    '6': standard_deviation
}

while True:
    choice = input('''
    Operação:
    1 - Distribuição de frequências;
    2 - Média;
    3 - Mediana;
    4 - Moda;
    5 - Variância;
    6 - Desvio padrão;
    ''')
    op = operations[choice]
    result = op()
    if result is not None:
        print(result)