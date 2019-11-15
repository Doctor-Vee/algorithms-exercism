class Phone(object):
    def __init__(self, phone_number):
        tel=""
        for p in phone_number:
            if p.isalpha():
                raise ValueError("Bad value")
            if p.isdigit():
                tel += p
        if len(tel) < 10 or len(tel) > 11:
            raise ValueError("Bad Value")
        if len(tel) == 11:
            if not int(tel[0]) == 1:
                raise ValueError("Bad Value")
            tel = tel[1:]
        if int(tel[0]) < 2 or int(tel[3]) < 2:
            raise ValueError("Bad value")  
        self.number = tel
        self.area_code = tel[:3]
    def pretty(self):
        return "(" + self.number[:3]+ ") " + self.number[3:6] + "-" + self.number[6:10]
