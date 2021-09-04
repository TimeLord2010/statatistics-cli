from average import average
from utils import get_data
import math

def variance (data = None):
    if data is None:
        data = get_data()
    data = [float(x) for x in data]
    avg = average(data, is_regular='1')
    n = len(data)
    is_populational = input('''
    1 - Amostral;
    2 - Populacional.
    ''')
    if is_populational != '1':
        n -= 1
    return sum([math.pow(x - avg, 2) for x in data]) / n
