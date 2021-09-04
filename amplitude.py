from utils import get_data

def amplitude ():
    data = get_data()
    data = [float(x) for x in data]
    return max(data) - min(data)