def distance(strand_a, strand_b):
    try:
        if len(strand_a) == len(strand_b):
            distance = 0
            for i, ch in enumerate(strand_a):
                if ch != strand_b[i]:
                    distance += 1
            return distance
        else:
            raise ValueError('strand_a and strand_b are not of equal length')
    except ValueError as e:
        raise ValueError(e)
