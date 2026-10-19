# Introduction
This project is a school management system with a text-based interface, written in `Python`. With this project, you can archive a school's information. You can add, delete, view, and edit the data of students, teachers, and courses. Each student can take several courses, and each teacher can teach several courses. The data is saved in a file so that it can be used again the next time.
### Data Storage
All of the program's data is stored in a file named `data.json` in `JSON` format. This file consists of three sections: 
- courses : which contains the ID, name, and units of each course 
- students : which contains the ID, first name, last name, and courses of each student 
- teachers : which contains the first name, last name, academic degree, and the courses each  teacher teaches.

When the program runs, this file is read automatically and its data is converted into objects so that they can be worked with. After making changes, you can save them to the data.json file by selecting the save option from the main menu.
