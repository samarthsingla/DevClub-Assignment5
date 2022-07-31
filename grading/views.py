from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from grading.models import Question, QuestionBank
from courses.models import Course
from django.http import JsonResponse


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


@csrf_exempt
def get_questions(request):
    user = request.user
    if user.is_authenticated and user.is_instructor:
        pass