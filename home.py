class university():
    student = ''
    course = ''
    lecturer = ''

    def Student(self):
        print(f"My name is {self.student}")
    
    def Lecturer(self):
        print(f"My lecturer is {self.lecturer}")

    def Course(self):
        print(f"My course is {self.course}")

c1 = university()
c1.student = 'Hildah'
c1.course = 'BSIT'
c1.lecturer = 'MR.kASOZI'
c1.Student()
c1.Lecturer()
c1.Course()
