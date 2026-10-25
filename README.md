# EduResults – Digital Exam & Results Management System

**A Python and MySQL-based application for managing student records, academic results, grades, and semester GPA.**

## 📌 Project Overview

EduResults is a Digital Exam & Results Management System developed to simplify the process of managing student information, course records, examination scores, and academic performance.

In many educational institutions, handling student results manually can be time-consuming and may lead to calculation errors, duplicate records, misplaced information, and delays in releasing results. EduResults aims to improve this process by providing a centralized database and a Python-based application for storing and retrieving academic information.

The system uses **Python** for application logic and **MySQL** for data storage. It demonstrates fundamental Object-Oriented Programming (OOP) concepts, database connectivity, data validation, SQL queries, and automated grade and GPA calculations.

## 🎯 Project Objectives

- Digitize student registration and academic result management.
- Store student and course information in a structured database.
- Record examination scores and automatically determine grades.
- Organize academic results by semester.
- Calculate semester GPA using course credit hours.
- Reduce duplicate records and improve data consistency.
- Demonstrate practical Python, MySQL, and OOP programming skills.

## ✨ Key Features

### 1. Student Management
- Register students using a unique Student ID.
- Request the student's first name and last name separately.
- Combine the names and store them as one full name.
- Record the student's program and current semester.
- Prevent registration of duplicate Student IDs.

### 2. Course Management
- Store course codes and course names.
- Assign credit hours to each course.
- Retrieve course information when entering results.
- Maintain a centralized list of courses.

### 3. Examination and Results Management
- Associate results with students and courses.
- Record academic scores on a scale of 0–100.
- Automatically assign grades based on predefined grade boundaries.
- Link each result to a specific semester.
- Prevent duplicate results for the same student, course, and semester.

### 4. Semester-Based Results
- Retrieve a student's results for a selected semester.
- Display course codes, course names, scores, and grades.
- Keep results for different semesters separate.
- Calculate GPA for the selected semester rather than combining all semesters.

### 5. GPA Calculation
- Calculate semester GPA using the grade points and credit hours of completed courses.
- Give courses with more credit hours proportionally greater weight in the calculation.

### 6. Database Integration
- Connect Python to MySQL using `mysql-connector-python`.
- Store records persistently in the `eduresults` database.
- Use SQL queries to insert, retrieve, and validate records.
- Handle database errors and roll back failed transactions where implemented.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic and program functionality |
| MySQL | Relational database management |
| MySQL Connector/Python | Connects Python to MySQL |
| SQL | Creating tables and managing records |
| Object-Oriented Programming | Organizing student and result data into classes |
| Git and GitHub | Version control and project documentation |

## 🗄️ Database Design

The project uses a MySQL database named `eduresults`, consisting of three main tables.

### Students Table

Stores student information.

| Column | Description |
|---|---|
| `student_id` | Unique student identifier and primary key |
| `name` | Student's combined first and last name |
| `program` | Academic program |
| `semester` | Student's current semester, from 1 to 6 |

### Courses Table

Stores information about courses offered by the institution.

| Column | Description |
|---|---|
| `course_code` | Unique course identifier and primary key |
| `course_name` | Full name of the course |
| `credit_hours` | Number of credit hours assigned to the course |

### Results Table

Stores student scores and grades for individual courses.

| Column | Description |
|---|---|
| `result_id` | Automatically generated result identifier |
| `student_id` | References the student who received the result |
| `course_code` | References the course associated with the result |
| `semester` | Semester in which the result was recorded |
| `score` | Student's numerical score |
| `grade` | Grade assigned based on the score |

**Database relationships:**

- One student can have multiple results.
- One course can appear in multiple student results.
- Each result belongs to one student and one course.
- The combination of Student ID, Course Code, and Semester must be unique.

These relationships help maintain data integrity and reduce unnecessary duplication.

## 📊 Grading System

The application uses the following grade boundaries and grade points.

