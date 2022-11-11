import math

print("Student Marks")
print()

num_marks =  int(input("Enter the number of student marks: "))
print()

totalMark = 0
list1 =[]

count = 1



for i in range(num_marks):
    studentMark = float(input("Please enter mark : "))
    totalMark += studentMark
    list1.append(studentMark)
    
    
print()

average_mark = (totalMark/num_marks)

print(f"The average mark is {average_mark:.1f}")

min_mark= min(list1)

max_mark = max(list1)



print(f"The  minimum mark is {min_mark:.1f}")
print(f"The maxmimum mark is {max_mark:.1f}")

print()
print("Student no.\tMark\tResult")

print()

for t in list1:
    if t >= 40:
        outcome = "passed"

      
    else:
         outcome = "Failed"
    
    

    print(f"{count}\t\t{t}\t{outcome}")
    count +=1
    
  