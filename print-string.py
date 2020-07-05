list = ['bunny', 'dino', 'hampster', 'tiger']

def print_string(list):
    result = ''
    for i in list[0:len(list) - 1]:
        result += f'{i}, '
    result = result + 'and ' + list[-1]
    return result

print(print_string(list))
