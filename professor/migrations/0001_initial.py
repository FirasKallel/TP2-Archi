# Generated by Django 3.0.5 on 2021-05-28 01:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('firstName', models.CharField(default='', max_length=70)),
                ('lastName', models.CharField(default='', max_length=70)),
                ('phoneNumber', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(blank=True, default='', max_length=100)),
                ('professor_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
