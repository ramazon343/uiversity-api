from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, LessonViewSet, TeacherViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]