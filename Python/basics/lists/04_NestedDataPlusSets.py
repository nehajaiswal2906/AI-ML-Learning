# Phase 7 — Problem 2: Nested Data + Sets

# You are given student enrollment data:

# students = [
#     ["Aman", ["Python", "AI", "Math"]],
#     ["Riya", ["Python", "DBMS"]],
#     ["Karan", ["AI", "Math", "Python"]],
#     ["Neha", ["Python", "AI"]],
#     ["Rohit", ["DBMS", "Math"]]
# ]

# Each student has:

# [name, list of courses]

# Your program must determine:

# All unique courses offered among these students.
# Students enrolled in both Python and AI.
# Students enrolled in Python but NOT AI.
# The most popular course — the course taken by the largest number of students.
# If two or more courses have the same highest enrollment, report all of them.
# Example reasoning

# For Python:

# Aman  ✓
# Riya  ✓
# Karan ✓
# Neha  ✓
# Rohit ✗

# So Python has 4 students.

# Important constraint

# Don't use collections.Counter.

# You should use sets where they make sense.

# Before coding

# Don't jump straight into Python.

# Give me:

# Input:
# Output:
# Data structures:
# Approach:
# Edge cases:

# You don't need a huge explanation. A few lines for each is enough.

# Then we'll code it.


students = [
    ["Aman", ["Python", "AI", "Math"]],
    ["Riya", ["Python", "DBMS"]],
    ["Karan", ["AI", "Math", "Python"]],
    ["Neha", ["Python", "AI"]],
    ["Rohit", ["DBMS", "Math"]]
 ]

distinctcourses=[]
pythonAndAi=[]
pythonNotAi=[]

for student in students:

    for i in range (0,len(student[1])):

        if student[1][i] not in distinctcourses:
            distinctcourses.append(student[1][i])

    if "Python" in student[1] and "AI" in student[1]:
        pythonAndAi.append(student[0])

    if "Python" in student[1] and "AI" not in student[1]:
        pythonNotAi.append(student[0])

print("\nAll unique courses offered among these students:-")

numbering=1
for i in distinctcourses:
    print(f"{numbering}. {i}")
    numbering+=1

print("\nStudents in both Python and Ai:- ")

numbering=1
for i in pythonAndAi:
    print(f"{numbering}. {i}")
    numbering+=1

print("\nStudents in Python but not in Ai:- ")

numbering=1
for i in pythonNotAi:
    print(f"{numbering}. {i}")
    numbering+=1

maxcount=0
course=[]

for i in distinctcourses:
    count=0

    for student in students:
        for j in range(0,len(student[1])):
            if student[1][j]==i:
                count+=1

    if count>maxcount:
        maxcount=count
        course=[i]

    elif count==maxcount:
        course.append(i)

if len(course)==1:
    print("\nThe most popular course is:",course[0])

elif len(course)>1:
    print("\nThe most popular courses are:-")
    numbering=1

    for i in course:
        print(f"{numbering}. {i}")
        numbering+=1
