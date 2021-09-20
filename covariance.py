from utils import get_float_data
from average import average

def covariance ():
    data1 = get_float_data()
    data2 = get_float_data()
    if len(data1) != len(data2):
        raise Exception('As séries precisam ter o mesmo tamanho.')
    n = len(data1)
    arr = []
    x_avg = average(data1)
    y_avg = average(data2)
    for x,y in zip(data1, data2):
        arr.append( (x - x_avg)*(y - y_avg) / n - 1 )
    return sum(arr)