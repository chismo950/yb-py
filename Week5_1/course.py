from database import create_table_course
from course_manager import add_course, view_courses, search_course, delete_course

def menu():
    print("\n==== Course Manager ====")
    print("1. Add Course")
    print("2. View All Courses")
    print("3. Search Course by Name")
    print("4. Delete Course by ID")
    print("5. Exit")

def main():
    create_table_course()
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            name = input("Enter name: ")
            unit = input("Enter unit: ")
            add_course(name, unit)
        elif choice == '2':
            courses = view_courses()
            for course in courses:
                print(course)
        elif choice == '3':
            name = input("Enter name to search: ")
            courses = search_course(name)
            for course in courses:
                print(course)
        elif choice == '4':
            course_id = int(input("Enter course ID to delete: "))
            delete_course(course_id)
        elif choice == '5':
            print("Goodbye!")
            break
                
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
