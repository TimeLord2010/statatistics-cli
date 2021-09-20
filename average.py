from utils import get_data
import math

def average (data = None, is_regular = '1'):
    if is_regular is None:
        is_regular = input('''
        1 - Regular;
        2 - Ponderada.
        ''')
    if is_regular == '1':
        if data is None:
            data = get_data()
        data = [float(d) for d in data]
        avg = sum(data) / len(data)
    else:
        if data is None:
            print('formato: valor*peso')
            data = get_data()
        if len(data) > 0 and isinstance(data[0], str):
            data = [x.split('*') for x in data]
        avg = sum([float(val)*float(weight) for (val, weight) in data]) / sum([x for (_, x) in data])
    return avg