from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Course(models.Model):
    title = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.title}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=30, unique=True)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.name} [{self.enrollment_number}]"