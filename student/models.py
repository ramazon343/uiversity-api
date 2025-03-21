from django.db import models

class EducationType(models.TextChoices):
    FULL_TIME = "full_time", "Full-time"
    PART_TIME = "part_time", "Part-time"

class StudentProfile(models.Model):
    full_name = models.CharField(max_length=255)
    course = models.PositiveIntegerField()
    education_type = models.CharField(
        max_length=20, choices=EducationType.choices, default=EducationType.FULL_TIME
    )
    birth_date = models.DateField()

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"

    def __str__(self):
        return f"{self.full_name} ({self.course}-kurs)"

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.full_name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="courses")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"{self.course.title} - {self.title}"