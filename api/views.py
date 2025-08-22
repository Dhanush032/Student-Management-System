
from rest_framework import viewsets, permissions
from .models import Student, Teacher, Course
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('teacher').all().order_by('id')
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.prefetch_related('courses').all().order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]
