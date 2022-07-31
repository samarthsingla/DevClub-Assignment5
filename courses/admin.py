from django.contrib import admin
from courses.models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'instructor_Count', 'student_Count')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Course, CourseAdmin)