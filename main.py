from distribution_form import distribution_form
from class_functions import class_functions
from standard_deviation import standard_deviation
from variance import variance
from average import average
from frequency import frequency_distribuition
from median import median
from mode import mode
from distribution_form import distribution_form
from relative_position import relative_position
from chebyshev_theorem import chebyshev_theorem
from rule_of_thumb import rule_of_thumb

operations = {
    '1': frequency_distribuition,
    '2': average,
    '3': median,
    '4': mode,
    '5': variance,
    '6': standard_deviation,
    '7': class_functions,
    '8': distribution_form,
    '9': relative_position,
    '10': chebyshev_theorem,
    '11': rule_of_thumb
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
    7 - Funções de classes;
    8 - Forma da distribuição;
    9 - Posição relativa;
    10 - Teorema de Chebyshev;
    11 - Regra empírica;
    12 - Detecção de valores atípicos;
    ''')
    op = operations[choice]
    result = op()
    if result is not None:
        print(result)