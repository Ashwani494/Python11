'''
type of method
1.instance method
2. class method
3. static method


'''
class Student:
    school="techsrijan"
    def get_marks(self,m1,m2,m3):  #instance method -accepts self argument
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def add_marks(self):
        return self.m1+self.m2+self.m3

    @classmethod
    def get_schoolname(cls): # class method -accepts cls argument
        return cls.school

    @staticmethod
    def msg():   # static method accepts no argument
        print("thank you")

s=Student()
s.get_marks(10,20,30)
print("total marks=",s.add_marks())
print(s.get_schoolname())
print(Student.get_schoolname())
Student.msg()
s.msg()