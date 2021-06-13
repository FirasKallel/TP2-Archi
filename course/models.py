from django.db import models

from professor.models import Professor
from promotion.models import Promotion
from student.models import Student


class Course(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    school_year = models.PositiveIntegerField(default=0)
    registered_students = models.ManyToManyField(Student)
    time_slot = models.CharField(max_length=70, blank=False, default='')
    in_charge = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='charged_courses')
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

