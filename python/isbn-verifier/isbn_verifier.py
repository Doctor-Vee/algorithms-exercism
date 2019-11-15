def is_valid(isbn):
    isbn = isbn.replace("-","")
    if not len(isbn) == 10:
        ValueError("bad input")
        return False
    sum = 0
    i = 10
    for isb in isbn:
        if isb == "X" and i == 1:
            isb = 10
        try:
            sum += int(isb) * i
        except:
            ValueError("bad input")
            return False
        i -= 1
    return sum % 11 == 0