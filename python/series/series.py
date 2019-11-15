def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError("length too high")
    i = 0
    result = []
    while i+length <= len(series):
        result.append(series[i:i+length])
        i+=1
    return result