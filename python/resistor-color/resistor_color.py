def color_code(color):
    code = {
            'black': 0,
            'brown': 1,
            'red': 2,
            'orange': 3,
            'yellow': 4,
            'green': 5,
            'blue': 6,
            'violet': 7,
            'grey': 8,
            'white': 9
    }
    return code[color]


def colors():
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']


# # Implementation of color_code from the community solutions
# def color_code(color):
#   return colors().index(color)