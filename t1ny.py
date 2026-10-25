import mysql.connector


# ==========================================
# MYSQL DATABASE CONNECTION
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="eduresults"
)

cursor = connection.cursor()


# ==========================================
# DATA STRUCTURES
# ==========================================

students = {}

courses = {}

results = []


# ==========================================
# GRADE BOUNDARIES
# ==========================================

# Tuple:
# minimum score, grade, grade point

grade_boundaries = (
    (90, "A+", 4.0),
    (80, "A", 4.0),
    (75, "B+", 3.5),
    (70, "B", 3.0),
    (65, "C+", 2.5),
    (60, "C", 2.0),
    (50, "C-", 1.5),
    (0, "F", 0.0)
)


# ==========================================
# STUDENT CLASS
# ==========================================

class Student:

    def __init__(
        self,
        student_id,
        name,
        program,
        semester
    ):

        self.student_id = student_id
        self.name = name
        self.program = program
        self.semester = semester

        # List containing student results
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
                result.grade_point *
                result.credit_hours
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

        print(
            "Semester GPA:",
            round(gpa, 2)
        )

        print("==============================================")


# ==========================================
# RESULT CLASS
# ==========================================

class Result:

    def __init__(
        self,
        result_id,
        course_code,
        course_name,
        credit_hours,
        semester,
        score
    ):

        self.result_id = result_id

        self.course_code = course_code

        self.course_name = course_name

        self.credit_hours = credit_hours

        self.semester = semester

        self.score = score

        self.grade = ""

        self.grade_point = 0

        self.calculate_grade()


    def calculate_grade(self):

        for minimum_score, grade, grade_point in grade_boundaries:

            if self.score >= minimum_score:

                self.grade = grade

                self.grade_point = grade_point

                return


    def display_result(self):

        print(
            self.course_code,
            "|",
            self.course_name,
            "|",
            self.score,
            "|",
            self.grade
        )


# ==========================================
# REGISTER STUDENT
# ==========================================

def register_student():

    print("\n================================")
    print("         REGISTER STUDENT")
    print("================================")

    student_id = input(
        "Enter Student ID: "
    )

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    existing_student = cursor.fetchone()

    if existing_student:

        print("Student already exists.")

        return

    name = input(
        "Enter Student Name: "
    )

    program = input(
        "Enter Program: "
    )

    try:

        semester = int(
            input("Enter Current Semester: ")
        )

    except ValueError:

        print("Semester must be a number.")

        return

    if semester < 1 or semester > 6:

        print(
            "Semester must be between 1 and 6."
        )

        return

    student = Student(
        student_id,
        name,
        program,
        semester
    )

    students[student_id] = student

    cursor.execute(
        """
        INSERT INTO students
        (student_id, name, program, semester)
        VALUES (%s, %s, %s, %s)
        """,
        (
            student_id,
            name,
            program,
            semester
        )
    )

    connection.commit()

    print(
        "\nStudent registered successfully."
    )


# ==========================================
# ADD COURSE
# ==========================================

def add_course():

    print("\n================================")
    print("            ADD COURSE")
    print("================================")

    course_code = input(
        "Enter Course Code: "
    )

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

    course_name = input(
        "Enter Course Name: "
    )

    try:

        credit_hours = int(
            input("Enter Credit Hours: ")
        )

    except ValueError:

        print(
            "Credit hours must be a number."
        )

        return

    if credit_hours <= 0:

        print(
            "Credit hours must be greater than 0."
        )

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

    print(
        "\nCourse added successfully."
    )


# ==========================================
# ENTER RESULT
# ==========================================

