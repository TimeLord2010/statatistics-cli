def get_data ():
    file_or_keyboard = input('''Tipo de entrada:
    1 - Arquivo;
    2 - Teclado.
    ''')
    if file_or_keyboard == '1':
        fileName = input('Nome do arquivo: ')
        content = ''
        with open('resources/' + fileName, 'r', encoding='utf8') as f:
            content = f.readlines()
        content = [x.replace("\n", '').strip() for x in content]
        return content
    else:
        current = None
        i = 1
        data = []
        print('Começe a digitar seus dados agora e quando terminar digite <fim> (com "<" e ">")')
        while current != '<fim>':
            if current is not None:
                data.append(current)
            current = input(f'[{i}] = ')
            i += 1
        return data

def is_integer_equivalent(n: float):
    temp2 = n - int(n)
    return temp2 == 0

def print_float(n: float):
    if is_integer_equivalent:
        n = int(n)
    return str(n)