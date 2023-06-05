import random
from s_csv import Files
class Student:
    def __init__(self,name,lst):
        self.name = name
        self.lst = lst
    def add_studentName(self):
        #[name,grade,course,marks]
        if self.name == " ":
            self.name = None
            self.lst.insert(0,self.name)
        else:  
            self.lst.insert(0,self.name)
    def del_studentName(self):
        self.lst.remove(self.name)
        x = "temp-student-" + str(random.randint(0,1000))
        self.lst.insert(0,x)
    def edit_studentName(self):
        newName = input("Enter edited name:")
        self.lst[0] = newName
    
    def get_student(self,num = len(Files.read())):
        l1 = []
        for i in Files.read():
            l1.append(i[1])
        return l1
        


            
