from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import CourseAddForm
from django.contrib import messages
from django.http import JsonResponse
from courses.models import Course
from django.http import HttpResponse
import json
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.INFO : '',
}
def add_course(request):
    if request.user.is_authenticated and request.user.is_instructor:
        if request.method == "POST":
            form = CourseAddForm(request.POST)
            if form.is_valid():
                inst = form.save()
                inst.members.add(request.user)
                messages.add_message(request, messages.SUCCESS, "Course Added Successfully!")
                form = CourseAddForm()
        else:
            form = CourseAddForm()
        return render(request, 'courses/add_course.html', {'form':form})

    else:
        return render(request, 'account/genericError.html', {'error_message':"You need to be logged in as an instructor to access this page"})

@csrf_exempt
def get_courses(request):
    if request.method == "POST":
        user = request.user
        if user.is_authenticated:
            courses = {}
            for course in user.course_set.all():
                courses[course.code] = course.title
            return JsonResponse(courses)
        else:
            pass
    else:
        return HttpResponse()


def view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "GET":
            if user.is_instructor:
                context = {}
                return render(request, 'courses/view_instructor.html', context)
            else:
                context = {}
                return render(request, 'courses/view_student.html', context)

@csrf_exempt
def course_info(request):
    user = request.user
    if user.is_authenticated:
        body = json.loads(request.body)
        code = body['code']
        course = Course.objects.get(code=code)
        info = {}
        info['title'] = course.title
        info['code'] = course.code
        info['credits'] = course.credits
        info['student_count'] = course.student_Count()
        info['instructor_count'] = course.instructor_Count()
        members = {}
        members_set = course.members.all()
        for m in members_set:
            members[m.username] = json.dumps({'name':m.name, 'is_instructor':m.is_instructor, 'email':m.email})
        info['members'] = json.dumps(members)
        #assignment list
        return JsonResponse(info)
    else:
        return HttpResponse(status=401)
