from django.urls import path, include 
from . import views

urlpatterns = [
    path("add/",views.add_course,name='courses-add_course'),
    path("get_courses/", views.get_courses, name='courses-get_courses'),
    path("view/", views.view, name="courses-view"),
    path("course_info", views.course_info, name="courses-course_info")
]