students = ["Sebastian", "Joaquin", "Pedro"]

students.append("Emiliano")
students.append(input("Enter your name: "))

for s in students:
    print(s)
else:
    print(f"The list contains {len(students)} students")
    # The len starts at 1 and the index at 0   