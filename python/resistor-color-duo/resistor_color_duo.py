def value(colors):
    colorList = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    code = ""
    for color in colors:
        if len(code) < 2:
            code += str(colorList.index(color))
    return int(code)
