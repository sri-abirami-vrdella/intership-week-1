#------------------print total mark of a student---------------
class student:

    def __init__(self,name,s1,s2,s3,s4,s5):
        self.name=name
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5

    def tota_mark(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5

stu1=student('sam',98,33,56,33,99)
stu2=student('dev',77,99,90,99,99)
stu3=student("charlie",44,88,55,24,67)
stu4=student("john",44,88,55,24,67)
stu5=student("joey",44,88,55,24,67)

a=input("enter student name: ")

if a==stu1.name:
    print(stu1.tota_mark())
elif a==stu2.name:
    print(stu2.tota_mark())
elif a==stu3.name:
    print(stu3.tota_mark())
elif a==stu4.name:
    print(stu4.tota_mark())
else:
    print(stu5.tota_mark())
#-------------------------------------------------------------------------