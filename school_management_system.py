# School Management System

# Initialize an empty list to store student records
students = []

def get_all_students():
    """Display all students in the list."""
    if not students:
        print("\nNo record found!\n")
        return

    print("\nPrinting list of students: \n")
    for student in students:
        i = 1
        print(f"Record: {i}\nName: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        i += 1
    print("\n")

def add_student(name, age, grade):
    """Add a new student to the list."""
    if not isinstance(age, (int, float)):
        print("\nAge must be a number!\n")
        return
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)
    print(f"\nStudent {name} added successfully!\n")

def search_student_by_name(name):
    """Find and display a student by name."""
    for student in students:
        if student['name'] == name:
            print(f"\nName: {student['name']}, Age: {student['age']}, Grade: {student['grade']}\n")
            return
    print(f"\nRecord not found against student name {name}\n")

def main():
    """Main function to run the school management system."""
    while True:
        print("##### Welcome to school management system #####")
        print("1. Add new student")
        print("2. View all students")
        print("3. Search student by name")
        print("4. Exit the system")
        print("################################################\n")
        choice = int(input("Enter your choice (1/4): "))

        if choice == 1:
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            grade = input("Enter student's grade: ")
            try:
                age = int(age)
            except ValueError:
                print("Student age must be a number")
                continue
            add_student(name, age, grade)

        elif choice == 2:
            get_all_students()

        elif choice == 3:
            name = input("Enter student's name to search: ")
            search_student_by_name(name)

        elif choice == 4:
            print("Exiting the system, Goodbye!")
            break

        else:
            print("Invalid choice, please select a number between 1 to 4")

# Run the system by calling the main function
if __name__ == "__main__":
    main()