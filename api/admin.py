from django.contrib import admin
from .models import Student, Teacher, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'enrollment_number')
    search_fields = ('name', 'email', 'enrollment_number')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialization')
    search_fields = ('name', 'email', 'specialization')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'teacher')
    search_fields = ('code', 'title')
    list_filter = ('teacher',)