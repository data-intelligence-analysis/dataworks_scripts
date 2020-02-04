from sqlite3 import connect
##Dennis Osafo
def show_menu():
    print("\n------")
    print ("MENU:")
    print ("_____")
    print ("1. Add a student")
    print ("2. Find a student")
    print ("3. Add a course")
    print ("4. Find a course")
    print ("5. Enroll a student")
    print ("6. Find Course(s) of a Student")
    print ("7. Find Student(s) of a Course")
    print ("8. Quit\n")
def add_student():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter student id...")
    y = input("Enter student name...")
    curs.execute("insert into student (studentid,studentname) values(\"" + x + "\", \""+y+"\");")
    conn.commit()
    print ("\nStudent " + x + "/" + y + " added successfully!")
    conn.close()
def find_student():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter student name...")
    curs.execute("select * from student where studentname like \"%" + x + "%\";")
    conn.commit()
    print("\nHere is the list...")
    for (name) in curs.fetchall():
        print(name)
    conn.close()
def add_course():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter course id...")
    y = input("Enter course name...")
    curs.execute("insert into course (courseid,coursename) values(\"" + x + "\", \""+y+"\");")
    conn.commit()
    print ("\nCourse " + x + "/" + y + " added successfully!")
    conn.close()
def find_course():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter course name...")
    curs.execute("select * from course where coursename like \"%" + x + "%\";")
    conn.commit()
    print("\nHere is the list...")
    for (name) in curs.fetchall():
        print(name)
    conn.close()
def enroll_student():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter student id...")
    y = input("\nEnter course id...")
    curs.execute("insert into enrollment(studentid, courseid) values(\""+x+"\",\""+y+"\");")
    conn.commit()
    print("\nEnrollment of student " + x +"in course" + y + "is successful")
    conn.close()


def find_a_course_for_student():
    conn = connect('training.db')
    curs = conn.cursor()
    x = input("\nEnter student id...")
    curs.execute("select student.studentname, course.coursename from student, course, enrollment where student.studentid = enrollment.studentid and course.courseid = enrollment.courseid and enrollment.studentid =\""+x+"\";")
    conn.commit()
    print("\nHere is the list...")
    for (name) in curs.fetchall():
        print(name)
    conn.close()

def find_student_for_course():
    conn = connect('training.db')
    curs = conn.cursor()
    x=input("\nEnter course id...")
    curs.execute("select student.studentname, course.coursename from student, course, enrollment where student.studentid = enrollment.studentid and course.courseid = enrollment.courseid and enrollment.courseid = \""+x+"\";")
    conn.commit()
    print("\nHere is the list...")
    for (name) in curs.fetchall():
        print(name)
    conn.close()

print("\nWelcome To Training Application!!!")
indicator = True
while indicator ==True:
    show_menu()
    option = input("Select an option....")
    if option =="1":
        try:
            add_student()
        except:
            print("Error: function is unsuccessful")
    elif option == "2":
        try:
            find_student()
        except:
            print("Error: function is unsuccessful")
    elif option == "3":
        try:
            add_course()
        except:
            print("Error: function is unsuccessful")
    elif option == "4":
        try:
            find_course()
        except:
            print("Error: function is unsuccessful")
    elif option == "5":
        try:
            enroll_student()
        except:
            print("Error: function is unsuccessful")
    elif option == "6":
        try:
            find_a_course_for_student()
        except:
            print("Error: function is unsuccessful")
    elif option == "7":
        try:
            find_student_for_course()
        except:
            print("Error: function is unsuccessful")
    elif option == "8":
        indicator = False
        ##raise SystemExit (alternative to indicator = False)
            
        
            
