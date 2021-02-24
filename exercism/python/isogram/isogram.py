def is_isogram(string):
    counts = {}
    new_string = string.lower().replace('-', '').replace(' ', '')

    for ch in set(new_string):
        counts[ch] = 0
    
    for ch in new_string:
        if counts[ch] == 1:
            return False
        else:
            counts[ch] += 1  
    return True
