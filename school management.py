students = {}

def add_student():
    name = input("Student name: ")

    if name not in students:
        students[name] = []
        print("Student added.")
    else:
        print("Student already exists.")

def add_grade():
    name = input("Student name: ")

    if name in students:
        grade = float(input("Grade: "))
        students[name].append(grade)
        print("Grade added.")
    else:
        print("Student not found.")

def show_students():
    if len(students) == 0:
        print("No students.")
        return

    for student, grades in students.items():
        print(student, grades)

def average_grade():
    name = input("Student name: ")

    if name in students:

        if len(students[name]) == 0:
            print("No grades.")
            return

        avg = sum(students[name]) / len(students[name])

        print("Average:", round(avg, 2))

    else:
        print("Student not found.")

def ranking():

    ranking_list = []

    for student, grades in students.items():

        if len(grades) > 0:
            avg = sum(grades) / len(grades)
        else:
            avg = 0

        ranking_list.append((student, avg))

    ranking_list.sort(key=lambda x: x[1], reverse=True)

    print("\n=== Ranking ===")

    for i, item in enumerate(ranking_list, start=1):
        print(i, "-", item[0], "-", round(item[1], 2))

while True:

    print("\n===== SCHOOL MANAGEMENT =====")
    print("1. Add Student")
    print("2. Add Grade")
    print("3. Show Students")
    print("4. Average Grade")
    print("5. Ranking")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        add_grade()

    elif choice == "3":
        show_students()

    elif choice == "4":
        average_grade()

    elif choice == "5":
        ranking()

    elif choice == "6":
        break

    else:
        print("Invalid option.")
