class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        self.rL = len(self.matrix)
        self.cL = len(self.matrix[0].split())
        self.matrow = []
        self.matcolumn = []
        for i in range(self.rL):
            self.matrow.append(self.matrix[i].split())

    def row(self, index):

        for i in range(len(self.matrow[index-1])):
            self.matrow[index-1][i] = int(self.matrow[index-1][i])
        return self.matrow[index-1]

    def column(self, index):
        temp = []
        for i in range(self.cL):
            for j in range(self.rL):
                temp.append(int(self.matrow[j][i]))
            self.matcolumn.append(temp)
            temp = []
        return self.matcolumn[index-1]