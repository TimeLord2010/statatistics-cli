from average import average
from utils import get_data
from math import pow

def variance (data = None, ponderation = lambda i: 1, is_populational = False):
    if data is None:
        data = get_data()
    data = [float(x) for x in data]
    avg = average(data, is_regular='1')
    n = len(data)
    if is_populational is None:
        is_populational = input('''
        1 - Amostral;
        2 - Populacional.
        ''')
    else:
        is_populational = '2' if is_populational else '1'
    if is_populational != '1':
        n -= 1
    total = sum([pow(x - avg, 2)*ponderation(i) for i, x in enumerate(data)]) 
    return  total / n