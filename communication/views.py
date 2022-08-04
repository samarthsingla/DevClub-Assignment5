from django.shortcuts import render, HttpResponse, redirect
import json
from communication.models import Announcement
from courses.models import Course
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def get_announcements(request):
    user = request.user
    if user.is_authenticated:
        data = json.loads(request.body)
        print(data)
        announcements = Announcement.objects.filter(course = Course.objects.get(code=data['code'])).order_by("-posted")
        obj = {}
        for each in announcements:
            obj[each.title] = json.dumps(each.announcement_info())
        return JsonResponse(obj)

@csrf_exempt
def post_announcement(request):
    user = request.user
    if user.is_authenticated and user.is_instructor:
        data = json.loads(request.body)
        print(data)
        code = data['code']
        title = data['title']
        content = data['content']
        announcement = Announcement()
        announcement.title = title
        announcement.content = content
        announcement.course = Course.objects.get(code=code)
        announcement.instructor = user
        announcement.save()
        return HttpResponse(status=200)
        
