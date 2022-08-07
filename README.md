# Noodl LMS
Noodl is a learning management system that is both intuitive and fun-to-use!

## Launch instructions
- Install requirements.txt (`pip install -r requirements.txt`) after creating and activating a virtual environment (`python3 -m venv env` for MacOS, `python -m venv env` otherwise. `source env/bin/activate` to activate).  
- run `python3 manage.py runserver` (MacOS) or `python manage.py runserver` (Otherwise) to run the server. Visit (http://127.0.0.1:8000/)[localhost]
- 
## Features

### The User System
- The user system is easy to use. You can sign up as a student or an instructor. 
- For now (during the testing phase), instructor sign up is unrestricted (no approval required)
- Email Authentication coming soon!

### Courses
- Noodl has a flexible course structure.
- An instructor can create a course, add students and instructors to the course. Course instructors can then add assignments, question banks, quizzes, make announcements etc. in the course. These can be accessed by a student enrolled in the course.

### Quizzes
- Courses can have multiple Question Banks associated with them. To make a question bank, visit Quizzes > Make Question Bank

- Each question bank can have many questions added to them using the Question Editor. To make questions, visit Quizzes > Question Editor

### Question Editor
The question editor is extremely easy to use. Add a question then type it's prompt (MathJAX Support coming soon), select question type (Objective or Subjective) and marks for correct and incorrect responses, add as many options as you want (if objective) and tick the correct options. Thats it.

### Announcements
Intructors can make course-wide announcements from the My Courses page (Courses > My Courses)

### In Development
