from rest_framework import serializers

from course.serializers import CourseSerializer
from professor.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    charged_courses = CourseSerializer(many=True, required=False)

    class Meta:
        model = Professor
        fields = '__all__'
        depth = 1