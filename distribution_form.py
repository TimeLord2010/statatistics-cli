from utils import get_data
from math import pow
from average import average
from standard_deviation import standard_deviation

def distribution_form ():
    data = get_data()
    n = len(data)
    avg = average(data)
    sd = standard_deviation(data)
    total = sum([pow(((x - avg)/sd), 3) for x in data])
    result = (n / ((n - 1)*(n - 2))) * total
    return result