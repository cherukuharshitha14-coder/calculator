while True:
    print("\n***** STUDENT MANAGEMENT SYSTEM *****")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        find_topper()
    elif choice == 7:
        average_marks()
    elif choice == 8:
        count_students()
    elif choice == 9:
        print("Exiting Student Management System...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
        
