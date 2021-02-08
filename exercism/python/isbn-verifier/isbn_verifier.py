# formula for valid isbn-10: (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
# if an x at the end, it represents 10
# ignore - characters
def is_valid(isbn):
    nums = isbn.replace('-', '')
    print('nums', nums)
    # do regex check for digits 0-9 or x or X only
    # if nums[9] 
    if len(nums) != 10:
        return False
    ints = []
    for num in nums:
        ints.append(int(num))
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

print(is_valid('3-598-21508-9'))
