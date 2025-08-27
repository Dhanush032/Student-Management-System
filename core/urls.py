from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version='v1',
        description="CRUD for Students, Teachers, Courses with JWT",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Frontend pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('students/', TemplateView.as_view(template_name='students.html'), name='students'),
    path('teachers/', TemplateView.as_view(template_name='teachers.html'), name='teachers'),
    path('courses/', TemplateView.as_view(template_name='courses.html'), name='courses'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

