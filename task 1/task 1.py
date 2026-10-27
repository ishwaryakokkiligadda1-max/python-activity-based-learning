n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Name: ")
    aggregate = float(input("Aggregate marks: "))
    subject = float(input("Minimum subject marks: "))
    attendance = float(input("Attendance percentage: "))
    income = float(input("Annual family income: "))

    if (aggregate >= 75 and subject >= 40
            and attendance >= 75 and income <= 200000):
        students.append((name, aggregate, attendance, income))

print("\nEligible Students:")

if students:
    # Rank by aggregate, attendance, then lower income
    students.sort(key=lambda x: (-x[1], -x[2], x[3]))

    for rank, student in enumerate(students, start=1):
        print(rank, student[0],
              "Aggregate:", student[1],
              "Attendance:", student[2],
              "Income:", student[3])
else:
    print("No eligible students found.")

