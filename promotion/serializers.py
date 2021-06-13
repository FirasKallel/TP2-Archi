from rest_framework import serializers

from promotion.models import Promotion
from student.serializers import StudentSerializer


class PromotionSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, required=False)

    class Meta:
        model = Promotion
        fields = '__all__'
        depth = 1
