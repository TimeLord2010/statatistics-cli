from variance import variance
from utils import get_data
from math import sqrt

def class_data ():
    print('formato: <menor>-<maior>|<quantidade> ')
    data = get_data()
    t = []
    for d in data:
        [interval, quantity] = [x.strip() for x in d.split('|')]
        [lower, upper] = [x.strip() for x in interval.split('-')]
        point = float(lower) + ((float(upper) - float(lower)) / 2)
        t.append((point, float(quantity)))
    return t

def class_average (pairs = None):
    sum_of_values = 0
    if pairs is None:
        pairs = class_data()
    for (point, quantity) in pairs:
        sum_of_values += point * quantity
    n = sum([q for (_, q) in pairs])
    return sum_of_values / n

def class_variance ():
    pairs = class_data()
    data = [x for (x, _) in pairs]
    avg = class_average(pairs)
    return variance(data, ponderation = lambda i: pairs[i][1], avg = avg, is_populational= True)

def class_standard_deviation ():
    variance = class_variance()
    return sqrt(variance)

def class_functions ():
    choice = input('''
    1 - Média;
    2 - Variância;
    3 - Desvio padrão.
    ''')
    if choice == '1':
        return class_average()
    elif choice == '2':
        return class_variance()
    else:
        return class_standard_deviation()