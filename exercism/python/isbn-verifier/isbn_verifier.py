def is_valid(isbn):
    ints, nums = [], isbn.replace('-', '')

    if len(nums) != 10: return False 

    for i, num in enumerate(nums):
        if str.isdigit(num):
            ints.append(int(num))
        else:
            if num == 'X' and i == 9:
                ints.append(10)
            else:
                return False

    product, multiplier = 0, 10

    for num in ints:
        product += num * multiplier 
        multiplier -= 1
    product = product % 11

    return False if product != 0 else True