| Score | Grade | Grade Point |
|---:|:---:|---:|
| 90–100 | A+ | 4.0 |
| 80–89 | A | 4.0 |
| 75–79 | B+ | 3.5 |
| 70–74 | B | 3.0 |
| 65–69 | C+ | 2.5 |
| 60–64 | C | 2.0 |
| 50–59 | C- | 1.5 |
| Below 50 | F | 0.0 |

*These boundaries reflect the project's current implementation. They should be adjusted if the institution uses a different grading policy.*

### Semester GPA Formula

EduResults calculates GPA using a credit-hour-weighted average:

\[
\text{GPA} =
\frac{\sum(\text{Grade Point}\times\text{Credit Hours})}
{\sum(\text{Credit Hours})}
\]

**Example:**

| Course | Grade Point | Credit Hours | Weighted Points |
|---|---:|---:|---:|
| Structured Programming | 4.0 | 3 | 12.0 |
| Database Systems | 3.5 | 3 | 10.5 |
| Software Engineering | 3.0 | 4 | 12.0 |
| **Total** | | **10** | **34.5** |

\[
\text{GPA}=\frac{34.5}{10}=3.45
\]

The semester GPA in this example is **3.45**.

## 📋 System Requirements

### Hardware
- A computer or laptop.
- Sufficient memory and storage to run Python and MySQL.

### Software
- Python 3.
- MySQL Server.
- MySQL Workbench or another MySQL client (optional).
- A code editor such as Visual Studio Code or PyCharm.
- Git (optional, for version control).

## 🚀 Installation and Setup

Follow these steps to run EduResults on your computer.

### Step 1: Install Python and MySQL

Install Python 3 and MySQL Server if they are not already installed.

Verify Python:

```bash
python --version
```

### Step 2: Clone the Repository

If the project is hosted on GitHub, clone it using:

```bash
git clone "https://github.com/rayanmartynt/OOP1_Assignment1_Rayan.Martin.Turay_905005656.git"
```

Navigate to the project directory:

```bash
cd EduResults
```

Replace the repository URL and directory name with your actual values.

### Step 3: Install the Required Python Package

Run:

```bash
pip install mysql-connector-python
```

### Step 4: Create the Database

Open MySQL Workbench or your preferred MySQL client and run:

```sql
CREATE DATABASE IF NOT EXISTS eduresults_ed;

USE eduresults_ed;
```

Create the `students`, `courses`, and `results` tables using the SQL statements provided in the project's database setup script or documentation.

### Step 5: Configure the Database Connection

In the Python source file, configure the connection using your local MySQL credentials:

```python
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="eduresults_ed"
)

cursor = connection.cursor()
```

Replace `YOUR_MYSQL_PASSWORD` with your actual MySQL password.

**Security note:** Do not commit real database passwords to a public GitHub repository. For a more secure setup, use environment variables or a local configuration file excluded from version control.

### Step 6: Run the Application

Run the main Python file from your terminal:

```bash
python main.py
```

Replace `main.py` with the actual filename containing your program's entry point.

## 🖥️ How to Use the System

The exact menu options depend on the implementation, but the intended workflow is:

1. **Start the application:** Connect to the MySQL database.
2. **Register a student:** Enter the Student ID, first name, last name, program, and current semester.
3. **Add courses:** Enter each course's code, name, and credit hours.
4. **Enter results:** Select the student and course, enter the semester and score, and determine the corresponding grade.
5. **View results:** Retrieve academic results for the relevant student and semester.
6. **Calculate GPA:** Calculate the semester GPA using grade points and credit hours.
7. **Review records:** Display registered students, available courses, and stored results as supported by the application.

## 🧱 Object-Oriented Programming Concepts

EduResults demonstrates important OOP concepts.

### Classes and Objects
The `Student` class represents student information, while the `Result` class represents an academic result.

### Encapsulation of Related Data
Student attributes and result-related information are grouped into objects, making the program easier to organize and maintain.

### Methods and Functions
Functions and methods handle tasks such as registration, course management, result entry, grade assignment, and GPA calculation.

### Data Structures
- **Dictionary:** Stores student objects using Student IDs as keys.
- **List:** Stores result records and, where implemented, each student's results.
- **Tuple:** Stores fixed grade boundaries and related grade-point information.

