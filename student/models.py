import uuid

from django.db import models

from promotion.models import Promotion


class Student(models.Model):
    registration_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=70, blank=False, default='')
    lastName = models.CharField(max_length=70, blank=False, default='')
    phoneNumber = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100, blank=True, default='')
    admission_year = models.PositiveIntegerField(default=0)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='students')
