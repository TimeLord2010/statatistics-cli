from utils import get_data
import math

def average ():
    is_regular = input('''
    1 - Regular;
    2 - Ponderada.
    ''')
    if is_regular == '1':
        data = get_data()
        data = [float(d) for d in data]
        print(sum(data) / len(data))
    else:
        print('formato: valor*peso')
        data = get_data()
        data = [x.split('*') for x in data]
        print(sum([float(val)*float(weight) for (val, weight) in data]) / sum([x for (_, x) in data]))