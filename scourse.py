import random
class Course:
    def __init__(self,course,lst):
        self.course = course
        self.lst = lst
    def add_studentcourse(self):
        #[name,grade,course,marks]
        if self.course == " ":
            self.course = None
            self.lst.insert(-2,self.course)
        else:  
            self.lst.insert(-2,self.course)
    def del_studentcourse(self):
        self.lst.remove(self.course)
        x = "temp-course-" + str(random.randint(0,1000))
        self.lst.insert(-2,x)
    def edit_studentcourse(self):
        newcourse = input("Enter edited course:")
        self.lst[-2] = newcourse