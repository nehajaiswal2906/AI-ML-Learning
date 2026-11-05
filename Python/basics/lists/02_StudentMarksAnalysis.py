# Challenge: Student Marks Analysis

# You receive:

# students = [
#     ["Aman", 78, 85, 91],
#     ["Riya", 92, 88, 95],
#     ["Karan", 67, 74, 81],
#     ["Neha", 92, 88, 95],
#     ["Rohit", 67, 74, 81]
# ]

# Each inner list is:

# [name, subject1, subject2, subject3]

# Your program must determine:

# The student with the highest total
# The highest total
# Whether multiple students have the same highest total
# The names of all students having that highest total
# The average mark across all individual marks
# The set of distinct marks appearing anywhere in the data
# Constraints

# Don't use:

# max()
# min()
# grandsum()

# You may use:

# lists
# sets
# loops
# len()
# normal conditionals
# Before coding

# Don't give me a line-by-line solution.

# Give me your architecture:

# Input:
# 

# Outputs:
# 

# Data structures:
# 

# Step 1:
# 

# Step 2:
# 

# Step 3:
# 

# 

# Edge cases:
# 


n=int(input("Number Of Students:"))
students=[]

for i in range(1,n+1):
    name=input(f"Name of Student {i}: ")
    sub1=int(input("Marks in Subject 1: "))
    sub2=int(input("Marks in Subject 2: "))
    sub3=int(input("Marks in Subject 3: "))
    students.append([name,sub1,sub2,sub3])

if len(students)==0:
    print("No students entered.")

else:
    maxmarks=0
    stuwithmaxmarks=[]
    distinctmarks=set()
    grandsum=0

    for student in students:
        totalmarks=student[1]+student[2]+student[3]
        grandsum+=totalmarks

        distinctmarks.add(student[1])
        distinctmarks.add(student[2])
        distinctmarks.add(student[3])

        if totalmarks>maxmarks:
            maxmarks=totalmarks
            stuwithmaxmarks=[]
            stuwithmaxmarks.append(student)

        elif totalmarks==maxmarks:
            stuwithmaxmarks.append(student)

    if len(stuwithmaxmarks)>1:
        print("Highest Marks is:",maxmarks)
        print("Multiple Students have highest marks.They are:-")

        for student in stuwithmaxmarks:
            print("->",student[0])

    else:
        print("Highest Marks is:",maxmarks)
        print("Student with highest marks:",stuwithmaxmarks[0][0])

    print("The average marks across all individual marks:-",grandsum/(len(students)*3))

    print("The set of Distinct marks across all subjects and all students:-")
    print(distinctmarks)

        
        