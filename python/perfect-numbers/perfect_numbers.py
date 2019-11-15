def classify(number):
    if number < 1:
        raise ValueError("Value too small")
    aliquot = 0
    for i in range(number-1):
        if number % (i+1) == 0:
            aliquot += i+1
    return "perfect" if aliquot == number else "abundant" if aliquot > number else "deficient"