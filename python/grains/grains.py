def square(number):
    if number > 64 or number < 1:
        raise ValueError("Sorry, Wrong Number")
    return 2 **(number-1)

def total(number):
    if number > 64 or number < 1:
        raise ValueError("Sorry, Wrong Number")
    sum = 0
    for i in range(number):
        sum += square(i+1)
    return sum