# Generated by Django 3.0.5 on 2021-05-28 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='', max_length=70),
        ),
    ]
