class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

def main():
    students = {}

    while True:
        print("\nStudent Grade Tracker")
        print("1. Add a new student")
        print("2. Add a grade for a student")
        print("3. Calculate average for a student")
        print("4. Display all students and their averages")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            if name not in students:
                students[name] = Student(name)
                print(f"Student {name} added.")
            else:
                print(f"Student {name} already exists.")
        elif choice == '2':
            name = input("Enter student's name: ")
            if name in students:
                grade = float(input("Enter grade: "))
                students[name].add_grade(grade)
                print(f"Added grade {grade} to student {name}.")
            else:
                print(f"Student {name} not found.")
        elif choice == '3':
            name = input("Enter student's name: ")
            if name in students:
                average = students[name].calculate_average()
                print(f"{name}'s average grade is {average:.2f}.")
            else:
                print(f"Student {name} not found.")
        elif choice == '4':
            for name, student in students.items():
                average = student.calculate_average()
                print(f"{name}: {average:.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
