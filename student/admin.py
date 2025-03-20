from django.contrib import admin
from .models import StudentProfile, Course, Lesson

@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "course", "education_type", "birth_date")
    search_fields = ("full_name", "course")
    list_filter = ("education_type", "course")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "video_url", "created_at")
    search_fields = ("title",)
    list_filter = ("course", "created_at")
