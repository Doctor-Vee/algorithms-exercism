def distance(strand_a, strand_b):
    if ( not len(strand_a) == len(strand_b)):
        raise ValueError("Issue")
    count = 0
    for i in range(len(strand_a)):
        if not strand_a[i] == strand_b[i]:
            count += 1
    return count