from utils import get_data, print_float
import pandas as pd
import math
import matplotlib.pyplot as plt

def create_frequency_distribuition (counter: dict):
    values = list(counter.values())
    df = pd.DataFrame({
        'Valor': list(counter.keys()),
        'Frequência absoluta': values,
        'Frequencia relativa': [x/sum(values) for x in values]
    })
    print(df)
    print(f'Total: {sum(values)}')
    plt.bar(counter.keys(), counter.values())
    plt.show()

def frequency_for_categorized (data):
    counter = {}
    for d in data:
        if d in counter:
            counter[d] = counter[d] + 1
        else:
            counter[d] = 1
    create_frequency_distribuition(counter)

def frequency_for_quantitative (data):
    data = [float(x) for x in data]
    ranges = get_quantitative_ranges(data)
    classes = {}
    for (lower, upper, label) in ranges:
        classes[label] = len([x for x in data if lower <= x <= upper])
    create_frequency_distribuition(classes)

def get_quantitative_ranges (data: list[float]):
    n = len(data)
    k = math.sqrt(n)
    amplitude = math.floor((max(data) - min(data)) / k)
    ranges = []
    _min = min(data)
    while _min <= max(data):
        lower = _min - (amplitude/2)
        upper = _min + (amplitude/2)
        ranges.append((lower, upper, f'{print_float(lower)} - {print_float(upper)}'))
        _min += amplitude + 1
    return ranges

def is_quantitative (data):
    return all([x.isdigit() for x in data])

def simple_distribution (data):
    if is_quantitative(data):
        frequency_for_quantitative(data)
    else:
        frequency_for_categorized(data)

def get_variable_info (data):
    if is_quantitative(data):
        data = [float(x) for x in data]
        ranges = get_quantitative_ranges(data)
        labels = [label for (_, _, label) in ranges]
        return (labels, lambda x: [i for i in range(len(ranges)) if float(x) >= ranges[i][0] and float(x) <= ranges[i][1]][0])
    else:
        labels = list(set(data))
        return (labels, lambda x: labels.index(x))

def frequency_distribuition (data = None):
    if data is None:
        data = get_data()
    has_separator = all([',' in x for x in data])
    if has_separator:
        indexes = input('''
        Somente duas variáveis podem ser comparadas de uma vez. 
        Escolha os índices das variáveis (formato: (indice1,indice2) ou (indice) para processar somente 1 variável): ''')
        [i1,i2] = [int(x.strip()) for x in indexes.split(',')]
        if i2 == None:
            data = [x.split(',')[x - 1].strip() for x in data]
            simple_distribution(data)
        else:
            data1 = []
            data2 = []
            for d in data:
                parts = d.split(',')
                data1.append(parts[i1 - 1].strip())
                data2.append(parts[i2 - 1].strip())
            (rows, row_comp) = get_variable_info(data1)
            (columns, column_comp) = get_variable_info(data2)
            my_table = {}
            for d1, d2 in zip(data1, data2):
                x = row_comp(d1)
                x_label = rows[x]
                if x_label not in my_table:
                    my_table[x_label] = {}
                row = my_table[x_label]
                y = column_comp(d2)
                y_label = columns[y]
                if y_label not in row:
                    row[y_label] = 0
                row[y_label] = row[y_label] + 1
            print(my_table)
            simple_distribution(data1)
            simple_distribution(data2)
    else:
        simple_distribution(data)