import json
import copy
from colorama import Style , init , Fore

init(autoreset=True)

class Course:
    id:int=0
    name:str=""
    unit:int=0
    score:float=0
    def __init__(self,id,name,unit):
        self.id=id
        self.name=name
        self.unit=unit
    def __eq__(self,other):
        if isinstance(other,Course):
            return self.id==other.id
        elif isinstance(other,int): 
            return self.id==other
        else:
            return False
    def __str__(self):
        return f"{self.id} \t {self.name} \t {self.unit}"

    
class Student:
    id:int=0
    name:str=""
    family:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family):
        self.id=id
        self.name=name
        self.family=family
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Student):
            return self.id==other.id
        elif isinstance(other,int): 
            return self.id==other
        else:
            return False
    def __str__(self):
        return f"{self.id} \t {self.name} \t {self.family}"

    
class Teacher:
    id:int=0
    name:str=""
    family:str=""
    grade:str=""
    courses:list[Course]=[]
    def __init__(self,id,name,family,grade):
        self.id=id
        self.name=name
        self.family=family
        self.grade=grade
        self.courses=[]
    def __eq__(self,other):
        if isinstance(other,Teacher):
            return self.id==other.id
        elif isinstance(other,int): 
            return self.id==other
        else:
            return False
    def __str__(self):
        return f"{self.id} \t {self.name} \t {self.family} \t {self.grade}"

    
class Classroom:
    id:int=0
    name:str=""
    course:Course=None
    teacher:Teacher=None
    student:list[Student]=[]
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __eq__(self,other):
        if isinstance(other,Teacher):
            return self.id==other.id
        elif isinstance(other,int): 
            return self.id==other
        else:
            return False

    
class School:
    name:str=""
    courses:list[Course]=[]
    teachers:list[Teacher]=[]
    students:list[Student]=[]
    classrooms:list[Classroom]=[]
    selected_student:Student=None
    selected_teacher:Teacher=None
    selected_course:Course=None
    def __init__(self,name):
        self.name=name

        
    def add_student(self,student:Student):
        if student in self.students:
            print(Fore.RED+"already exit")
        else:
            self.students.append(student)
            
    def add_teacher(self,teacher:Teacher):
        if teacher in self.teachers:
            print(Fore.RED+"already exit")
        else:
            self.teachers.append(teacher)
            
    def add_course(self,course:Course):
        if course in self.courses:
            print(Fore.RED+"already exit")
        else:
            self.courses.append(course)

    def add_classroom(self,classroom:Classroom):
        if classroom in self.classrooms:
            print(Fore.RED+"already exit")
        else:
            self.classrooms.append(classroom)

    def print_students(self):
        print("id \t name \t family")
        for student in self.students:
            print(student)

    def remove_student(self,id:int):
            if id in self.students:
                self.students.remove(id)
            else:
                print(Fore.RED+"dosent exit")

    def edit_student(self,student:Student):
        if student not in self.students:
            print(Fore.RED+"doesent exit")
        else:
            k=self.students.index(student)
            self.students[k].name=student.name
            self.students[k].family=student.family

    def print_teacher(self):
        print("id \t name \t family \t grade")
        for teacher in self.teachers:
            print(teacher)

    def remove_teacher(self,id:int):
        if id in self.teachers:
            self.teachers.remove(id)
        else:
            print(Fore.RED+"dosent exit")

    def edit_teacher(self,teacher:Teacher):
        if teacher not in self.teachers:
            print(Fore.RED+"doesent exit")
        else:
            k=self.teachers.index(teacher)
            self.teachers[k].name=teacher.name
            self.teachers[k].family=teacher.family
            self.teachers[k].grade=teacher.grade

    def print_courses(self):
        print("id \t name \t unit")
        for course in self.courses:
            print(course)
            
    def remove_course(self,id:int):
            if id in self.courses:
                self.courses.remove(id)
            else:
                print(Fore.RED+"dosent exit")
                
    def edit_course(self,course:Course):
        if course not in self.courses:
            print(Fore.RED+"doesent exit")
        else:
            k=self.courses.index(course)
            self.courses[k].name=course.name
            self.courses[k].unit=course.unit
    
 
    def load_data(self):
        f1=open("data.json","rt")
        ss=json.load(f1)
        f1.close()
        courses=ss["courses"]
        students=ss["students"]
        teachers=ss["teachers"]
            
        self.courses=[Course(course["id"],course["name"],course["units"])for course in courses]
         
        for s in students:
            student=Student(s["id"],s["name"],s["family"])
            for crs in s["courses"]:
                course_id=crs[0]
                score=crs[1]
                k=self.courses.index(course_id)
                course=copy.deepcopy(self.courses[k])
                course.score=score
                student.courses.append(course)
            self.students.append(student)


        for t in teachers:
            teacher=Teacher(t["id"],t["name"],t["family"],t["grade"])
            for crs in t["courses"]:
                k=self.courses.index(crs)
                course=self.courses[k]
                teacher.courses.append(course)
            self.teachers.append(teacher)


    def save_data(self):

        teachers=[]
        students=[]

        for teacher in self.teachers:
            courses=[]
            for c in teacher.courses:
                courses.append(c.id)
            t={"id":teacher.id,"name":teacher.name,"family":teacher.family,"grade":teacher.grade,"courses":courses}
            teachers.append(t)


        for student in self.students:
            courses=[]
            for c in student.courses:
                p=[c.id , c.score]
                courses.append(p)
            s={"id":student.id,"name":student.name,"family":student.family,"courses":courses}
            students.append(s)


        s1={"courses" : [{"id":course.id,"name":course.name,"units":course.unit }for course in self.courses],
        "students":students,
        "teachers":teachers
        }

        ss=json.dumps(s1)
        f1=open("data.json","wt")
        f1.write(ss)
        f1.close()


 
