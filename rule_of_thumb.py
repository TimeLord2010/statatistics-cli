from utils import get_data
from standard_deviation import standard_deviation
from relative_position import relative_position

sd_map = {
    1: 0.68,
    2: 0.95,
    3: 0.997,
}

def rule_of_thumb ():
    print('A regra empírica diz que:')
    print('1 desvio padrão contem 68% dos valores;')
    print('2 desvios padrões contem 95% dos valores;')
    print('3 desvios padrões contém 99.7% dos valores')
    data = get_data()
    data = [float(x) for x in data]
    for n in range(1, 4):
        percent = count_percent_sd(data, n) * 100
        expected = sd_map[n] * 100
        print(f'{percent}% estão em {n} desvios padrões. Esperado era {expected}%')
    print(data)
    i = int(input('Escolha um valor da amostra usando o índice: '))
    x = data[i]

def count_percent_sd (data, n):
    sd = standard_deviation(data)
    selected = []
    for x in data:
        relative = relative_position(data, x = x)
        if relative <= sd*n:
            selected.append(x)
    found = len(selected)
    return found / len(data)
