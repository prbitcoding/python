class Student:
    def __init__(self, name):
        self.name = name
        self._marks = []

    def add_mark (self, mark):
        if 0 <= mark <= 100:
            self._marks.append(mark)
        else:
            raise ValueError("mark between 0 to 100")

    @property
    def average(self):
        if not self._marks:
            return 0
        return sum(self._marks) / len(self._marks)
    
    def __str__(self):
        return f"{self.name}: {self.average:.2f} average over {len(self._marks)} marks"

    
    
student = Student("total average")
student.add_mark(90)
student.add_mark(80)
student.add_mark(70)
student.add_mark(60)
student.add_mark(50)
student.add_mark(50)
student.add_mark(99)

print(student.average)   