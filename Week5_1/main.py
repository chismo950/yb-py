from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, update_user, search_user_advanced

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Search By ID and Name")
    print("7. Update User by ID")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        if choice == '7':
            user_id = input("Enter User ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            update_user(user_id, name, email)
        elif choice == '6':
            user_id = input("Enter User ID: ")
            name = input("Enter name: ")
            user = search_user_advanced(user_id, name)
            print(user)
                
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
