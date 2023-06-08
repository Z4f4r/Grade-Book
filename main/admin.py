from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass


# @admin.register(Enrollment)
# class EnrollmentAdmin(admin.ModelAdmin):
#     pass
