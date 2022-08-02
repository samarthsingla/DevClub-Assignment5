from django.urls import path, include 
from . import views

urlpatterns = [
    path('question-editor/', views.question_Editor, name='grading-question_Editor'),
    path('getqbanks/', views.get_qbanks, name='grading-get_qbanks'),
    path('addquestions/', views.add_questions, name='grading-add_questions'),
    path('add-questionbank/', views.new_qbank, name='grading-new_qbank')
]