def enter_result():

    print("\n================================")
    print("           ENTER RESULT")
    print("================================")

    student_id = input(
        "Enter Student ID: "
    )

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    student_data = cursor.fetchone()

    if not student_data:

        print("Student not found.")

        return

    try:

        semester = int(
            input("Enter Semester: ")
        )

    except ValueError:

        print(
            "Semester must be a number."
        )

        return

    if semester < 1 or semester > 6:

        print(
            "Semester must be between 1 and 6."
        )

        return

    course_code = input(
        "Enter Course Code: "
    )

    cursor.execute(
        """
        SELECT *
        FROM courses
        WHERE course_code = %s
        """,
        (course_code,)
    )

    course_data = cursor.fetchone()

    if not course_data:

        print("Course not found.")

        return

    try:

        score = float(
            input("Enter Score: ")
        )

    except ValueError:

        print("Score must be a number.")

        return

    if score < 0 or score > 100:

        print(
            "Score must be between 0 and 100."
        )

        return

    # Check whether result already exists
    cursor.execute(
        """
        SELECT *
        FROM results
        WHERE student_id = %s
        AND course_code = %s
        AND semester = %s
        """,
        (
            student_id,
            course_code,
            semester
        )
    )

    existing_result = cursor.fetchone()

    if existing_result:

        print(
            "This student already has a result "
            "for this module in this semester."
        )

        return

    course_name = course_data[1]

    credit_hours = course_data[2]

    # Create Result object
    result = Result(
        None,
        course_code,
        course_name,
        credit_hours,
        semester,
        score
    )

    # Add to global list
    results.append(result)

    # Create student object if necessary
    if student_id not in students:

        student = Student(
            student_data[0],
            student_data[1],
            student_data[2],
            student_data[3]
        )

        students[student_id] = student

    # Add result to student's list
    students[student_id].add_result(
        result
    )

    # Save to MySQL
    cursor.execute(
        """
        INSERT INTO results
        (
            student_id,
            course_code,
            semester,
            score,
            grade
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            student_id,
            course_code,
            semester,
            score,
            result.grade
        )
    )

    connection.commit()

    print(
        "\nResult saved successfully."
    )

    print("Module:", course_name)

    print("Score:", score)

    print("Grade:", result.grade)

    print(
        "Grade Point:",
        result.grade_point
    )


# ==========================================
# LOAD SEMESTER RESULTS
# ==========================================

def load_student_results(
    student_id,
    semester
):

    student_results = []

    cursor.execute(
        """
        SELECT
            results.result_id,
            results.course_code,
            courses.course_name,
            courses.credit_hours,
            results.semester,
            results.score,
            results.grade

        FROM results

        JOIN courses
        ON results.course_code =
           courses.course_code

        WHERE results.student_id = %s
        AND results.semester = %s

        ORDER BY courses.course_code
        """,
        (
            student_id,
            semester
        )
    )

    rows = cursor.fetchall()

    for row in rows:

        result = Result(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )

        # Use grade stored in database
        result.grade = row[6]

        # Set grade point based on stored grade
        for minimum_score, grade, grade_point in grade_boundaries:

            if result.grade == grade:

                result.grade_point = grade_point

                break

        student_results.append(result)

    return student_results


# ==========================================
# VIEW SEMESTER RESULTS
# ==========================================

def view_semester_results():

    print("\n================================")
    print("       VIEW SEMESTER RESULT")
    print("================================")

    student_id = input(
        "Enter Student ID: "
    )

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    student_data = cursor.fetchone()

    if not student_data:

        print("Student not found.")

        return

    try:

        semester = int(
            input("Enter Semester: ")
        )

    except ValueError:

        print(
            "Semester must be a number."
        )

        return

    semester_results = load_student_results(
        student_id,
        semester
    )

    if len(semester_results) == 0:

        print(
            "\nNo results found for Semester",
            semester
        )

        return

    student = Student(
        student_data[0],
        student_data[1],
        student_data[2],
        semester
    )

    for result in semester_results:

        student.add_result(result)

    student.display_results()


# ==========================================
# CALCULATE SEMESTER GPA
# ==========================================

def calculate_semester_gpa():

    print("\n================================")
    print("       CALCULATE SEMESTER GPA")
    print("================================")

    student_id = input(
        "Enter Student ID: "
    )

    cursor.execute(
        """
        SELECT *
        FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    student_data = cursor.fetchone()

    if not student_data:

        print("Student not found.")

        return

    try:

        semester = int(
            input("Enter Semester: ")
        )

    except ValueError:

        print(
            "Semester must be a number."
        )

        return

    semester_results = load_student_results(
        student_id,
        semester
    )

    if len(semester_results) == 0:

        print(
            "\nNo results found for this semester."
        )

        return

    student = Student(
        student_data[0],
        student_data[1],
        student_data[2],
        semester
    )

    for result in semester_results:

        student.add_result(result)

    gpa = student.calculate_gpa()

    print("\n================================")

    print("Student:", student.name)

    print("Semester:", semester)

    print(
        "Semester GPA:",
        round(gpa, 2)
    )

    print("================================")


# ==========================================
# DISPLAY ALL STUDENTS
# ==========================================

def display_students():

    print("\n================================")
    print("          ALL STUDENTS")
    print("================================")

    cursor.execute(
        "SELECT * FROM students"
    )

    student_rows = cursor.fetchall()

    if not student_rows:

        print(
            "No students registered."
        )

        return

    for student in student_rows:

        print("\n----------------------------")

        print(
            "Student ID:",
            student[0]
        )

        print(
            "Name:",
            student[1]
        )

        print(
            "Program:",
            student[2]
        )

        print(
            "Current Semester:",
            student[3]
        )


# ==========================================
# DISPLAY ALL COURSES
# ==========================================

def display_courses():

    print("\n================================")
    print("           ALL COURSES")
    print("================================")

    cursor.execute(
        "SELECT * FROM courses"
    )

    course_rows = cursor.fetchall()

    if not course_rows:

        print(
            "No courses available."
        )

        return

    for course in course_rows:

        print("\n----------------------------")

        print(
            "Course Code:",
            course[0]
        )

        print(
            "Course Name:",
            course[1]
        )

        print(
            "Credit Hours:",
            course[2]
        )


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n==========================================")
    print("              EDURESULTS")
    print("   Digital Exam & Results Management")
    print("==========================================")

    print("1. Register Student")
    print("2. Add Course")
    print("3. Enter Result")
    print("4. View Semester Result")
    print("5. Calculate Semester GPA")
    print("6. Display Students")
    print("7. Display Courses")
    print("8. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    if choice == "1":

        register_student()

    elif choice == "2":

        add_course()

    elif choice == "3":

        enter_result()

    elif choice == "4":

        view_semester_results()

    elif choice == "5":

        calculate_semester_gpa()

    elif choice == "6":

        display_students()

    elif choice == "7":

        display_courses()

    elif choice == "8":

        print(
            "\nThank you for using EduResults."
        )

        connection.close()

        break

    else:

        print(
            "\nInvalid choice. Please try again."
        )