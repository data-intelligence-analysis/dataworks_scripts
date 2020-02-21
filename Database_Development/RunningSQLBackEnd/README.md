# <u>Student Training Manager</u>

A student application that is to be used by a hypothetical training institution. This institution offers various courses that the student can enroll in. A uniqued identifier, like an Id, is assigned to the name of the courses (courseid, coursename) to indentify the course and the data would be transformed into a table and essential create a database that can be interogatted using sqlite. A course can have unlimited students as well. Just like the development of the course table, the application will develop a student table, containing a unique identifier that is assigned to the student name (studentid, studentname) that will share a relationship with the course table and ultimately create a relational database. Furthermore, students can enroll in one or more courses, however, a student may choose not to enroll in any courses.


##  Table of Contents
1. [Requirements](#Requirements)

2. [Background](#Background)

3. [Installation](#Installation)

4. [Usage](#Usage)

5. [Support](#Support)

6. [Roadmap](#Roadmap)


## Requirements
1. Python 3.0 and later releases (Python 3.x.x).
2. IDLE3
3. Command Prompt (cmd) or Terminal
4. Can be installed on both Mac Os X and Windows

## Background
To create the application, the following steps must be achieved: 
1.	Identify entities and relationships
2.	Create empty database (training.db) per the Relational Schema using SQLite
3.	Create a front-end of the application (training.py) using Python 
4.	Connect the front-end application (training.py) with the back-end database (training.db)


## Installation
This script requires Python 3.0 or any other of the Python 3 releases (Python 3.x.x), to execute and must be installed on your Windows or Macintosh machine. 

Installation guide for windows can be found on https://phoenixnap.com/kb/how-to-install-python-3-windows
Installation guide for Macintosh can be found on https://docs.python.org/3/using/mac.html



## Usage
1. Application can be executed using IDLE Python 3.0 and above. 

  Application can be runned as an executable on Mac Os X by following these steps:
  a. Open Terminal, navigate to where your folder is located and give the python file training.py executable permissions by using the following command chmod +x training.py or chmod 755 training.py
  
  ```Command Prompt
  cd /Users/user_name.../StudentManager
  name_of_the_device:StudentManger user_name$>chmod +x training.py
  name_of_the_device:StudentManger user_name$>./training.py
  Welcome To Training Application!!!

  ------
  MENU:
  _____
  1. Add a student
  2. Find a student
  3. Add a course
  4. Find a course
  5. Enroll a student
  6. Find Course(s) of a Student
  7. Find Student(s) of a Course
  8. Quit

  Select an option....
  ```
2. You can also use PyInstaller, which bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.
  PyInstaller is available on PyPI. You can install it through pip:

    pip install pyinstaller



## Support
For any help or assistance please address the following user credentials:  

Emails are always welcome. You can contact developer on the following: 
	1. Email: menace3780@gmail.com
	2. Name: Dennis Osafo


## Roadmap
In the future the application would include calculating the GPA of the student based on the grade point of each subject created and assign that to the database. 




