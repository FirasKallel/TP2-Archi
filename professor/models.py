import uuid

from django.db import models


class Professor(models.Model):
    firstName = models.CharField(max_length=70, blank=False, default='')
    lastName = models.CharField(max_length=70, blank=False, default='')
    phoneNumber = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=100, blank=True, default='')
    professor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=70, blank=False, default='')
