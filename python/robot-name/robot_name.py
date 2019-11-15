import random

def rnd(seed=""):
    return chr(random.randint(65,90)) + chr(random.randint(65,90)) + str(random.randint(100,999))

class Robot(object):
    def __init__(self):
        self.name = rnd()

    def reset(self):
        self.name = rnd(chr(random.randint(65,90)))