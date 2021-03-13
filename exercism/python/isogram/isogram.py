def is_isogram(string):
    counts = set()

    for ch in string.lower():
        if ch.isalpha():
            if ch not in counts:
                counts.add(ch)  
            else:
                return False
    return True
