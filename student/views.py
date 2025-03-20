from rest_framework import viewsets, permissions
from .models import StudentProfile, Course, Lesson
from .serializers import StudentSerializer, CourseSerializer, LessonSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class LessonViewSet(viewsets.ModelViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
