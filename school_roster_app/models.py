from django.db import models

# Create your models here.
import csv
import os
import os.path

class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def load_all(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, cls.DATA_FILE)
        
        people = []
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                person = cls(**row)
                people.append(person)

        return people


class Staff(Person):
    DATA_FILE = "../data/staff.csv"

    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    def __repr__(self):
        return f"staff: {self.name}"


class Student(Person):
    DATA_FILE = "../data/students.csv"

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    def __str__(self):
        return f"{self.name.upper()}\n--------------\nage: {self.age}\nid: {self.school_id}"




class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all()
        self.students = Student.load_all()

    def find_student_by_id(self, school_id):
        for student in self.students:
            if student.school_id == school_id:
                return student
        
        return None

    def find_staff_by_id(self, employee_id):
        for staff in self.staff:
            if staff.employee_id == employee_id:
                return staff
        
        return None
    
    def update_student_csv(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, 'w') as csvfile:
            fieldnames = ['name','age','role','school_id','password']
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow({'name':student.name, 'age':student.age, 'role':student.role, 'school_id':student.school_id, 'password':student.password})
        return True

    def add_student(self, student_data):
        """
        Given a student data (dict), create a new student object and add it to self.students.
        """
        self.students.append(student_data)

        #save to cvs
        self.update_student_csv()
            
        return self.students
