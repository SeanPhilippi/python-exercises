# formula for valid isbn-10: (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
# if an x at the end, it represents 10
# ignore - characters
def is_valid(isbn):
    isbn.replace('-', '')
    nums = isbn.split()
    ints = list(map(int, nums))
    # do calculation using array of nums

    
