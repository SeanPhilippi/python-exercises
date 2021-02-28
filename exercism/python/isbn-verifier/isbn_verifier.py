# formula for valid isbn-10: (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
# if an x at the end, it represents 10
# ignore - characters
def is_valid(isbn):
    print('isbn', isbn)
    nums = isbn.replace('-', '')
    print('nums', nums)
    # do regex check for digits 0-9 or x or X only
    # if nums[9] 
    if len(nums) != 10:
        return False
    ints = []
    for i, num in enumerate(nums):
        print('num', num)
        if str.isdigit(num):
            ints.append(int(num))
        else:
            if num == 'X' and i == 9:
                ints.append(10)
            else:
                return False
    # ints = list(map(int, nums))
    print('ints', ints)
    # do calculation using array of nums
    product = 0
    multiplier = 10
    for num in ints:
        product += num * multiplier 
        multiplier -= 1
    product = product % 11
    if product == 0:
        return True
    else:
        return False

print(is_valid('3-598-21508-9'))
