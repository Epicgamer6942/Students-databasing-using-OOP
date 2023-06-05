from sname import *
from sgrade import *
from scourse import *
from smarks import *
from s_csv import *
#[name,grade,course,marks]
def main():
    lst = []
    backup = []
    while True:
        files = Files("student.csv",lst,backup)
        sname = input("Enter name:")
        sgrade = input("Enter grade:")
        smarks = int(input("Enter your marks:"))
        scourse = input("Enter course name:")
        grade = Grade(sgrade,lst)
        name = Student(sname,lst)
        marks = Marks(smarks,lst)
        course = Course(scourse,lst)
        name.add_studentName()
        grade.add_studentgrade()
        course.add_studentcourse()
        marks.add_studentmarks()
        print("Choices for program are:\n1.New record\n2.View all records\n3.edit records\n4.Delete record\n5.Commit\n6.Rollback changes\n0.Quit")
        inp = input("Enter choice:")
        
        if inp == 1:
            files.add()
        elif inp == 2:
            files.read()
        elif inp == 3:
            name.edit_studentName()
            grade.edit_studentgrade()
            course.edit_studentcourse()
            marks.edit_studentmarks()
            files.add()
        elif inp == 4:
            nm = input("Enter the name to delete:")
            files.delrec(nm)
        elif inp == 5:
            files.commit() 
        elif inp == 6:
            files.rollback()
        elif inp == 0:
            break       
        print(lst)
main()





