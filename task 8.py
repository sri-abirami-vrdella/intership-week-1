#------------------print total mark of students---------------

class Students:
    total_mark = 500
    class_total = 0
    obj_count = 0

    def __init__(self, name, s1, s2, s3, s4, s5):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5

        total = self.stotal_mark()
        Students.class_total += total
        Students.obj_count += 1

    def stotal_mark(self):

        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5

    @classmethod
    def class_average(cls):

        if cls.obj_count == 0:
            return 0
        return cls.class_total / cls.obj_count

    @staticmethod
    def average_percentage(total):

        return (total / Students.total_mark) * 100

    @classmethod
    def display(cls):

        print(f"Total possible marks per student: {cls.total_mark}")


class VII_A(Students):
    def __init__(self, name, s1, s2, s3, s4, s5):
        super().__init__(name, s1, s2, s3, s4, s5)

    def display(self):
        print(f"Total marks for student {self.name}: {self.stotal_mark()}")


# ------------------Main program------------------

stu1 = VII_A('sam', 98, 33, 56, 33, 99)
stu2 = VII_A('dev', 77, 99, 90, 99, 99)
stu3 = VII_A("charlie", 44, 88, 55, 24, 67)
stu4 = VII_A("john", 44, 88, 55, 24, 67)
stu5 = VII_A("joey", 44, 88, 55, 24, 67)

a = input("Enter student's name: ").strip().lower()

students_list = [stu1, stu2, stu3, stu4, stu5]
found = False

for s in students_list:
    if s.name.lower() == a:
        total = s.stotal_mark()
        print(f"Total marks of {s.name}: {total}")
        print(f"Percentage: {Students.average_percentage(total):.2f}%")
        found = True
        break

if not found:
    print("Student not found!")

print(f"\nClass average mark: {Students.class_average():.2f}")
print(f"Total number of students: {Students.obj_count}")
