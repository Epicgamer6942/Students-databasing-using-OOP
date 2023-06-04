from sname import *
from sgrade import *
from scourse import *
from smarks import *
from s_csv import *
#[name,grade,course,marks]

lst = []
backup = []
files = Files("student.csv",lst,backup)
grade = Grade("XII",lst)
name = Student("Arjun",lst)
marks = Marks("85",lst)
course = Course("Computer Science",lst)
name.add_studentName()
grade.add_studentgrade()
course.add_studentcourse()
marks.add_studentmarks()
print(lst)
files.rollback()




