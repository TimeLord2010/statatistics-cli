from utils import get_data
import math

def median ():
    data = get_data()
    if len(data) % 2 == 0:
        i = (len(data) - 1) / 2
        lower = math.floor(i)
        upper = math.ceil(i)
        print((float(data[lower]) + float(data[upper])) / 2)
    else:
        i = len(data) / 2
        i = math.floor(i)
        print(data[i])