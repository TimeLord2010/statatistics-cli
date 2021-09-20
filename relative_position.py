from utils import get_float_data
from average import average
from standard_deviation import standard_deviation

def relative_position (data = None, i = None, x = None):
    if data is None:
        data = get_float_data()
    avg = average(data)
    sd = standard_deviation(data)
    if x is None:
        if i is None:
            i = int(input('Escolha o índice do item desejado.'))
        x = data[i]
    return (x - avg) / sd