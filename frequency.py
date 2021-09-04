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
    n = len(data)
    k = math.sqrt(n)
    amplitude = math.floor((max(data) - min(data)) / k)
    classes = {}
    _min = min(data)
    while _min <= max(data):
        lower = _min - (amplitude/2)
        upper = _min + (amplitude/2)
        classes[f'{print_float(lower)} - {print_float(upper)}'] = len([x for x in data if lower <= x <= upper])
        _min += amplitude
    create_frequency_distribuition(classes)

def frequency_distribuition ():
    data = get_data()
    is_quantitative = all([x.isdigit() for x in data])
    if is_quantitative:
        frequency_for_quantitative(data)
    else:
        frequency_for_categorized(data)