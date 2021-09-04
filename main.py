from frequency import frequency_distribuition

operations = {
    '1': frequency_distribuition
}

while True:
    choice = input('''
    Operação:
    1 - Distribuição de frequências;
    ''')
    op = operations[choice]
    op()