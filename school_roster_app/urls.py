# school_roster_app/urls.py
from django.urls import path
from . import views

app_name = "school_app" #must be called app_name
urlpatterns = [
    path("", views.index, name="home"),
    path("staff/", views.list_staff, name="list_staff"), #link to all the staffs
    path("staff/<str:employee_id>/", views.staff_detail, name="staff_detail"), #chhange to str b/c csv is str
    path("students/", views.list_students, name="list_students"),
    path("students/<str:student_id>/", views.student_detail, name="student_detail"),
    path("new/", views.student_new, name = 'student_new' )
]