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
### Student
| property | describtion |
|---|---|
|id (int)|The student’s unique identifier, used to find, edit, and delete the student.|
|name(str)| The student’s first name.
|family(str)|The student’s last name.
|courses(list[Course])|The courses the student has enrolled in. The score for each course is stored on these course objects.|

### Teacher
| property | describtion |
| --- | --- |
|id (int)| The teacher’s unique identifier, used to find, edit, and delete the teacher.|
|name (str)| The teacher’s first name.|
|family (str)| The teacher’s last name|
|grade (str)| The teacher’s academic degree, such as BSC or MSC.|
|courses (list[Course])| The courses the teacher is assigned to teach.|

### Course
| property | describtion |
| --- | --- |
|id (int)| The course’s unique identifier, used to find, edit, and delete the course|
|name (str)| The name of the course, such as java or py.|
|unit (int)| The number of units (credits) of the course|
|score (float)| The student’s score in this course.|

### Classroom
| property | describtion |
| --- | --- |
|id (int)| The classroom’s unique identifier.|
|name (str)| The name of the classroom.|
|course (Course)| The course that is taught in this classroom.|
|teacher (Teacher)| The teacher who teaches this course in the classroom.|
|students (list[Student])| The students enrolled in this classroom.|

### School
| property | describtion |
| --- | --- |
|name (str)| The name of the school.|
|courses (list[Course])| All the courses defined in the school.|
|teachers (list[Teacher])| All the teachers registered in the school.|
|students (list[Student])| All the students registered in the school.|
|selected_student (Student)| The student currently selected in the menu, which the “select student” options work on.|
# How it works ?
When you run the program , the main menu is printed :
```
1.students
2.teachers
3.courses
4.classrooms
5.save
0.exit
)):
```
1. Opens the students menu .Where you can print all students , add a student , delete a student and edit a student and select a student from all students which opens another menu.In this menu you can see there full information, add a course , remove a course and set there score .
2. Opens the teacher menu , which almost works like students menu .
3. Opens the courses menu , where you can print, add, edit, and delete courses.
4. In this menu you can manage classrooms(a course , its teacher and its students)
5. Save the current changes you made . (Changes you make stay in memory until you choose this option .)
# Example
After choosing `1` the students menu prints:
```
1.print students
2.add student
3.edit student
4.delete student
5.select student
0.back
)):
```
Typing `1` here prints all students:
```
id 	 name 	 family
2001 	 ali 	 rezaie
2002 	 reza 	 alinia
2003 	 ahmad 	 hoseini
```
Typing `5` lets you work with one student.By entering there ID you can access to Sub_menu for that student:
```
id 	 name 	 family
2001 	 ali 	 rezaie
2002 	 reza 	 alinia
2003 	 ahmad 	 hoseini
id:2001
```
```
1.show info
2.add course
3.remove course
4.set scores
0.back
:))1
id: 2001
name: ali
family: rezaie
id 	 name 	 unit 	 score
1001 	 java 	 4 	 17
1002 	 c# 	 3 	 0
```
Typing `0` goes back one menu each time.
