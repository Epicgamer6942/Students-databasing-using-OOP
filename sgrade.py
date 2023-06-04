import random
class Grade:
    def __init__(self,grade,lst):
        self.grade = grade
        self.lst = lst
    def add_studentgrade(self):
        #[name,grade,course,marks]
        if self.grade == " ":
            self.grade = None
            self.lst.insert(1,self.grade)
        else:  
            self.lst.insert(1,self.grade)
    def del_studentgrade(self):
        self.lst.remove(self.grade)
        x = "temp-grade-" + str(random.randint(0,1000))
        self.lst.insert(1,x)
    def edit_studentgrade(self):
        newgrade = input("Enter edited grade:")
        self.lst[1] = newgrade
        