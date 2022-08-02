from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from grading.models import Question, QuestionBank
from courses.models import Course
from django.http import JsonResponse
import json

def question_Editor(request):
    return render(request, 'grading/q_editor.html', {})

@csrf_exempt
def get_qbanks(request):
    user = request.user
    if user.is_authenticated and user.is_instructor:
        qbanks = {}
        # print(request.POST)
        course_code = request.POST.get("code")
        course = Course.objects.get(code=course_code)
        questionBanks = QuestionBank.objects.filter(course= course)
        #append an "Uncategorized" question bank for uncategorized questions
        for qbank in questionBanks:
            qbanks[qbank.qb_code] = qbank.name
        return JsonResponse(qbanks)
    else:
        return render(request, 'account/genericError.html', {'error_message':'You need to be logged in as an instructor to add questions'})


@csrf_exempt
def get_questions(request):
    user = request.user
    if user.is_authenticated and user.is_instructor:
        pass

@csrf_exempt
def add_questions(request):
    user = request.user
    if user.is_authenticated and user.is_instructor:
        body = json.loads(request.body)
        print(body)
        qb_code = body.get('qb_code')
        course_code = body.get('qb_code')
        qb = QuestionBank.objects.get(qb_code = qb_code)
        for key in body:
            print(key)
            if(key not in 'qb_code course_code'):
                ques = body.get(key)
                # print(ques)
                instance = Question.objects.create(author=user,content = ques)
                instance.question_bank.add(qb)
        return HttpResponse()
    else:
        return render(request, 'account/genericError.html', {'error_message':'You need to be logged in as an instructor to add questions'})

@csrf_exempt
def new_qbank(request):
    user = request.user 
    if user.is_authenticated and user.is_instructor:
        if request.method == "GET":
            return render(request, 'grading/new_qbank.html')
        else:
            data = json.loads(request.body)
            print(request.body)
            qb = QuestionBank()
            qb.course = Course.objects.get(code=data['course_code'])
            qb.qb_code = data['code']
            if(QuestionBank.objects.filter(qb_code = data['code']).exists()):
                print("Oops")
                return HttpResponse(status=401)
            qb.name = data['name']
            qb.save()
            print("Saved")
            return redirect('grading-question_Editor')
    else:
        return render(request, 'account/genericError.html', {'error_message':'You need to be logged in as an instructor to create question banks'})

