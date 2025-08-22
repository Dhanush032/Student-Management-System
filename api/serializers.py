
from rest_framework import serializers
from .models import Student, Teacher, Course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'specialization']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), source='teacher', write_only=True, required=False
    )
    class Meta:
        model = Course
        fields = ['id', 'title', 'code', 'description', 'teacher', 'teacher_id']

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    course_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), write_only=True, required=False, source='courses'
    )
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'enrollment_number', 'courses', 'course_ids']
