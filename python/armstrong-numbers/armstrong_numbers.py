def is_armstrong_number(number):
    numstr = str(number)
    x = (len(numstr))
    sum = 0
    
    for num in numstr:
        sum += int(num) ** x
    
    return True if sum == number else False