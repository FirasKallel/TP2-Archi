from django.db import models

from course.models import Course
from student.models import Student


class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(default=0)
