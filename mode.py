from utils import get_data

def mode ():
    data = get_data()
    counter = {}
    for d in data:
        if d in counter:
            counter[d] = counter[d] + 1
        else:
            counter[d] = 1
    maximum = max(counter.values())
    for key in counter.keys():
        if counter[key] == maximum:
            print(key)
            return None
    raise IndexError('Did not find maximum value in counter.')