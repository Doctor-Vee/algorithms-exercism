class School(object):
    def __init__(self):
        self.result = {}
        self.new_result = {}
        self.result_array = []
    def add_student(self, name, grade):
        try:
            self.result["grade"+str(grade)].append(name)
        except:
            self.result["grade"+str(grade)] = [name]

    def roster(self):
        for key in sorted(self.result.keys()):
            self.new_result[key] = self.result[key]
        for i in range(12):
            try:
                self.new_result["grade"+str(i+1)].sort()
                self.result_array+=self.new_result["grade"+str(i+1)]
            except:
                continue
        return self.result_array

    def grade(self, grade_number):
        self.roster()
        try:
            return self.result["grade"+str(grade_number)]
        except:
            return []