# Introduction
This project is a school management system with a text-based interface, written in `Python`. With this project, you can archive a school's information. You can add, delete, view, and edit the data of students, teachers, and courses. Each student can take several courses, and each teacher can teach several courses. The data is saved in a file so that it can be used again the next time.
### Data Storage
All of the program's data is stored in a file named `data.json` in `JSON` format. This file consists of three sections: 
1. courses : Contains the ID, name, and units of each course.
2. students : Contains the ID, first name, last name, and courses of each student 
3. teachers : Contains the ID, first name, last name, academic degree, and the courses each  teacher teaches.
4. classrooms : Contains the ID,name,teachers and tudents.

When the program runs, this file is read automatically and its data is converted into objects so that they can be worked with. After making changes, you can save them to the data.json file by selecting the save option from the main menu.
## Classes
### Students
| property | describtion |
|---|---|
|id (int)|The student’s unique identifier, used to find, edit, and delete the student.|
|name(str)| The student’s first name.
|family(str)|The student’s last name.
|courses(list[Course])|The courses the student has enrolled in. The score for each course is stored on these course objects.|

### Teachers
| property | describtion |
| --- | --- |
|id (int)| The teacher’s unique identifier, used to find, edit, and delete the teacher.|
|name (str)| The teacher’s first name.|
|family (str)| The teacher’s last name|
|grade (str)| The teacher’s academic degree, such as BSC or MSC.|
|courses (list[Course])| The courses the teacher is assigned to teach.|

### Courses
| property | describtion |
| --- | --- |
|id (int)| The course’s unique identifier, used to find, edit, and delete the course|
|name (str)| The name of the course, such as java or py.|
|unit (int)| The number of units (credits) of the course|
|score (float)| The student’s score in this course.|
