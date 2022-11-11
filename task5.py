# Module grade calculator
from math import sqrt

print( "Module Grade Calculator")
print("-" * 23)

print()
module_name = input("Module? ")
students = int (input("Students? "))

total_mark = 0
min_mark = 0
max_mark = 0
num_passed = 0
marks = []
for i in range (students):
    mark = int (input ("Mark? "))
    
    marks.append(mark)
    
    min_mark= marks[0]
    
    for j in range (len(marks)):
        
        if (marks[j] < min_mark):
            
            min_mark = marks[j]

    if mark > max_mark:
        max_mark = mark

    

    if mark > 40:
        print("Passed")

        num_passed = num_passed + 1
    else:
         print("Failed")

    total_mark = mark
    

a = total_mark / students
#removed the second/

d= 0
for i in range(students):
#    mark = int(input ("Mark? "))

    d = d + (mark - a) * 2

d = sqrt(d/students)



print ()
print()
print ("Report for module ", module_name)
print("-" * 30)
print()
print("Number of students on module =",students)
print("Number students who passed the module=", num_passed)
print("Number of students who failed the module =", students- num_passed)
print("Maximum mark =", max_mark)
print("Minumum mark =",min_mark)
print("Average mark =", a)
print("standard deviation =", d)
#changed it to standard deviation