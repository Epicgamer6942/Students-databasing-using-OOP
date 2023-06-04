import random
class Marks:
    def __init__(self,marks,lst):
        self.marks = marks
        self.lst = lst
    def add_studentmarks(self):
        #[name,grade,course,marks]
        if self.marks == " ":
            self.marks = None
            self.lst.insert(-1,self.marks)
        else:  
            self.lst.insert(-1,self.marks)
    def del_studentmarks(self):
        self.lst.remove(self.marks)
        x = "temp-marks-" + str(random.randint(0,1000))
        self.lst.insert(-1,x)
    def edit_studentmarks(self):
        newmarks = input("Enter edited marks:")
        self.lst[-1] = newmarks