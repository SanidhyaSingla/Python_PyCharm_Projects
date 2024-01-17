n = int(input("Please enter the number of students: "))

total_marks = []

for i in range(1, n+1):
    marks = int(input("Please enter the marks of student"))

    total_marks.append(marks)

print("The highest marks are", max(total_marks))

