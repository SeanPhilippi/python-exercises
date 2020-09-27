# pdf = open('../../Desktop/The-Pe-Diet.pdf')
# print(f'Current position: {pdf.tell()}')
# print(pdf.read(30))
# pdf.close()
# print(f'File closed? {pdf.closed}')

with open('file.txt', 'w') as the_file:
    the_file.write('This is line one.\nThis is line two.\nFinally, we are on the third line of the file.')
line_num = 1

with open('file.txt') as the_file:
    for line in the_file:
        print(f'{line_num}: {line.rstrip()}')
        line_num += 1

try:
    with open('animals.txt', 'r') as animals:
        animals_text = animals.read()
        sep_animals = animals_text.splitlines()
        sorted_animals = sorted(sep_animals)
        print(sorted_animals)
except:
    print('Could not open animals.txt')
