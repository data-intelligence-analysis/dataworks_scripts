# <u>Student Training Manager</u>

A student application that is to be used by a hypothetical training institution. This hypothetical institution offers various courses that the student can enroll in. A uniqued identifier, like an Id, is assigned to the name of the courses (courseid, coursename) to indentify the course and the data would be transformed into a table and essential create a database that can be interogatted using sqlite. A course can have unlimited students as well. Just like the development of the course table, the application will develop a student table, containing a unique identifier that is assigned to the student name (studentid, studentname) that will share a relationship with the course table and ultimately create a relational database. Therefore, students can enroll in one or more courses, however, a student may choose not to enroll in any courses.


##  Table of Contents
1. [Requirements](#Requirements)

2. [Installation](#Installation)

3. [Usage](#Usage)

4. [Support](#Support)

5. [Roadmap](#Roadmap)

6. [License](#License)

7. [Contributing](#Contributing)


## Requirements
1. Python 3.0 and later releases (Python 3.x.x).
2. IDLE3
3. Command Prompt (cmd) or Terminal
4. Can be installed on both Mac Os X and Windows

## Installation
This script requires Python 3.0 or any other of the Python 3 releases (Python 3.x.x), to execute and must be installed on your Windows or Macintosh machine. 

Installation guide for windows can be found on https://phoenixnap.com/kb/how-to-install-python-3-windows
Installation guide for Macintosh can be found on https://docs.python.org/3/using/mac.html



## Usage
1. Application can be run using the IDLE Python 3.0 and above. 

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
2. PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.
  PyInstaller is available on PyPI. You can install it through pip:

    pip install pyinstaller



## Support


## Roadmap


## License


## Contributing


