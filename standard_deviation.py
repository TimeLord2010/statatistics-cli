from variance import variance
from math import sqrt

def standard_deviation (data = None):
    v = variance(data)
    return sqrt(v)
