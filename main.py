import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "Rayan",
    password = "!Rayan32136.",
    database = "eduresult_db"
)
cursor = connection.cursor()

#Dictionary that stores all students data
students = {}

#Dictionary that stores all the modules
courses = {}

#Empty list for results
results = []

#Tuple for fixed grade boundries
grade_boundries = (
    (90, "A+", 4.0),
    (85, "A", 4.0),
    (80, "A-", 3.7),
    (75, "B+", 3.7),
    (70, "B", 3.5),
    (65, "B-", 3.3),
    (60, "C+", 3.0),
    (55, "C", 2.3),
    (50, "C-", 2.0),
    (49, "F", 0.0)
)

#Student Class
class Student:
    def __int__(self, student_id, first_name, last_name, program, semester):

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.program = program
        self.semester = semester

        #Empty list tha store student's results
        self.results = []

        def add_result(self, result):
            self.results.append(result)

        def calculate_gpa(self):
            if len(self.results) == 0:
                return 0
            total_points = 0
            total_credits = 0

            for result in self.results:
                total_points += (
                    result.grade_point * result.credit_hours
                )
                total_credits += result.credit_hours

            if total_credits == 0:
                return 0

            gpa = total_points / total_credits

            return gpa

        def display_results(self):
            print("\n==============================================")
            print("              SEMESTER RESULT")
            print("==============================================")
            print("Student ID :", self.student_id)
            print("Name       :", self.name)
            print("Program    :", self.program)

            if len(self.results) > 0:
                print(
                    "Semester   :",
                    self.results[0].semester
                )
            print("----------------------------------------------")
            print(
                "Course Code | Module | Score | Grade"
            )
            print("----------------------------------------------")

            for result in self.results:
                result.display_result()
            print("----------------------------------------------")

            gpa = self.calculate_gpa()
            print("Semester GPA:",round(gpa, 2))
            print("==============================================")

class Results:
    def __init__(self, result_id, module_code, module_name, credit_hours, semester, score):
        self.result_id = result_id
        self.module_code = module_code
        self.module_name = module_name
        self.credit_hours = credit_hours
        self.semester = semester
        self.score = score
        self.grade = ""
        self.grade_point = 0

        self.calculate_grade()

    def calculate_grade(self):
        for minimum_score, grade, grade_point in grade_boundries:
            if self.score >= minimum_score:
                self.grade = grade
                self.grade_point = grade_point

                return

    def display_result(self):
        print(self.module_code, "|",
              self.module_name, "|",
              self.score, "|",
              self.grade
        )

#REGISTER STUDENT FUNCTION
def register_student(self):
    print("========================================")
    print("           REGISTER STUDENT")
    print("========================================")
    try:
        student_id = int(input("Enter student's ID: "))
    except ValueError:
        print("Student's ID must be a number.")
        return
    cursor.execute("""
    SELECT * FROM students Where student_id = &s
    """,
                   (student_id,)
    )
    existing_student = cursor.fetchone()
    if existing_student:
        print("Student alreaddy exists.")
        return
    #Proceedes to ask for student name if they don't exist
    first_name = input("Enter Student First Name: ")
    last_name = input("Enter Student Last Name: ")
    program = input("Enter Program: ")
    try:
        semester = int(input("Enter Current Semester:"))
    except ValueError:
        print("Semester must be a number.")
        return
    if semester < 1 or semester > 8:
        print("Semester must be between 1 and 8.")
        return
    student = Student(
        student_id,
        first_name,
        last_name,
        program,
        semester
    )
    students[student_id] =student
    cursor.execute(
        """
        INSERT INTO students (student_id, first_name, last_name, program, semester)
        VALUES (%s, %s, %s, %s, %s)
        """,

                student_id,
                first_name,
                last_name,
                program,
                semester
        )
    )
    connection.commit()
    print("\nStudent registered successfully.")

#ADD COURSE FUNCTION
def add_course():

    print("\n================================")
    print("            ADD COURSE")
    print("================================")

    course_code = input("Enter Course Code: ")
    cursor.execute(
        """
        SELECT *
        FROM courses
        WHERE course_code = %s
        """,
        (course_code,)
    )
    existing_course = cursor.fetchone()
    if existing_course:
        print("Course already exists.")
        return

    course_name = input("Enter Course Name: ")

    #Using try-catch for the program not to crash if there's an input error
    try:
        credit_hours = int(input("Enter Credit Hours: "))
    except ValueError:
        print("Credit hours must be a number.")
        return

    if credit_hours <= 0:
        print("Credit hours must be greater than 0.")
        return

    # Tuple
    course = (
        course_code,
        course_name,
        credit_hours
    )

    courses[course_code] = course
    cursor.execute(
        """
        INSERT INTO courses
        (course_code, course_name, credit_hours)
        VALUES (%s, %s, %s)
        """,
        course
    )

    connection.commit()
    print("\nCourse added successfully.")



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
