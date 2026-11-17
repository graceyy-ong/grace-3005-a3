# connect to postgres
import psycopg

# get + display every student.
def getAllStudents():
    cursor.execute("SELECT * FROM students ORDER BY student_id")
    for student in cursor.fetchall():
        print(student)

# insert a new student (name, email, date) and receive a student id from pg
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(
        """
        INSERT INTO students
            (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
        RETURNING student_id
        """,
        (first_name, last_name, email, enrollment_date),
    )

    student_id = cursor.fetchone()[0]

    # save change to db
    connection.commit()

    print("Added student:", student_id)

# given the id, change the corresponding student's email
def updateStudentEmail(student_id, new_email):
    cursor.execute(
        "UPDATE students SET email = %s WHERE student_id = %s",
        (new_email, student_id),
    )
    rows_changed = cursor.rowcount

    # save change to db
    connection.commit()

    if rows_changed > 0:
        print("Email updated.")
    else:
        print("Student not found.")

# given the id, delete the correspondin student's info (from list)
def deleteStudent(student_id):
    cursor.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,),
    )
    rows_changed = cursor.rowcount

    # save change to db
    connection.commit()

    if rows_changed > 0:
        print("Student deleted.")
    else:
        print("Student not found.")


# login
connection = psycopg.connect(
    host="localhost",
    dbname="student_management",
    user="graceong",
)
cursor = connection.cursor()

try:
    # menu continues until 5 is entered
    while True:
        print("\n1. Display all students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")

        choice = input("What would you like to do? ")

        try:
            # display
            if choice == "1":
                getAllStudents()

            # add
            elif choice == "2":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                email = input("Email: ")
                enrollment_date = input("Enrollment date (YYYY-MM-DD, or leave blank for NULL): ")
                if enrollment_date == "":
                    enrollment_date = None

                addStudent(first_name, last_name, email, enrollment_date)

            # update
            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ")

                updateStudentEmail(student_id, new_email)

            # delete
            elif choice == "4":
                student_id = int(input("Student ID: "))

                deleteStudent(student_id)

            # quit
            elif choice == "5":
                break

            else:
                print("Choose a number from 1 to 5.")

        except ValueError:
            print("Student ID must be a whole number.")

        except psycopg.Error as error:
            # Undo a failed transaction so the connection remains usable.
            connection.rollback()
            print("Database error:", error)


# Close database resources when the program ends.
finally:
    cursor.close()
    connection.close()