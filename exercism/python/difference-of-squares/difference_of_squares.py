def square_of_sum(number):
    sum = 0
    while 0 < number:
        sum += number
        number -= 1
    return sum ** 2
        

def sum_of_squares(number):
    sum = 0
    while 0 < number:
        sum += number ** 2
        number -= 1
    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
