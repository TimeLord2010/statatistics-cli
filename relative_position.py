from utils import get_data
from average import average
from standard_deviation import standard_deviation

def relative_position ():
    data = get_data()
    avg = average(data)
    sd = standard_deviation(data)
    i = int(input('Escolha o índice do item desejado.'))
    return (data[i] - avg) / sd