sc1=School("sama")
sc1.load_data()
level="root"
while True:
    if level=="root":
        print("1.students")
        print("2.teachers")
        print("3.courses")
        print("4.classrooms")
        print("5.save")
        print("0.exit")
        cmd=int(input(")):"))
        if cmd==1:
            level="students"
        elif cmd==2:
            level="teachers"
        elif cmd==3:
            level="courses"
        elif cmd==4:
            level="classrooms"
        elif cmd==5:
            sc1.save_data()
        elif cmd==0:
            break
        
    elif level=="students":
        print("1.print students")
        print("2.add student")
        print("3.edit student")
        print("4.delete student")
        print("5.select student")
        print("0.back")
        cmd=int(input(")):"))

        if cmd==1:
            sc1.print_students() 
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            sc1.add_student(Student(id,name,family))
        elif cmd==3:
            sc1.print_students() 
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            sc1.edit_student(Student(id,name,family))
        elif cmd==4:
            sc1.print_students() 
            id=int(input("id:"))
            sc1.remove_student(id)
        elif cmd==5:
            sc1.print_students()
            id=int(input("id:"))
            if sc1.students.count(id)==0:
                print(Fore.RED+"this is not exit")
            else:
                k=sc1.students.index(id)
                sc1.selected_student=sc1.students[k]
                level="select_student"
        elif cmd==0:
            level="root"


    elif level=="select_student":
        print("1.show info")
        print("2.add course")
        print("3.remove course")
        print("4.set scores")
        print("0.back")
        cmd=int(input(":))"))
        if cmd==1:
            print("id:",sc1.selected_student.id)
            print("name:",sc1.selected_student.name)
            print("family:",sc1.selected_student.family)
            print("id \t name \t unit \t score")
            for course in sc1.selected_student.courses:
                print(f"{course.id} \t {course.name} \t {course.unit} \t {course.score}")
        elif cmd==2:
            for course in sc1.courses:
                if course not in sc1.selected_student.courses:
                    print(course.id,course.name,course.unit)
            id=int(input("id:"))
            if sc1.courses.count(id)==0: 
                print("this is not exit")
            else:
                k=sc1.courses.index(id)
                sc1.selected_student.courses.append(sc1.courses[k])
        elif cmd==3:
            print("id \t name \t unit")
            for course in sc1.selected_student.courses:
                print(course)
            id=int(input("id:"))
            sc1.selected_student.courses.remove(id)    
        elif cmd==4:
            pass
        elif cmd==0:
            level="students"
      



            
    elif level=="teachers":
        print("1.print teachers")
        print("2.add teacher")
        print("3.edit teacher")
        print("4.delete teacher")
        print("5.select teacher")
        print("0.back")
        cmd=int(input(")):"))
        
        if cmd==1:
           sc1.print_teacher()
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            sc1.add_teacher(Teacher(id,name,family,grade))
        elif cmd==3:
            sc1.print_teacher()
            id=int(input("id:"))
            name=input("name:")
            family=input("family:")
            grade=input("grade:")
            sc1.edit_teacher(Teacher(id,name,family,grade))
        elif cmd==4:
            sc1.print_teacher()
            id=int(input("id:"))
            sc1.remove_teacher(id)
        elif cmd==5:
            sc1.print_teacher()
            id=int(input("id:"))
            if sc1.teachers.count(id)==0:
                print(Fore.RED+"this is not exit")
            else:
                k=sc1.teachers.index(id)
                sc1.selected_teacher=sc1.teachers[k]
                level="select_teacher"
        elif cmd==0:
            level="root"
    elif level=="select_teacher":
        print("1.show info")
        print("2.add course")
        print("3.remove course")
        print("0.back") 
        cmd=int(input(":))"))
        if cmd==1:
            print("id:",sc1.selected_teacher.id)
            print("name:",sc1.selected_teacher.name)
            print("family:",sc1.selected_teacher.family)
            print("grade:",sc1.selected_teacher.grade)
            print("id \t name \t unit")
            for course in sc1.selected_teacher.courses:
                print(course)
        elif cmd==2:
            for course in sc1.courses:
                if course not in sc1.selected_teacher.courses:
                    print(course.id,course.name,course.unit) 
            id=int(input("id:"))
            if sc1.courses.count(id)==0:
                print(Fore.RED+"this is not exit")
            else:
                k=sc1.courses.index(id)
                sc1.selected_teacher.courses.append(sc1.courses[k])
        elif cmd==3:
            print("id \t name \t unit")
            for course in sc1.selected_teacher.courses:
                print(course)
            id=int(input("id:"))
            sc1.selected_teacher.courses.remove(id)  
        elif cmd==0:
            level="teachers"
        


            
    elif level=="courses":
        print("1.print courses")
        print("2.add course")
        print("3.edit course")
        print("4.delete course")
        print("5.select course")
        print("0.back")   
        cmd=int(input(")):"))
        
        if cmd==1:
            sc1.print_courses()
        elif cmd==2:
            sc1.print_courses()
            id=int(input("id:"))
            name=input("name:")
            unit=input("unit:")
            sc1.add_course(Course(id,name,unit))
        elif cmd==3:
            sc1.print_courses()
            id=int(input("id:"))
            name=input("name:")
            unit=input("unit:")
            sc1.edit_course(Course(id,name,unit))
        elif cmd==4:
            sc1.print_courses()
            id=int(input("id:"))
            sc1.remove_course(id)
        elif cmd==5:
            pass
        elif cmd==0:
            level="root"     
        


    elif level=="classrooms":
        print("1.show classroom")
        print("2.add classroom")
        print("3.edit classroom")
        print("4.delete classroom")
        print("5.select classroom")
        print("0.back")
        cmd=int(input(")):"))
        if cmd==1:
            pass
        elif cmd==2:
            id=int(input("id:"))
            name=input("name:")
            for course in sc1.courses:
                print(course.id,course.name,course.unit) 
            id=int(input("id:"))
            if sc1.courses.count(id)==0:
                print("this is not exit")
            else:
                k=sc1.courses.index(id)
                sc1.selected_course=sc1.courses[k]
            selected_teacher=None
            for teacher in sc1.teachers:
                if sc1.selected_course.id in teacher.courses :
                    print("id:",teacher.id,"name:",teacher.name,"family:",teacher.family,"grade:",teacher.grade)
            id=int(input("id:"))
            k=sc1.teachers.index(id)
            selected_teacher=sc1.teachers[k]
            selected_student=[]
            while True:
                for student in sc1.students:
                    if student not in selected_student:
                        crss=[crs  for crs in student.courses if crs.score<10 ]
                        if sc1.selected_course in crss:
                            print(student)
                id=input("id:")            
                if id == "x":
                    break
                else:
                    id = int(id)
                    k=sc1.students.index(id)
                    selected_student.append(sc1.students[k])

        elif cmd==3:
            pass
        elif cmd==4:
            pass
        elif cmd==5:
            pass
        elif cmd==0:
            level="root"









