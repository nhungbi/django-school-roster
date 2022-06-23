# school_roster_app/views.py

import re
from django.shortcuts import render
from .models import School, Student # import our School class

my_school = School("Django School") # create a school instance

def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {
        "school_name": my_school.name,
        'staff_list': my_school.staff} #a list of all staff obj
    
    return render(request, "pages/list_staff.html", my_data)


def staff_detail(request, employee_id):
    my_data = {
        'staff': my_school.find_staff_by_id(employee_id) #staff object
    }

    return render(request, 'pages/staff_detail.html', my_data)



def list_students(request):
    my_data = {
        "school_name": my_school.name,
        'students_list': my_school.students} #a list of all student obj
    
    return render(request, "pages/list_students.html", my_data)


def student_detail(request, student_id):
    my_data = {
        'student': my_school.find_student_by_id(student_id) } #student object

    return render(request, 'pages/student_detail.html', my_data)

# views.py

from django.shortcuts import render, redirect, reverse

# ...

def student_new(request):
    ## POST request
    if request.method == "POST":
        # extract the fields that we want from that post data
        form_data = {
          "name": request.POST["name"],
          "age": request.POST["age"],
          "school_id": request.POST["id"],
          "password": request.POST["password"],
          "role": "Student"
        }
        
        # create new internal data object
        new_student = Student(**form_data)
        
        # add to internal data collection and write out new data to csv
        my_school.add_student(new_student) 
        
        # redirect to a new page
        return redirect(reverse('school_app:student_detail', args=(new_student.school_id,)))
        
    ## GET request
    return render(request, "pages/students_new.html")
