def square(num):
    if not 0 < num < 65:
        raise ValueError('Number must greater than 0')
    total = 1
    while num > 1:
        total *= 2
        num -= 1
    return total

def total():
    count = 1
    grains = 1
    total = 1
    while count < 64:
        grains *= 2
        total += grains
        count += 1

    return total
