from average import average
from utils import get_data
from math import pow

def variance (data = None, ponderation = lambda i: 1, avg = None, is_populational = False):
    if data is None:
        data = get_data()
    data = [float(x) for x in data]
    if avg is None:
        avg = average(data, is_regular='1')
    if is_populational is None:
        is_populational = input('''
        1 - Amostral;
        2 - Populacional.
        ''')
    else:
        is_populational = '2' if is_populational else '1'
    total = 0
    n = 0
    for i, x in enumerate(data):
        p = ponderation(i)
        n += p
        y = pow(x - avg, 2) * p
        total += y
    if is_populational != '1':
        n -= 1
    return  total / n