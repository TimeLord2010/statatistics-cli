from average import average
from utils import get_data
from standard_deviation import standard_deviation

def coefficient_of_variation ():
    data = get_data()
    deviation = standard_deviation(data)
    avg = average(data)
    return deviation / avg