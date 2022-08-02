from django.urls import path, include 
from . import views

urlpatterns = [
    path('questions/', views.question_Editor, name='grading-question_Editor'),
    path('getqbanks/', views.get_qbanks, name='grading-get_qbanks'),
    path('addquestions/', views.add_questions, name='grading-add_questions')
]