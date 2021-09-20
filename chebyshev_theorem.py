from math import pow

def chebyshev_theorem ():
    z = float(input('Informe z: '))
    return 1 - (1 / pow(z, 2))