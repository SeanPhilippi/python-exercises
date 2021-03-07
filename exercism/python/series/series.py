def slices(series, length):
    try:
        if length <= 0:
            raise ValueError('Length must be greater than or equal to 0.')
        if len(series) < length:
            raise ValueError('The series is too short for that length.')
        slices = []
        for i, num in enumerate(series):
            if i + length <= len(series):
                slices.append(series[i:length + i])
            else:
                break
        return slices
    except ValueError as err:
        raise ValueError(err)
