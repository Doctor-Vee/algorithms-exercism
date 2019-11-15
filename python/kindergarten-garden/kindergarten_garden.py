class Garden(object):
    def __init__(self, diagram, students=[
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred", 
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = students
        self.students.sort()
        self.diagram = diagram.split("\n")

    def plants(self, student):
        i = self.students.index(student)
        plants = []
        plantCode = self.diagram[0][i*2:i*2+2] + self.diagram[1][i*2:i*2+2]

        for code in plantCode:
            if code == "V":
                plants.append("Violets")
            elif code == "R":
                plants.append("Radishes")
            elif code == "C":
                plants.append("Clover")
            else:
                plants.append("Grass")
        return plants