### Database Connectivity
The application uses SQL statements through MySQL Connector/Python to communicate with the relational database.

## 🔒 Data Integrity and Validation

The project includes or is designed to support the following safeguards:

- Unique Student IDs.
- Required student names and program information.
- Semester validation from 1 to 6.
- Score validation from 0 to 100.
- Valid references between students, courses, and results.
- Prevention of duplicate results for the same student, course, and semester.
- Database transaction handling for failed insert operations.

The exact safeguards depend on which validation checks are implemented in the current source code.

## ⚠️ Current Scope and Limitations

EduResults is an educational project focused on core programming and database concepts.

Depending on the current implementation, the system may not yet include:

- A graphical user interface or web interface.
- Student and lecturer authentication.
- Role-based access control.
- Password management.
- PDF transcript generation.
- Automated email or SMS notifications.
- Deployment to a remote server.
- A production-grade audit trail and backup system.

These features can be considered for future development.

## 🔮 Future Improvements

Possible enhancements include:

1. Add secure login for administrators, lecturers, and students.
2. Introduce role-based permissions.
3. Develop a graphical interface or web application.
4. Allow lecturers to enter and update results through a dedicated dashboard.
5. Allow students to view their own results securely.
6. Generate downloadable academic transcripts.
7. Add cumulative GPA calculations across multiple semesters.
8. Create result reports and academic performance charts.
9. Add database backup and recovery procedures.
10. Deploy the application for access within an educational institution.

## 🧪 Testing

The following test cases can be used to evaluate the application.

| Test Case | Expected Result |
|---|---|
| Register a student with valid details | Student is saved successfully |
| Register an existing Student ID | Duplicate registration is rejected |
| Leave a name field empty | Registration is rejected |
| Enter a non-numeric semester | Validation error is displayed |
| Enter a semester outside 1–6 | Validation error is displayed |
| Enter a score outside 0–100 | Score is rejected |
| Enter a valid score | Corresponding grade is assigned |
| Record a duplicate result for the same course and semester | Duplicate is rejected |
| Calculate GPA for a semester with results | Semester GPA is calculated |
| Query a semester without results | An appropriate message is displayed |

## 📁 Project Structure

EduResults uses a simple, single-file structure. All Python application logic, including student registration, course management, result entry, grade calculation, GPA calculation, and database connectivity, is contained in `main.py`.

```text
EduResults/
│
├── main.py             # Main Python application
├── requirements.txt    # Required Python packages
├── README.md           # Project documentation
└── .gitignore          # Files excluded from Git
```

**Main file: `main.py`**

This file contains:
- MySQL database connection.
- Student and result classes.
- Student registration.
- Course management.
- Examination result entry.
- Automatic grade calculation.
- Semester-based result viewing.
- Semester GPA calculation.
- Main program menu and application logic.

**Database file: `database.sql`**

Contains the SQL statements for creating the `eduresults` database tables and, if required, inserting sample course records.

**Dependencies file: `requirements.txt`**

Contains the Python packages required to run the application.

Example:

```text
mysql-connector-python
```

Install the dependency with:

```bash
pip install -r requirements.txt
```

**Documentation file: `README.md`**

Explains the project's purpose, features, technologies, database structure, installation instructions, and usage.

**Note:** Only `main.py` contains the Python application code. The other files are for database setup, dependency installation, documentation, and repository configuration.


## 🎓 Educational Value

EduResults provides practical experience in:

- Python programming.
- Object-Oriented Programming.
- Relational database design.
- SQL queries and constraints.
- Input validation and exception handling.
- Database transactions.
- Grade and GPA calculations.
- Software testing and documentation.
- Version control with Git and GitHub.

## 👨‍💻 Author

**Name:** Rayan Martin Turay

**Project:** EduResults – Digital Exam & Results Management System

**Developed using:** Python and MySQL

**Project focus:** Student records, academic results, grade assignment, and semester GPA calculation.

---

*EduResults aims to make academic result management more organized, consistent, and efficient through software automation and structured database storage.*
