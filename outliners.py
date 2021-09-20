from math import abs
from utils import get_float_data
from standard_deviation import standard_deviation
from relative_position import relative_position

def outliners ():
    data = get_float_data()
    sd = standard_deviation(data)
    outs = []
    for x in data:
        relative = relative_position(data, x=x)
        if abs(relative) > sd*3:
            outs.append(x)
    return outs