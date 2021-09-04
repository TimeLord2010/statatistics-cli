from utils import get_data
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

def frequency_for_categorized ():
    data = get_data()
    counter = {}
    for d in data:
        if d in counter:
            counter[d] = counter[d] + 1
        else:
            counter[d] = 1
    create_frequency_distribuition(counter)

def frequency_for_quantitative ():
    data = get_data()
    data = [float(x) for x in data]
    n = len(data)
    k = math.sqrt(n)
    amplitude = math.floor((max(data) - min(data)) / k)
    classes = {}
    _min = min(data)
    while _min <= max(data):
        lower = _min - (amplitude/2)
        upper = _min + (amplitude/2)
        classes[f'{lower} - {upper}'] = len([x for x in data if lower <= x <= upper])
        _min += amplitude
    create_frequency_distribuition(classes)

def frequency_distribuition ():
    data_type = input('''
    Tipo de dado:
    1 - Categorizado;
    2 - Quantitativo.
    ''')
    if data_type == '1':
        frequency_for_categorized()
    else:
        frequency_for_quantitative()