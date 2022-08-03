from . import views
from django.urls import path 

urlpatterns = [
    path("get_announcements/",views.get_announcements, name="communication-get_announcements")
    
]