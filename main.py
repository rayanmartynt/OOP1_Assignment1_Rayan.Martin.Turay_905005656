import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "Rayan",
    password = "!Rayan32136.",
    database = "eduresult_db"
)
cursor = connection.cursor()

#Dictionary that contains all students
students = {}

#Dictionary that stores all the modules


#Main Function
def main():
    while True:
        print("========================================")
        print("              EDURESULTS")
        print(" Digital Exam & Results Management")
        print("========================================")

        #Menu
        print("1. Register Student")
        print("2. Add Course")
        print("3. Enter Student Result")
        print("4. View Student Result")
        print("5. Calculate Student Average")
        print("6. Display All Students")
        print("7. Display All Courses/Programme")
        print("8. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            register_student()
        elif choice == 2:
            add_course()
        elif choice == 3:
            enter_result()
        elif choice == 4:
            view_results()
        elif choice == 5:
            calculate_student_average()
        elif choice == 6:
            display_students()
        elif choice == 7:
            display_courses()

        elif choice == 8:
            print("========================================")
            print("Thank you for using EduResults.")
            print("========================================")
        else:
            print("Invalid Choice.")
            print("Please select an option from 1 to 8.")

#Entry point of the program
if __name__ == '__main__':
    main()
